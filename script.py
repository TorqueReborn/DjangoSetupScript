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
        if item.name not in [".venv", script] and item.suffix != ".code-workspace":
            try:
                shutil.rmtree(item) if item.is_dir() else item.unlink()
            except:
                print(f"Unable to remove {item}")

def create_django_project(project_name):
    """ Create django project """
    try:
        # Run django-admin start-project
        subprocess.run(
            f"django-admin startproject {project_name} .",
            shell=True,
            capture_output=True,
            text=True
        )
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def create_django_app(app_name):
    """ Create django app """
    try:
        # Run django-admin start-project
        subprocess.run(
            f"python manage.py startapp {app_name}",
            shell=True,
            capture_output=True,
            text=True
        )
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def main():
    # Check if project name is provided
    argLength = len(sys.argv)
    if argLength < 2:
        help()
        sys.exit(1)
    
    match sys.argv[1]:
        case "clean":
            clean()
            sys.exit(1)
        case _:
            create_django_project(sys.argv[1])
    
    if argLength == 3:
        create_django_app(sys.argv[2])

if __name__ == '__main__':
    main()