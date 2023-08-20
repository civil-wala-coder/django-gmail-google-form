from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UsersSerializers
from .models import Users

@api_view()
def hello_users(request):
    return Response('Hello Users!!!!')

@api_view(['GET'])
def getAllUsers(request):
    users = Users.objects.all()
    serializedUser = UsersSerializers(users, many=True)
    return Response({'data': serializedUser.data})


@api_view(['POST'])
def create_user(request):
    serializedUser = UsersSerializers(data=request.data)
    if serializedUser.is_valid():
        serializedUser.save()
        return Response({'data':serializedUser.data})
    return Response('serializedUser.data not valid!!')