from reviews.models import Review
from rest_framework import serializers

class ReviewSerializer(serializers.ModelSerializer):
    book = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
    
    def validate_rating(self, value):
        if value < 0 or value > 10 or not isinstance(value, int):
            raise serializers.ValidationError("Рейтинг должен быть целым числом от 0 до 10")
        return value
