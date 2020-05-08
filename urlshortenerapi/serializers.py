# serializers.py

from rest_framework import serializers

from .models import URL, URLVisit, CustomURL

class CustomURLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomURL
        fields = ('name', 'parent_url', 'created_date')

class URLVisitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = URLVisit
        fields = ('date_visited', 'url')


class URLSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = URL
        fields = ('original_name', 'shortened_version', 'latest_custom_url', 'created_date')

    def _create_custom_url_reference(self, custom_url, parent_url):
        new_custom_url = CustomURL(name=custom_url, parent_url=parent_url)
        new_custom_url.save()

    def create(self, validated_data):
        """
        This method actually functions as an "upsert" on URLs.  Ideally you would have a
        separate Update method but for the sake of time I've violated separation of concerns
        by sticking both operations here.
        """
        url_id = validated_data.get('original_name')
        matching_url = URL.objects.filter(original_name=url_id).first()
        custom_url = validated_data.get('latest_custom_url')
        existing_custom_url = CustomURL.objects.filter(name=custom_url).first()

        if matching_url:

            if not existing_custom_url:
                matching_url.latest_custom_url = validated_data.get('latest_custom_url')
                matching_url.save()
                self._create_custom_url_reference(custom_url, matching_url)

            return matching_url

        new_url = URL.objects.create(**validated_data)

        self._create_custom_url_reference(custom_url, new_url)

        return new_url
