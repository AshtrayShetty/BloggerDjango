import datetime
import os

AWS_ACCESS_KEY_ID=os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_FILE_EXPIRE=200
AWS_PRELOAD_METADATA=True
AWS_QUERYSTRING_AUTH=True

DEFAULT_FILE_STORAGE='aws.utils.MediaRootS3BotoStorage'
STATICFILE_STORAGE='aws.utils.StaticRootS3BotoStorage'
AWS_STORAGE_BUCKET_NAME=os.environ.get('AWS_STORAGE_BUCKET_NAME')
S3DIRECT_REGION='us-west-2'
S3_URL=f'//{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/'
MEDIA_URL=f'//{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/media/'
MEDIA_ROOT=MEDIA_URL
STATIC_URL=S3_URL+'staic/'
ADMIN_MEDIA_PREFIX=STATIC_URL+'admin/'

two_months=datetime.timedelta(days=61)
date_two_months_later=datetime.date.today()+two_months
expires=date_two_months_later.strftime("%A, %d %B %Y 20:00:00 GMT")

AWS_HEADERS={
	'Expires':expires,
	'Cache-Control':'max-age=%d'%(int(two_months.total_seconds()),),
}