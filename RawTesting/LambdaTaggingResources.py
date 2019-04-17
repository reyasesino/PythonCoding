import boto3

client = boto3.client('resourcegroupstaggingapi')
s3 = boto3.client('s3')


def tagging(resourcename , resourceid ,region, missingkeys):
    jsonvalue = {}
    jsonvalue['resourcename'] = resourcename
    resourceidtype = resourceid.split("/")
    jsonvalue['resourceidtype'] = resourceidtype[0]
    jsonvalue['resource'] = resourceidtype[1:]
    jsonvalue['region'] = region
    jsonvalue['missingKeys'] = missingkeys

    return jsonvalue

def lambda_handler(event, context):
    response = client.get_resources()
    resources = response['ResourceTagMappingList']
    taggingKeys = ['Name', 'CostCentre', "owner", "Environment"]
    filemain = ""

    for resourcetag in resources:
        keyshaving = taggingKeys
        if (resourcetag['Tags']):
            for tag in resourcetag['Tags']:
                if tag["Key"] in keyshaving:
                    keyshaving.remove(tag["Key"])
            resourcearn = resourcetag['ResourceARN'].split(":")
            filemain = filemain + str(tagging(resourcearn[2],resourcearn[5],resourcearn[3],keyshaving)) + "\n"
        else:
            getting = resourcetag['ResourceARN'].split(":")
            tagging(getting[2],getting[5], getting[3],keyshaving)
            filemain = filemain + str(tagging(resourcearn[2],resourcearn[5],resourcearn[3],keyshaving)) + "\n"

    s3respnse = s3.put_object(
        Body=filemain,
        Bucket='sqlbackupdb',
        Key='notagresources'
    )
    print(filemain)

    return

