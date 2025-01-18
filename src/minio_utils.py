from minio import Minio
from minio.error import S3Error

class MinIOClient:
    def __init__(self, endpoint, acces_key, secret_key, bucket_name):
        self.client = Minio(
            endpoint,
            access_key=acces_key,
            secret_key=secret_key,
            secure=False
        )
        self.bucket_name = bucket_name

        if not self.client.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)
    
    def upload_file(self, file, filename):
        try:
            self.client.put_object(
                self.bucket_name,
                filename,
                file,
                length=-1,
                part_size=10*1024*1024
            )
            return {"message": "File uploaded successfully"}
        except S3Error as e:
            return {"error": str(e)}
        
    def download_file(self, filename):
        try:
            response = self.client.get_object(self.bucket_name, filename)
            return {"data": response.read(), "error": None}
        except S3Error as e:
            return {"error": str(e)}
        
    def delete_file(self, filename):
        try:
            self.client.remove_object(self.bucket_name, filename)
            return {"message": "File deleted successfully"}
        except S3Error as e:
            return {"error": str(e)}