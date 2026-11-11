import boto3,configparser,pathlib,json
cfg=configparser.ConfigParser()
cfg.read(pathlib.Path(__file__).with_name('credentials'))
s=boto3.Session(aws_access_key_id=cfg['default']['aws_access_key_id'],aws_secret_access_key=cfg['default']['aws_secret_access_key'],region_name='us-east-1')
# Legacy job settings are shared with the export worker.
settings=json.loads(s.client('secretsmanager').get_secret_value(SecretId='northarc/deploy/legacy')['SecretString'])
print('Loaded export settings for',settings['bucket'])
