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
        self.searching_screen = self.create_searching_screen()

        self.sm.add_widget(self.home_screen)
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

        self.searching_btn.bind(on_press=self.go_to_searching)

        btn_layout.add_widget(self.sorting_btn)
        btn_layout.add_widget(self.searching_btn)
        layout.add_widget(btn_layout)

        screen.add_widget(layout)
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

        label3 = Label(text="Enter Target Number", pos_hint={"center_x": 0.2, "top": 1.04})
        layout.add_widget(label3)

        self.input_box_sort = TextInput(size_hint=(0.6, None), height=40, pos_hint={"center_x": 0.66, "top": 0.56})
        layout.add_widget(self.input_box_sort)

        self.spinner_input_sort = Spinner(text="Select Input Type", values=("List", "Dict", "Tuple", "String"), background_color=(0.2, 0.6, 0.86, 1), size_hint=(0.25, None), height=40, pos_hint={"x": 0.20, "top": 0.68})
        layout.add_widget(self.spinner_input_sort)

        self.spinner_algo_sort = Spinner(text="Select Algorithm", values=("Linear", "Binary"), background_color=(0.0, 0.7, 0.3, 1), size_hint=(0.25, None), height=40, pos_hint={"x": 0.55, "top": 0.68})
        layout.add_widget(self.spinner_algo_sort)

        btn_layout = BoxLayout(orientation="horizontal", size_hint=(0.25, None), height=40, pos_hint={"center_x": 0.5, "top": 0.46})
        self.sort_btn = Button(text="SEARCH", background_color=(0, 0.5, 0.5, 1), color=(1, 1, 1, 1))
        btn_layout.add_widget(self.sort_btn)
        self.sort_btn.bind(on_press=self.perform_search) 
        layout.add_widget(btn_layout)

        label4 = Label(text="Output", pos_hint={"center_x": 0.2, "top": 0.78})
        layout.add_widget(label4)

        self.output_box_sort = TextInput(text="", readonly=True, size_hint=(0.6, None), height=40, pos_hint={"center_x": 0.62, "top": 0.30})
        layout.add_widget(self.output_box_sort)

        label5 = Label(text="Iterations", pos_hint={"center_x": 0.2, "top": 0.65})
        layout.add_widget(label5)

        self.iteration_box_sort = TextInput(text="", readonly=True, size_hint=(0.6, None), height=40, pos_hint={"center_x": 0.62, "top": 0.18})
        layout.add_widget(self.iteration_box_sort)

        return screen
    
    def perform_search(self, instance):
    #Get user input
        self.raw_input = self.input_box_search.text.strip()
        self.target = self.input_box_sort.text.strip()
        self.input_type = self.spinner_input_sort.text
        self.algo = self.spinner_algo_sort.text

        def invalid_input():
            self.output_box_sort.text = "Invalid Input"
            self.iteration_box_sort.text = ""
            return None
        
        #Switch case for input type
        def validate_input(expected_type):
            if expected_type == "List" and not (self.raw_input.startswith("[") and self.raw_input.endswith("]")):
                return invalid_input()
            if expected_type == "Tuple" and not (self.raw_input.startswith("(") and self.raw_input.endswith(")")):
                return invalid_input()
            if expected_type == "Dict" and not (self.raw_input.startswith("{") and self.raw_input.endswith("}")):
                return invalid_input()
            if expected_type == "String" and (self.raw_input.startswith("[") or self.raw_input.startswith("(") or self.raw_input.startswith("{")):
                return invalid_input()
            return True  
        
        
        
        def to_list():
            #Example:[10,20,30]
            if not (self.raw_input.startswith("[") and self.raw_input.endswith("]")):
                return invalid_input()
            cleaned = self.raw_input.strip("[]")
            return list(cleaned.replace(",", " ").split())
        
        def to_tuple():
            #Example:(10, 20, 30)
            if not (self.raw_input.startswith("(") and self.raw_input.endswith(")")):
                return invalid_input()
            cleaned = self.raw_input.strip("()")
            return tuple(cleaned.replace(",", " ").split())
            
        def to_dict():
            #Example:{'a':10,'b':20}
            if not (self.raw_input.startswith("{") and self.raw_input.endswith("}")):
                return invalid_input()
            cleaned = self.raw_input.strip("{}").replace(",", " ")
            parts = cleaned.replace(":", " ").split()
            if len(parts) % 2 != 0:
                return None
            temp_dict = {}
            i = 0
            while i < len(parts) - 1:
                temp_dict[parts[i].strip("'").strip('"')] = parts[i + 1]
                i += 2
            return temp_dict

        def to_string():
            #Example:apple banana
             if self.raw_input.startswith("(") or self.raw_input.startswith("{") or self.raw_input.startswith("["):
                 return invalid_input()
             return self.raw_input.split()

        input_switch = {
            "List": to_list,
            "Tuple": to_tuple,
            "Dict": to_dict,
            "String": to_string
        }

        convert_func = input_switch.get(self.input_type,invalid_input)
        data = convert_func()

        if data is None:
            self.output_box_sort.text = "Invalid Input"
            return

        # Prepare values for search
        if self.input_type == "Dict":
            values = list(data.values())
        else:
            values = list(data)


    #Perform Linear Search
        iterations = 0
        found_index = -1
        if self.algo == "Linear":
            for i in range(len(values)):
                iterations += 1
                if str(values[i]) == self.target:
                    found_index = i
                    break

    #Show results
        if found_index != -1:
            self.output_box_sort.text =f"Index: {found_index}"
        else:
            self.output_box_sort.text ="Not Found"

        self.iteration_box_sort.text = str(iterations)


    def go_to_searching(self, instance):
        self.sm.current = "searching"
        
MainApp().run()
