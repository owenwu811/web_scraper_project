import boto3

# Create a session using your Linode Object Storage keys
session = boto3.Session(
    aws_access_key_id='HZV2SBFE3ISIZJMOCH33',
    aws_secret_access_key='your_secret_access_key'
)

# Create a resource service client by name using the session
s3 = session.resource('s3')

# Upload the file
s3.Bucket('web-scraper-bucket-astro-2391').upload_file('/home/chatgpt/custom_utilities/utility_library/tmp/data_visualization.png', 'data_visualization.png')
