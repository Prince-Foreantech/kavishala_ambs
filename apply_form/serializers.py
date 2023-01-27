from rest_framework import serializers

class user(serializers.Serializer):
    username=serializers.CharField(max_length=50)
    password=serializers.CharField(max_length=50)
    name=serializers.CharField(max_length=100)
    email=serializers.EmailField()
    contact_number=serializers.IntegerField()
    college_name=serializers.CharField(max_length=100)
    city=serializers.CharField(max_length=50)
    course_year=serializers.CharField(max_length=150)
    instagram_url=serializers.CharField(max_length=500)
    twitter_url=serializers.CharField(max_length=500)
    facebook_url=serializers.CharField(max_length=500)
    confirmation = serializers.CharField(max_length=10)
    