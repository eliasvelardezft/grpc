import os

from flask import Flask, render_template
import grpc

from recommendations_pb2 import MovieCategory, RecommendationRequest
from recommendations_pb2_grpc import RecommendationsStub

app = Flask(__name__)

recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "localhost")
recommendations_channel = grpc.insecure_channel(f"{recommendations_host}:50051")
recommendations_client = RecommendationsStub(recommendations_channel)


@app.route("/")
def render_homepage():
    recommendations_request = RecommendationRequest(
        user_id=1,
        category=MovieCategory.SCI_FI,
        max_results=2,
    )
    recommendations_response = recommendations_client.Recommend(recommendations_request)
    return render_template(
        "home.html",
        recommendations=recommendations_response.recommendations,
        category_name=MovieCategory.Name(MovieCategory.SCI_FI),
    )