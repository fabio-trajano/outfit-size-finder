import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import joblib
import os
import json
from .serializers import SizePredictionSerializer

# Load the model at module level to avoid reloading it for every request
MODEL_PATH = os.path.join("machine_learning", "models", "model.pkl")
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")
MODEL = joblib.load(MODEL_PATH)

class SizePredictionView(APIView):
    """
    POST endpoint to predict the clothing size using a logistic regression model based on user inputs.
    
    Expects the following JSON body:
    {
        "height": float,
        "weight": float,
        "preference": "tight" | "loose" | "regular",
        "age": int,
        "body_shape": "slim" | "average" | "athletic" | "plus-size"
    }

    Returns:
    - HTTP 200: {"predicted_size": "XXS" | "XS" | "S" | "M" | "L" | "XL" | "XXL"}
    - HTTP 400: {"error": "Invalid input data"}
    """
    def post(self, request):
        # Validate input data
        serializer = SizePredictionSerializer(data=request.data)
        if serializer.is_valid():
            # Extract data
            data = serializer.validated_data
            # Convert input to a DataFrame with appropriate column names
            features = pd.DataFrame([[
                data["height"],
                data["weight"],
                data["preference"],
                data["age"],
                data["body_shape"]
            ]], columns=["height", "weight", "preference", "age", "body_shape"])
            # Make prediction
            predicted_size = MODEL.predict(features)
            return Response({"predicted_size": predicted_size[0]}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ModelMetricsView(APIView):
    """
    GET endpoint to retrieve the evaluation metrics of the trained model.
    Returns:
    - HTTP 200: JSON object with metrics (precision, recall, F1-score, etc.)
    - HTTP 500: {"error": "Metrics file not found"}
    """
    def get(self, request):
        metrics_path = os.path.join("machine_learning", "models", "metrics.json")
        try:
            with open(metrics_path, "r") as f:
                metrics = json.load(f)
            return Response(metrics, status=status.HTTP_200_OK)
        except FileNotFoundError:
            return Response({"error": "Metrics file not found"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
