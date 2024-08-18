from django.shortcuts import render
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        # Get JSON data from the request
        json_data = request.body
        try:
            # Convert JSON data into stream
            stream = io.BytesIO(json_data)
            # Parse stream into Python data
            python_data = JSONParser().parse(stream)
            # Deserialize data
            serializer = StudentSerializer(data=python_data)
            if serializer.is_valid():
                serializer.save()
                res = {'msg': 'Data Created Successfully'}
                # Render response
                json_data = JSONRenderer().render(res)
                return HttpResponse(json_data, content_type='application/json')
            else:
                # Render validation errors
                json_data = JSONRenderer().render(serializer.errors)
                return HttpResponse(json_data, content_type='application/json', status=400)
        except JSONParser.ParseError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)
