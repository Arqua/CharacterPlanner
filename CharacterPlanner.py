import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import BooleanProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.core.text import FontContextManager as FCM
from kivy.uix.treeview import TreeView
from kivy.uix.treeview import TreeViewLabel
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.image import Image
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleboxlayout import  RecycleBoxLayout
from kivy.uix.recycleview.views import RecycleDataViewBehavior
kivy.require('1.11.0')

class CP(Widget):
    pass

# level = 1
# def MonsterKill(kill):
#   kill = input(int(killed))
#   if level == 1:
#   return kill*50
#   elif level <= 59:
#   return kill*(50+(level-1)*5)

# def ProgressFill(exp):
#    while (exp/100) < 1:
#        pass
#    if (exp/100) == 1:
#        return levelup = 1 and exp == 0
#    elif (exp/100) > 1:
#        return levelup = 1 and exp = exp%100       # this isn't correct right now as the % each exp gives is less each
# this will be fixed by a level exp modifier later

# def LevelUp(levelup):
#    if levelup == 1:
#        return level += 1, levelup -= 1 #somehow need to add in particle effects on level up

# lbl = Label(font_context='C://CharacterPlanner.py',family_name='Folkard')


class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    class SelectableLabel(RecycleDataViewBehavior, Label):
        index = None
        selected = BooleanProperty(False)
        selectable = BooleanProperty(True)

        def refresh_view_attrs(self, rv, index, data):
            ''' Catch and handle the view changes '''
            self.index = index
            return super(SelectableLabel, self).refresh_view_attrs(
                rv, index, data)
#   We ignore the SelectableLabel error here as it is referenced in the .kv file
        def on_touch_down(self, touch):
            ''' Add selection on touch down '''
            if super(SelectableLabel, self).on_touch_down(touch):
                return True
            if self.collide_point(*touch.pos) and self.selectable:
                return self.parent.select_with_touch(self.index, touch)
#   We ignore the SelectableLabel error here as it is referenced in the .kv file
        def apply_selection(self, rv, index, is_selected):
            ''' Respond to the selection of items in the view. '''
            self.selected = is_selected
            if is_selected:
                print("selection changed to {0}".format(rv.data[index]))
            else:
                print("selection removed for {0}".format(rv.data[index]))


class RV(RecycleView):
    def __init__(self, **kwargs):
        super(RV, self).__init__(**kwargs)
        self.data = [{'text': str(x)} for x in range(100)]


class CharacterPlannerApp(App):
    def build(self):
        return CP()


if __name__ == "__main__":
    CharacterPlannerApp().run()
