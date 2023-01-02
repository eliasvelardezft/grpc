import grpc

from recommendations_pb2 import (
    MovieCategory, RecommendationRequest
)
from recommendations_pb2_grpc import RecommendationsStub

def main():
    channel = grpc.insecure_channel("localhost:50051")
    client = RecommendationsStub(channel)

    request = RecommendationRequest(
        user_id=1,
        category=MovieCategory.SCI_FI,
        max_results=2
    )

    response = client.Recommend(request)

    print(response)


if __name__ == "__main__":
    main()