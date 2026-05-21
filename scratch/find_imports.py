import os
import ast

def get_imports(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        try:
            tree = ast.parse(f.read())
        except Exception:
            return set()
    
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                imports.add(name.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])
    return imports

def main():
    root_dir = r"d:\TopsPython\Projects\BatchPro"
    all_imports = set()
    for root, dirs, files in os.walk(root_dir):
        if 'venv' in dirs:
            dirs.remove('venv')
        if '.git' in dirs:
            dirs.remove('.git')
        for file in files:
            if file.endswith(".py"):
                all_imports.update(get_imports(os.path.join(root, file)))
    
    print("Detected imports:")
    for imp in sorted(all_imports):
        print(imp)

if __name__ == "__main__":
    main()
