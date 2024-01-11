import flet as ft

def main(page: ft.Page):
    page.title = "Calculadora"
    resultado = ft.Text(value="0")

    page.add(
        ft.Row(controls=[resultado]),

        ft.Row(controls=[
            ft.ElevatedButton(text = "AC", expand=1),
            ft.ElevatedButton(text = "+/-", expand=1),
            ft.ElevatedButton(text = "%", expand=1),
            ft.ElevatedButton(text = "/", expand=1),
        ]),

        ft.Row(controls=[
            ft.ElevatedButton(text = "7", expand=1),
            ft.ElevatedButton(text = "8", expand=1),
            ft.ElevatedButton(text = "9", expand=1),
            ft.ElevatedButton(text = "*", expand=1),
        ]),

        ft.Row(controls=[
            ft.ElevatedButton(text = "4", expand=1),
            ft.ElevatedButton(text = "5", expand=1),
            ft.ElevatedButton(text = "6", expand=1),
            ft.ElevatedButton(text = "-", expand=1),
        ]),

        ft.Row(controls=[
            ft.ElevatedButton(text = "1", expand=1),
            ft.ElevatedButton(text = "2", expand=1),
            ft.ElevatedButton(text = "3", expand=1),
            ft.ElevatedButton(text = "+", expand=1),
        ]),

        ft.Row(controls=[
            ft.ElevatedButton(text = "0", expand=2),
            ft.ElevatedButton(text = ".", expand=1),
            ft.ElevatedButton(text = "=", expand=1),
        ]),
    )

ft.app(target=main)