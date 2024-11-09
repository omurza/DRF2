from rest_framework import serializers  # Import serializers from Django REST Framework
from .models import NewsKg  # Ensure you import your NewsKg model

class SettingsNewsKg(serializers.ModelSerializer):  # It's a good practice to add 'Serializer' at the end
    class Meta:
        model = NewsKg  # Use 'model' instead of 'models'
        fields = ['id', 'title', 'description']  # Correct the typo 'descroption' to 'description'
