import os

def read_repo(repo_path: str, max_files=20, max_chars=8000):
    collected = []
    total = 0

    for root, _, files in os.walk(repo_path):
        for name in files:
            if name.endswith((".py", ".js", ".ts", ".md")):
                path = os.path.join(root, name)
                try:
                    with open(path, "r", errors="ignore") as f:
                        content = f.read()
                        collected.append(
                            f"\n--- FILE: {path} ---\n{content[:1000]}"
                        )
                        total += len(content)
                except Exception:
                    pass

                if total > max_chars:
                    return "\n".join(collected)

    return "\n".join(collected)
