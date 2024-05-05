from rest_framework import serializers

from ads.models import Ad, Review


class AdSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для модели Ad"""
    class Meta:
        model = Ad
        fields = ('pk', 'title', 'price', 'description', 'image', 'created_at')


class AdDetailSerializer(serializers.ModelSerializer):
    """Класс-сериализатор для просмотра детальной информации по объявлению"""
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_email = serializers.CharField(source="author.email", read_only=True)
    author_phone = serializers.CharField(source="author.phone", read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    """"Класс-сериализатор для модели Review"""
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_image = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = '__all__'

    def get_author_image(self, obj):
        request = self.context.get("request")
        if obj.author.image:
            return request.build_absolute_uri(obj.author.image.url)
