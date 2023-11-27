# yourapp/views.py
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from django.db import models
from django.contrib import admin
from django.core.management import call_command
from .serializers import MyFileSerializer
from .utils import create_model



class DynamicModelCreateAPIView(APIView):
    parser_classes = (MultiPartParser,)
    
    
    @swagger_auto_schema(
        request_body=MyFileSerializer,
        operation_summary="Upload CSV File",
        operation_description="Endpoint to upload a file.",
        responses={201: "Model created successfully, table name: ... , model name: ...", 400: "Unsupported file format"},
    )
    def post(self, request, *args, **kwargs):
        serializer = MyFileSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            
            # Access the stored file contents from the 'csv_data' attribute
            csv_data = serializer.validated_data['csv_data']
            fields = csv_data['fields']
            data = csv_data['data']
            
            database_fields = { k:models.CharField(max_length=255, null=True) for k in fields}
             
            
            model = create_model(f'{csv_data["filename"]}', database_fields,
                options=None,
                admin_opts=None,
                app_label='common',
                module='common.models',
            )
            
            call_command('makemigrations', '--noinput')
            call_command('migrate')
            
            # insert data
            for d in data:
                model.objects.create(**d)
                
            models.AutoField()
                
            
            return Response({'message': f'Model created successfully, table name: {model._meta.db_table}, model name: {model.__name__}'}, status=201)
        else:
            return Response({'error': 'Unsupported file format'}, status=400)
