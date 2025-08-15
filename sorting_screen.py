from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from Bubblesort import BubbleSort
from Insertionsort import InsertionSort
from Selectionsort import SelectionSort


class SortingScreen:

    def __init__(self,screen_manager):
        self.sm = screen_manager
        self.layout = FloatLayout()

        #colors
        label_color = (0.15, 0.15, 0.15, 1)
        input_bg = (1, 1, 1, 1)
        input_fg = (0.1, 0.1, 0.1, 1)
        button_color = (0.0, 0.6, 0.55, 1)
       
        #Title
        self.layout.add_widget(Label(
            text="[b]SORTING ALGORITHM[/b]",
            markup=True,
            font_size=28,
            color=label_color,
            size_hint=(1, 0.1),
            pos_hint={"x": 0, "top": 0.98}
        ))

        #Enter the data label
        self.layout.add_widget(Label(
            text="[b]ENTER THE INPUT[/b]",
            markup=True,
            size_hint=(0.3, 0.08),
            pos_hint={"x": 0.02, "top": 0.89},
            color=label_color,
            font_size=23
        ))

        #Back button
        back_button = Button(
            text="Back",
            size_hint=(0.15, 0.08),
            pos_hint={"left": 0.85, "top": 0.98},
            background_color=(1, 0.757, 0.027, 1),
            bold=True
        )
        back_button.bind(on_press=self.go_to_home)
        self.layout.add_widget(back_button)


        #Data Input
        self.data_input = TextInput(
            multiline=False,
            size_hint=(0.9, 0.08),
            pos_hint={"x": 0.05, "top": 0.81},
            background_color=input_bg,
            foreground_color=input_fg
        )
        self.layout.add_widget(self.data_input)

        #Data Input Type
        self.input_type = Spinner(
            text="Input Type",
            values=("List", "Tuple", "Dictionary"),
            size_hint=(0.25, 0.08),
            pos_hint={"x": 0.05, "top": 0.68},
            background_color=input_bg,
            color=input_fg
        )
        self.layout.add_widget(self.input_type)

        #Input Type Spinner
        self.sorting_order = Spinner(
            text="Sorting Order",
            values=("Ascending", "Descending"),
            size_hint=(0.25, 0.08),
            pos_hint={"x": 0.375, "top": 0.68},
            background_color=input_bg,
            color=input_fg
        )
        self.layout.add_widget(self.sorting_order)

        #Algorithm spinner
        self.algorithm = Spinner(
            text="Algorithm",
            values=("Bubble Sort", "Insertion Sort","Selection Sort"),
            size_hint=(0.25, 0.08),
            pos_hint={"x": 0.70, "top": 0.68},
            background_color=input_bg,
            color=input_fg
        )
        self.layout.add_widget(self.algorithm)

        #Sorting button
        sort_button = Button(
            text="Sort",
            size_hint=(0.9, 0.08),
            pos_hint={"x": 0.05, "top": 0.58},
            background_color=button_color,
            color=(1, 1, 1, 1),
            bold=True
        )
        sort_button.bind(on_press=self.input_convertion)
        self.layout.add_widget(sort_button)

        #Iterations Label
        self.layout.add_widget(Label(
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
        self.layout.add_widget(self.iter_result)

        #Output Label
        self.layout.add_widget(Label(
            text="[b]Output[/b]",
            markup=True,
            size_hint=(0.2, 0.08),
            pos_hint={"x": 0.05, "top": 0.35},
            color=label_color,
            font_size=18
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
        self.layout.add_widget(self.output_box)

    def input_convertion(self, instance):
        raw_input = self.data_input.text.strip()
        input_type = self.input_type.text
        order = self.sorting_order.text
        
        try:
            match input_type:
                case "List":
                    data = [i.strip() for i in raw_input.split(",")]

                case "Tuple":
                    data = tuple(p.strip() for p in raw_input.split(","))

                case "Dictionary":
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

                case _:
                    self.output_box.text = "Invalid Input Type Selected"
                    return

            
            if self.algorithm.text == "Bubble Sort":
                sorter = BubbleSort(data)
                sorted_data, iterations = sorter.Bubble(order)

                self.output_box.text = str(sorted_data)
                self.iter_result.text = str(iterations)
            
            elif self.algorithm.text == "Insertion Sort":
                sorter = InsertionSort(data)
                sorted_data, iterations = sorter.Insertion(order)

                self.output_box.text = str(sorted_data)
                self.iter_result.text = str(iterations)
            
            elif self.algorithm.text == "Selection Sort":
                sorter = SelectionSort(data)
                sorted_data, iterations = sorter.Selection(order)

                self.output_box.text = str(sorted_data)
                self.iter_result.text = str(iterations)

            else:
                self.output_box.text = "Selected algorithm not implemented yet."
                self.iter_result.text = ""

        except Exception:
            self.output_box.text = "Invalid Input"
            self.iter_result.text = ""


    def go_to_home(self,instance):
        print("Back button pressed!")
        App.get_running_app().root.current = "home"
    

    def get_layout(self):
        return self.layout
