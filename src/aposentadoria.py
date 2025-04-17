import datetime
from datetime import datetime

import flet as ft
from flet import AppBar, View
from flet.core.colors import Colors
from flet.core.dropdown import Option
from flet.core.elevated_button import ElevatedButton
from flet.core.text import Text
from flet.core.types import MainAxisAlignment, CrossAxisAlignment


def main(page: ft.Page):
    page.title = "Exemplo Rotas"
    page.theme_mode = ft.ThemeMode.LIGHT  # ou ft.ThemeMode.DARK
    page.window.width = 375
    page.window.height = 667

    def conta(e):
        salario = int(input_salario.value)
        calcular = (salario * 60) / 100
        return calcular

    def verificar_aposentadoria(e):

        idade = int(input_idade.value)
        contribuicao = int(input_contribuicao.value)

        try:
            if genero.value == "Masculino":
                if categoria.value == "idade":
                    if idade >= 65 and contribuicao >= 15:
                        calcular = conta(e)

                        if contribuicao > 15:
                            ano_excedido = (contribuicao - 15) * 2
                            valor = (ano_excedido / 100) * calcular
                            txt_resultado.value = (f'Você ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {valor}')

                        else:
                            txt_resultado.value = (f'Você ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {calcular}')

                    else:
                        diferenca_idade = idade - 65
                        data_atual = datetime.today().year
                        data_prevista = data_atual - diferenca_idade
                        txt_resultado.value = (f'você não pode se aposentar ainda.\n'
                                               f'Data prevista para sua aposentadoria, ano {data_prevista}')

                else:
                    if contribuicao >= 35:
                        calcular = conta(e)
                        if contribuicao > 35:
                            ano_excedido = (contribuicao - 35) * 2
                            valor = (ano_excedido / 100) + calcular
                            txt_resultado.value = (f'Você ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {valor}')
                        else:
                            txt_resultado.value = (f'Você ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {calcular}')

                    else:
                         diferenca_contribuicao = contribuicao - 35
                         data_atual = datetime.today().year
                         data_prevista = data_atual - diferenca_contribuicao
                         txt_resultado.value = (f'você não pode se aposentar ainda.\n'
                                                f'Data prevista para sua aposentadoria, ano {data_prevista}')




            else:
                if categoria.value == "idade":
                    if idade >= 62 and contribuicao >= 15:
                        calcular = conta(e)
                        if contribuicao > 15:
                            ano_excedido = (contribuicao - 15) * 2
                            valor = (ano_excedido / 100) + calcular
                            txt_resultado.value = (f'Você ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {valor}')

                        else:
                            txt_resultado.value = (f'Você ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {calcular}')


                    else:
                        diferenca_idade = idade - 65
                        diferenca_contribuicao = contribuicao - 15
                        data_atual = datetime.today().year
                        data_prevista = data_atual - diferenca_idade or data_atual - diferenca_contribuicao
                        txt_resultado.value = (f'você não pode se aposentar ainda.\n'
                                               f'Data prevista para sua aposentadoria, ano {data_prevista}')

                else:
                    if contribuicao >= 30:
                        calcular = conta(e)
                        if contribuicao > 30:
                            ano_excedido = (contribuicao - 30) * 2
                            valor = (ano_excedido / 100) + calcular
                            txt_resultado.value = (f'Você ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {valor}')
                        else:
                            txt_resultado.value = (f'Você ja pode se aposentar.\n'
                                                   f'Valor estimado para ser recebido R$ {calcular}')

                    else:
                         diferenca_contribuicao = contribuicao - 30
                         data_atual = datetime.today().year
                         data_prevista = data_atual - diferenca_contribuicao
                         txt_resultado.value = (f'você não pode se aposentar ainda.\n'
                                                f'Data prevista para sua aposentadoria, ano {data_prevista}')

            page.update()
            page.go('/quarta')

        except ValueError as e:
            txt_resultado.value = 'Digite somente numeros'
            page.update()

    def gerenciar_rotas(e):
        page.views.clear()
        page.views.append(
            View(
                "/primeira",
                [
                    AppBar(title=Text(""), bgcolor=Colors.BLUE_100),
                    ft.Image(src="../img.png"),
                    ElevatedButton(text="Simular Aposentadoria", on_click=lambda _: page.go("/segunda")),
                    ElevatedButton(text="Regras", on_click=lambda _: page.go("/terceira"))
                ],
                vertical_alignment=MainAxisAlignment.CENTER,
                horizontal_alignment=CrossAxisAlignment.CENTER,
                bgcolor=Colors.BLUE_100

            )
        )

        if page.route == "/segunda":
            page.views.append(
                View(
                    "/segunda",
                    [
                        AppBar(title=Text("Simulação"), bgcolor=Colors.BLUE_100),
                        Text(value=f"Simulação de Aposentadoria"),
                        input_idade,
                        genero,
                        input_contribuicao,
                        input_salario,
                        categoria,
                        ElevatedButton(text="Enviar", on_click=lambda _: verificar_aposentadoria(e))
                    ],
                    vertical_alignment=MainAxisAlignment.CENTER,
                    horizontal_alignment=CrossAxisAlignment.CENTER,
                    bgcolor=Colors.WHITE
                )
            )


        elif page.route == "/terceira":
            page.views.append(
                View(
                    "/terceira",
                    [
                        AppBar(title=Text("Regras da Aposentadoria"), bgcolor=Colors.BLUE_100),
                        Text(value=f"Aposentadoria por Idade:\n"
                                   f"\nHomens: 65 anos de idade e pelo menos 15 anos de contribuição."
                                   f"\nMulheres: 62 anos de idade e pelo menos 15 anos de contribuição.\n"),

                        Text(value=f"Aposentadoria por Tempo de Contribuição:\n"
                                   f"\nHomens: 35 anos de contribuição."
                                   f"\nMulheres: 30 anos de contribuição.\n"),

                        Text(value=f"Valor Estimado do Benefício:\n"
                                   f"\nO valor da aposentadoria será uma média de 60% da média salarial informada, acrescido de 2% por ano que exceder o tempo mínimo de contribuição.")
                    ],
                    bgcolor=Colors.WHITE
                )
            )


        elif page.route == "/quarta":
            page.views.append(
                View(
                    "/quarta",
                    [
                        AppBar(title=Text("Resultado"), bgcolor=Colors.BLUE_100),
                        txt_resultado,
                    ],
                    bgcolor=Colors.WHITE
                )
            )
        page.update()

    def voltar(e):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    txt_resultado = ft.Text(value="")
    input_idade = ft.TextField(label="Idade", hint_text="idade atual")
    input_contribuicao = ft.TextField(label="Tempo de Contribuição", hint_text="tempo de Contribuição")
    input_salario = ft.TextField(label="Média Salarial", hint_text="média salarial")
    genero = ft.Dropdown(
        label="Gênero",
        width=page.window.width,
        options=[Option(key="Masculino", text="masculino"), Option(key="Feminino", text="feminino")]
    )

    categoria = ft.Dropdown(
        label="Categoria de Aposentadoria",
        width=page.window.width,
        options=[Option(key="idade", text="Aposentadoria por Idade"),
                 Option(key="contribuicao", text="Aposentadoria por Tempo de Contribuição")]
    )

    page.on_route_change = gerenciar_rotas
    page.on_view_pop = voltar
    page.go(page.route)


ft.app(main)
