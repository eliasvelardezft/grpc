import random

import grpc

from recommendations_pb2 import RecommendationResponse, MovieCategory, MovieRecommendation
from recommendations_pb2_grpc import RecommendationsServicer


movies_by_category = {
    MovieCategory.MYSTERY: [
        MovieRecommendation(id=1, title="Shutter Island"),
        MovieRecommendation(id=2, title="Eyes Wide Shut"),
        MovieRecommendation(id=3, title="Number 23"),
    ],
    MovieCategory.SCI_FI: [
        MovieRecommendation(id=4, title="Interstellar"),
        MovieRecommendation(id=5, title="Inception"),
        MovieRecommendation(id=6, title="Dune"),
    ],
    MovieCategory.ROMANCE: [
        MovieRecommendation(id=7, title="Me Before You"),
        MovieRecommendation(id=8, title="Her"),
        MovieRecommendation(id=9, title="A Star Is Born"),
    ],
}


class RecommendationService(RecommendationsServicer):
    def Recommend(self, request, context):
        if request.category not in movies_by_category:
            context.abort(grpc.StatusCode.NOT_FOUND, "Category not found.")

        movies_for_category = movies_by_category[request.category]
        num_results = min(request.max_results, len(movies_for_category))
        movies_to_recommend = random.sample(
            movies_for_category, num_results
        )

        return RecommendationResponse(recommendations=movies_to_recommend)