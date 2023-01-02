from recommendations_pb2 import (
    MovieCategory,
    MovieRecommendation,
)

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