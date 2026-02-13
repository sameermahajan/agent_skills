import requests
from skills.repo_explainer.tool import read_repo

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
MODEL = "llama3.1"


def load_skill(skill_path):
    with open(f"{skill_path}/SKILL.md", "r", encoding="utf-8") as f:
        return f.read()


def call_ollama(messages):
    response = requests.post(
        OLLAMA_URL,
        headers={"Content-Type": "application/json"},
        json={
            "model": MODEL,
            "messages": messages
        },
        timeout=120
    )
    response.raise_for_status()

    data = response.json()
    return data["choices"][0]["message"]["content"]


def run_repo_explainer(repo_path, question):
    skill_md = load_skill("skills/repo_explainer")

    repo_content = read_repo(repo_path)
    print("repo_path = ", repo_path)
    print("repo_content = ", repo_content)

    system_prompt = f"""
You are an AI agent.

You have access to the following Agent Skill.
Follow it EXACTLY.

--- BEGIN SKILL ---
{skill_md}
--- END SKILL ---
"""

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": f"""
repo_path: {repo_path}
question: {question}
repository contents: {repo_content}
"""
        }
    ]

    response = call_ollama(messages)
    # print("RESPONSE:", first_response)
    return response

if __name__ == "__main__":
    repo = r"C:\AITraining\lca-langgraph-essentials"
    question = "Explain what this project does and suggest improvements"

    result = run_repo_explainer(repo, question)
    print("\nFINAL ANSWER:\n", result)
