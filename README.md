# Sensor-Fault-Detection

### Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class
indicates that the failure was caused by something else.

### Solution Proposed 
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.
## Tech Stack Used
1. Python 
2. FastAPI 
3. Machine learning algorithms
4. Docker
5. MongoDB

## Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions
5. Terraform

## How to run?
Before we run the project, make sure that you are having MongoDB in your local system, with Compass since we are using MongoDB for data storage. You also need AWS account to access the service like S3, ECR and EC2 instances.

## Data Collections
![image](https://user-images.githubusercontent.com/57321948/193536736-5ccff349-d1fb-486e-b920-02ad7974d089.png)


## Project Archietecture
![image](https://user-images.githubusercontent.com/57321948/193536768-ae704adc-32d9-4c6c-b234-79c152f756c5.png)


## Deployment Archietecture
![image](https://user-images.githubusercontent.com/57321948/193536973-4530fe7d-5509-4609-bfd2-cd702fc82423.png)


### Step 1: Clone the repository
```bash
git clone https://github.com/sethusaim/Sensor-Fault-Detection.git
```

### Step 2- Create a conda environment after opening the repository

```bash
conda create -n sensor python=3.7.6 -y
```

```bash
conda activate sensor
```

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Export the environment variable
```bash
export AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>

export AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

export AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION>

export MONGODB_URL="mongodb+srv://<username>:<password>@ineuron-ai-projects.7eh1w4s.mongodb.net/?retryWrites=true&w=majority"

```

### Step 5 - Run the application server
```bash
python app.py
```

### Step 6. Train application
```bash
http://localhost:8080/train

```

### Step 7. Prediction application
```bash
http://localhost:8080/predict

```

## Run locally

1. Check if the Dockerfile is available in the project directory

2. Build the Docker image
```
docker build --build-arg AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID> --build-arg AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY> --build-arg AWS_DEFAULT_REGION=<AWS_DEFAULT_REGION> --build-arg MONGODB_URL=<MONGODB_URL> . 

```

3. Run the Docker image
```
docker run -d -p 8080:8080 <IMAGE_NAME>
```

To run the project  first execute the below commmand.
MONGO DB URL: 
```
mongodb+srv://avnish:XglZZ9OkjjUw74pZ@ineuron-ai-projects.7eh1w4s.mongodb.net/admin?authSource=admin&replicaSet=atlas-okvkrd-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true
```
windows user

```
MONGO_DB_URL=mongodb+srv://avnish:XglZZ9OkjjUw74pZ@ineuron-ai-projects.7eh1w4s.mongodb.net/admin?authSource=admin&replicaSet=atlas-okvkrd-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true
```

Linux user

```
export MONGO_DB_URL=mongodb+srv://avnish:XglZZ9OkjjUw74pZ@ineuron-ai-projects.7eh1w4s.mongodb.net/admin?authSource=admin&replicaSet=atlas-okvkrd-shard-0&w=majority&readPreference=primary&appname=MongoDB%20Compass&retryWrites=true&ssl=true
```

then run 
```
python main.py
```



#####################################################

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
* All this configuratuin firl will help in respective operations

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

# pipeline folder:
* 



# Step to push into git repository after you clone.
```bash
git add .
```

```bash
git commit -m "statement"
```

For main branch:
```bash
git push origin main
```
or 
```bash
git push origin main --force
```

For master branch:
```bash
git push origin master
```
or
```bash
git push origin master --force
```

To get the remove url use below command:
```bash
git remote -v
```


# connecting mongodb atlas in local use following libraries
!pip install pymongo[srv]
!pip install dnspython
!python -m pip install mongo[srv] dnspython