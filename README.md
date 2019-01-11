# Airflow on ECS sample

## Require
- AWS CLI, [ECS CLI](https://github.com/aws/amazon-ecs-cli)
- Ansible (for deploying dag)

## Create Cluster
ref) https://docs.aws.amazon.com/ja_jp/AmazonECS/latest/developerguide/ecs-cli-tutorial-ec2.html
```
# create ECS cluster -> vpc, security-group 
$ ecs-cli up --keypair keypair_name --capability-iam --size 1 --instance-type r5.large --cluster-config ec2-tutorial

# allow ssh for deploying dag files
$ aws ec2 authorize-security-group-ingress --group-id created_security_group_id --protocol tcp --port 22 --cidr your_cidr

# deploy dag files on EC2 instances
$ cd ansible
$ vi hosts  # edit ip address
$ ansible-playbook -i hosts site.yml
$ cd ..

# up
$ ecs-cli compose up --create-log-groups --cluster-config ec2-tutorial
```

