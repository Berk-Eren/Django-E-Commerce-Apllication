class IsUniqueWithPublisher:
    requires_context = True

    def __init__(self, fields):
        self.fields = fields

    def __call__(self, value, serializer_field):
        pass

[
    '''serializers.UniqueTogetherValidator(
                queryset=model.objects.all(),
                fields=['published_by', 'name']
    )'''
    IsUniqueWithPublisher(
        fields = ["name"]
    )
]