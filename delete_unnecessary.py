import os
for root, dirs, files in os.walk(os.getcwd()):
    if '.git' in root or '.vscode' in root:
        continue
    for file in files:
        if file.startswith("._") or file.endswith(".out") or file.endswith('.txt') or '.' not in file:
            os.remove(os.path.join(root, file))
