from flet import Container, Row, Column, VerticalDivider, alignment, colors, border_radius, padding
from collections import Counter
from .diagram import DiagramWidget
from .graph import Graph
from .data_table import DataTableWidget
from .themes import *

class StatisticWidget(Container):
    def __init__(self):
        super().__init__()

        self.expand = True

        self.graph = Graph()
        self.packet = DiagramWidget()
        self.data_table = DataTableWidget(self.graph, self.packet)

        self.content = Column(
            expand_loose=True,
            spacing=0,
            controls=[
                Container(
                    expand=2,
                    alignment=alignment.center_left,
                    content=Row(
                        spacing=0,
                        controls=[
                            Container(
                                expand=1,
                                content=self.packet
                            ),
                            VerticalDivider(width=1, thickness=1, color=colors.BLACK26),
                            Container(
                                expand=4,
                                content=Container(content=self.graph, expand=True, bgcolor=PRIMARY)
                            )
                        ]
                    )
                ),
                Container(
                    expand=4,
                    alignment=alignment.center_left,
                    content=self.data_table
                )
            ]
        )