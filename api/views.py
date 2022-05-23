from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Classify
from rest_framework import viewsets, generics, status
from rest_framework import permissions
from rest_framework.decorators import api_view
from api.serializers import  ClassifySerializer, responceSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
import ai
# Create your views here.
# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all().order_by('-date_joined')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.AllowAny]
from tensorflow.keras.models import load_model
import numpy as np
import cv2
# class ClassifyViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Classify.objects.all()
#     serializer_class = ClassifySerializer
#     permission_classes = [permissions.AllowAny]
# @api_view(['POST',])
# def Classify(request):
        
#         classify = Classify()
#         if request.method == "POST":
#             serializer = ClassifySerializer(classify, data=request.data)

#             data = {}

#             image = classify.image()

#             img_arr=cv2.imread(image)

#             img_arr=cv2.resize(img_arr,(224,224))

#             test = np.array(img_arr)
#             test = test/255.0

#             aimodel = load_model("../Documents/Python Scripts/Project Model/aiModel.h5")
#             predict = aimodel.predict(test)
#             data['spam'] = np.argmax(predict)
            
        
#             return Response(data = data, status=status.HTTP_404_NOT_FOUND)  
        
                
class ClassifyImage(APIView):
    serializer_class =ClassifySerializer
    queryset = Classify.objects.all()
    permission_class = permissions.AllowAny
    def post(self, request):
        
        if request.method == "POST":

            classify = Classify()
        
            serializer = ClassifySerializer(classify, data=request.data)
            classify.image = request.data.get('image',"")
            classify.save()
           
            data = {}
            

            image = classify.image

            print(image)
            img_arr=cv2.imread(str(image))

            img_arr=cv2.resize(img_arr,(224,224))

            test = np.array([img_arr])
            test = test/255.0

            aimodel = load_model("ai/aiModel.h5")
            predict = aimodel.predict(test)
           
            print(predict)

            data['spam'] = np.argmax(predict)
            # return Response(status=status.HTTP_200_OK)
            return Response(data = data, status=status.HTTP_200_OK)  
        else:
            data['error'] = 0
            return Response(data = data, status = status.HTTP_404_NOT_FOUND)
# class UserDetailView(generics.GenericAPIView):
#     queryset = [Human.objects.all(), Hero.objects.all()]
#     serializer_class = HumanSerializers
#     permission_classes = [permissions.AllowAny ]
#     def post(self, request):
#         user = User.objects.get(id=request.user.id)

#         if user:
#             ser = UserSerializers(user)
#             return JsonResponse({"user_detail":ser.data}, status=status.HTTP_200_OK)
#         else:
#             return JsonResponse({"error":"User Doesnot exist"}, status=status.HTTP_404_NOT_FOUND)