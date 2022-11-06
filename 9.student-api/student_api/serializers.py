from student_api import models
from rest_framework import serializers

class InstitueSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Institute
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    # Nested Serializer
    # Read-only fields are included in the API output, but should not be included in the input during create or update operations. 
    institute = InstitueSerializer(read_only = True)
    class Meta:
        model = models.Student
        fields = "__all__"

    def create(self, validated_data):
        print("Hey your request is succesful!!")
        return super().create(validated_data)