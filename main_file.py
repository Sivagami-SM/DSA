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
    
    def convert_input(self, raw_input, input_type):
            is_dict_format = ":" in raw_input
            is_list_tuple_format = "," in raw_input and not is_dict_format        

            match input_type:
                case "List":
                     if is_dict_format:
                         return None
                     return [i.strip() for i in raw_input.split(",")]

                case "Tuple":
                     if is_dict_format:
                         return None
                     return tuple(p.strip() for p in raw_input.split(","))

                case "Dictionary":
                    if not is_dict_format:
                        return None
                    sep = raw_input.split(",")
                    data = {}
                    for item in sep:
                        kv = item.split(":")
                        key = kv[0].strip()
                        value_str = kv[1].strip()
                        try:
                            if '.' in value_str:
                                value = float(value_str)
                            else:
                                value = int(value_str)
                        except ValueError:
                            value = value_str
                        data[key] = value
                    return data

                case _:
                    return None

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
        self.sorting_page = SortingScreen(self.sm,self.convert_input) 
        sorting_screen.add_widget(self.sorting_page.layout)
        self.sm.add_widget(sorting_screen)

        searching_screen = Screen(name="searching")
        self.searching_page = SearchingScreen(self.sm,self.convert_input) 
        searching_screen.add_widget(self.searching_page.layout)
        self.sm.add_widget(searching_screen)
        
        self.sm.current = "home"
        return self.sm
    

if __name__ == "__main__":
    MainApp().run()
