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
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import urllib

# METHOD #1: OpenCV, NumPy, and urllib
def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format

    req = urllib.request.urlopen(url)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1)

    return img
    
                
class ClassifyImage(APIView):
    serializer_class =ClassifySerializer
    queryset = Classify.objects.all()
    permission_class = permissions.AllowAny
    def post(self, request):
        
        if request.method == "POST":

            classify = Classify()
        
            serializer = ClassifySerializer(classify, data=request.data)

            url = request.data.get('image',"")
            print("url......",url)
            image = url_to_image(url)

            data = {}
   
            img_arr=cv2.resize(image,(224,224))

            test = np.array([img_arr])
            test = test/255.0

            aimodel = load_model("ai/model_aug.h5")
           
            predict = aimodel.predict(test)
           
            data['spam'] = np.argmax(predict)
            print(np.argmax(predict))

            return Response(data = data, status=status.HTTP_200_OK)  
        else:
            data['error'] = 0
            return Response(data = data, status = status.HTTP_404_NOT_FOUND)

