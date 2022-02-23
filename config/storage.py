from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

# class S3StaticStorage(S3Boto3Storage):
#     location = 'static'

#     def __init__(self, *args, **kwargs):
#         kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
#         super(S3StaticStorage, self).__init__(*args, **kwargs)


class S3MediaStorage(S3Boto3Storage):
    location = 'media'

    def __init__(self, *args, **kwargs):
        kwargs['custom_domain'] = settings.AWS_CLOUDFRONT_DOMAIN
        super(S3MediaStorage, self).__init__(*args, **kwargs)