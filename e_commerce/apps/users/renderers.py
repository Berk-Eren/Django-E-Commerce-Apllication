from rest_framework import renderers



class UserRenderer(renderers.JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        print(data, accepted_media_type, renderer_context)
        return super().render(data, accepted_media_type, renderer_context)