from rest_framework.relations import PrimaryKeyRelatedField


class PrimaryKeyOnGetWholeField(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.class_name = kwargs.pop("class_name", None)
        self.class_serializer = kwargs.pop("class_serializer", None)
        PrimaryKeyRelatedField.__init__(self, **kwargs)

    def get_queryset(self):
        return self.class_name.objects.all()

    def to_representation(self, value):
        try:
            model = self.class_name.objects.get(id=value.pk)
        except self.class_name.DoesNotExist:
            return None
        serializer = self.class_serializer(model)
        return serializer.data
