import os
import sys
import django
import shutil
import subprocess
from pathlib import Path

def help():
    print("#===============================================#")
    print("#              DJANGO SETUP SCRIPT              #")
    print("#-----------------------------------------------#")
    print("# Create project                                #")
    print("# python ./script.py <project_name>             #")
    print("# python ./script.py <project_name> <app_name>  #")
    print("#                                               #")
    print("# Clean                                         #")
    print("# python ./script.py clean                      #")
    print("#===============================================#")

def clean():
    """ Clean the directory excluding script, venv and workspace """
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
        subprocess.run(
            f"python manage.py startapp {app_name}",
            shell=True,
            capture_output=True,
            text=True
        )
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def install_app_in_settings(project_name, app_name):
    """ app is installed inside INSTALLED_APPS of settings.py """
    with open(f"{project_name}/settings.py", "r+") as f:
        lines = f.readlines()

        for i, line in enumerate(lines):
            if "INSTALLED_APPS" in line:
                close = next(j for j in range(i + 1, len(lines)) if "]" in lines[j])
                lines.insert(close, f"\t'{app_name}',\n")
                break
        f.seek(0)
        f.writelines(lines)
        f.truncate()

def migration():
    """ Create tables for django """
    try:
        subprocess.run(
            f"python manage.py makemigrations",
            shell=True,
            capture_output=True,
            text=True
        )
        subprocess.run(
            f"python manage.py migrate",
            shell=True,
            capture_output=True,
            text=True
        )
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

def create_super_user(project_name):
    """ Create super user """
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", f"{project_name}.settings")
    django.setup()

    from django.contrib.auth import get_user_model
    User = get_user_model()

    username = "ghost"
    password = "12345678"
    email = "ghost@gmail.com"
    
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)

def main():
    # Check if project name is provided
    argLength = len(sys.argv)
    if argLength < 2:
        help()
        sys.exit(1)
    
    project_name = sys.argv[1]
    match sys.argv[1]:
        case "clean":
            clean()
            sys.exit(1)
        case _:
            create_django_project(project_name)
    
    if argLength == 3:
        app_name = sys.argv[2]
        create_django_app(app_name)
        install_app_in_settings(project_name, app_name)
    
    migration()
    create_super_user(project_name)
    
if __name__ == '__main__':
    main()