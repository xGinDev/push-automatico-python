import os
import subprocess

def git_auto_commit_push():
    try:
        # Cambia al directorio del repositorio
        os.chdir('https://github.com/xGinDev/push-automatico-python.git')

        # Realiza un git add
        subprocess.run(['git', 'add', '.'])

        # Realiza un git commit
        subprocess.run(['git', 'commit', '-m', 'Commit automático'])

        # Realiza un git push
        subprocess.run(['git', 'push'])
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    git_auto_commit_push()