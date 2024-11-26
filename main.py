from kivy.app import App
from kivy.uix.label import Label

class FoodCalculatorApp(App):
    def build(self):
        return Label(text="Welcome to Food Calculator!")

if __name__ == "__main__":
    FoodCalculatorApp().run()
