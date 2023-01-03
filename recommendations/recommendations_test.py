from recommendations import RecommendationService
from recommendations_pb2 import MovieCategory, RecommendationRequest

def test_recommendations():
    service = RecommendationService()
    request = RecommendationRequest(
        user_id=1,
        category=MovieCategory.SCI_FI,
        max_results=2
    )
    response = service.Recommend(request, None)
    assert len(response.recommendations) == 2
