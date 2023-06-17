import pydot
import os


g = pydot.graph_from_dot_file(os.path.join(os.path.dirname(__file__), 'graph.dot'))[0]
