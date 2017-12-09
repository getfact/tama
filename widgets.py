from kivy.uix.screenmanager import Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.progressbar import ProgressBar

class Home(Screen):
    def __init__(self, **kwargs):
        super(Home, self).__init__(**kwargs)

        self.add_widgets()

    def add_widgets(self, *args):
        status_grid = StatusGrid()
        self.add_widget(status_grid)


class StatusGrid(GridLayout):
    def __init__(self, **kwargs):
        super(StatusGrid, self).__init__(**kwargs)

        self.cols = 2
        self.size_hint = (.5, .1)
        self.pos_hint = {'center_x': .2, 'center_y': .9}
        self.add_widgets()

    def add_widgets(self, *args):
        hunger_text = Label(text='HUNGER', font_size=12)
        happy_text = Label(text='HAPPY', font_size=12)
        hunger_bar = ProgressBar()
        happy_bar = ProgressBar()
        status_list = [hunger_text, hunger_bar,
                happy_text, happy_bar]
        [self.add_widget(widget) for widget in status_list]
