Create and activate a virtual environment
```
python3 -m venv ./venv
source venv/bin/activate
```
Install Flask with pip install:
```
pip install flask==1.1.2
```
Save the required libs
```
pip freeze > requirements.txt
```

Test the application in local
```
python3 hello.py
```

When you deploy, Elastic Beanstalk creates a new virtual environment on the server instances and installs the libraries listed in requirements.txt. 
To minimize the size of the source bundle that you upload during deployment, add an .ebignore file that tells the EB CLI to leave out the virt folder.

```
echo venv > .ebignore
```

ATTENTION: install EB CLI using https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html#eb-cli3-install.scripts

Initialize Elastic Beanstalk application
```
eb init -p python-3.7 PythonHelloWorld --region <region> --profile <profile>
```

__Customize file .ebextensions.__: you can add AWS Elastic Beanstalk configuration files (.ebextensions) to your web application's source code to configure your environment and customize the AWS resources that it contains. 
Configuration files are YAML- or JSON-formatted documents with a .config file extension that you place in a folder named .ebextensions and deploy in your application source bundle.
For example
```
option_settings:
  aws:ec2:vpc:
    VPCId: 'vpc-abc123'
    Subnets: 'subnet-abc123,subnet-abc123'
    ELBSubnets: 'subnet-def123,subnet-def123
    ELBScheme: 'public'
```

Create Elastic Beanstalk environment and upload application
```
eb create PythonHelloWorld-Production -cname pyhelloworld --elb-type application --instance-type t3.medium --min-instances 2 --max-instances 2 --vpc
```