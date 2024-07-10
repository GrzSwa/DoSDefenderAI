from flet import Container, Column, Text, colors, FontWeight, PieChart, PieChartSection, PieChartEvent, Row, padding,TextButton
from .themes import *

class DiagramWidget(Container):
    def __init__(self):
        super().__init__(bgcolor=PRIMARY, padding=padding.only(left=10,top=10))

        self.pieChartValues = {"Attack": 0, "Normal": 1, "Suspect": 0}
        self.title = "Packets"
        self.normal_radius = 37
        self.hover_radius = 42
        self.chart = PieChart(
            sections_space=0,
            center_space_radius=32,
            on_chart_event=self.on_chart_event,
            expand=True,
            sections=self.diagram(self.pieChartValues)[1]
        )


        self.expand = True

        self.content = Column(
            spacing=0,
            controls=[
                Text(self.title, size=16, color=SECONDARY_TEXT, weight=FontWeight.W_500),
                Container(
                    expand=True,
                    content=self.chart
                ),
                Container(
                    height=30,
                    padding=padding.only(left=5),
                    content=Row(
                        controls=self.diagram(self.pieChartValues)[0]

                    )
                ),
            ]
        )

    def update_pie(self, value:dict):
        self.chart.sections = self.diagram(value)[1]
        self.chart.update()
    def on_chart_event(self, e: PieChartEvent) -> None:
        for idx, section in enumerate(self.chart.sections):
            if idx == e.section_index:
                section.radius = self.hover_radius
                section.title = f"{section.value}%"
            else:
                section.radius = self.normal_radius
                section.title = None
        self.chart.update()

    def diagram(self, data:dict):
        values = []
        legends = []
        color = ["#FC451E", "#A648F0", "#A7FFFC"]
        i = 0
        amount = 0
        for value in data.values():
            amount += value


        for label,value in data.items():
            pie = PieChartSection(
                value=round((value/amount)*100),
                color=color[i],
                radius=self.normal_radius,
            )

            leg = Row(
                spacing=3,
                controls=[
                    Container(
                        bgcolor=color[i],
                        width=10,
                        height=10,
                    ),
                    Text(label, size=10, color=SECONDARY_TEXT)
                ]
            )

            i += 1
            values.append(pie)
            legends.append(leg)
        return legends, values


