# imports tkinter, os and controller
from tkinter import *
import os
import controller as c


# creates a new class called Main_GUI
class Main_GUI():

    # initializes the class
    def __init__(self):
        self.locationlist = []

    # method for the tkinter window
    def GUI_screen(self, wn):
        
        self.wn = wn
        self.wn.title('MAPS')
        self.wn.geometry('500x450')

        # creates a frame
        self.fr1 = Frame(self.wn)
        self.fr1.pack()

        # creates a label
        self.labF = Label(self.fr1, text='Starting Location')
        self.labF.grid(row=0, column=0)

        # gets the entry for description
        self.enF = Entry(self.fr1, width=30)
        self.enF.grid(row=0, column=1)

        # creates a label
        self.labT = Label(self.fr1, text='Ending Location')
        self.labT.grid(row=1, column=0)

        # gets the entry for amount
        self.enT = Entry(self.fr1, width=30)
        self.enT.grid(row=1, column=1)

        # creates a label
        self.labe = Label(self.fr1, 
                          text='Sample Location: 3700 Parkview Lane, Irvine, CA 92612')
        self.labe.grid(row=2, column=1)

        # creates a label
        self.labw = Label(self.fr1, 
                          text='STEP 1: COMPLETE THIS STEP  BEFORE PROCEDDING')
        self.labw.grid(row=3, column=1)

        # creates a button
        self.okay = Button(self.fr1, text='STEP 1: Search', 
                           command=self.location_list)
        self.okay.grid(row=4, column=1)

        # creates a new frame
        self.fr2 = Frame(self.wn)
        self.fr2.pack()

        # creates a label
        self.lab3 = Label(self.fr1, text='                ')
        self.lab3.grid(row=5, column=0)

        # creates a label
        self.lab0 = Label(self.fr2, text='STEP 2: Selecet Your Choice')
        self.lab0.grid(row=0, column=0)
   
        # creates button for returning distance
        self.Dis = Button(self.fr2, text='Distance', 
                          command=self.distance_return)
        self.Dis.grid(row=1, column=0)

        # creates button for returning time
        self.Tim = Button(self.fr2, text='Time', command=self.time_return)
        self.Tim.grid(row=2, column=0)

        # creates button for returning direction
        self.Direct = Button(self.fr2, text='Direction', 
                             command=self.directions_return)
        self.Direct.grid(row=3, column=0)

        # creates button for Latitude and Longitude
        self.LL = Button(self.fr2, text='Latitude and Longitude', 
                         command=self.LatandLong_return)
        self.LL.grid(row=5, column=0)

        # creates button for download direction
        self.Down = Button(self.fr2, text='Save directions', 
                           command=self.view_download)
        self.Down.grid(row=4, column=0)

        # creates a label
        self.lab1 = Label(self.fr2, text='                ')
        self.lab1.grid(row=6, column=0)

        # creates a label
        self.lab2 = Label(self.fr2, text='Feel like doing something?')
        self.lab2.grid(row=7, column=0)

        # creates a label
        self.lab2 = Label(self.fr2, text='Complete step 1 and click here')
        self.lab2.grid(row=8, column=0)

        # creates button for point of interest
        self.POI = Button(self.fr2, text='Point of Interest', 
                          command=self.view_pointOfInterest)
        self.POI.grid(row=9, column=0)

        # creates a label
        self.lab4 = Label(self.fr2, text='                ')
        self.lab4.grid(row=10, column=0)

        # creates a button to quit
        self.Qui = Button(self.fr2, text='I think its time to Quit', 
                          command=self.wn.destroy)
        self.Qui.grid(row=11, column=0)

    # method to create a list with entered locations exist 
    def location_list(self):
        try:
            # creates a new list
            self.locationlist = []
            # gets the values
            self.from_loc = self.enF.get()
            self.to_loc = self.enT.get()
            # appends the values
            self.locationlist.append(self.from_loc)
            self.locationlist.append(self.to_loc)
            # opens distance in model for checking values
            h = self.locationlist
            s = c.Controller()
            self.ret_dit_val = s.return_dist(h)
            #checks if the entry widget is empty
            if self.from_loc == '' or self.to_loc == '':
                # calls the error method
                self.field_error()
                self.location_list()

            # checks if the entries are equal
            elif self.from_loc == self.to_loc:
                # calls the error method
                self.same_error()
                self.location_list()

            # checks if distance value is 0
            elif self.ret_dit_val == 0:
                # calls the error method
                self.valid_error()
                self.location_list()

            # else it returns the list
            else:
                return self.locationlist
        except:
            return 0

    # method to get distance from model and print it in a
    # tkinter window
    def distance_return(self):
        a = self.locationlist
        d = c.Controller()
        self.ret_dist_value = d.return_distance(a)

        # creates a new window to print the distance
        self.master = Tk()
        t = self.ret_dist_value
        self.master.minsize(width=400, height=400)

        lab1 = Label(self.master,
                     text='Total distance from {} to {} is'.format(self.from_loc, self.to_loc),
                     font=("Helvetica", 14))
        lab1.grid(row=0, column=0)

        
        # shows as text in the window
        lab2 = Label(self.master, text=t, font=("Helvetica", 20))
        lab2.grid(row=3, column=0)

        # creates a label
        lab3 = Label(self.master, text='miles', font=("Helvetica", 16))
        lab3.grid(row=4, column=0)

        # creates a label
        lab4 = Label(self.master, text='Have a safe journey !!', 
                     font=("Helvetica", 14))
        lab4.grid(row=6, column=0)

        # creates a button
        But1 = Button(self.master, text='Back to main menu', 
                      command=self.destroy_dist)
        But1.grid(row=8, column=0)

        mainloop()

    # this method destroys the directions screen
    def destroy_dist(self):
        self.master.destroy()
        
    # method to get time from model and print it in a
    # tkinter window    
    def time_return(self):
        b = self.locationlist
        l = c.Controller()
        ret_time_value = l.return_time(b)

        # creates new window to return time
        self.master = Tk()
        o = ret_time_value/60
        self.master.minsize(width=400, height=400)

        lab1 = Label(self.master,
                     text='Total time from {} to {} is'.format(self.from_loc, self.to_loc),
                     font=("Helvetica", 14))
        lab1.grid(row=0, column=0)

        
        # shows as text in the window
        lab2 = Label(self.master, text=o, font=("Helvetica", 20))
        lab2.grid(row=3, column=0)

        # creates a new label
        lab3 = Label(self.master, text='minutes', font=("Helvetica", 16))
        lab3.grid(row=4, column=0)

        # creates a new label
        lab4 = Label(self.master, text='Have a safe journey !!', 
                     font=("Helvetica", 14))
        lab4.grid(row=6, column=0)

        # creates a new button
        But1 = Button(self.master, text='Back to main menu', 
                      command=self.destroy_time)
        But1.grid(row=8, column=0)

        mainloop()

    # method to destry the time screen
    def destroy_time(self):
        self.master.destroy()

    # method to get directions from model and print it in a
    # tkinter window
    def directions_return(self):
        d = self.locationlist
        k = c.Controller()
        ret_direc_value = k.return_direction(d)
        # creates a new window to print directions
        self.master = Tk()
        p = ret_direc_value
        self.master.minsize(width=400, height=400)
        
        # creates a new label
        lab1 = Label(self.master,
                     text='Directions from {} to {} is'.format(self.from_loc, self.to_loc),
                     font=("Helvetica", 14))
        lab1.grid(row=0, column=0)

        
        # shows as text in the window
        lab2 = Label(self.master, text=p, font=("Helvetica", 12))
        lab2.grid(row=3, column=0)

        # creates a new label
        lab4 = Label(self.master, text='Have a safe journey !!', 
                     font=("Helvetica", 14))
        lab4.grid(row=6, column=0)

        # creates a new button    
        But1 = Button(self.master, 
                      text='Back to main menu', command=self.destroy_dir)
        But1.grid(row=8, column=0)

        mainloop()

    #method to destroy the directions screen
    def destroy_dir(self):
        self.master.destroy()

    # method to get the filename and path to be stored in
    def view_download(self):
        # prompts user for filename and path directory
        # to save the directions file
        self.Dwindow = Tk()

        # creates a new label
        label_1 = Label(self.Dwindow, text='Filename')
        label_1.grid(row=1, column=0)

        # creates a entry widget
        self.filename = Entry(self.Dwindow, width=60)
        self.filename.grid(row=1, column=1)

        # creates a label
        label_2 = Label(self.Dwindow, text='Path')
        label_2.grid(row=2, column=0)

        # creates an entry widget
        self.path = Entry(self.Dwindow, width=60)
        self.path.grid(row=2, column=1)

        # creates a button to submit 
        s_button = Button(self.Dwindow, text='Submit', command=self.get_path)
        s_button.grid(row=3, column=1)

        # creates a button to quit
        q_button = Button(self.Dwindow, text='Quit', command=self.Dwindow.destroy)
        q_button.grid(row=4, column=1)
        
        self.Dwindow.mainloop()

    # method to get path and to save in the desired
    # path
    def get_path(self):
        self.path1 = self.path.get()
        self.filename1 = self.filename.get()
        self.fullpath = os.path.join(str(self.path1), str(self.filename1)+'.txt')
        h = self.locationlist
        g = c.Controller()
        self.ret_direc_value = g.return_direction(h)
        # errors handled
        if self.filename1 == '' or self.path1 == '':
            self.error_view()
        else:
            self.print_directions()
            
        self.Dwindow.destroy()

    # method to print the directtions on to a file
    def print_directions(self):
        if os.path.exists(self.path1) == True:
            f = open(self.fullpath, 'a+')
            for i in self.ret_direc_value:
                f.write(i)
            f.close()
        else:
            self.error_view()

    # me to return the latitude and longitude of a location
    def LatandLong_return(self):
        m = self.locationlist
        o = []
        n = c.Controller()
        ret_LatLng_value = n.return_LatandLong(m)

        # new screen to print the lat and long of the starting
        # location
        self.master = Tk()
        o = ret_LatLng_value
        self.master.minsize(width=400, height=400)

        # creates a label
        lab1 = Label(self.master,
                     text='Latitude and Longitude of {} is'.format(self.from_loc),
                     font=("Helvetica", 14))
        lab1.grid(row=0, column=0)

        
        # shows as text in the window
        lab2 = Label(self.master, text=o, font=("Helvetica", 20))
        lab2.grid(row=3, column=0)

        # creates a label
        lab4 = Label(self.master, text='Have a safe journey !!', 
                     font=("Helvetica", 14))
        lab4.grid(row=6, column=0)

        # creates a button
        But1 = Button(self.master, text='Back to main menu', 
                      command=self.destroy_LL)
        But1.grid(row=8, column=0)

        mainloop()

    # destroys the latitude and longitude screen
    def destroy_LL(self):
        self.master.destroy()

    # new method to get values about your interests
    def view_pointOfInterest(self):
        # creates a new window
        self.Dwindow = Tk()

        # creates a label to get keyword
        label_1 = Label(self.Dwindow, text='Keyword(Ex: Restaurant)')
        label_1.grid(row=1, column=0)

        # entry widget
        self.keyword = Entry(self.Dwindow, width=60)
        self.keyword.grid(row=1, column=1)

        # label to restrict the number of results
        label_2 = Label(self.Dwindow, text = 'No. of results')
        label_2.grid(row=2, column=0)

        # entry widget
        self.result = Entry(self.Dwindow, width=60)
        self.result.grid(row=2, column=1)

        # submit button to process
        s_button = Button(self.Dwindow, text='Submit',
                          command=self.process_POI)
        s_button.grid(row=3, column=1)

        # quit button to quit
        q_button = Button(self.Dwindow, text='Quit', 
                          command=self.Dwindow.destroy)
        q_button.grid(row=4, column=1)
        
        self.Dwindow.mainloop()

    # processes the details about the point of interest
    def process_POI(self):
        # gets the values throught the entry widget
        self.keyword1 = self.keyword.get()
        self.result1 = self.result.get()
        keyw = self.keyword1
        rest = self.result1
        # errors handled
        if self.keyword1 == '' or self.result1 == '':
            self.field_error()
            self.process_POI()

        elif self.result1.isdigit():
            q = self.locationlist
            w = c.Controller()
            ret_POI_value = w.return_POI(q, keyw, rest)
            d= ''
            for i in ret_POI_value:
                d += i+'\n'
            # new window created
            self.master = Tk()
            v = d
            self.master.minsize(width=400, height=400)

            # new label created
            lab1 = Label(self.master,
                         text='Results:',
                         font=("Helvetica", 16))
            lab1.grid(row=0, column=0)

            
            # shows as text in the window
            lab2 = Label(self.master, text=v, font=("Helvetica", 14))
            lab2.grid(row=3, column=0)

            # creates a new button
            But1 = Button(self.master, text='Back to main menu', 
                          command=self.destroy_POI)
            But1.grid(row=8, column=0)

            mainloop()
            
        else:
            self.int_error()
            self.process_POI()
            
    # destroys the point of interest method
    def destroy_POI(self):
        self.master.destroy()

    # handels the error while saving the download file
    def error_view(self):
        # new window created
        self.Ewindow = Tk()
        # label created
        label_1 = Label(self.Ewindow, text='Either path is incorrect '
                        'or the fileds are empty')
        label_1.pack()

        # new button created
        button_t = Button(self.Ewindow, text = 'Try Again',
                          command = self.Ewindow.destroy)
        button_t.pack()
        self.Ewindow.mainloop()

    # handels the error while the fields are empty
    def field_error(self):
        # creates a new window
        self.Ewindow = Tk()
        # creates a label
        label_1 = Label(self.Ewindow, text='Fields are empty')
        label_1.pack()

        # creates a button
        button_t = Button(self.Ewindow, text = 'Try Again',
                          command = self.Ewindow.destroy)
        button_t.pack()
        self.Ewindow.mainloop()

    # handels the error while the entry is not an intger value
    def int_error(self):
        # creates a new window
        self.Ewindow = Tk()
        # create a label
        label_1 = Label(self.Ewindow, text='Enter a integer value')
        label_1.pack()

        # creates a new button
        button_t = Button(self.Ewindow, text = 'Try Again',
                          command = self.Ewindow.destroy)
        button_t.pack()
        self.Ewindow.mainloop()

    # handels the error while the starting and the ending locations
    # are the same
    def same_error(self):
        # creates a new window
        self.Ewindow = Tk()
        # creates a label
        label_1 = Label(self.Ewindow, text='Both the locations are same')
        label_1.pack()

        # creates a button
        button_t = Button(self.Ewindow, text = 'Try Again',
                          command = self.Ewindow.destroy)
        button_t.pack()
        self.Ewindow.mainloop()

    # handels the error while the entry is invlid
    def valid_error(self):
        # creates a new window 
        self.Ewindow = Tk()
        # creates the label
        label_1 = Label(self.Ewindow, text='Invalid entry. Please Try again')
        label_1.pack()

        # creates a button
        button_t = Button(self.Ewindow, text = 'Try Again',
                          command = self.Ewindow.destroy)
        button_t.pack()
        self.Ewindow.mainloop()

    # main method to run this code using the controller
    def run(self):
        wn = Tk()
        my_gui = Main_GUI()
        my_gui.GUI_screen(wn)
        wn.mainloop()
