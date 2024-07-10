from flet import Container, padding, Column, Text, colors, FontWeight, Divider
from .network_traffic import NetworkTrafficChart
from .themes import *

class Graph(Container):
    def __init__(self):
        super().__init__()
        self.padding = padding.symmetric(vertical=15, horizontal=10)
        self.chart = NetworkTrafficChart()
        self.content = Column(
            spacing=0,
            controls=[
                Text("Network traffic", size=16, color=SECONDARY_TEXT, weight=FontWeight.W_500),
                Divider(height=10, opacity=0),
                self.chart
            ]

        )

