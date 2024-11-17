import os
import subprocess

def main():
    print("Running post-generation hook...")
    
    # Change to the newly created project directory
    os.chdir(os.getcwd())
    
    # init direnv
    subprocess.call(['direnv', 'allow'])
    
    # setup virtualenv
    subprocess.call(['uv', 'venv'])
    
if __name__ == '__main__':
    main()