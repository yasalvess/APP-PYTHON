from kivy.app import App #para criar o aplicativo
from kivy.uix.boxlayout import BoxLayout #para organizazr os widgeta em uma estrutra de layout vertical
from kivy.uix.button import Button #para adicionar botões
from kivy.uix.textinput import TextInput #para entrada e exibição de texto

class MainApp(App): #a classe  herda 'App' que é a base de qualquer aplicativo no Kivy
    def build(self): #o método build define a interfaze do aplicativo
        self.icon = "calculator.png" #definindo um icone para o app
        self.operators = ['/', '*', '+', '-'] # lista de operadores que serão usados na calculadora
        self.last_was_operator = None #variaveis de controle para verificar o último botão pressionado
        self.last_button = None
        
        main_layout = BoxLayout(orientation = "vertical") #layout vertical
        self.solution = TextInput(background_color = "black", foreground_color = "white") # criação da caixa de texto onde os números e operações aparecerão
        
        main_layout.add_widget(self.solution) #Adiciona o textInput ao layout principal, passa ele mesmo e a solution
        
        buttons = [ #estrutura do botão
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]
        #row representa uma linha de botões
        for row in buttons: #iniviando um loop que percorre cada sublista dentro da lista buttons
            h_layout = BoxLayout() #criando um layout horizontal para cada linha
            #a variavél label representa um único botão dentro da linha
            for label in row: #dentro de cada row, iniciamos outro loop para percorrer os elementos dessa linha
                button = Button( #criano um botão para cada item da linha
                    text = label, font_size= 30, background_color = "grey",
                    pos_hint= {"center_x": 0.5, "center_y": 0.5}, #centraliza o botão no eixo horizontal e vertical dentro do layout
                )
                button.bind(on_press= self.on_button_press) #tornando o botão funcional ao pressionar
                h_layout.add_widget(button) #adicionao o botão criado ao layout horizontal
            main_layout.add_widget(h_layout) #adicionando a linha ao main_layout, que contém toda interface do aplicativo
        
        equal_button = Button(
            text = "=", font_size= 30, background_color = "grey",
            pos_hint= {"center_x": 0.5, "center_y": 0.5}, 
        )
        equal_button.bind(on_press = self.on_solution) #liga a função ao botão para ser executada quando ele for pressionado
        main_layout.add_widget(equal_button)  #add o botão ao layout
        
        return main_layout #return para exibir a interface
    
    def on_button_press(self, instance): #instance é o botão que foi pressionado
        current = self.solution.text #obtendo o texto atual da calculadora, que contem os numeros e op digitados
        button_text = instance.text # obtem o texto do botão que foi pressionado
        
        if button_text == 'C':
            self.solution.text = ''
if __name__ == "__main__":
    app = MainApp()
    app.run()
