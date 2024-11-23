import os
import subprocess
import shutil

def remove(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)

def main():
    print("Running post-generation hook...")
    
    # Change to the newly created project directory
    os.chdir(os.getcwd())
    
    # init direnv
    subprocess.call(['direnv', 'allow'])
    
    # Python
    python_enabled = '{{ cookiecutter.python_enabled }}'
    
    if python_enabled == 'y':
        subprocess.call(['uv', 'venv'])
        subprocess.call(['uv', 'sync'])
        print("Python project initialized")
        
    # K8s
    if '{{ cookiecutter.k8s_enabled }}' != 'y':
        remove('{{ cookiecutter.project_slug }}/taskfiles/k8s.taskfile.yml')
        remove('{{ cookiecutter.project_slug }}/taskfiles/k8s.k3d.taskfile.yml')
        
    # Replay file: with `project-template` is the name of this template
    replay_file = os.path.expanduser('~/.cookiecutter_replay/project-template.json')

    # Copy the replay file to the newly generated project and delete the original
    if os.path.exists(replay_file):
        shutil.copy(replay_file, 'cookiecutter_replay.json')
        remove(replay_file)
        print("Replay file copied to the project directory and deleted from the default location.")
    else:
        print("Replay file not found.")
    
    
if __name__ == '__main__':
    main()