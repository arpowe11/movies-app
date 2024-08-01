# How to Set Up a Django Project

### If using VS-Code
1. Make a new empty folder for your project, name it either the name of oyur project or anything
2. Run your python version for the following commands in terminal (this sets up the virtual enviroment)
    - ```python3.12 -m venv .venv``` (you can name the venv anything, usually its named .venv)
    - ```source .venv/bin/activate``` (the first thing after source is the name of your venv)
3. Set up the django project in terminal
    - ```pip install django```
    - ```django-admin startproject config .```
    - ```python manage.py startapp <NAME_OF_PROJECT>```
4. Setting up the py files
    - Go to config/settings.py and locate the list named **INSTALLED APPS**
    - Start creating your views and adding those views to the config/urls.py file
