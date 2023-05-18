# Devprod_aws_boto3

Scenario: Our DevOps engineering team often uses a development lab to test releases of our application. The Managers are complaining about the rising cost of our development lab and need to save money by stopping 3 ec2 instances after all engineers are clocked out after a productive workday. We want to ensure that only our Development instances are stopped to make sure nothing in Production is accidentally stopped. Add logic to your script that only stops running instances that have the Environment: Dev tag.

What is Python:

Python is a very versatile simple programming language, it could be used for so many things. Python is a general-purpose, object-oriented programming language that has several implications across the software, web development, data science and automation environments. The language’s dynamic semantics, high-level built in data structure, dynamic typing and dynamic binding make it one of the most useful languages for rapid application development.

What is Boto3

Boto3 is the name of the Python SDK for AWS. It allows you to directly create, update, and delete AWS resources from your Python scripts. You use the AWS SDK for Python (Boto3) to create, configure, and manage AWS services, such as Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Simple Storage Service (Amazon S3). The SDK provides an object-oriented API as well as low-level access to AWS services.

What is AWS EC2

To put it simply, an EC2 is a virtual machine that represents a physical server for you to deploy your applications. Instead of purchasing your own hardware and connecting it to a network, Amazon gives you nearly unlimited virtual machines to run your applications while they take care of the hardware.

Prerequisites:

AWS CLI and Boto3 installed
AWS account with I AM user access, NOT root user
Basic AWS command line knowledge
Basic Python programming language
Basic knowledge of AWS Interactive Development Environment (IDE)
Ok let's get started.


BUT, there is another fun way to create all three instances just using Python Script. I will show you how after these few steps first.

Let’s go back to our AWS cloud 9 IDE environment.

Install Boto3
First, we want to make sure Boto3 is installed in the IDE environment. This allows Boto3 to interact our 3 instances we created in the AWS console.

pip install boto 3
Great! We got it installed!!


We also want to make sure AWS CLI is installed as well.

pip3 install awscli

<img width="788" alt="Screenshot 2023-05-18 at 09 13 26" src="https://github.com/Mamiololo01/Automating_AWS_ec2_with_boto3/assets/67044030/a2c3038e-8b16-4090-aef7-e21af300693c">


Great! Once this step is done, go to Github to Create and Clone the repo.

Create A new repository> Repository name: Automating_AWS_ec2_with_boto3 > Public > Add a README file > Add. gitignore template: Python > License: none > Create Repository


Next, back to the Cloud9 environment terminal: Enter following command to clone the repo.

git clone "Your own Github repo URL"

git clone https://github.com/Mamiololo01/Automating_AWS_ec2_with_boto3/

Awesome! We got Automating_AWS_ec2_with_boto3 Folder in the AWS cloud9 IDE

Next create a new branch and Python file.

We need to create a new file before we get started! Select File > New From Template > Python File > Save As… and give it a name. Make sure you KEEP the extension .py.

Make sure we are in the correct working directory.

cd week14EC2ProjectDev

Python Script to Start EC2 Instances
Ok! We are going to create a Python script to start all EC2 instances with the Environment Dev tags.

As this point we already Manually created 3 instances in the AWS console. Let’s switch it up and utilize the power of Python script to create 3 instances instead.

Attached is the file startec2.py to create AWS ec2 instances.


Ok, let’s run the script in AWS cloud 9 IDE to Start and create all three Development instances.


Look at that! How efficient is that!! We got 3 Development instances created and let’s go to AWS console and double check that if all three instances are there.


Awesome! All three Development instances are there!

<img width="804" alt="Screenshot 2023-05-18 at 08 45 22" src="https://github.com/Mamiololo01/Automating_AWS_ec2_with_boto3/assets/67044030/0a0ad2b4-5160-47b5-b4d6-f02850f41f87">

<img width="1031" alt="Screenshot 2023-05-18 at 08 45 47" src="https://github.com/Mamiololo01/Automating_AWS_ec2_with_boto3/assets/67044030/0f8889fe-7b29-4eca-a06f-d2a668ad32d2">


Python Script to Stop all three Development Instances
Ok, now we can stop all three Develoment instances using this Python script I’ve attached below.


Ok, let’s run the Python script in AWS cloud 9 IDE to Stop all three Development instances.


Great! All 3 Development Instances are stopped! Mission accomplished! Saving money never goes out of style! :D

<img width="718" alt="Screenshot 2023-05-18 at 08 49 08" src="https://github.com/Mamiololo01/Automating_AWS_ec2_with_boto3/assets/67044030/188ef693-347d-4538-9c34-7e855a4928c9">


<img width="993" alt="Screenshot 2023-05-18 at 08 49 33" src="https://github.com/Mamiololo01/Automating_AWS_ec2_with_boto3/assets/67044030/5df3c0cc-4a3f-4da5-b093-c4b97af35580">


Awesome! 

