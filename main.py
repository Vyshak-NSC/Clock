import kivy
from time import strftime
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
    started = False
    timer_count = 0
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
    
    def on_start(self):
        Clock.schedule_interval(self.update_time, 0.016)

    def update_time(self, nap):
        self.main.ids['screen_manager'].get_screen('clock').ids['show_time'].text = strftime('%I:%M:%S %p')
        if self.started:
            self.timer_count += nap
        minutes, seconds = divmod(self.timer_count, 60)
        
        self.main.ids['screen_manager'].get_screen('stopwatch').ids['stopwatch'].text = strftime('%02d:%02d:%02d' % (int(minutes), int(seconds), int(seconds*100 %100)))

    def stopwatch_start(self):
        self.main.ids['screen_manager'].get_screen('stopwatch').ids['start'].text = ('Start' if self.started else 'Stop')
        self.started = not self.started
    
    def stopwatch_reset(self):
        if self.started:
            self.started = False
            self.main.ids['screen_manager'].get_screen('stopwatch').ids['start'].text = 'Start'
        self.timer_count = 0
if __name__ == '__main__':
    ClockApp().run()
    