from rest_framework import serializers
from .models import *

class ActivitySerializer(
    serializers.ModelSerializer
):

    class Meta:

        model=ActivityRecord

        fields='__all__'