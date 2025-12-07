import sys
import shutil
import subprocess
from pathlib import Path

def help():
    print("#===============================================#")
    print("#              DJANGO SETUP SCRIPT              #")
    print("#-----------------------------------------------#")
    print("# Create project                                #")
    print("# python ./script.py <project_name>             #")
    print("#                                               #")
    print("# Clean                                         #")
    print("# python ./script.py clean                      #")
    print("#===============================================#")

def clean():
    script = Path(__file__).name
    for item in Path(".").iterdir():
        if item.name not in [".venv", script]:
            try:
                shutil.rmtree(item) if item.is_dir() else item.unlink()
            except:
                print(f"Unable to remove {item}")

def create_django_project(project_name):
    """ Create django project """
    try:
        # Run django-admin start-project
        result = subprocess.run(
            f"django-admin startproject {project_name} .",
            shell=True,
            capture_output=True,
            text=True
        )
        print(result)
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def main():
    # Check if project name is provided
    if len(sys.argv) != 2:
        help()
        sys.exit(1)
    
    match sys.argv[1]:
        case "clean":
            clean()
        case _:
            create_django_project(sys.argv[1])

if __name__ == '__main__':
    main()