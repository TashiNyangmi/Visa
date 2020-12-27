import boto3

class AWSmanager:
    def __init__(self):
        self.s3 = boto3.resource('s3')

#   #define connections to boto3 and save file to s3
    def save_to_s3(self):
        s3 = boto3.client('s3')
        boto3.client('s3').upload_file('master_df.csv', 'visa2021', 'master_df.csv')

    def listBucketFile(self, bucketName):
        bucket = self.s3.Bucket(bucketName)
        files = bucket.objects.all()
        for file in files:
            print(file.key)

aws = AWSmanager()
aws.save_to_s3()
aws.listBucketFile("visa2021")

