from rest_framework import serializers

import csv

class MyFileSerializer(serializers.Serializer):
    file = serializers.FileField()
    
    def validate(self, attrs):
        super().validate(attrs)
        
        # check if all rows have the same number of columns and has no empty fields
        from io import TextIOWrapper
        file = attrs['file']
        with TextIOWrapper(file, encoding='utf-8') as csv_file:
            csv_reader = csv.reader(csv_file)
        
            fields = [field for field in next(csv_reader) if field != ''] 
            rows = [row[1:] for row in list(csv_reader) if row]
            data = [dict(zip(fields, row)) for row in rows]
            
            if not all([len(row) == len(fields) for row in rows]):
                raise serializers.ValidationError('All rows must have the same number of columns')
            
            if not all([all(row) for row in rows]):
                raise serializers.ValidationError('All fields must be filled')
            
            attrs['csv_data'] = {
                'fields': fields,
                'rows': rows,
                'data': data,
            }
            
            return attrs
        