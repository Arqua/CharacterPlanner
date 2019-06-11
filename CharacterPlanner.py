import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.treeview import TreeView
from kivy.uix.treeview import TreeViewLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
kivy.require('1.11.0')


class CP(Widget):
    pass


class CharacterPlannerApp(App):
    def build(self):
        return CP()


if __name__ == "__main__":
    CharacterPlannerApp().run()
