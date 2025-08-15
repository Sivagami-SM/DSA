from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from Linearsearch import LinearSearch
from Binarysearch import BinarySearch
from kivy.app import App


class SearchingScreen:

    def __init__(self,screen_manager,convert_input_fn):
        self.sm = screen_manager
        self.convert_input = convert_input_fn
        self.layout = FloatLayout()

         #colors
        label_color = (0.15, 0.15, 0.15, 1)
        input_bg = (1, 1, 1, 1)
        input_fg = (0.1, 0.1, 0.1, 1)
        button_color = (0.0, 0.6, 0.55, 1)
       
        #Title
        self.layout.add_widget(Label(
            text="[b]SEARCHING ALGORITHM[/b]",
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
    

        #Data Label
        self.data_input = TextInput(
            multiline=False,
            size_hint=(0.9, 0.08),
            pos_hint={"x": 0.05, "top": 0.81},
            background_color=input_bg,
            foreground_color=input_fg
        )
        self.layout.add_widget(self.data_input)

        #Data Input
        self.input_type = Spinner(
            text="Input Type",
            values=("List", "Tuple", "Dictionary"),
            size_hint=(0.25, 0.08),
            pos_hint={"x": 0.15, "top": 0.68},
            background_color=input_bg,
            color=input_fg
        )
        self.layout.add_widget(self.input_type)

        #Target Label
        self.layout.add_widget(Label(
            text="[b]Enter Target Number[/b]",
            markup=True,
            size_hint=(0.2, 0.08),
            pos_hint={"x": 0.05, "top": 0.53},
            color=label_color,
            font_size=20
        ))

        #Target input box
        self.target_input = TextInput(
            multiline=False,
            size_hint=(0.65, 0.10),
            pos_hint={"x": 0.25, "top": 0.53},
            background_color=input_bg,
            foreground_color=input_fg
        )
        self.layout.add_widget(self.target_input)

        #Algorithm spinner
        self.algorithm = Spinner(
            text="Algorithm",
            values=("Linear Search", "Binary Search"),
            size_hint=(0.25, 0.08),
            pos_hint={"x": 0.55, "top": 0.68},
            background_color=input_bg,
            color=input_fg
        )
        self.layout.add_widget(self.algorithm)

        #Searching button
        search_button = Button(
            text="Search",
            size_hint=(0.9, 0.08),
            pos_hint={"x": 0.05, "top": 0.39},
            background_color=button_color,
            color=(1, 1, 1, 1),
            bold=True
        )
        search_button.bind(on_press=self.input_conversion)
        self.layout.add_widget(search_button)

        #Iterations Label
        self.layout.add_widget(Label(
            text="[b]Iterations[/b]",
            markup=True,
            size_hint=(0.2, 0.08),
            pos_hint={"x": 0.05, "top": 0.26},
            color=label_color,
            font_size=25
        ))

        #Iterations  box
        self.iter_result = TextInput(
            multiline=False,
            readonly=True,
            size_hint=(0.65, 0.10),
            pos_hint={"x": 0.25, "top": 0.28},
            background_color=input_bg,
            foreground_color=input_fg
        )
        self.layout.add_widget(self.iter_result)

        #Output Label
        self.layout.add_widget(Label(
            text="[b]Output[/b]",
            markup=True,
            size_hint=(0.2, 0.08),
            pos_hint={"x": 0.05, "top": 0.15},
            color=label_color,
            font_size=25
        ))

        #Output Box
        self.output_box = TextInput(
            multiline=True,
            readonly=True,
            size_hint=(0.65, 0.10),
            pos_hint={"x": 0.25, "top": 0.15},
            background_color=input_bg,
            foreground_color=input_fg
        )
        self.layout.add_widget(self.output_box)

        
    def input_conversion(self, instance):
        raw_input = self.data_input.text.strip()
        target = self.target_input.text.strip()
        input_type = self.input_type.text

        try:
            data = self.convert_input(raw_input, input_type)
            if data is None:
                self.output_box.text = "Invalid Input Type Selected"
                return
           
            if self.algorithm.text == "Linear Search":
                searcher = LinearSearch(data)
                searched_data, iterations = searcher.Linear(target)
                self.output_box.text = str(searched_data)
                self.iter_result.text = str(iterations)

            elif self.algorithm.text == "Binary Search":
                searcher = BinarySearch(data)
                searched_data, iterations = searcher.Binary(target)
                self.output_box.text = str(searched_data)
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
