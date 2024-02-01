import subprocess, os, sys, shutil

def download(repository_url):
    """ Deletes and Redownloads the Website to keep it up to date """

    if os.path.exists("Sudoku\\main.py"):
        shutil.rmtree("Sudoku\\")
        print("removed old versions")

    # Specify the full path to the git executable
    git_executable = r"C:\Users\Corsin_Lussmann\AppData\Local\Git\bin\git.exe"

    # Run the 'git clone' command to clone the repository
    try:
        command = [git_executable, 'clone', repository_url, "Sudoku\\"]
        subprocess.run(command)
    except:
        raise RuntimeError("Downloaded the new Version")
    

download("https://github.com/Flyingfoxi/Sudoku")