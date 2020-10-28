from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.decorators import api_view,authentication_classes
from rest_framework import status
from tank.models import Tank
from tank.serializers import TankSerializer

from rest_framework import generics


class TankListCreateView(generics.ListCreateAPIView):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer
    lookup_field = 'id'

    def create(self,request):
        serializer = TankSerializer(data = request.data)
        if serializer.is_valid():
            data = serializer.validated_data

            tank = Tank.objects.create(
                        tank_name= data.get('tank_name'),
                        product = data.get('product'),
                        capacity = data.get("capacity"),
                        owner_id = request.user
            )

            serialized_data = TankSerializer(tank).data
            
            return Response(serialized_data,status=status.HTTP_201_CREATED)
        return Response({"message":"invalid data","data":request.data},status=status.HTTP_400_BAD_REQUEST)


class TankDetailUpdateView(generics.RetrieveUpdateAPIView):
    
    queryset = Tank.objects.all()
    serializer_class = TankSerializer
    # permission_classes = [IsAdminUser]
    lookup_field = 'id'
    












@api_view(['POST','GET','PUT'])
def TankView(request,*args, **kwargs):
    try:
        

        if request.method == 'POST' and not kwargs.get('id'):
            # endpoint to create a tank
            # user has to be authenticated
            serializer = TankSerializer(data = request.data)
            if serializer.is_valid():
                data = serializer.validated_data

                tank = Tank.objects.create(
                            tank_name= data.get('tank_name'),
                            product = data.get('product'),
                            capacity = data.get("capacity"),
                            owner_id = request.user
                )

                serialized_data = TankSerializer(tank).data
                
                return Response(serialized_data,status=status.HTTP_201_CREATED)
            return Response({"message":"invalid data","data":request.data},status=status.HTTP_400_BAD_REQUEST)







        if (request.method == 'PUT' or request.method == 'POST') and kwargs.get('id'):
            # endpoint to update a specify tank
            # user has to be authenticated
            tank_list = Tank.objects.filter(owner_id=request.user,id=kwargs.get("id"))
            serializer = TankSerializer(data = request.data)
            if serializer.is_valid():
                data = serializer.validated_data
                tank_updated_list = tank_list.update(**data)
                return Response(data,status=status.HTTP_200_OK)
            return Response({"message":"invalid data","data":request.data},status=status.HTTP_400_BAD_REQUEST)





        if request.method == 'GET':
            # endpoint return a list of tanks
            # endpoint return a single tank when query with and id
            if kwargs.get('id'):
                tank = Tank.objects.get(id=kwargs.get('id'))
                serializer = TankSerializer(tank)
                return Response(serializer.data)
            tank = Tank.objects.all()
            serializer = TankSerializer(tank,many=True)
            return Response(serializer.data)

        return Response({"message": "unauthorized method"},status=status.HTTP_401_UNAUTHORIZED)
    except Exception as e:
        print(e)
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

