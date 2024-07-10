from flet import (Container,MainAxisAlignment,IconButton,icons, Column, LinearGradient, alignment, border,colors,GradientTileMode)

import math
from .local_storage import header,describe

class LeftBar(Container):
    def __init__(self, obj:object):
        super().__init__()
        self.expand = True,
        self.content = Column(
            alignment=MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                Container(
                    expand=True,
                    border=border.only(right=border.BorderSide(1, colors.GREY_400)),
                    content=Column(
                        alignment=MainAxisAlignment.SPACE_BETWEEN,
                        controls=[
                            obj,
                            IconButton(
                                icon=icons.SETTINGS,
                                icon_size=20,
                                icon_color="#525252",
                                on_click=lambda e: print("Settings")
                            ),
                        ]
                    )

                ),
            ]
        )