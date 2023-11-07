#!/usr/bin/python3
import tkinter
from page2 import create_2nd_frame, go_to_second_page, configure_text_kilo_or_livre_page2
import classes_page1
from classes_page1 import page1_EntryManager
import frame_manager
import pickle
checker = None

def configure_text_kilo_or_livre(check):
        global checker
        
        checker = check.get()
        
        print(check.get())
        if check.get() == 2:
            Jet_pumps_mass_flow_rate_frame.config(text="Mass Flow Rate (lb/min)")
            center_jet_pump1_frame.config(text="CTR JET 1 (lb/min)")
            center_jet_pump2_frame.config(text="CTR JET 2 (lb/min)")
            start_mass1_label.config(text='Mass (lb) "0"min')
            end_mass2_label.config(text='Mass (lb) "5"min')
            start_mass2_label.config(text='Mass (lb) "0"min')
            end_mass1_label.config(text='Mass (lb) "5"min')
            mass_rate1_label.config(text="(lb/min)")
            mass_rate2_label.config(text="(lb/min)")
            if rate1 != 0:
                print("rate1 lb checker")
                if 154.3 <= rate1 <= 233.7:
                    mass_rate1_result.configure(bg='green')
                else:
                    mass_rate1_result.configure(bg='red')
            if rate2 != 0:
                print("rate2 lb cgecker")
                if 154.3 <= rate2 <= 233.7:
                    mass_rate2_result.configure(bg='green')
                else:
                    mass_rate2_result.configure(bg='red')
        elif check.get() == 1:
            Jet_pumps_mass_flow_rate_frame.config(text="Mass Flow Rate (Kg/min)")
            center_jet_pump1_frame.config(text="CTR JET 1 (Kg/min)")
            center_jet_pump2_frame.config(text="CTR JET 2 (Kg/min)")
            start_mass1_label.config(text='Mass (Kg) "0"min')
            end_mass2_label.config(text='Mass (Kg) "5"min')
            start_mass2_label.config(text='Mass (Kg) "0"min')
            end_mass1_label.config(text='Mass (Kg) "5"min')
            mass_rate1_label.config(text="(Kg/min)")
            mass_rate2_label.config(text="(Kg/min)")
            if rate1 != 0:
                print("hi am here")
                if 70 <= rate1 <= 106:
                    mass_rate1_result.configure(bg='green')
                else:
                    mass_rate1_result.configure(bg='red')
            if rate2 != 0:
                print("hi am here")
                if 70 <= rate2 <= 106:
                    mass_rate2_result.configure(bg='green')
                else:
                    mass_rate2_result.configure(bg='red')
        
def show_previous_frame(frame1tobedestroyed):
    # Show the previous frames
  

    # Destroy the new frame
    frame1tobedestroyed.grid_forget()

def go_to_next_page():
    new_frame.grid(row=0, column=0, sticky="news")
