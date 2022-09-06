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
    prev_scr = 'clock'
    def build(self):
        self.main = Main()
        return self.main
        
    def click(self,scr_name, direction='left'):
        if scr_name == 'stopwatch':
            direction = ('left' if self.prev_scr == 'clock' else 'right')
        self.main.ids['screen_manager'].current = scr_name
        self.main.ids['screen_manager'].transition.direction = direction
        self.prev_scr = scr_name
if __name__ == '__main__':
    ClockApp().run()