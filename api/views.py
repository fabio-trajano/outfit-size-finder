from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import joblib
import os
from .serializers import SizePredictionSerializer

class SizePredictionView(APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Load the trained model
        model_path = os.path.join("machine_learning", "models", "model.pkl")
        self.model = joblib.load(model_path)

    def post(self, request):
        # Validate input data
        serializer = SizePredictionSerializer(data=request.data)
        if serializer.is_valid():
            # Extract data
            data = serializer.validated_data
            features = [[
                data["height"],
                data["weight"],
                data["preference"],
                data["age"],
                data["body_shape"]
            ]]
            # Make prediction
            predicted_size = self.model.predict(features)
            return Response({"predicted_size": predicted_size[0]}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

