from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import BmiInputSerializer, BmiOutputSerializer
from .calculate import Bmi, calculate_age


class CalculateBmiAPIView(APIView):
    '''
    You can use this APIView to calculate your BMI (Body Mass Index)
    
    Inputs (Json) :
        {
            'weight': (integer as kilogram),
            'height': (integer as centimeter),
            'gender': ('male' or 'female'),
            'year': (integer jalali year),
            'month': (integer jalali month),
            'day': (integer jalali day)
        }
    
    Output (Json) :
        {'bmi': float, 'weight': 'string', 'age': integer}
    
    '''
    
    def get(self, request, formate=None):
        try:
            serializer = BmiInputSerializer(data=request.GET)

            if serializer.is_valid():
                data = serializer.data

                age = calculate_age(
                    data.get('year'), data.get('month'), data.get('day'))
                
                b = Bmi(age, data.get('weight'), data.get('height'), data.get('gender'))
                result = b.calculate()
                result.update({'age': age})

                serialized = BmiOutputSerializer(data=result)

                if serialized.is_valid():
                    return Response(serialized.data, status.HTTP_200_OK)
                
                else:
                    Response({'error': 'Internal Server Error!'}, status.HTTP_500_INTERNAL_SERVER_ERROR)
            
            else:
                return Response({'error': 'Bad Request.'}, status.HTTP_400_BAD_REQUEST)
        
        except:
            return Response({'error': 'Internal Server Error!'}, status.HTTP_500_INTERNAL_SERVER_ERROR)

