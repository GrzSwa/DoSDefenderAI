import time
from flet import (Container, DataTable, DataColumn, Text, FontWeight, Column, ScrollMode, DataRow, DataCell, Row, colors, MainAxisAlignment,
                  BoxShadow, padding,alignment,border,Icon,icons,Offset,ShadowBlurStyle,TextAlign)
from .themes import *
import random
from sniffer.sniffer import Sniffer, save_file
from .local_storage import dos
class DataTableWidget(Container):
    def __init__(self, chart: object, pie:object):
        super().__init__()
        self.chart = chart
        self.pie = pie
        self.pie_value = {"Attack": 0, "Normal": 0, "Suspect": 0}
        self.x = 0
        self.amount = 0
        self.table = DataTable(
            columns=[
                DataColumn(Text("Timestamp", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
                DataColumn(Text("Source IP", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
                DataColumn(Text("Packets Amount", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
                DataColumn(Text("Destination Port", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
                DataColumn(Text("Avg packet size", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
                DataColumn(Text("Protocol", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
                DataColumn(Text("Flow Duration", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
                DataColumn(Text("Label", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
            ],
            width=2000,
            expand=True,
            heading_row_height=0,
            data_row_max_height=40,
        )
        self.header = DataTable(
            columns=[
                DataColumn(Text("Timestamp", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
                DataColumn(Text("Source IP", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
                DataColumn(Text("Packets Amount", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
                DataColumn(Text("Destination Port", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
                DataColumn(Text("Avg packet size", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
                DataColumn(Text("Protocol", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
                DataColumn(Text("Flow Duration", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
                DataColumn(Text("Label", weight=FontWeight.W_500, color=SECONDARY_TEXT)),
            ],
            width=2000,
            expand=True,
            heading_row_height=35,
            data_row_max_height=40,


        )
        self.packet_amount = Text("0 items", color=PRIMARY_TEXT)
        self.content = Container(
            expand=True,
            bgcolor=PRIMARY,
            content=Column(
                expand=True,
                alignment=MainAxisAlignment.START,
                spacing=1,
                controls=[
                    Container(
                        bgcolor=colors.WHITE,
                        border=border.only(top=border.BorderSide(1, colors.GREY_400), bottom=border.BorderSide(1, colors.GREY_400)),
                        content=self.header,
                        padding=padding.symmetric(vertical=5),
                        shadow=BoxShadow(
                            spread_radius=-15,
                            blur_radius=15,
                            color=colors.BLUE_GREY_300,
                            offset=Offset(0.0, 10.0),
                            blur_style=ShadowBlurStyle.NORMAL
                        )
                    ),
                    Container(
                        expand=True,
                        content=Column(
                            controls=[
                                Column(
                                    expand=True,
                                    scroll=ScrollMode.ADAPTIVE,
                                    controls=[self.table]
                                ),
                                Container(
                                    alignment=alignment.center,
                                    bgcolor=BACKGROUND_COLOR,
                                    border=border.only(top=border.BorderSide(1, colors.GREY_400)),
                                    content=Row(
                                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                                        controls=[
                                            Container(
                                                content=self.packet_amount,
                                                padding=padding.symmetric(horizontal=5,vertical=2)
                                            ),
                                            Container(
                                                padding=padding.symmetric(horizontal=5,vertical=2),
                                                on_click=lambda e: save_file(),
                                                content=Row(
                                                    alignment=MainAxisAlignment.END,
                                                    spacing=2,
                                                    controls=[
                                                        Icon(name=icons.SAVE,color=PRIMARY_TEXT, size=14),
                                                        Text("Export data", color=PRIMARY_TEXT, size=13)
                                                    ]
                                                )
                                            )
                                        ]
                                    )
                                )
                            ]
                        )
                    )
                ]
            )
        )


    def update_data(self, src_ip,flow_pkt,dst_port,packet_length,protocol,flow_dur,label,amount = 1):
        timestamp = int(time.time())
        data = DataRow(
            color=colors.with_opacity(0.9,colors.RED) if label == "DoS" else None,
            cells=[
                DataCell(Text(str(timestamp), color=PRIMARY_TEXT)),
                DataCell(Text(src_ip, color=PRIMARY_TEXT)),
                DataCell(Text(flow_pkt, color=PRIMARY_TEXT)),
                DataCell(Text(dst_port, color=PRIMARY_TEXT)),
                DataCell(Text(str(packet_length), color=PRIMARY_TEXT)),
                DataCell(Text(protocol, color=PRIMARY_TEXT)),
                DataCell(Text(str(flow_dur), color=PRIMARY_TEXT)),
                DataCell(Text(label, color=PRIMARY_TEXT)),
            ]
        )
        if label == "DoS":
            self.pie_value ["Attack"] += 1
        elif label == "Normal":
            self.pie_value ["Normal"] += 1
        else:
            self.pie_value ["Suspect"] += 1

        self.amount += amount
        self.table.rows.append(data)
        self.pie.update_pie(self.pie_value)
        self.table.update()
        self.packet_amount.value = f"{self.amount} Items"
        self.packet_amount.update()
        return timestamp


    def new_packet(self, dos_test=False):
        sniffer = Sniffer()
        if dos_test:
            sniffer.dos_test(dos,self.chart.chart.create_data_points, self.update_data)
        else:
            sniffer.run(self.chart.chart.create_data_points, self.update_data)

    # def new_packet(self):
    #     i = 0
    #     tmp = ""
    #     p = ""
    #     while i < 10:
    #         ip = f"{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}"
    #
    #         packet = random.randint(0, 200)
    #         pro = "TCP" if random.randint(0, 2) % 2 == 0 else "UDP"
    #         if tmp == "" and p == "":
    #             tmp = ip
    #             p = pro
    #         self.update_data(
    #             src_ip=ip,
    #             flow_pkt=random.randint(0, 65535),
    #             dst_port=random.randint(0, 65535),
    #             packet_length=packet,
    #             protocol=pro,
    #             flow_dur=random.randint(0, 100),
    #             label="Normal" if i != 8 else "DoS"
    #         )
    #         self.chart.chart.create_data_points(self.x, packet)
    #         self.x += 1
    #         i += 1
    #         time.sleep(1)
    #
    #     self.update_data(
    #         src_ip=tmp,
    #         flow_pkt=random.randint(0, 65535),
    #         dst_port=random.randint(0, 65535),
    #         packet_length=random.randint(0, 200),
    #         protocol=p,
    #         flow_dur=random.randint(0, 100),
    #         label="Normal"
    #     )