# this function creates a new frame when the start button in the main fuel gauger file is called
#it also activate the next page button, and gives it a command to go to the next page when the next page button is hit
def create_new_frame(frame, button, start_button):
    global page1_entry_manager
    next_page_button = button
    
    next_page_button.configure(state=tkinter.NORMAL)
    start_button.configure(state=tkinter.DISABLED)
    # Create a new frame
    global new_frame
    new_frame = tkinter.Frame(frame)
    new_frame.grid(row=0, column=0, sticky="news")
    #next_page_button.configure(command=lambda: go_to_next_page())

    def check_entry_pressure(event):
        try:
            value = float(event.widget.get())

            if 2.8 <= value <= 3.2:
                event.widget.configure(bg='green')
            else:
                event.widget.configure(bg='red')
        except ValueError:
            event.widget.configure(bg='red')

    # Add widgets to the new frame
    # Example:
    pumps_pressure_frame = tkinter.LabelFrame(new_frame, text = "Pumps Pressure (bar)")
    pumps_pressure_frame.grid(row = 0, column = 0, sticky="news", padx=20, pady=10)
    ######
    left_pump_frame = tkinter.LabelFrame(pumps_pressure_frame, text = "Left Pump (bar)")
    left_pump_frame.grid(row = 0, column = 0, sticky="news", padx=20, pady=10)
    left_pump1_label = tkinter.Label(left_pump_frame, text="L.T pump1")
    left_pump1_label.grid(row=0, column=0)
    left_pump1_entry = tkinter.Entry(left_pump_frame)

    left_pump1_entry.grid(row=0, column=1)
    left_pump1_entry.bind("<KeyRelease>", check_entry_pressure)
    
    ######
    left_pump2_label = tkinter.Label(left_pump_frame, text="L.T pump2")
    left_pump2_label.grid(row=1, column=0)
    left_pump2_entry = tkinter.Entry(left_pump_frame)
    left_pump2_entry.grid(row=1, column=1)
    left_pump2_entry.bind("<FocusOut>", check_entry_pressure)
    ######
    right_pump_frame = tkinter.LabelFrame(pumps_pressure_frame, text = "Right Pump (bar)")
    right_pump_frame.grid(row = 0, column = 1, sticky="news", padx=20, pady=10)
    right_pump1_label = tkinter.Label(right_pump_frame, text="R.T pump1")
    right_pump1_label.grid(row=0, column=2)
    right_pump1_entry = tkinter.Entry(right_pump_frame)
    right_pump1_entry.grid(row=0, column=3)
    right_pump1_entry.bind("<FocusOut>", check_entry_pressure)
    #######
    right_pump2_label = tkinter.Label(right_pump_frame, text="R.T pump2")
    right_pump2_label.grid(row=1, column=2)
    right_pump2_entry = tkinter.Entry(right_pump_frame)
    right_pump2_entry.grid(row=1, column=3)
    right_pump2_entry.bind("<FocusOut>", check_entry_pressure)

    global Jet_pumps_mass_flow_rate_frame
    global center_jet_pump1_frame
    global center_jet_pump2_frame
    global start_mass1_label
    global end_mass2_label
    global start_mass2_label
    global end_mass1_label
    global mass_rate1_label
    global mass_rate2_label
    global mass_rate1_result
    global mass_rate2_result
    global rate1
    global rate2

    Jet_pumps_mass_flow_rate_frame = tkinter.LabelFrame(new_frame, text = "Mass Flow Rate (Kg/min)")
    Jet_pumps_mass_flow_rate_frame.grid(row = 1, column = 0, sticky="news", padx=20, pady=10)

    center_jet_pump1_frame = tkinter.LabelFrame(Jet_pumps_mass_flow_rate_frame, text = "CTR JET 1 (Kg/min)")
    center_jet_pump1_frame.grid(row = 0, column = 0, sticky="news", padx=20, pady=10)

    start_mass1_label = tkinter.Label(center_jet_pump1_frame, text='Mass (kg) "0"min')
    start_mass1_label.grid(row=0, column=0)
    start_mass1_entry = tkinter.Entry(center_jet_pump1_frame)
    start_mass1_entry.grid(row=0, column=1)
    ######
    end_mass1_label = tkinter.Label(center_jet_pump1_frame, text='Mass (kg) "5"min')
    end_mass1_label.grid(row=1, column=0)
    end_mass1_entry = tkinter.Entry(center_jet_pump1_frame)
    end_mass1_entry.grid(row=1, column=1)
    
    rate1 = 0
    rate2 = 0

    def calculate_rate1():
        global rate1
        try:
            start_mass = float(start_mass1_entry.get())
            end_mass = float(end_mass1_entry.get())
            rate1 = abs(end_mass - start_mass) / 5  # Assuming 5 minutes duration
            #mass_rate1_result.configure(state='normal')
            mass_rate1_result.configure(text=f'{rate1:.2f}')
            #mass_rate1_result_entry.delete(0, tkinter.END)  # Clear any previous value
            #mass_rate1_result_entry.insert(0, f'{rate:.2f}')
            #mass_rate1_result_entry.configure(state='readonly')
            #Check if rate is between 80 and 100
            if checker == 1:
                if 70 <= rate1 <= 106:
                    mass_rate1_result.configure(bg='green')
                else:
                    mass_rate1_result.configure(bg='red')  # Reset to default color
            if checker == 2:
                if 154.3 <= rate1 <= 233.7:
                    mass_rate1_result.configure(bg='green')
                else:
                    mass_rate1_result.configure(bg='red')  # Reset to default color
        except ValueError:
            mass_rate1_result.configure(state='normal')
            #mass_rate1_result_entry.delete(0, tkinter.END)
            mass_rate1_result.configure(text="Invalid input", bg='white')
            #mass_rate1_result_entry.configure(state='readonly')  # Set as readonly after displaying error
    calculate_button = tkinter.Button(center_jet_pump1_frame, text="Calculate Rate", command=calculate_rate1)
    calculate_button.grid(row=2, column=0)
    mass_rate1_result = tkinter.Label(center_jet_pump1_frame, borderwidth=1, relief="solid", width=17, height=1)
    mass_rate1_result.grid(row=2, column=1)
    mass_rate1_label = tkinter.Label(center_jet_pump1_frame, text="(Kg/min)")
    mass_rate1_label.grid(row=3, column=0)
    start_mass1_entry.bind("<KeyRelease>", lambda event: calculate_rate1())
    end_mass1_entry.bind("<KeyRelease>", lambda event: calculate_rate1())
    ################
    center_jet_pump2_frame = tkinter.LabelFrame(Jet_pumps_mass_flow_rate_frame, text = "CTR JET 2 (Kg/min)")
    center_jet_pump2_frame.grid(row = 0, column = 1, sticky="news", padx=20, pady=10)

    start_mass2_label = tkinter.Label(center_jet_pump2_frame, text='Mass (kg) "0"min')
    start_mass2_label.grid(row=0, column=0)
    start_mass2_entry = tkinter.Entry(center_jet_pump2_frame)
    start_mass2_entry.grid(row=0, column=1)
    ######
    end_mass2_label = tkinter.Label(center_jet_pump2_frame, text='Mass (kg) "5"min')
    end_mass2_label.grid(row=1, column=0)
    end_mass2_entry = tkinter.Entry(center_jet_pump2_frame)
    end_mass2_entry.grid(row=1, column=1)
    def calculate_rate2():
        global rate2
        try:
            start_mass = float(start_mass2_entry.get())
            end_mass = float(end_mass2_entry.get())
            rate2 = abs(end_mass - start_mass) / 5  # Assuming 5 minutes duration
            #mass_rate2_result.configure(state='normal')
            mass_rate2_result.configure(text=f'{rate2:.2f}')
            #mass_rate1_result_entry.delete(0, tkinter.END)  # Clear any previous value
            #mass_rate1_result_entry.insert(0, f'{rate:.2f}')
            #mass_rate1_result_entry.configure(state='readonly')
            #Check if rate is between 80 and 100
            if checker == 1:
                if 70 <= rate2 <= 106:
                    mass_rate2_result.configure(bg='green')
                else:
                    mass_rate2_result.configure(bg='red')  # Reset to default color
            if checker == 2:
                if 154.3 <= rate2 <= 233.7:
                    mass_rate2_result.configure(bg='green')
                else:
                    mass_rate2_result.configure(bg='red')  # Reset to default color
        except ValueError:
            #mass_rate2_result.configure(state='normal')
            #mass_rate1_result_entry.delete(0, tkinter.END)
            mass_rate2_result.configure(text="Invalid input", bg='white')
            #mass_rate1_result_entry.configure(state='readonly')  # Set as readonly after displaying error
    calculate_button = tkinter.Button(center_jet_pump2_frame, text="Calculate Rate", command=calculate_rate2)
    calculate_button.grid(row=2, column=0)
    mass_rate2_result = tkinter.Label(center_jet_pump2_frame, borderwidth=1, relief="solid", width=17, height=1)
    mass_rate2_result.grid(row=2, column=1)
    mass_rate2_label = tkinter.Label(center_jet_pump2_frame, text="(Kg/min)")
    mass_rate2_label.grid(row=3, column=0)
    start_mass2_entry.bind("<KeyRelease>", lambda event: calculate_rate2())
    end_mass2_entry.bind("<KeyRelease>", lambda event: calculate_rate2())
    
    ###############################################################################################
    next_reset_frame = tkinter.Frame(new_frame)
    next_reset_frame.grid(row = 6, column = 0, sticky="news", padx=20, pady=20)
    #Back Button  
     
    back_button = tkinter.Button(next_reset_frame, text="Back", command=lambda: show_previous_frame(new_frame))
    back_button.grid(row=6, column=0, pady=(10, 0))

    page1_entry_manager = classes_page1.page1_EntryManager(left_pump1_entry, left_pump2_entry, right_pump1_entry, right_pump2_entry, start_mass1_entry, end_mass1_entry, start_mass2_entry, end_mass2_entry, mass_rate1_result, mass_rate2_result)
    #def on_next():
        #page1_entry_maneger.store_entries()
        #create_2nd_frame(frame) 
    
    error_label = tkinter.Label(new_frame, text="", fg="red")
    error_label.grid(row=3, column=0, pady=(0, 10))

    def on_continue():
        if page1_entry_manager.are_entries_filled() and page1_entry_manager.check_mass_rates(mass_rate1_result, mass_rate2_result):
            dictionary_page1 = page1_entry_manager.store_entries(checker)
            with open('dictionary_page0.pkl', 'rb') as file:
                dictionary_page0 = pickle.load(file)

            # Merge dictionaries
            dictionary_page0.update(dictionary_page1)
            with open('dictionary_page0.pkl', 'wb') as file:
                pickle.dump(dictionary_page0, file)

            print(f"hi {checker}")
            create_2nd_frame(frame, next_page_button, continue_button)
            configure_text_kilo_or_livre_page2(checker)
            error_label.config(text="")  # Clear any previous error message
        # hide_page1_frames()
        # entry_manager.reset_entries()
        else:
            error_label.config(text="Error: Please fill in all the entries.")
            tkinter.messagebox.showerror("Error", "Please fill in all the entries.")
    def on_next_page():
        if page1_entry_manager.are_entries_filled():
            dictionary_page1 = page1_entry_manager.store_entries(checker)
            with open('dictionary_page0.pkl', 'rb') as file:
                dictionary_page0 = pickle.load(file)

            # Merge dictionaries
            dictionary_page0.update(dictionary_page1)
            with open('dictionary_page0.pkl', 'wb') as file:
                pickle.dump(dictionary_page0, file)
            configure_text_kilo_or_livre_page2(checker)
            go_to_second_page()
            error_label.config(text="")  # Clear any previous error message
        # hide_page1_frames()
        # entry_manager.reset_entries()
        else:
            error_label.config(text="Error: Please fill in all the entries.")
            tkinter.messagebox.showerror("Error", "Please fill in all the entries.")

    continue_button = tkinter.Button(next_reset_frame, text="continue", command = on_continue)
    continue_button.grid(row=6, column=1, pady=(10, 0))
    next_page_button = tkinter.Button(next_reset_frame, text="Next Page", command = on_next_page)
    next_page_button.grid(row=6, column=2, pady=(10, 0))
    next_page_button.configure(state=tkinter.DISABLED)

    

        
    #reset_page_button = tkinter.Button(next_reset_frame, text="reset", command = erase_page1_entries)
    #reset_page_button.grid(row=6, column=3, pady=(10, 0))
    


    #a function that erases the entries of page1 from the main frame

#def erase_page1_entries():
    #page1_entry_manager.reset_entries()

        
   
