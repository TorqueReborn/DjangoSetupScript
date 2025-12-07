
"""
Django Project Setup Script
Usage: python .script.py <project_name> <app_name>
"""
import sys
import subprocess

def create_django_project(project_name):
    """ Create django project """
    try:
        # Run django-admin start-project
        result = subprocess.run(
            f"django-admin startproject {project_name}",
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
        print("#===============================================#")
        print("#              DJANGO SETUP SCRIPT              #")
        print("#-----------------------------------------------#")
        print("# Usage: python create_django.py <project_name> #")
        print("#===============================================#")
        sys.exit(1)
    
    project_name = sys.argv[1]
    
    # Create the project
    create_django_project(project_name)


if __name__ == '__main__':
    main()