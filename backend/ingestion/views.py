from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

import pandas as pd


@api_view(['GET'])
def get_records(request):

    records = ActivityRecord.objects.all()

    serializer = ActivitySerializer(
        records,
        many=True
    )

    return Response(serializer.data)


@api_view(['POST'])
def upload_csv(request):

    file = request.FILES['file']

    df = pd.read_csv(file)

    for index,row in df.iterrows():

        ActivityRecord.objects.create(

            company_id=1,

            source=row['source'],
            category=row['category'],
            quantity=row['quantity'],
            unit=row['unit'],
            scope=row['scope']

        )

    return Response({
        'message':'Upload Successful'
    })