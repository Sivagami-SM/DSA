from kivy.app import App 
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.spinner import Spinner

Window.size = (500, 500)

class MainApp(App):
    def build(self):
        self.sm = ScreenManager()

        self.home_screen = self.create_home_screen()
        self.sorting_screen = self.create_sorting_screen()
        self.searching_screen = self.create_searching_screen()

        self.sm.add_widget(self.home_screen)
        self.sm.add_widget(self.sorting_screen)
        self.sm.add_widget(self.searching_screen)

        return self.sm

    def create_home_screen(self):
        screen = Screen(name="home")

        layout = BoxLayout(orientation="vertical", padding=30, spacing=40)

        toolbar = Label(text="DSA Algorithm", height=30, color=(1, 1, 1, 1), bold=True, font_size=40)
        layout.add_widget(toolbar)

        btn_layout = BoxLayout(orientation="horizontal", padding=(40, 0), height=50, spacing=25)

        self.sorting_btn = Button(text="Sorting", background_color=(0.29, 0, 0.51, 1), color=(1, 1, 1, 1))
        self.searching_btn = Button(text="Searching", background_color=(0, 0.5, 0.5, 1), color=(1, 1, 1, 1))

        self.sorting_btn.bind(on_press=self.go_to_sorting)
        self.searching_btn.bind(on_press=self.go_to_searching)

        btn_layout.add_widget(self.sorting_btn)
        btn_layout.add_widget(self.searching_btn)
        layout.add_widget(btn_layout)

        screen.add_widget(layout)
        return screen

    def create_sorting_screen(self):
        screen = Screen(name="sorting")
        layout = FloatLayout()
        screen.add_widget(layout)

        label = Label(text="Sorting", size_hint=(1, None), height=70, pos_hint={"top": 0.94}, bold=True, font_size=30)
        layout.add_widget(label)

        label2 = Label(text="Enter Input", pos_hint={"center_x": 0.2, "top": 1.26})
        layout.add_widget(label2)

        self.input_box_sort = TextInput(size_hint=(0.6, None), height=40, pos_hint={"center_x": 0.6, "top": 0.79})
        layout.add_widget(self.input_box_sort)

        self.spinner_input_sort = Spinner(text="Select Input Type", values=("List", "Dict", "Tuple", "String"), background_color=(0.2, 0.6, 0.86, 1), size_hint=(0.25, None), height=40, pos_hint={"x": 0.06, "top": 0.61})
        layout.add_widget(self.spinner_input_sort)

        self.spinner_order_sort = Spinner(text="Select Order", values=("Ascending", "Descending"), background_color=(1.0, 0.5, 0.0, 1), size_hint=(0.25, None), height=40, pos_hint={"x": 0.4, "top": 0.61})
        layout.add_widget(self.spinner_order_sort)

        self.spinner_algo_sort = Spinner(text="Select Algorithm", values=("Bubble", "Insertion", "Selection"), background_color=(0.0, 0.7, 0.3, 1), size_hint=(0.25, None), height=40, pos_hint={"x": 0.7, "top": 0.61})
        layout.add_widget(self.spinner_algo_sort)

        btn_layout = BoxLayout(orientation="horizontal", size_hint=(0.25, None), height=40, pos_hint={"center_x": 0.5, "top": 0.46})
        self.sort_btn = Button(text="SORT", background_color=(0, 0.5, 0.5, 1), color=(1, 1, 1, 1))
        btn_layout.add_widget(self.sort_btn)
        layout.add_widget(btn_layout)

        label3 = Label(text="Sorted Output", pos_hint={"center_x": 0.2, "top": 0.78})
        layout.add_widget(label3)

        self.output_box_sort = TextInput(text="", readonly=True, size_hint=(0.6, None), height=40, pos_hint={"center_x": 0.62, "top": 0.30})
        layout.add_widget(self.output_box_sort)

        label4 = Label(text="Iterations", pos_hint={"center_x": 0.2, "top": 0.65})
        layout.add_widget(label4)

        self.iteration_box_sort = TextInput(text="", readonly=True, size_hint=(0.6, None), height=40, pos_hint={"center_x": 0.62, "top": 0.18})
        layout.add_widget(self.iteration_box_sort)

        return screen

    def create_searching_screen(self):
        screen = Screen(name="searching")
        layout = FloatLayout()
        screen.add_widget(layout)

        label = Label(text="Searching", size_hint=(1, None), height=70, pos_hint={"top": 0.94}, bold=True, font_size=30)
        layout.add_widget(label)

        label2 = Label(text="Enter Input", pos_hint={"center_x": 0.2, "top": 1.26})
        layout.add_widget(label2)

        self.input_box_search = TextInput(size_hint=(0.6, None), height=40, pos_hint={"center_x": 0.6, "top": 0.79})
        layout.add_widget(self.input_box_search)

        self.spinner_input_search = Spinner(text="Select Input Type", values=("List", "Dict", "Tuple", "String"), background_color=(0.2, 0.6, 0.86, 1), size_hint=(0.25, None), height=40, pos_hint={"x": 0.06, "top": 0.61})
        layout.add_widget(self.spinner_input_search)

        self.spinner_order_search = Spinner(text="Select Order", values=("Ascending", "Descending"), background_color=(1.0, 0.5, 0.0, 1), size_hint=(0.25, None), height=40, pos_hint={"x": 0.4, "top": 0.61})
        layout.add_widget(self.spinner_order_search)

        self.spinner_algo_search = Spinner(text="Select Algorithm", values=("Linear", "Binary"), background_color=(0.0, 0.7, 0.3, 1), size_hint=(0.25, None), height=40, pos_hint={"x": 0.7, "top": 0.61})
        layout.add_widget(self.spinner_algo_search)

        btn_layout = BoxLayout(orientation="horizontal", size_hint=(0.25, None), height=40, pos_hint={"center_x": 0.5, "top": 0.46})
        self.search_btn = Button(text="SORT", background_color=(0, 0.5, 0.5, 1), color=(1, 1, 1, 1))
        btn_layout.add_widget(self.search_btn)
        layout.add_widget(btn_layout)

        label3 = Label(text="Sorted Output", pos_hint={"center_x": 0.2, "top": 0.78})
        layout.add_widget(label3)

        self.output_box_display = TextInput(text="", readonly=True, size_hint=(0.6, None), height=40, pos_hint={"center_x": 0.62, "top": 0.30})
        layout.add_widget(self.output_box_display)

        label4 = Label(text="Iterations", pos_hint={"center_x": 0.2, "top": 0.65})
        layout.add_widget(label4)

        self.iteration_box_display = TextInput(text="", readonly=True, size_hint=(0.6, None), height=40, pos_hint={"center_x": 0.62, "top": 0.18})
        layout.add_widget(self.iteration_box_display)

        return screen

    def go_to_sorting(self, instance):
        self.sm.current = "sorting"

    def go_to_searching(self, instance):
        self.sm.current = "searching"

MainApp().run()
