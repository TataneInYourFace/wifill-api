from rest_framework.relations import PrimaryKeyRelatedField


class PrimaryKeyGetWholeField(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.class_name = kwargs.pop("class_name", None)
        self.class_serializer = kwargs.pop("class_serializer", None)
        super().__init__(**kwargs)

    def get_queryset(self):
        return self.class_name.objects.all()

    def to_representation(self, value):
        model = self.class_name.objects.get(id=value.pk)
        serializer = self.class_serializer(model)
        return serializer.data
