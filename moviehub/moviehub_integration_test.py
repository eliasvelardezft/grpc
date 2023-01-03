from urllib.request import urlopen

from recommendations_pb2 import MovieCategory


def test_render_homepage():
    homepage = urlopen("http://localhost:5000").read().decode("utf-8")
    assert f"<h1>{MovieCategory.Name(MovieCategory.SCI_FI)} movies you may like</h1>" in homepage
