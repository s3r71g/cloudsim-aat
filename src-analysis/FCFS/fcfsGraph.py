import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.widgets import Button
import numpy as np

# CSV Data
data = pd.read_csv('src-analysis/FCFS/cloudlet_output.csv')

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate metrics
df["Response Time"] = df["Finish Time"] - df["Start Time"]
df["Waiting Time"] = df["Start Time"]  # Waiting time is Start Time for Round Robin Scheduler
df["Execution Time"] = df["Time"]

# Resource Utilization
total_time = df["Finish Time"].max()
df["Utilization"] = df["Execution Time"] / total_time * 100

# Create figures for each graph
fig1, ax1 = plt.subplots(figsize=(10, 7))
fig2, ax2 = plt.subplots(figsize=(10, 7))
fig3, ax3 = plt.subplots(figsize=(10, 7))

# 1. Resource Utilization Graph
ax1.bar(df["Cloudlet ID"], df["Utilization"], color='blue', alpha=0.7)
ax1.set_title("Resource Utilization Graph")
ax1.set_xlabel("Cloudlet ID")
ax1.set_ylabel("Utilization (%)")
ax1.grid(axis='y', linestyle='--', alpha=0.6)

# 2. Response Time Graph
ax2.bar(df["Cloudlet ID"], df["Response Time"], color='green', alpha=0.7)
ax2.set_title("Response Time of Each Task")
ax2.set_xlabel("Cloudlet ID")
ax2.set_ylabel("Response Time (Seconds)")
ax2.grid(axis='y', linestyle='--', alpha=0.6)

# 3. Waiting Time Graph
ax3.bar(df["Cloudlet ID"], df["Waiting Time"], color='orange', alpha=0.7)
ax3.set_title("Waiting Time of Each Task")
ax3.set_xlabel("Cloudlet ID")
ax3.set_ylabel("Waiting Time (Seconds)")
ax3.grid(axis='y', linestyle='--', alpha=0.6)

# Function to close all figures
def close_all_figures():
    plt.close(fig1)
    plt.close(fig2)
    plt.close(fig3)

# Define the function to switch between the graphs
def show_utilization(event):
    close_all_figures()  # Close all open figures
    fig1.canvas.draw()
    plt.show()

def show_response_time(event):
    close_all_figures()  # Close all open figures
    fig2.canvas.draw()
    plt.show()

def show_waiting_time(event):
    close_all_figures()  # Close all open figures
    fig3.canvas.draw()
    plt.show()

# Add buttons to the first figure for switching
# ax_button1 = fig1.add_axes([0.7, 0.05, 0.2, 0.075])  # Position of button
# button1 = Button(ax_button1, 'Response Time', color='lightgoldenrodyellow', hovercolor='lightcoral')
# button1.on_clicked(show_response_time)

# ax_button2 = fig1.add_axes([0.7, 0.15, 0.2, 0.075])  # Position of button
# button2 = Button(ax_button2, 'Waiting Time', color='lightgoldenrodyellow', hovercolor='lightcoral')
# button2.on_clicked(show_waiting_time)

# Show the first figure initially
plt.show()
