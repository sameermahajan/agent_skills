# Skill: Repository Explainer

## Description
Analyze a local source code repository and explain what it does.

## Tools
- read_repo(repo_path: string)

## Tool Usage Rules
- You MUST use read_repo to inspect the repository
- Do NOT invent files or content
- Use the tool at most once per request

## Inputs
- repo_path: filesystem path to the repository
- question: what the user wants to know

## Output Requirements
- Be concise
- Be technically accurate
- Structure the answer with headings

## Instructions
1. Call read_repo(repo_path)
2. Analyze the returned content
3. Answer the user's question
