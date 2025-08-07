from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.uix.dropdown import DropDown

Window.size = (550, 550)


class HomeScreen(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.set_name_home()

        layout = BoxLayout(orientation="vertical",padding=30, spacing=40)

        toolbar = Label(text="DSA Algorithm", height=30, color=(1, 1, 1, 1), bold=True, font_size=40)
        layout.add_widget(toolbar)

        btn_layout = BoxLayout(orientation = "horizontal",padding = (40, 0),height = 50,spacing = 25)
        
        sorting_btn = Button(text = "Sorting",background_color = (0.29, 0, 0.51, 1),color = (1, 1, 1, 1))
        sorting_btn.bind(on_release=self.go_to_sorting)

        searching_btn = Button(text = "Searching",background_color = (0, 0.5, 0.5, 1),color = (1, 1, 1, 1))
    
        btn_layout.add_widget(sorting_btn)
        btn_layout.add_widget(searching_btn)
        layout.add_widget(btn_layout)

        self.add_widget(layout)

    def set_name_home(self):
        self.name = "home"

    def go_to_sorting(self, instance):
        self.manager.current = "sorting"

class SortingScreen(Screen):
    def __init__(self):
        Screen.__init__(self)
        self.set_name_sorting()

        self.layout = FloatLayout()
        self.add_widget(self.layout)

        label = Label(text = "Sorting",size_hint = (1, None),height = 70,pos_hint = {"top": 1},bold=True,font_size = 30)
        self.layout.add_widget(label)

        label2 = Label(text = "Enter Input:",pos_hint = {"center_x": 0.2, "top": 1.36})
        self.layout.add_widget(label2)

        self.input_box = TextInput(size_hint = (0.6, None),height = 40,pos_hint = {"center_x": 0.6, "top": 0.88})
        self.layout.add_widget(self.input_box)

        self.input_type_btn = Button(text = "Select Input Type",background_color=(0.2, 0.6, 0.86, 1),pos_hint = {"x": 0.05, "top": 0.7},size_hint = (0.25, None),height = 40)
        self.layout.add_widget(self.input_type_btn)
        self.create_input_type_dropdown()

        self.order_btn = Button(text = "Select Order",background_color=(1.0, 0.5, 0.0, 1),pos_hint = {"x": 0.4, "top": 0.7},size_hint = (0.25, None),height = 40)
        self.layout.add_widget(self.order_btn)
        self.create_order_dropdown()

        self.algo_btn = Button(text = "Select Algorithm",background_color=(0.0, 0.7, 0.3, 1),pos_hint = {"x": 0.7, "top": 0.7},size_hint = (0.25, None),height = 40)
        self.layout.add_widget(self.algo_btn)
        self.create_algo_dropdown()

        label3 = Label(text = "Sorted Output:",pos_hint = {"center_x": 0.2, "top": 1.08})
        self.layout.add_widget(label3)

        label4 = Label(text = "Iterations:",pos_hint = {"center_x": 0.2, "top": 1.01})
        self.layout.add_widget(label4)

        self.output_box = Label(text = "",size_hint = (0.6, None),height = 30,pos_hint = {"center_x": 0.5, "top": 0.55})
        self.layout.add_widget(self.output_box)

    def set_name_sorting(self):
        self.name = "sorting"

    def create_input_type_dropdown(self):
        self.dropdown_input = DropDown()

        btn1 = Button(text = "List",size_hint_y = None,height = 44)
        btn1.bind(on_release=self.select_input_list)
        self.dropdown_input.add_widget(btn1)

        btn2 = Button(text = "Dict",size_hint_y = None,height = 44)
        btn2.bind(on_release=self.select_input_dict)
        self.dropdown_input.add_widget(btn2)

        btn3 = Button(text = "Tuple",size_hint_y = None,height = 44)
        btn3.bind(on_release=self.select_input_tuple)
        self.dropdown_input.add_widget(btn3)

        btn4 = Button(text = "String",size_hint_y = None,height = 44)
        btn4.bind(on_release=self.select_input_string)
        self.dropdown_input.add_widget(btn4)

        self.input_type_btn.bind(on_release=self.dropdown_input.open)

    def create_order_dropdown(self):
        self.dropdown_order = DropDown()

        btn1 = Button(text = "Ascending",size_hint_y = None,height = 44)
        btn1.bind(on_release=self.select_order_asc)
        self.dropdown_order.add_widget(btn1)

        btn2 = Button(text = "Descending",size_hint_y = None,height = 44)
        btn2.bind(on_release=self.select_order_desc)
        self.dropdown_order.add_widget(btn2)

        self.order_btn.bind(on_release=self.dropdown_order.open)

    def create_algo_dropdown(self):
        self.dropdown_algo = DropDown()

        btn1 = Button(text = "Bubble",size_hint_y = None,height = 44)
        btn1.bind(on_release=self.select_algo_bubble)
        self.dropdown_algo.add_widget(btn1)

        btn2 = Button(text = "Insertion",size_hint_y = None,height = 44)
        btn2.bind(on_release=self.select_algo_insertion)
        self.dropdown_algo.add_widget(btn2)

        btn3 = Button(text = "Selection",size_hint_y = None,height = 44)
        btn3.bind(on_release=self.select_algo_selection)
        self.dropdown_algo.add_widget(btn3)

        self.algo_btn.bind(on_release=self.dropdown_algo.open)

    # Selection handlers
    def select_input_list(self, instance):
        self.input_type_btn.text = "List"
        self.dropdown_input.dismiss()

    def select_input_dict(self, instance):
        self.input_type_btn.text = "Dict"
        self.dropdown_input.dismiss()

    def select_input_tuple(self, instance):
        self.input_type_btn.text = "Tuple"
        self.dropdown_input.dismiss()

    def select_input_string(self, instance):
        self.input_type_btn.text = "String"
        self.dropdown_input.dismiss()

    def select_order_asc(self, instance):
        self.order_btn.text = "Ascending"
        self.dropdown_order.dismiss()

    def select_order_desc(self, instance):
        self.order_btn.text = "Descending"
        self.dropdown_order.dismiss()

    def select_algo_bubble(self, instance):
        self.algo_btn.text = "Bubble"
        self.dropdown_algo.dismiss()

    def select_algo_insertion(self, instance):
        self.algo_btn.text = "Insertion"
        self.dropdown_algo.dismiss()

    def select_algo_selection(self, instance):
        self.algo_btn.text = "Selection"
        self.dropdown_algo.dismiss()

class MainApp(App):
    def build(self):
        sm = ScreenManager()

        home = HomeScreen()
        sorting = SortingScreen()

        sm.add_widget(home)
        sm.add_widget(sorting)

        return sm

MainApp().run()
