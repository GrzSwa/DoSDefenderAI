from flet import Container, alignment, padding,IconButton,Text,colors, icons, Icon,Offset
from .themes import *

class ActionButtonOne(Container):
    def __init__(self, table: object) -> None:
        super().__init__()
        self.table = table
        self.content = IconButton(
            icon=icons.PLAY_ARROW_ROUNDED,
            icon_size=20,
            icon_color="#525252",
            on_click = lambda e: self.activate(e,table.data_table)
        )

    def activate(self,event, callback):
        if event.control.icon == "play_arrow_rounded":
            event.control.icon = "stop_rounded"
            event.control.update()
            callback.new_packet()
        else:
            event.control.icon = "play_arrow_rounded"
            event.control.update()


class ActionButtonTwo(Container):
    def __init__(self, table: object):
        super().__init__()
        self.table = table
        self.lorem = "DoS Defender AI"
        self.alignment = alignment.center
        self.padding = padding.symmetric(horizontal=10, vertical=5)
        self.content = Text(self.lorem, size=14, color=colors.BLACK)
        self.on_click = lambda e: self.dos_test(e,table.data_table)

    def dos_test(self,event,callback):
        callback.new_packet(True)

class WindowButton(Container):
    def __init__(self, icon, hover_color,callback):
        super().__init__()
        self.icon = icon
        self.hover_color = hover_color
        self.alignment = alignment.center
        self.padding = padding.symmetric(horizontal=15)
        self.on_hover = self.hover_button
        self.content = Icon(
            name=self.icon,
            size=14,
            color="#525252",

        )
        self.on_click = lambda e: callback()

    def hover_button(self,event):
        event.control.bgcolor = self.hover_color if event.data == "true" else None
        event.control.content.color = colors.WHITE if self.hover_color == colors.RED and event.data == "true" else "#525252"
        event.control.update()
