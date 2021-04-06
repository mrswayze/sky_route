from graph_search import bfs, dfs
from vc_metro import vc_metro
from vc_landmarks import vc_landmarks
from landmark_choices import landmark_choices

landmark_string=""
for key, value in landmark_choices.items():
    landmark_string += key + ": " + value + "\n"

def greet():
    print("Hi there and welcome to SkyRoute!")