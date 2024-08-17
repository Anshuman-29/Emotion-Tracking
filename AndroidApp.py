from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict

class ButtonPressApp(App):
    def build(self):
        self.button_presses = defaultdict(list)
        
        layout = GridLayout(cols=2)
        buttons = ["HH", "HD", "DH", "DD"]
        for button_name in buttons:
            btn = Button(text=button_name, on_press=self.record_press(button_name))
            layout.add_widget(btn)
        
        analysis_layout = BoxLayout(orientation='vertical')
        analysis_types = ["Daily", "Weekly", "Monthly", "Yearly"]
        for analysis in analysis_types:
            btn = Button(text=f"{analysis} Analysis", on_press=self.plot_graph(analysis.lower()))
            analysis_layout.add_widget(btn)
        
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(layout)
        main_layout.add_widget(analysis_layout)
        
        return main_layout
    
    def record_press(self, button_name):
        def callback(instance):
            timestamp = datetime.now()
            self.button_presses[button_name].append(timestamp)
            print(f"{button_name} pressed at {timestamp}")
        return callback

    def plot_graph(self, analysis_type):
        def callback(instance):
            if not any(self.button_presses.values()):
                print("No data to display.")
                return

            data = {button: pd.Series(times) for button, times in self.button_presses.items()}
            df = pd.DataFrame({btn: pd.to_datetime(times) for btn, times in data.items()})
            plt.figure(figsize=(10, 6))

            if analysis_type == "daily":
                for btn in df.columns:
                    df[btn].dt.hour.value_counts().sort_index().plot(label=btn)
                plt.xlabel("Time of Day")
                plt.ylabel("Number of Presses")
                plt.title("Daily Analysis: Button Presses vs. Time of Day")

            elif analysis_type == "weekly":
                for btn in df.columns:
                    df[btn].dt.day_name().value_counts().sort_index().plot(label=btn)
                plt.xlabel("Day of the Week")
                plt.ylabel("Number of Presses")
                plt.title("Weekly Analysis: Button Presses vs. Day of the Week")

            elif analysis_type == "monthly":
                for btn in df.columns:
                    df[btn].dt.day.value_counts().sort_index().plot(label=btn)
                plt.xlabel("Day of the Month")
                plt.ylabel("Number of Presses")
                plt.title("Monthly Analysis: Button Presses vs. Day of the Month")

            elif analysis_type == "yearly":
                for btn in df.columns:
                    df[btn].dt.month_name().value_counts().sort_index().plot(label=btn)
                plt.xlabel("Month of the Year")
                plt.ylabel("Number of Presses")
                plt.title("Yearly Analysis: Button Presses vs. Month of the Year")

            plt.legend(title="Buttons")
            plt.show()
        return callback

if __name__ == '__main__':
    ButtonPressApp().run()
