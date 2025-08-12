from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen

Window.size = (700, 500)
Window.clearcolor = (0.94, 0.94, 0.96, 1)


class SortingApp(App):

    def build_home_screen(self):
        layout = FloatLayout()

        layout.add_widget(Label(
            text="[b]DATA STRUCTURES AND ALGORITHM[/b]",
            markup=True,
            font_size=28,
            color=(0.15, 0.15, 0.15, 1),
            size_hint=(1, 0.2),
            pos_hint={"x": 0, "top": 0.95}
        ))

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

        search_btn = Button(
            text="Search Screen",
            size_hint=(0.5, 0.15),
            pos_hint={"center_x": 0.5, "top": 0.4},
            background_color=(0.2, 0.6, 0.86, 1),
            color=(1, 1, 1, 1),
            bold=True
        )
        layout.add_widget(search_btn)

        return layout

    def build_sorting_screen(self):
        layout = FloatLayout()

        #colors
        label_color = (0.15, 0.15, 0.15, 1)
        input_bg = (1, 1, 1, 1)
        input_fg = (0.1, 0.1, 0.1, 1)
        button_color = (0.0, 0.6, 0.55, 1)
       
        #Title
        layout.add_widget(Label(
            text="[b]SORTING ALGORITHM[/b]",
            markup=True,
            font_size=28,
            color=label_color,
            size_hint=(1, 0.1),
            pos_hint={"x": 0, "top": 0.98}
        ))

        #Enter the data label
        layout.add_widget(Label(
            text="[b]ENTER THE INPUT[/b]",
            markup=True,
            size_hint=(0.3, 0.08),
            pos_hint={"x": 0.02, "top": 0.89},
            color=label_color,
            font_size=23
        ))

        #Back button
        self.back_button = Button(
            text="Back",
            size_hint=(0.15, 0.08),
            pos_hint={"left": 0.98, "top": 0.98},
            background_color=(1, 0.757, 0.027, 1),
            bold=True
        )
        self.back_button.bind(on_press=self.go_home)
        layout.add_widget(self.back_button)


        #Data Label
        self.data_input = TextInput(
            multiline=False,
            size_hint=(0.9, 0.08),
            pos_hint={"x": 0.05, "top": 0.81},
            background_color=input_bg,
            foreground_color=input_fg
        )
        layout.add_widget(self.data_input)

        #Data Input
        self.input_type = Spinner(
            text="Input Type",
            values=("List", "Tuple", "Dictionary", "String"),
            size_hint=(0.25, 0.08),
            pos_hint={"x": 0.05, "top": 0.68},
            background_color=input_bg,
            color=input_fg
        )
        layout.add_widget(self.input_type)

        #Input Type Spinner
        self.sorting_order = Spinner(
            text="Sorting Order",
            values=("Ascending", "Descending"),
            size_hint=(0.25, 0.08),
            pos_hint={"x": 0.375, "top": 0.68},
            background_color=input_bg,
            color=input_fg
        )
        layout.add_widget(self.sorting_order)

        #Algorithm spinner
        self.algorithm = Spinner(
            text="Algorithm",
            values=("Bubble Sort", "Insertion Sort", "Selection Sort"),
            size_hint=(0.25, 0.08),
            pos_hint={"x": 0.70, "top": 0.68},
            background_color=input_bg,
            color=input_fg
        )
        layout.add_widget(self.algorithm)

        #Sorting button
        self.sort_button = Button(
            text="Sort",
            size_hint=(0.9, 0.08),
            pos_hint={"x": 0.05, "top": 0.58},
            background_color=button_color,
            color=(1, 1, 1, 1),
            bold=True
        )
        self.sort_button.bind(on_press=self.input_conversion)
        layout.add_widget(self.sort_button)

        #Iterations Label
        layout.add_widget(Label(
            text="[b]Iterations[/b]",
            markup=True,
            size_hint=(0.2, 0.08),
            pos_hint={"x": 0.05, "top": 0.48},
            color=label_color,
            font_size=25
        ))

        #Iterations box
        self.iter_result = TextInput(
            multiline=False,
            readonly=True,
            size_hint=(0.65, 0.06),
            pos_hint={"x": 0.25, "top": 0.48},
            background_color=input_bg,
            foreground_color=input_fg
        )
        layout.add_widget(self.iter_result)

        #Output Label
        layout.add_widget(Label(
            text="[b]Output[/b]",
            markup=True,
            size_hint=(0.2, 0.08),
            pos_hint={"x": 0.05, "top": 0.35},
            color=label_color,
            font_size=25
        ))

        #Output Box
        self.output_box = TextInput(
            multiline=True,
            readonly=True,
            size_hint=(0.65, 0.20),
            pos_hint={"x": 0.25, "top": 0.35},
            background_color=input_bg,
            foreground_color=input_fg
        )
        layout.add_widget(self.output_box)

        return layout

    def build(self):
        self.sm = ScreenManager()

        home_screen = Screen(name="home")
        home_screen.add_widget(self.build_home_screen())

        self.sorting_screen = Screen(name="sorting")
        self.sorting_screen.add_widget(self.build_sorting_screen())

        self.search_screen = Screen(name="search")
        self.search_screen.add_widget(Label(text="Search screen coming soon!"))

        self.sm.add_widget(home_screen)
        self.sm.add_widget(self.sorting_screen)
        self.sm.add_widget(self.search_screen)

        self.sm.current = "home"
        return self.sm
    
    def go_home(self,instance):
        self.sm.current="home"

    def go_to_sorting(self,instance):
        self.sm.current="sorting"

    def input_conversion(self, instance):
        raw_input = self.data_input.text.strip()
        input_type = self.input_type.text

        try:
            match input_type:
                case "List":
                    data = [i.strip() for i in raw_input.split(",")]

                case "Tuple":
                    data = tuple(p.strip() for p in raw_input.split(","))

                case "Dictionary":
                    data = {}
                    for item in raw_input.split(","):
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

                case "String":
                    data = [i.strip() for i in raw_input.split(",")]
                    for item in data:    
                        try:
                            float(item)
                            self.output_box.text = "Invalid Input Type Selected"
                            return
                        except ValueError:
                            continue

                case _:
                    self.output_box.text = "Invalid Input Type Selected"
                    return

            order = self.sorting_order.text
            if self.algorithm.text == "Insertion Sort":
                sorter = InsertionSort(data)
                sorted_data, iterations = sorter.Insertion(order)
                self.output_box.text = str(sorted_data)
                self.iter_result.text = str(iterations)
            else:
                self.output_box.text = "Selected algorithm not implemented yet."
                self.iter_result.text = ""

        except Exception:
            self.output_box.text = "Invalid Input"
            self.iter_result.text = ""


if __name__ == "__main__":
    SortingApp().run()


