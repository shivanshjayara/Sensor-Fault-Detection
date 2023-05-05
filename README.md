# Sensor-Fault-Detection
This is an air pressure system binary classification project in which the affirmative class indicates that the failure is caused by a certain component of the APS while the negative class indicates that the failure was caused by something else.

# setup.py file: Why we need this file?
* Most of the time it happen, that some of the module is not found which we created. Even if our code is present but whenever we try to import it  says "module not found". 
* To avoid those errors we try to setup our projects in such a way that our code can be updated or utilize it as a library. Even path is present still we face similar error.
* We write code in this file so that "sensor" folder can be treated as a library. Make sure "__init__.py" file is present.
*So we use this file to create a libraries. For thses things we import find_packages library. This will search the root directories for python modules/libraries having .py extension.
* In short, it is use to create the package for your project so that it can be use as a library

# requirements.txt:
* here -e . will trigger the setup.py file and is equivalent to find_packages(). This will find the libraries from the sensor package.

# pipeline folder:
* Script for ML piepline

# data access folder: 
* Bringing data from data base

# cloud storage folder:
* To upload, downlad file, download and svave model in s3 bucket
* Everything that are use with the help of s3 bucket.
* To manage cloud services

# configuration
 folder:
* Since we have so many configurations like connection for mongoDB, cloud, etc.
* So these configuration need to be centralized somewhere. 
* So we will create a folder that will maintain the connection configuration.

# Constant folder:
* Every projects some contants.
* Like, db name, model name, file name, folder name, etc. These are hard coded name.
* How to maintain those name, for that we create a folder.
* We only write variable declaration here.

# ORM
* There are functions which returns something and some of them is not return.
* Feature store- MongoDB
* Running a pipeline in development, we can call orchestration.
* Every step has som einput and and some output. So for this we need to connect our component is such a way that we get the desired input and output.

# Entity folder: 2:45
* To define every input and output for every component. 
* Even for every pipeline
* Machine Learning artifcat: Term that describe the output(a fully trained model, a model checkpoint, or a file) created by the training process. While running a piepline if any thing is generated, that output we call a artifact.
* It contains artifact_entity.py file, this is for all the output in every stage and config_entity.py file, this file is for input to every component. While bring the data may be we need to store it some where so for that purpose we have this config_entity.py file.

# ml folder:
* May we create our own ml algorithm.
* May be we create our own loss function.
* May be we need some feature engineer, custom function etc which are specific to the ML.
* For these things we need this folder.

# 