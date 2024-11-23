import os
import subprocess

def main():
    print("Running post-generation hook...")
    
    # Change to the newly created project directory
    os.chdir(os.getcwd())
    
    # init direnv
    subprocess.call(['direnv', 'allow'])
    
    python_enabled = '{{ cookiecutter.python_enabled }}'
    
    if python_enabled == 'y':
        subprocess.call(['uv', 'venv'])
        print("Python project initialized")
    
    
if __name__ == '__main__':
    main()