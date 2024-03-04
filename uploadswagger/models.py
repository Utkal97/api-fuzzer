from django.db import models

class SwaggerFile(models.Model):
    file = models.FileField(upload_to='swagger_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)