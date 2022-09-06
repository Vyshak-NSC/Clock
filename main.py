import time, kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import Screen, ScreenManager, NoTransition
from kivy.properties import ObjectProperty
kivy.require('2.1.0')

class Main(GridLayout):
    screen_manager = ObjectProperty()

class ClockScreen(Screen):
    pass

class StopWatchScreen(Screen):
    pass

class TimerScreen(Screen):
    pass

class ScreenManagerClass(ScreenManager):
    pass

class ClockApp(App):
    def build(self):
        self.all = Main()
        return self.all
        
    def click(self):
        self.all.ids['screen_manager'].current = 'stopwatch'
if __name__ == '__main__':
    ClockApp().run()