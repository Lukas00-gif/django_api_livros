from dataclasses import fields
from rest_framework import serializers
from books import models


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Books
        #todos os campos do models 
        fields = '__all__'

