import PySimpleGUI as sg

sg.theme('Default1')

class TelaCalcular:
    def __init__(self):
        layout = [
            [sg.Text('Altura:', size=(7, 0)), sg.Input(size=(10, 0), key='altura')],
            [sg.Text('Peso:', size=(7, 0)), sg.Input(size=(10, 0), key='peso')],
            [sg.Text('Situação:', size=(7, 0)), sg.Text('', size=(40, 0), key='resultado')],
            [sg.Button('Calcular', size=(50, 0))]
        ]

        self.janela = sg.Window('Calculadora de IMC').layout(layout)

    def Iniciar(self):
        while True:
            self.button, self.values = self.janela.Read()

            altura = self.values['altura']
            peso = self.values['peso']

            if self.button == 'Calcular':
                imc = float(peso) / (float(altura) * float(altura))

                if imc < 18.5:
                    self.janela['resultado'].update(f'IMC de {imc:.2f} - Abaixo do peso')
                elif 18.5 <= imc <= 24.9:
                    self.janela['resultado'].update(f'IMC de {imc:.2f} - Peso Normal')
                elif 25 <= imc <= 29.9:
                    self.janela['resultado'].update(f'IMC de {imc:.2f} - Sobrepeso')
                elif 25 <= imc <= 29.9:
                    self.janela['resultado'].update(f'IMC de {imc:.2f} - Sobrepeso')
                elif 30 <= imc <= 34.9:
                    self.janela['resultado'].update(f'IMC de {imc:.2f} - Obesidade Grau I')
                elif 35 <= imc <= 39.9:
                    self.janela['resultado'].update(f'IMC de {imc:.2f} - Obesidade Grau II (Severa)')
                elif imc > 40:
                    self.janela['resultado'].update(f'IMC de {imc:.2f} - Obesidade Grau III (Mórbida)')

tela = TelaCalcular()
tela.Iniciar()

