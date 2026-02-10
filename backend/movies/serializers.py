from shared.serializers import BaseSerializer


class MovieSerializer(BaseSerializer):
    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'title': instance.title,
            'duration': str(instance.duration),
            'genre': GenreSerializer(instance.genre).serialize(),
        }
    


class GenreSerializer(BaseSerializer):
    def serialize_instance(self, instance) -> dict:
        return {
            'id': instance.pk,
            'name': instance.name,
            'description': instance.description,
        }
    
    