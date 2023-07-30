
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Sample data for the graphs
Types_Persons = ['Educated', 'Uneducated', 'Employed', 'Unemployed']
counts = [30,80,40,50]

# Create a tkinter window
root = tk.Tk()
root.title("Types of Persons Data")

# Function to create and display a pie chart
def show_pie_chart():
    fig_pie, ax_pie = plt.subplots()
    ax_pie.pie(counts, labels=Types_Persons, autopct='%1.1f%%', startangle=90)
    ax_pie.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    canvas_pie = FigureCanvasTkAgg(fig_pie, master=frame_graph)
    canvas_pie.draw()
    canvas_pie.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Function to create and display a bar graph
def show_bar_graph():
    fig_bar, ax_bar = plt.subplots()
    ax_bar.bar(Types_Persons, counts)

    canvas_bar = FigureCanvasTkAgg(fig_bar, master=frame_graph)
    canvas_bar.draw()
    canvas_bar.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



# Create a frame to hold the graph widgets
frame_graph = tk.Frame(root)
frame_graph.pack()

# Create buttons to switch between graphs
btn_pie_chart = tk.Button(root, text="Pie Chart", command=show_pie_chart)
btn_pie_chart.pack()

btn_bar_graph = tk.Button(root, text="Bar Graph", command=show_bar_graph)
btn_bar_graph.pack()



# Start the tkinter main loop
root.mainloop()