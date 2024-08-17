import tkinter as tk
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict

# Initialize the main application window
root = tk.Tk()
root.title("Button Press Analysis")
root.geometry("300x400")

# Data structure to hold button press counts and timestamps
button_presses = defaultdict(list)

# Function to record button presses
def record_press(button_name):
    timestamp = datetime.now()
    button_presses[button_name].append(timestamp)
    print(f"{button_name} pressed at {timestamp}")

# Function to plot the graph based on the analysis type
def plot_graph(analysis_type):
    if not any(button_presses.values()):
        print("No data to display.")
        return

    data = {button: pd.Series(times) for button, times in button_presses.items()}

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

# Create button grid
buttons = ["HH", "HD", "DH", "DD"]
for i, button_name in enumerate(buttons):
    button = tk.Button(root, text=button_name, width=10, height=2,
                       command=lambda name=button_name: record_press(name))
    button.grid(row=i//2, column=i%2, padx=10, pady=10)

# Analysis buttons
analysis_types = ["daily", "weekly", "monthly", "yearly"]
for i, analysis in enumerate(analysis_types):
    button = tk.Button(root, text=f"{analysis.capitalize()} Analysis", width=20,
                       command=lambda analysis=analysis: plot_graph(analysis))
    button.grid(row=2+i, column=0, columnspan=2, padx=10, pady=5)

# Start the Tkinter event loop
root.mainloop()
