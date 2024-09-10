# airflow-python-mysql
1. Set up a project folder.
 # bash
  >> mkdir airflow-mysql-docker-app
  >> cd airflow-mysql-docker-app
  >> git init

2. Create a .gitignore file to exclude sensitive information: Create a .gitignore file and add the following to ignore files and folders that should not be pushed to GitHub, like data files, environment variables, and logs.
   # bash 
  >> touch .gitignore
Add the following contents to .gitignore:
  # bash 
  # Ignore data and logs
/data/
/logs/

# Ignore environment files containing secrets
.env
env/

# Python related files
__pycache__/
*.pyc

# Docker and Airflow
airflow.db
airflow-webserver.pid
docker-compose.override.yml


   
 
