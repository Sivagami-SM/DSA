from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.spinner import Spinner
from kivy.uix.screenmanager import Screen

Window.size = (500, 500)

class HomeScreen:
    def __init__(self):
        self.screen = Screen(name="home")

        layout = BoxLayout(orientation="vertical", padding=30, spacing=40)

        toolbar = Label(text="DSA Algorithm", height=30, color=(1, 1, 1, 1), bold=True, font_size=40)
        layout.add_widget(toolbar)

        btn_layout = BoxLayout(orientation="horizontal", padding=(40, 0), height=50, spacing=25)

        self.sorting_btn = Button(text="Sorting", background_color=(0.29, 0, 0.51, 1), color=(1, 1, 1, 1))
        self.searching_btn = Button(text="Searching", background_color=(0, 0.5, 0.5, 1), color=(1, 1, 1, 1))

        btn_layout.add_widget(self.sorting_btn)
        btn_layout.add_widget(self.searching_btn)
        layout.add_widget(btn_layout)

        self.screen.add_widget(layout)

class SortingScreen:
    def __init__(self):
        self.screen = Screen(name="sorting")
        self.layout = FloatLayout()
        self.screen.add_widget(self.layout)

        label = Label(text="Sorting", size_hint=(1, None), height=70, pos_hint={"top": 1}, bold=True, font_size=30)
        self.layout.add_widget(label)

        label2 = Label(text="Enter Input:", pos_hint={"center_x": 0.2, "top": 1.36})
        self.layout.add_widget(label2)

        self.input_box = TextInput(size_hint=(0.6, None), height=40, pos_hint={"center_x": 0.6, "top": 0.88})
        self.layout.add_widget(self.input_box)

        self.spinner_input = Spinner(text="Select Input Type", values=("List", "Dict", "Tuple", "String"),background_color=(0.2, 0.6, 0.86, 1),size_hint=(0.25, None), height=40, pos_hint={"x": 0.05, "top": 0.79})
        self.layout.add_widget(self.spinner_input)

        self.spinner_order = Spinner(text="Select Order", values=("Ascending", "Descending"),background_color=(1.0, 0.5, 0.0, 1),size_hint=(0.25, None), height=40, pos_hint={"x": 0.4, "top": 0.79})
        self.layout.add_widget(self.spinner_order)

        self.spinner_algo = Spinner(text="Select Algorithm", values=("Bubble", "Insertion", "Selection"),background_color=(0.0, 0.7, 0.3, 1),size_hint=(0.25, None), height=40, pos_hint={"x": 0.7, "top": 0.79})
        self.layout.add_widget(self.spinner_algo)

        label3 = Label(text="Sorted Output:", pos_hint={"center_x": 0.2, "top": 1.08})
        self.layout.add_widget(label3)

        label4 = Label(text="Iterations:", pos_hint={"center_x": 0.2, "top": 1.01})
        self.layout.add_widget(label4)

        self.output_box = Label(text="", size_hint=(0.6, None), height=30, pos_hint={"center_x": 0.5, "top": 0.55})
        self.layout.add_widget(self.output_box)


class SearchingScreen:
    def __init__(self):
        self.screen = Screen(name="searching")
        self.layout = FloatLayout()
        self.screen.add_widget(self.layout)

        label = Label(text="Searching", size_hint=(1, None), height=70, pos_hint={"top": 1}, bold=True, font_size=30)
        self.layout.add_widget(label)

        label2 = Label(text="Enter Input:", pos_hint={"center_x": 0.2, "top": 1.36})
        self.layout.add_widget(label2)

        self.input_box = TextInput(size_hint=(0.6, None), height=40, pos_hint={"center_x": 0.6, "top": 0.88})
        self.layout.add_widget(self.input_box)

        self.spinner_input = Spinner(text="Select Input Type", values=("List", "Dict", "Tuple", "String"),background_color=(0.2, 0.6, 0.86, 1),size_hint=(0.25, None), height=40, pos_hint={"x": 0.05, "top": 0.79})
        self.layout.add_widget(self.spinner_input)

        self.spinner_order = Spinner(text="Select Order", values=("Ascending", "Descending"),background_color=(1.0, 0.5, 0.0, 1),size_hint=(0.25, None), height=40, pos_hint={"x": 0.4, "top": 0.79})
        self.layout.add_widget(self.spinner_order)

        self.spinner_algo = Spinner(text="Select Algorithm", values=("Linear", "Binary"),background_color=(0.0, 0.7, 0.3, 1),size_hint=(0.25, None), height=40, pos_hint={"x": 0.7, "top": 0.79})
        self.layout.add_widget(self.spinner_algo)

        label3 = Label(text="Sorted Output:", pos_hint={"center_x": 0.2, "top": 1.08})
        self.layout.add_widget(label3)

        label4 = Label(text="Iterations:", pos_hint={"center_x": 0.2, "top": 1.01})
        self.layout.add_widget(label4)

        self.output_box = Label(text="", size_hint=(0.6, None), height=30, pos_hint={"center_x": 0.5, "top": 0.55})
        self.layout.add_widget(self.output_box)

class MainApp(App):
    def build(self):
        sm = ScreenManager()

        self.home_screen = HomeScreen()
        self.sorting_screen = SortingScreen()
        self.searching_screen = SearchingScreen()

        self.home_screen.sorting_btn.bind(on_release=self.go_to_sorting)
        self.home_screen.searching_btn.bind(on_release=self.go_to_searching)

        sm.add_widget(self.home_screen.screen)
        sm.add_widget(self.sorting_screen.screen)
        sm.add_widget(self.searching_screen.screen)

        return sm

    def go_to_sorting(self, instance):
        self.root.current = "sorting"

    def go_to_searching(self,instance):
        self.root.current = "searching"

MainApp().run()
