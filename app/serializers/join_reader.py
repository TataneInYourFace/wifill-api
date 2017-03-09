from rest_framework import serializers


class JoinReader(serializers.ModelSerializer):
    class Meta:
        join_fields = {}

    def create_joins(self, validated_data):
        array = []
        for key, class_name in self.Meta.join_fields.items():
            if key in validated_data:
                array.append({
                    "class_name": class_name,
                    "data": validated_data.pop(key)
                })
        return array

    def update_joins(self, user, validated_data):
        array = []
        for key, class_name in self.Meta.join_fields.items():
            if key in validated_data:
                data = validated_data.pop(key)
                join_ids = []
                for join in data:
                    id_join = join.get("id")
                    if id_join is not None:
                        join_ids.append(id_join)
                join_set = class_name.objects.filter(user=user)
                for join in join_set:
                    if join.id not in join_ids:
                        join.delete()
                array.append({
                    "class_name": class_name,
                    "data": data
                })
        return array
