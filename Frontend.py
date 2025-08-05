from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.window import Window

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

        btn_layout = MDBoxLayout(orientation="vertical", spacing=25, size_hint_y=None, height=200, padding=(40, 0))

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
        # Searching button doesn't navigate yet; can add later

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

        layout.add_widget(MDLabel(text="Input Type:", halign="left", theme_text_color="Secondary"))
        input_type_layout = MDGridLayout(cols=4, spacing=10, padding=10, size_hint_y=None, height=50)
        self.input_type_buttons = []
        for t in ["List", "Dict", "Tuple", "String"]:
            btn = MDRaisedButton(text=t, md_bg_color="lightblue", size_hint_x=None, width=80)
            self.input_type_buttons.append(btn)
            input_type_layout.add_widget(btn)
        layout.add_widget(input_type_layout)

        layout.add_widget(MDLabel(text="\nSorting Order:", halign="left", theme_text_color="Secondary"))
        order_layout = MDGridLayout(cols=2, spacing=10, padding=10, size_hint_y=None, height=50)
        self.order_buttons = []
        for o in ["Ascending", "Descending"]:
            btn = MDRaisedButton(text=o, md_bg_color="lightgreen", size_hint_x=None, width=120)
            self.order_buttons.append(btn)
            order_layout.add_widget(btn)
        layout.add_widget(order_layout)

        layout.add_widget(MDLabel(text="\nAlgorithm:", halign="left", theme_text_color="Secondary"))
        algo_layout = MDGridLayout(cols=3, spacing=10, padding=10, size_hint_y=None, height=50)
        self.algo_buttons = []
        for algo in ["Bubble", "Insertion", "Selection"]:
            btn = MDRaisedButton(text=algo, md_bg_color="orange", size_hint_x=None, width=100)
            self.algo_buttons.append(btn)
            algo_layout.add_widget(btn)
        layout.add_widget(algo_layout)

        layout.add_widget(MDLabel(text="\n\nSorted Output:", halign="left",theme_text_color="Secondary"))

        self.output_box=MDTextField(
            hint_text="",
            readonly=True,
            size_hint_x=0.9,
            pos_hint={"center_x": 0.5}
        )
        layout.add_widget(self.output_box)
        screen.add_widget(layout)
        return screen


MainApp().run()


