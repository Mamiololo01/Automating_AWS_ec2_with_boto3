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

Launch EC2 Instances in the AWS management console.
Click Launch Instance >Name your instance: Week 14 EC2Project > “Additional tags” > Add tag > Key: Environment > Value: Dev



We are going to create 3 instances, 3 for Development environment, tagged Dev. The goal of this project is to lower cost in the Development environment. The rest under Quick Start > Amazon Linux > Instance Type T2.micro instnace type. > Key Pair: “Myownkeypair” > Launch Instance. Repeat two more steps to create all three instances tagged “Dev”

Ok, great! We got all 3 instances running.


BUT, there is another fun way to create all three instances just using Python Script. I will show you how after these few steps first.

Let’s go back to our AWS cloud 9 IDE environment.

Install Boto3
First, we want to make sure Boto3 is installed in the IDE environment. This allows Boto3 to interact our 3 instances we created in the AWS console.

pip install boto 3
Great! We got it installed!!


We also want to make sure AWS CLI is installed as well.

pip3 install awscli

Great! Once this step is done, go to Github to Create and Clone the repo.

Create A new repository> Repository name: Week14EC2ProjectDev > Public > Add a README file > Add. gitignore template: Python > License: none > Create Repository


Next, back to the Cloud9 environment terminal: Enter following command to clone the repo.

git clone "Your own Github repo URL"

git clone https://github.com/Jleeluit/Week14EC2ProjectDev

Awesome! We got Week14EC2ProjectDev Folder in the AWS cloud9 IDE

Next create a new branch and Python file.


We need to create a new file before we get started! Select File > New From Template > Python File > Save As… and give it a name. Make sure you KEEP the extension .py.


Make sure we are in the correct working directory.

cd week14EC2ProjectDev

Python Script to Start EC2 Instances
Ok! We are going to create a Python script to start all EC2 instances with the Environment Dev tags.

As this point we already Manually created 3 instances in the AWS console. Let’s switch it up and utilize the power of Python script to create 3 instances instead.

Below is the Python Script code in GitHub Gist. Feel free use this code.


Ok, let’s run the script in AWS cloud 9 IDE to Start and create all three Development instances.


Look at that! How efficient is that!! We got 3 Development instances created and let’s go to AWS console and double check that if all three instances are there.


Awesome! All three Development instances are there!


I almost forgot to create three Production Instances. Initially, I can just add that Production Python script with the Environment instances. But, O’well Let’s repeat the step.

Ok, let’s run the script in AWS cloud 9 IDE to Start and create all three Production instances.



We also got 3 Production instances created and let’s go to AWS console and double check that if it is there.


Great! All three Production instances are there!

Python Script to Stop all three Development Instances
Ok, now we can stop all three Develoment instances using this Python script I’ve attached below.


Ok, let’s run the Python script in AWS cloud 9 IDE to Stop all three Development instances.


Great! All 3 Development Instances are stopped! Mission accomplished! Saving money never goes out of style! :D


Here are the links Via AWS Boto3 Documentation to start and stop an EC2 instance.

start_instances — Boto3 1.26.111 documentation (amazonaws.com)

stop_instances - Boto3 1.26.110 documentation
Client / stop_instances Stops an Amazon EBS-backed instance. For more information, see Stop and start your instance in…
boto3.amazonaws.com

Push Python Script Code to GitHub
Last 3 steps, let’s push all three of the Python scripts code to my GitHub Account. (I will just use one for step guide purposes).

git push  git push --set-upstream origin Week14EC2Project
We will configure Git with our Usename and password. (Remember, the password is the Personal Access Token) Here is the link if you need to create a new Personal Access Token.

Creating a personal access token - GitHub Enterprise Server 3.4 Docs
Personal access tokens are an alternative to using passwords for authentication to GitHub Enterprise Server when using…
docs.github.com


Click on the Source Control Icon, and Click + sign before the green U letter to stage the changes.


Type in Name: RunDevelopmentInstances > It is important to Type in CONTROL & ENTER in order to push the Code to GitHub. (I am missing one screen shot, It is at the bottom left corner following the previous step, you will see and loop icon and up arrow, click on that, then this will be the last step to push the code to GitHub).



Awesome! Click Compare & Pull request to Create pull request in GitHub! (You can customized the comment)

