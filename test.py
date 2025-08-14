from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.core.window import Window
from sorting_screen import SortingScreen
from searching_screen import SearchingScreen
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (700, 500)
Window.clearcolor = (0.94, 0.94, 0.96, 1)


class MainApp(App):

    def build_home_screen(self):
        layout = FloatLayout()

        # Title
        layout.add_widget(Label(
            text="[b]DATA STRUCTURES AND ALGORITHM[/b]",
            markup = True,
            font_size=28,
            color=(0.15, 0.15, 0.15, 1),
            size_hint=(1, 0.2),
            pos_hint={"x": 0, "top": 0.95}
        ))

        # Sorting Button → go to sorting screen
        sorting_btn = Button(
            text="Sorting Screen",
            size_hint=(0.5, 0.15),
            pos_hint={"center_x": 0.5, "top": 0.6},
            background_color=(0.0, 0.6, 0.55, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        sorting_btn.bind(on_press=self.go_to_sorting)
        layout.add_widget(sorting_btn)
        

        # Searching Button → go to searching screen
        searching_btn = Button(
            text="Searching Screen",
            size_hint=(0.5, 0.15),
            pos_hint={"center_x": 0.5, "top": 0.4},
            background_color=(0.0, 0.5, 0.75, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        searching_btn.bind(on_press=self.go_to_searching)
        layout.add_widget(searching_btn)
        
        return layout
    
    def go_to_sorting(self, instance):
        self.sm.current = "sorting"

    def go_to_searching(self, instance):
        self.sm.current = "searching"


    def build(self):
        self.sm = ScreenManager()
        
        home_screen = Screen(name="home")
        home_screen.add_widget(self.build_home_screen())
        self.sm.add_widget(home_screen)
        
        sorting_screen = Screen(name="sorting")
        sorting_page = SortingScreen(self.sm) 
        sorting_screen.add_widget(sorting_page.get_layout())
        self.sm.add_widget(sorting_screen)

        searching_screen = Screen(name="searching")
        searching_page = SearchingScreen(self.sm) 
        searching_screen.add_widget(searching_page.get_layout())
        self.sm.add_widget(searching_screen)
        
        self.sm.current = "home"
        return self.sm


if __name__ == "__main__":
    MainApp().run()