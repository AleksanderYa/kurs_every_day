from datetime import datetime
from rest_framework import serializers

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "T.settings")
from rest_framework.renderers import JSONRenderer

# import django
# django.setup()


class Comment:
    def __init__(self, email, content, created=None):
        self.email = email
        self.content = content
        self.created = created or datetime.now()

comment = Comment(email='leila@example.com', content='foo bar')



class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

serializer = CommentSerializer(comment)



json = JSONRenderer().render(serializer.data)
print(json)


















