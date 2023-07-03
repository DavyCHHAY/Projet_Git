import subprocess
import sys

def lint_python_file(file_path):
    # Vérification de la syntaxe avec l'option -m py_compile
    syntax_check = subprocess.run(['python', '-m', 'py_compile', file_path], capture_output=True)
    if syntax_check.returncode != 0:
        print("Erreur de syntaxe dans le fichier :", file_path)
        print(syntax_check.stderr.decode('utf-8'))
        return 1
    return 0
    
lint_python_file(sys.argv[1])
