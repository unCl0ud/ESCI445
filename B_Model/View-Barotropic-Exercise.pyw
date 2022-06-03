#!/usr/bin/env python
# File: View-Exercise-6.pyw

'''This Tkinter application reads 2-D barotropic model data.
The input a numpy array file with '.npy' extension consisting of
a (n, nx, ny) numpy array where:
    n is # of time levels
    nx is # of x grid points
    ny is # of y grid points'''

# Written by Alex DeCaria
# Latest version date:  2/22/15

import sys
if sys.version_info[0] != 3:
    from Tkinter import *    # if Python 2.X
else:
    from tkinter import *    # if Python 3.X
    
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.figure as fig
import matplotlib.backends.backend_tkagg as tkagg
from tkFileDialog import askopenfilename as pickfile
import csv
import os.path as pth

# Define class for GUI Application
class View_Barotropic:

    def __init__(self, m):
        
        self.master = m  #  Master window reference
        self.master.title('View Barotropic Model')  #  Give title to master window

        #filename = 'IO-Files\\barotropic-output.txt'
        filename = pickfile(filetypes = [('numpy', '.npy')],
                            multiple=False) # Select data file

        # Block of code if file picked
        if len(filename) != 0:
            extension = pth.splitext(filename)[1]
            self.data = self.read_numpy(filename)  #  read in data from file
            self.create_widgets()  #  Call method to create widgets

        # If file not picked
        else:
            print('\nNo file chosen.\n')

    # Method to read numpy data file
    def read_numpy(self, filename):
        return np.load(filename)

    # Method to create widgets
    def create_widgets(self):

        self.f = fig.Figure(figsize=(4,3)) # Creates figure
        
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
        self.a.contour(np.transpose(self.data[n,:,:]))
        self.canvas.draw()
        
# ------------ END OF APP DEFINITION -------------------------------------------------------

# Calls Tk library, instantiates application, and enters the main loop
root = Tk()
app = View_Barotropic(root)
root.mainloop()

