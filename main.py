import flet as ft
from components.statistic import StatisticWidget
from components import themes as t
from components.action_button import ActionButtonOne,ActionButtonTwo,WindowButton
from components.left_bar import LeftBar
def main(page: ft.Page):
    page.adaptive = True
    page.bgcolor = t.BACKGROUND_COLOR
    page.window_frameless = True
    page.window_resizable = True
    page.window_min_width = 1400
    page.window_min_height = 720
    page.spacing = 0
    page.padding = 0

    def minimalize():
        page.window_minimized = True
        page.update()
    def maximalize():
        page.window_maximized = True
        page.update()

    statistic = StatisticWidget()
    ab1:ft.Container = ActionButtonOne(statistic)
    ab2:ft.Container = ActionButtonTwo(statistic)
    page.add(
        ft.Container(
            expand=True,
            border=ft.border.all(1, ft.colors.GREY_400),
            content=ft.Column(
                expand=True,
                spacing=0,
                controls=[
                    ft.WindowDragArea(
                        ft.Container(
                            height=40,
                            border=ft.border.only(bottom=ft.border.BorderSide(1, ft.colors.GREY_400)),
                            gradient=ft.LinearGradient(
                                begin=ft.alignment.center_left,
                                end=ft.alignment.center,
                                stops=[0.0,0.2,0.35],
                                colors=[
                                    "#00ff9f",
                                    "#9df7c0",
                                    t.BACKGROUND_COLOR,
                                ]
                            ),
                            content=ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                controls=[
                                    ft.Container(
                                        content=ft.Row(
                                            controls=[
                                                ft.Container(
                                                    content=ft.IconButton(
                                                        icon=ft.icons.MENU_ROUNDED,
                                                        icon_size=20,
                                                        icon_color="#525252",
                                                        on_click=lambda e: print("Menu")
                                                    )
                                                ),
                                                ab2
                                            ]
                                        )
                                    ),
                                    ft.Container(
                                        content=ft.Row(
                                            alignment=ft.MainAxisAlignment.END,
                                            spacing=6,
                                            controls=[
                                                WindowButton(ft.icons.MINIMIZE_ROUNDED, ft.colors.BLACK12, minimalize),
                                                WindowButton(ft.icons.CHECK_BOX_OUTLINE_BLANK_ROUNDED,
                                                             ft.colors.BLACK12, maximalize),
                                                WindowButton(ft.icons.CLOSE, ft.colors.RED, page.window_destroy)
                                            ]
                                        )
                                    ),

                                ]
                            )
                        )
                    ),
                    ft.Row(
                        expand=True,
                        spacing=0,
                        controls=[
                            LeftBar(ab1),
                            ft.Container(
                                expand=True,
                                alignment=ft.alignment.top_center,
                                margin=0,
                                content=statistic
                            )
                        ]
                    )
                ]
            )
        )

    )


ft.app(main)
