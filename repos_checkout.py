import os
from contextlib import contextmanager
import pathlib

@contextmanager
def change_dir(destination):
    """
    Change the current working directory to the specified destination.
    """
    
    try:
        cwd = os.getcwd()
        if not os.path.exists(pathlib.Path(destination)):
            os.makedirs(destination)
        os.chdir(destination)
        yield
        
    finally:
        os.chdir(cwd)
        
def get_repos():
    """
    Get the list of repositories from the specified URL.
    """

    repos = [
        "git://github.com/your_username/repo1.git",
        "git://github.com/your_username/repo2.git",
        "git://github.com/your_username/repo3.git",
    ]
    
    threads = []
    for destination in (os.path.join(os.getcwd(), e.split('/')[-1].replace('.git', '')) for e in repos):
        t = Thread(target=clone_repos, args=(repos, destination))
        thread.append(t)
        t.start()
        
    [t.join() for t in thread]
    
    def clone_repos(repos, destination):
        with change_dir(destination):
            for repo in repos:
                repo_name = repo.split('/')[-1].replace('.git', '')
                if not os.path.exists(repo_name):
                    with tqdm(total=100, desc=f"Cloning {repo_name}", unit="%") as pbar:
                        for i in range(100):
                            time.sleep(0.01)
                            pbar.update(1)
                    os.system(f"git clone {repo}")
                    print(f"Cloned {repo_name}")
                else:
                    print(f"{repo_name} already exists")
    return repos


if __name__ == "__main__":
    repos = get_repos()