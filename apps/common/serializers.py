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
            filename = csv_file.name[:-4]
            
            csv_reader = csv.reader(csv_file)
            
            fields = next(csv_reader)
            first_column = fields[0]
            
            # check if first column is sequence and in that case skip first column
            if first_column in ('', 'id', 'Id', 'ID', 'pk', 'Pk', 'PK'):
                fields = fields[1:]
                rows = [row[1:] for row in list(csv_reader) if len(row)>1]
            else:
                rows = [row for row in list(csv_reader)]
        
            data = [dict(zip(fields, row)) for row in rows]
            
            if not all([len(row) == len(fields) for row in rows]):
                raise serializers.ValidationError('All rows must have the same number of columns')
            
            if not all([all(row) for row in rows]):
                raise serializers.ValidationError('All fields must be filled')
            
            attrs['csv_data'] = {
                'fields': fields,
                'rows': rows,
                'data': data,
                'filename': filename,
            }
            
            return attrs
        