##In a knockout tournament, if there are N players, then:
##Each match eliminates 1 player
##The tournament continues until 1 winner remains
##So the number of matches = N - 1

from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (700, 500)
Window.clearcolor = (0, 0, 0, 1)

class TournamentApp(App):
    def build(self):
        layout = FloatLayout()

        # Title
        self.label_title = Label(
            text="[b]TOURNAMENT MATCH COUNTER[/b]",
            markup = True,
            font_size=25,
            color=(1,1,1,1),
            pos_hint={"x": 0.25, "top": 1},
            size_hint=(0.5, 0.2)
        )
        layout.add_widget(self.label_title)

        # Input Label
        self.input_label = Label(
            text="[b]Enter the number of Players[/b]",
            markup = True,
            font_size=20,
            color=  (0.9, 0.9, 0.9, 1),
            pos_hint={"x": 0.0, "top": 0.75},
            size_hint=(0.5, 0.2)
        )
        layout.add_widget(self.input_label)

        # Input box for players
        self.input_box = TextInput(
            hint_text="",
            multiline=False,
            font_size=25,
            size_hint=(0.4, 0.1),
            pos_hint={"x": 0.4, "top": 0.7}
        )
        layout.add_widget(self.input_box)

        # Button
        btn = Button(
            text="Calculate Matches",
            size_hint=(0.5, 0.1),
            pos_hint={"center_x": 0.5, "center_y": 0.45}
        )
        btn.bind(on_press=self.calculate_matches)
        layout.add_widget(btn)

        # Output Label
        self.output_label = Label(
            text="",
            font_size=20,
            size_hint=(0.8, 0.2),
            pos_hint={"center_x": 0.5, "center_y": 0.35}
        )
        layout.add_widget(self.output_label)

        return layout

    def calculate_matches(self, instance):
        try:
            players = int(self.input_box.text.strip())
            matches = 0
            remaining = players

            # While loop to calculate matches
            while remaining > 1:
                matches += 1
                remaining -= 1

            self.output_label.text = f"Total matches: {matches}"
        except:
            self.output_label.text = ""


if __name__ == "__main__":
    TournamentApp().run()
