from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

class RequiresView(ObtainAuthToken):
    def post(self, request, format=None):
        return Response(request.data)
