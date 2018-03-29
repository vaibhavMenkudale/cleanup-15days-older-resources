#!/usr/bin/python3 -tt

## This code will delete instance by id and return response ##

import boto3


def deleteInstance(Id):
    ec2=boto3.resource('ec2')
    instance=ec2.Instance(Id)
    return instance.terminate


