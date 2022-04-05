# Udacity Data Engineering Capstone Project
    The goal of this project is to showcase all that I've learned throughout the Data Engineering course on Udacity.
Instead of the datasets provided for the project I thought it would be interesting to look at New York Crime data.
Ideally I'd like to consider this as a project to build a platform for crime data analysts and scientists. 

# Datasets
-new york city crime data 2006-2017 https://www.kaggle.com/mrmorj/new-york-city-police-crime-data-historic
-new york city arrest data 2006-2017 https://www.kaggle.com/danilzyryanov/arrests-data-by-new-york-police-department


# Prerequisites:
-AWS EMR Cluster
-Apache Spark
-configparser to run the python scripts

# Tools:
-AWS S3: Data Storage
-AWS Redshift: Data warehouse and data analysis
-Python - Data Processing
    +Pandas: Data Analysis and constructing fact and dim tables
    +Pyspark: Data processing on large data set

# Data Model:





## Problems:

1. Had an issue with creating pipenv v-environment with python 3.7.9. 
Error: 
pipenv install python 3.7.9
   requirements.txt found, instead of Pipfile! Converting…
   Warning: Your Pipfile now contains pinned versions, if your requirements.txt did. 
   We recommend updating your Pipfile to specify the "*" version, instead.
   Installing python…
   Looking in indexes: https://pypi.python.org/simple

Error:  An error occurred while installing python!
ERROR: Could not find a version that satisfies the requirement python (from versions: none)
ERROR: No matching distribution found for python

Fix:
delete python 3.7.9 from your system
re-download and install python 3.7.9 from website
pipenv install --python 3.7.9
  pipenv is aware of pyenv, but it doesn't 
  automatically use the same Python version unless you state it.
  This tells pipenv to scan your system and find the corresponding python version you listed. 


2.  Unable to pipenv install packages within venv:
Error: 
pipenv install numpy
 File "/home/richarda/.local/share/virtualenvs/ny_crime_capstone_project-FiLd2WC8/lib/python3.7/site-packages/pip/_internal/exceptions.py", line 10, in <module>
    from pip._vendor.six import iteritems
ModuleNotFoundError: No module named 'pip._vendor.six'

Fix:
exit virtual environment
python3 -m pip install --user pipx
python3 -m pipx ensurepath
pipx install pipenv


3. Pyspark import error:
Error:
  a. Pyspark isn't defined
  b. import pyspark could not be resolved
  c. import pyspark.sql could not be resolved
  
  What have I done:
    -pip installed pyspark both in virtural environment and on system
    -installed pyspark in virtual environment
  
  Fix:
  -uninstall pyspark and all related dependencies from machine and start over

  -----------------------------------------------------------------

  -install java-jdk 8
    +sudo apt install openjdk-8-jdk

  -set the java home environment variable 
    +sudo nano /etc/environment
    +enter in: 
        JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"
    +apply changes: 
        source /etc/environment

  -make sure java jdk is set correctly:
    +enter in terminal:
      echo $JAVA_HOME
    +this should output the filepath where JAVA_HOME is located
  
  -add "source /etc/environment" to bashrc file:
    +to get into bashrc:
      =nano ~/.bashrc or vim ~/.bashrc
  
  -check java version to make sure its installed correctly:
    +enter
      java -version

  -----------------------------------------------------------------

  -Go to spark https://spark.apache.org/downloads.html 
    +choose spark version 3.2.1
    +choose package, in my case "Pre-built for Apache Hadoop 3.3 and later"
  
  -move tgz file from download directory to home or local
  
  -extract and install spark zip file
    +enter "sudo tar -zxvf spark-3.2.1-bin-hadoop3.2.tgz" 
  
  -set SPARK environment variables:
    +enter:
      export SPARK_HOME=/home/richarda/spark-3.2.1-bin-hadoop3.2
      export PATH=$PATH:$SPARK_HOME/bin
      export PYSPARK_PYTHON=/usr/local/bin/python3.7
      export PYSPARK_DRIVER_PYTHON=/usr/local/bin/python3.7

      export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
      export PATH=$PATH:$JAVA_HOME/jre/bin

  -apply the changes to bashrc
    +enter
      source ~/.bashrc

  -Check to see if spark or pyspark runs:
    +cd into your spark folder
      cd /home/richarda/spark-3.2.1-bin-hadoop3.2
    +find pyspark.cmd
      enter:
        ls -la
    +enter:
      pyspark  
    +if pyspark starts up, then it worked!

----------------------------------------------------------------

  
4. Java gateway process exited before sending its port number
-go to bashrc file
  +nano ~/.bashrc
  +add line:
    export PYSPARK_SUBMIT_ARGS="--master local[2] pyspark-shell"
-this adds pyspark-shell to the shell environment variable PYSPARK SUBMIT ARGS
-this is because of a change in python/java_gateway.py which requires PYSPARK_SUBMIT_ARGS includes
   pyspark-shell.

5. Python package `pandas` is required for viewing data.