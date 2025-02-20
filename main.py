from kivy.app import App #para criar o aplicativo
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.icon = "calculator.png"
        self.operators = ['/', '*', '+', '-']
        self.last_was_operator = None
        self.last_button = None
        
        main_layout = BoxLayout(orientation = "vertical")
        self.solution = TextInput(background_color = "black", foreground_color = "white")
        
        main_layout.add_widget(self.solution) #dentro do layout principal, passa ele mesmo e a solution

if __name__ == "__main__":
    app = MainApp()
    app.run()
