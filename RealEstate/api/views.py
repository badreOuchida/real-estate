from .serializers import PropSerializer , BlogSerializes
from rest_framework.decorators import api_view ,permission_classes,authentication_classes
from rest_framework.generics import ListAPIView
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from django.contrib.auth import authenticate


from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token



from core.models import Propreties , Blogs

import datetime 
    
# using now() to get current time 



# get the data 




class PropertiesAPI(ListAPIView):
    queryset = Propreties.objects.all()
    serializer_class = PropSerializer
    pagination_class = PageNumberPagination
    authentication_classes = ()
    permission_classes = ()
    #filter_backends = (SearchFilter, OrderingFilter)
    #search_fields = ('title', 'body', 'author__username')




class BlogsAPI(ListAPIView):
    queryset = Blogs.objects.all()
    serializer_class = BlogSerializes
    pagination_class = PageNumberPagination
    authentication_classes = ()
    permission_classes = ()




@api_view(['GET'])
@permission_classes([])
def PropertieAPI(request,pk):
    try:
        propretie = Propreties.objects.get(pk=pk)
    except Propreties.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PropSerializer(propretie)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes([])
def BlogAPI(request,pk):
    try:
        blog = Blogs.objects.get(pk=pk)
    except Blogs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BlogSerializes(blog)
        return Response(serializer.data)


# update data 



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def BlogUpdatAPI(request,pk):
    try:
        blog = Blogs.objects.get(pk=pk)
    except Blogs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.data == {}:
        return Response({'response':'You got somethings wrong'})

    if request.method == 'PUT':
        serializer = BlogSerializes(blog,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'response':'data was succsefuly updated',
                'id':blog.id,
                'data-updated': datetime.datetime.now() 
                })

    return Response({'response':'You got somethings wrong'})



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def PropertieUpdatAPI(request,pk):
    try:
        propretie = Propreties.objects.get(pk=pk)
    except Blogs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.data == {}:
        return Response({'response':'You got somethings wrong'})

    if request.method == 'PUT':
        serializer = PropSerializer(propretie,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'response':'data was succsefuly updated',
                'id':propretie.id,
                'data-updated': datetime.datetime.now() 
                })

    return Response({'response':'You got somethings wrong'})


# Add items

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def PropertieAddAPI(request):
    if request.data == {}:
        return Response({'response':'You got somethings wrong'})

    if request.method == 'POST':
        serializer = PropSerializer(data=request.data)
        if serializer.is_valid():
            propertie = serializer.save()
            return Response({
                'response':'data was succsefuly created',
                'id':propertie.id,
                'data-updated': datetime.datetime.now() 
                })

    return Response({'response':'You got somethings wrong'})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def BlogAddAPI(request):
    if request.data == {}:
        return Response({'response':'You got somethings wrong'})

    if request.method == 'POST':
        serializer = BlogSerializes(data=request.data)
        if serializer.is_valid():
            blog = serializer.save()
            return Response({
                'response':'data was succsefuly created',
                'id':blog.id,
                'data-updated': datetime.datetime.now() 
                })

    return Response({'response':'You got somethings wrong'})

# delete items

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def PropertieDeleteAPI(request,pk):
    try:
        propretie = Propreties.objects.get(pk=pk)
    except Blogs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = propertie.delete()
        if operation : 
            return Response({'response':'your operation is succsefuly passed'})

    return Response({'response':'You got somethings wrong'})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def BlogDeleteAPI(request,pk):
    try:
        blog = Blogs.objects.get(pk=pk)
    except Blogs.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = blog.delete()
        if operation : 
            return Response({'response':'your operation is succsefuly passed'})

    return Response({'response':'You got somethings wrong'})




#login


class CustomAuthToken(ObtainAuthToken):

    authentication_classes = []
    permission_classes = []

    def post(self, request):
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username,password=password)

        if user : 

            try :
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)

            return Response({
                'response':'user succsefuly authenticate',
                'token':token.key, 
                })
        else : 
            return Response({
                'response':"Information doesn't match "
                })

