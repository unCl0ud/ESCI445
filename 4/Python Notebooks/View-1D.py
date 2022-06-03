#!/usr/bin/env python
# File: View-1D.pyw

'''This Tkinter application reads 1-D model data.
It expects an input NumPy array file with the .npy extension.  The 
input array will be of shape (nt, nx) where nt is the number of 
time levels and nx is the number of data points.'''

# Written by Alex DeCaria
# Latest version date:  1/9/2019

import sys
from tkinter import *    # if Python 3.X
from tkinter.filedialog import askopenfilename as pickfile
    
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as fig
import matplotlib.backends.backend_tkagg as tkagg


# Define class for GUI Application
class View_1D:

    def __init__(self, m):
        
        self.master = m  #  Master window reference
        self.master.title('View-1D')  #  Give title to master window

        filename = pickfile(filetypes = [('model output','.npy')],
                            multiple=False) # Select data file

        # Block of code if file picked
        if len(filename) != 0:
            self.nx, self.data = self.read_data(filename)  #  read in data from file
            # self.nx is the number of grid points
            # self.data is the data array (each row is a time level)

            # Block of code if data file read successfully
            if self.nx != False:
                self.create_widgets()  #  Call method to create widgets

            # If data file not read successfully
            else:
                print('\nThere was a problem parsing the data file.')
                print(' It may be the wrong format.\n')

        # If file not picked
        else:
            print('\nNo file chosen.\n')

    # Method to read data file
    def read_data(self, filename):
        #  Extract data  from file
        try:
            data = np.load(filename)
            nx = np.shape(data)[1]
            return nx, data
        except:
            return False, False  # Returns False if there was a problem

    # Method to create widgets
    def create_widgets(self):
        # Set up figure parameters
        p_max, p_min = np.max(self.data[0,:]), np.min(self.data[0,:])
        p_max = np.max(self.data[0,:])
        self.p_range = 1.5*max((abs(p_max),abs(p_min)))
        self.x = np.arange(0,self.nx) # array for x values
        self.f = fig.Figure(figsize=(4,3))  #  this creates the figure for the plot

        # Creates an outer frame within the main window
        self.outer_frame = Frame(self.master)
        self.outer_frame.pack(expand=YES, fill=BOTH)

        # Creates a frame for displaying plots
        self.canvas = tkagg.FigureCanvasTkAgg(self.f,self.outer_frame)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=YES)

        # Create a frame for widgets
        self.widget_frame = Frame(self.outer_frame)
        self.widget_frame.pack(side = BOTTOM, expand=YES)

        # Create a slider for picking time level
        self.tl_scale = Scale(self.widget_frame, orient = HORIZONTAL, from_=0,
                            to=np.shape(self.data)[0]-1,command = self.plot_figure)
        self.tl_scale.set(0)
        self.tl_scale.pack(fill = BOTH, expand=YES)        

    # Method to plot figure
    def plot_figure(self, val = 0):
        # clear and recreate figure
        self.f.clf() 
        self.a = self.f.add_subplot(111)
        # Set plot limits
        n = self.tl_scale.get() #  data row number (time level)
        pmax, pmin = np.max(self.data[n,:]), np.min(self.data[n,:])
        prange = 1.1*max((abs(pmax),abs(pmin)))
        ylim = max(self.p_range, prange)
        self.a.set_ylim(-ylim, ylim)
        self.a.set_xlim(self.x[0], self.x[-1])
        self.a.plot(self.x, self.data[n,:], '-')
        self.canvas.draw()
        
# ------------ END OF APP DEFINITION -------------------------------------------------------

# Calls Tk library, instantiates application, and enters the main loop
root = Tk()
app = View_1D(root)
root.mainloop()

