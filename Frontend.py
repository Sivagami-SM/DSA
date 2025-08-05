from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.menu import MDDropdownMenu
from kivy.core.window import Window
from kivy.metrics import dp

Window.size = (550, 550)


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.theme_style = "Light"

        self.sm = MDScreenManager()

        self.home_screen = self.create_home_screen()
        self.sorting_screen = self.create_sorting_screen()

        self.sm.add_widget(self.home_screen)
        self.sm.add_widget(self.sorting_screen)

        return self.sm

    def create_home_screen(self):
        screen = MDScreen(name="home")
        layout = MDBoxLayout(orientation="vertical", padding=30, spacing=40)

        toolbar = MDTopAppBar(title="DSA Algorithm", pos_hint={"top": 1}, md_bg_color="indigo")
        layout.add_widget(toolbar)

        btn_layout = MDBoxLayout(orientation="horizontal", spacing=25, size_hint_y=None, height=200, padding=(40, 0))

        sorting_btn = MDRaisedButton(
            text="Sorting",
            md_bg_color="indigo",
            text_color="white",
            pos_hint={"center_x": 0.5}
        )
        sorting_btn.bind(on_release=self.go_to_sorting)

        searching_btn = MDRaisedButton(
            text="Searching",
            md_bg_color="teal",
            text_color="white",
            pos_hint={"center_x": 0.5}
        )

        btn_layout.add_widget(sorting_btn)
        btn_layout.add_widget(searching_btn)

        layout.add_widget(btn_layout)
        screen.add_widget(layout)

        return screen

    def go_to_sorting(self, instance):
        self.sm.current = "sorting"

    def create_sorting_screen(self):
        screen = MDScreen(name="sorting")
        layout = MDBoxLayout(orientation="vertical", padding=20, spacing=20)

        toolbar = MDTopAppBar(title="Sorting", pos_hint={"top": 1}, md_bg_color="indigo")
        layout.add_widget(toolbar)

        layout.add_widget(MDLabel(text="Enter Input:", halign="center", theme_text_color="Secondary"))
        self.input_box = MDTextField(hint_text="", size_hint_x=0.9, pos_hint={"center_x": 0.5})
        layout.add_widget(self.input_box)

        # Dropdown for Input Type
        layout.add_widget(MDLabel(text="Input Type:", halign="left",theme_text_color="Secondary"))
        self.input_type_button = MDRaisedButton(text="Select Input Type", pos_hint={"center_x": 0.5},md_bg_color="teal")
        layout.add_widget(self.input_type_button)
        self.init_input_type_menu()

        # Dropdown for Sorting Order
        layout.add_widget(MDLabel(text="\nSorting Order:", halign="left", theme_text_color="Secondary"))
        self.order_button = MDRaisedButton(text="Select Order", pos_hint={"center_x": 0.5},md_bg_color="green")
        layout.add_widget(self.order_button)
        self.init_order_menu()

        # Dropdown for Algorithm
        layout.add_widget(MDLabel(text="\nAlgorithm:", halign="left", theme_text_color="Secondary"))
        self.algo_button = MDRaisedButton(text="Select Algorithm", pos_hint={"center_x": 0.5},md_bg_color="indigo")
        layout.add_widget(self.algo_button)
        self.init_algo_menu()

        # Output Box
        layout.add_widget(MDLabel(text="\n\nSorted Output:", halign="left", theme_text_color="Secondary"))
        self.output_box = MDTextField(
            hint_text="",
            readonly=True,
            size_hint_x=0.9,
            pos_hint={"center_x": 0.5}
        )
        layout.add_widget(self.output_box)

        screen.add_widget(layout)
        return screen

    def init_input_type_menu(self):
        items = []
        for i in ["List", "Dict", "Tuple", "String"]:
            items.append({
                "text": i,
                "viewclass": "OneLineListItem",
                "on_release": self.get_input_type_callback(i)
            })

        self.input_type_menu = MDDropdownMenu(
            caller=self.input_type_button,
            items=items,
            position="auto",
            max_height=dp(200)
        )

        def open_input_menu(instance):
            self.input_type_menu.open()
        self.input_type_button.bind(on_release=open_input_menu)

    def init_order_menu(self):
        items = []
        for i in ["Ascending", "Descending"]:
            items.append({
                "text": i,
                "viewclass": "OneLineListItem",
                "on_release": self.get_order_callback(i)
            })

        self.order_menu = MDDropdownMenu(
            caller=self.order_button,
            items=items,
            position="auto",
            max_height=dp(200)
        )

        def open_order_menu(instance):
            self.order_menu.open()
        self.order_button.bind(on_release=open_order_menu)

    def init_algo_menu(self):
        items = []
        for i in ["Bubble", "Insertion", "Selection"]:
            items.append({
                "text": i,
                "viewclass": "OneLineListItem",
                "on_release": self.get_algo_callback(i)
            })

        self.algo_menu = MDDropdownMenu(
            caller=self.algo_button,
            items=items,
            position="auto",
            max_height=dp(200)
        )

        def open_algo_menu(instance):
            self.algo_menu.open()
        self.algo_button.bind(on_release=open_algo_menu)

    def get_input_type_callback(self, value):
        def callback():
            self.input_type_button.text = value
            self.input_type_menu.dismiss()
        return callback

    def get_order_callback(self, value):
        def callback():
            self.order_button.text = value
            self.order_menu.dismiss()
        return callback

    def get_algo_callback(self, value):
        def callback():
            self.algo_button.text = value
            self.algo_menu.dismiss()
        return callback


MainApp().run()
