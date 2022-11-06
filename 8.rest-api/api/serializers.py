from rest_framework import serializers
from api import models


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    roll = serializers.IntegerField()
    marks = serializers.IntegerField()
    timestamp = serializers.DateTimeField()


# The ModelSerializer class lets you automatically create a Serializer class with fields that correspond to the Model fields.
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tags
        fields = "__all__"


class ArticleSerializer(serializers.ModelSerializer):
    # Read-only fields are included in the API output, but should not be included in the input during create or update operations.
    tags = TagSerializer(many = True , read_only = True)

    class Meta:
        model = models.Article
        fields = "__all__"

    def create(self, validated_data):
        # return self.Meta.model.objects.create(**validated_data)
        print("Hey!! your data has been saved.")
        return super().create(validated_data)