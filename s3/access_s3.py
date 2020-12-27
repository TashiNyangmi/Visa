import boto3
import io
import pandas as pd
import json

# bucket_name = ''
# object_key = ''


s3 = boto3.client('s3')
obj = s3.get_object(Bucket = 'visa2021', Key = 'master_df.csv')

data = obj['Body'].read()
df = pd.read_csv(io.BytesIO(data), encoding = 'utf-8')

print(df.head())


