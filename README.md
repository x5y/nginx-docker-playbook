# nginx-docker Playbook

A simple Ansible playbook to deploy an nginx Docker container on an EC2 instance

## Requirements

* Ansible >= 2.9
* pip

## Setup

You must have an existing AWS account with the following:
* An IAM user with an access key and create permissions for VPC, EC2
* An existing key pair configured in your machine's ssh config

Run the following pip command to install the required packages:

```bash
pip install -r requirements.txt
```

Set the environment variables ```AWS_ACCESS_KEY_ID``` and ```AWS_SECRET_ACCESS_KEY``` to their respective values

Set the variable ```key-pair``` in global_vars/all to the name of your key pair

## Usage

Run the following command to execute the playbook:
```bash
ansible-playbook main.yml
```

You will be prompted to add the provisioned EC2 instance to your known hosts unless you set the environment variable: ANSIBLE_HOST_KEY_CHECKING=False

## Playbook Summary

The playbook starts in the ```main.yml``` file and covers three separate task files, ```provision_ec2.yml```, ```setup_docker.yml```, and ```scripts.yml```

The ```group_vars/all``` file contains varaibles which can be set if desired.

### provision_ec2.yml

Provisions AWS infrastructure.
* Creates a VPC called test-vpc and add an internet gateway and subnet with public route table
* Adds a security group with ssh access (22) from your current IP and global http (80) access
* Launches a CentOS 7 AMI with your specified key pair in the subnet

### setup_docker.yml

Sets up the Docker container with nginx.
* Sets up firewalld with port 80 enabled
* Installs docker-ce
* Builds and creates an nginx container with port 80 forwarded to the host

### scripts.yml

Run scripts on container
* Runs a word count script on the default nginx page and outputs it to the terminal
* Creates cron jobs to log docker container health and status to a resource log
* You can access the resource log at [ec2_public_dns]/resource.html

## Risks

* The playbook isn't fully idempotent. It will always create a new EC2 instance.
* There is no clean up task, so you'll have to do it manuall through the AWS web console.
* It will endlessly log the container status, so may potentially run out of disk space.
* The centos user has passwordless sudo, so anybody with ssh access can run anything as root.
