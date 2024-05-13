import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QHBoxLayout

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.layout = QVBoxLayout()

        self.numero_um_label = QLabel("Numero um")
        self.numero_um = QLineEdit()
        
        self.numero_dois_label = QLabel("Numero dois")
        self.numero_dois = QLineEdit("Numero dois")
        self.resultado_label = QLabel()
        
        self.botoes_layout = QHBoxLayout()

        self.layout.addWidget(self.numero_um_label)
        self.layout.addWidget(self.numero_um)
        
        self.layout.addWidget(self.numero_dois_label)
        self.layout.addWidget(self.numero_dois)

        self.soma_button = QPushButton("+")
        self.subtracao_button = QPushButton("-")
        self.multiplicacao_button = QPushButton("*")
        self.divisao_button = QPushButton("/")

        self.soma_button.clicked.connect(self.somar)
        self.subtracao_button.clicked.connect(self.subtrair)
        self.multiplicacao_button.clicked.connect(self.multiplicar)
        self.divisao_button.clicked.connect(self.dividir)

        self.botoes_layout.addWidget(self.soma_button)
        self.botoes_layout.addWidget(self.subtracao_button)
        self.botoes_layout.addWidget(self.multiplicacao_button)
        self.botoes_layout.addWidget(self.divisao_button)

        self.layout.addLayout(self.botoes_layout)
        self.layout.addWidget(self.resultado_label)

        self.setLayout(self.layout)

    def somar(self):
        try:
            resultado = float(self.numero_um.text()) + float(self.numero_dois.text())
            self.resultado_label.setText(f"Resultado: {resultado}")
        except ValueError:
            self.resultado_label.setText("Erro: Insira números válidos")

    def subtrair(self):
        try:
            resultado = float(self.numero_um.text()) - float(self.numero_dois.text())
            self.resultado_label.setText(f"Resultado: {resultado}")
        except ValueError:
            self.resultado_label.setText("Erro: Insira números válidos")

    def multiplicar(self):
        try:
            resultado = float(self.numero_um.text()) * float(self.numero_dois.text())
            self.resultado_label.setText(f"Resultado: {resultado}")
        except ValueError:
            self.resultado_label.setText("Erro: Insira números válidos")

    def dividir(self):
        try:
            resultado = float(self.numero_um.text()) / float(self.numero_dois.text())
            self.resultado_label.setText(f"Resultado: {resultado}")
        except ValueError:
            self.resultado_label.setText("Erro: Insira números válidos")
        except ZeroDivisionError:
            self.resultado_label.setText("Erro: Divisão por zero")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculadora()
    window.show()
    sys.exit(app.exec_())
