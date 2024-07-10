from flet import (Container, LineChart,LinearGradient,ChartCirclePoint,ChartPointLine,LineChartData,colors,alignment,
                  LineChartDataPoint, ChartAxis, ChartAxisLabel, Text, FontWeight, ChartGridLines)
from .themes import *


class NetworkTrafficChart(LineChart):
    def __init__(self):
        super().__init__()
        self.points = []
        # self.min_x = (int(min(self.points, key=lambda x: x[0][0])) if self.points else None)
        # self.max_x = (int(min(self.points, key=lambda x: x[0][0])) if self.points else None)

        self.min_y = int(min(self.points, key=lambda y: y[1])[1]) if self.points else None
        self.max_y = int(max(self.points, key=lambda y: y[1])[1]) if self.points else None
        self.min_x = int(min(self.points, key=lambda x: x[0])[0]) if self.points else None
        self.max_x = int(max(self.points, key=lambda x: x[0])[0]) if self.points else None

        self.horizontal_grid_lines = ChartGridLines(
            interval=10,
            color=colors.with_opacity(0.1, colors.BLACK54),
            width=0.5
        )
        self.tooltip_bgcolor = colors.with_opacity(0.8, BACKGROUND_COLOR)
        self.bottom_axis = ChartAxis(labels_interval=1, labels_size=25)
        #self.left_axis = ChartAxis(labels_size=10)
        self.expand = True
        self.line = LineChartData(
            color="RED",
            stroke_width=1,
            curved=True,
            stroke_cap_round=True,
            below_line_gradient=LinearGradient(
                begin=alignment.top_center,
                end=alignment.bottom_center,
                colors=[
                    colors.with_opacity(0.25, colors.BLUE_ACCENT),
                    "transparent"
                ]
            )
        )

        self.line.data_points = self.points
        self.data_series = [self.line]

    def create_data_points(self,x,y):
        self.points.append(
            LineChartDataPoint(
                x,
                y,
                show_below_line=True,
                show_above_line=True,
                selected_below_line=ChartPointLine(
                    width=0.5,color=colors.BLACK, dash_pattern=[2,4]
                ),
                selected_point=ChartCirclePoint(stroke_width=1)
            )
        )

        self.update()


