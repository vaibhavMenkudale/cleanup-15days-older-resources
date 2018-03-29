#!/usr/bin/env python3

## This code will return  list of instances older than 15 days##

import datetime
import boto3


today=datetime.date.today()
fifteenDaysAgo=today-datetime.timedelta(days=15)



def getOlderInstanceId():
    ec2=boto3.client('ec2') 
    olderInstances=[]
    for res in ec2.describe_instances()['Reservations']:
        if res['Instances'][0]['LaunchTime'].date() < fifteenDaysAgo:
            olderInstances.append(res['Instances'][0]['InstanceId'])
    
    return olderInstances


def main():
    print(getOlderInstanceId())

if __name__=='__main__':
    main()

#O/P 
# ['i-0e2804eed33b35c5d']
#
