from tkinter import *
import backend

class Base_Screen(Tk):
    def __init__(self):
        super().__init__()
        self.title('Electrical Assistant')
        self.geometry('800x800')
        self.configure(bg='#1e293b')
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(2, weight=1)
        
        self.Label = Label(text='Automation & Electrical Assistant',bg='#256eb0',fg= 'white',font=('Arial Black',22))
        self.Label.grid(row=0,column=0,columnspan=3,sticky='we',pady=20)
        
        self.Ohm_btn = Button(text="Ohm's Law",bg ='#334155',fg='#f8fafc',font=('Segoe Ui',11,'bold'),pady=8, relief='flat', command=self.show_ohm)
        self.Ohm_btn.grid(row=1,column=0, padx=10, sticky='we')
        
        self.Resistance_btn = Button(text="Resistanse circuit",bg ='#334155',fg='#f8fafc',font=('Segoe Ui',11,'bold'),pady=8, relief='flat', command=self.show_resistance)
        self.Resistance_btn.grid(row=1,column=1, padx=10, sticky='we')
        
        self.Temputare_btn = Button(text="Industrial Sensor(PLC)",bg ='#334155',fg='#f8fafc',font=('Segoe Ui',11,'bold'),pady=8, relief='flat', command=self.show_temperature)
        self.Temputare_btn.grid(row=1,column=2, padx=10, sticky='we')
        
        self.ohm_page = Ohmscreen(self)
        self.resistance_page = Count_resistance(self)
        self.temperature_page = count_Temperatur(self)
        
        self.current_page = self.ohm_page
        self.current_page.grid(row=2,column=0,columnspan=3,pady=40, sticky='n')

    def show_ohm(self):
        self.current_page.grid_forget()
        self.current_page = self.ohm_page
        self.current_page.grid(row=2,column=0,columnspan=3,pady=40, sticky='n')

    def show_resistance(self):
        self.current_page.grid_forget()
        self.current_page = self.resistance_page
        self.current_page.grid(row=2,column=0,columnspan=3,pady=40, sticky='n')

    def show_temperature(self):
        self.current_page.grid_forget()
        self.current_page = self.temperature_page
        self.current_page.grid(row=2,column=0,columnspan=3,pady=40, sticky='n')

class Ohmscreen(Frame):
    def __init__(self,parent):
        super().__init__(parent,bg= '#1e293b')      
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        
        self.main_title = Label(self,text='Leave the unkown value blank', bg='#1e293b',fg='#94a3b8',font=('Arial Black',13),pady=15)
        self.main_title.grid(row=0,column=1,columnspan=2,pady=(20,10))
        
        self.voltage_lbl = Label(self,text='Voltage (V)', bg='#1e293b',fg='#4ade80',font=('Arial Black',11),pady=15)
        self.voltage_lbl.grid(row=1,column=1,pady=10,padx=10,sticky='e')
        self.voltage_ent = Entry(self,width=25, font=('Arial', 12), bg='#334155', fg='white', insertbackground='white', relief='solid')
        self.voltage_ent.grid(row=1,column=2,pady=10,padx=10,sticky='w')
        
        self.resistance_lbl = Label(self,text='Resistance (R)', bg='#1e293b',fg='#4ade80',font=('Arial Black',11),pady=15)
        self.resistance_lbl.grid(row=2,column=1,pady=10,padx=10,sticky='e')
        self.resistance_ent = Entry(self,width=25, font=('Arial', 12), bg='#334155', fg='white', insertbackground='white', relief='solid')
        self.resistance_ent.grid(row=2,column=2,pady=10,padx=10,sticky='w')
        
        self.current_lbl = Label(self,text='Current (I)', bg='#1e293b',fg='#4ade80',font=('Arial Black',11),pady=15)
        self.current_lbl.grid(row=3,column=1,pady=10,padx=10,sticky='e')
        self.current_ent = Entry(self,width=25, font=('Arial', 12), bg='#334155', fg='white', insertbackground='white', relief='solid')
        self.current_ent.grid(row=3,column=2,pady=10,padx=10,sticky='w')
        
        self.result_btn = Button(self,text="Calculate Ohm's law",fg='white',bg='#256eb0',font=('Arial',14,'bold'), padx=20, pady=6, relief='flat')
        self.result_btn.config(command=self.check_two_inputs)
        self.result_btn.grid(row=4,column=1,columnspan=2,pady=25)

        self.error_lbl = Label(self,text='Error: Provide exactly two values',fg='#f87171',font=('Arial',16,'bold'),bg='#1e293b')
        self.res_lbl = Label(self,fg='#4ade80',font=('Arial Black',20),bg='#1e293b')

    def check_two_inputs(self):
        self.error_lbl.grid_forget()
        self.res_lbl.grid_forget()

        v = self.voltage_ent.get().strip()
        r = self.resistance_ent.get().strip()
        c = self.current_ent.get().strip()

        count = 0
        if v != '': count += 1
        if r != '': count += 1
        if c != '': count += 1

        if count != 2:
            self.error_lbl.grid(row=6,column=1,columnspan=2,pady=10)
            return
        elif count == 2:
            calc_object = backend.Ohm_law(v,r,c)
            result = calc_object.ohm_law()
            self.res_lbl.config(text=f"Result = {result}")
            self.res_lbl.grid(row=6,column=1,columnspan=2,pady=10)

class count_Temperatur(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg='#1e293b') 
        
        self.columnconfigure(0, weight=1)
        
        self.title_lbl = Label(self, text='Machine Temperature Moitoring System (Safety limit: 100°C)', bg='green', fg='white', font=('Arial Black', 16))
        self.title_lbl.grid(row=0, column=0, sticky='we', pady=20, padx=10)
        
        self.check_btn = Button(self, text="Check Temperature", fg='white', bg='#256eb0', font=('Arial', 14, 'bold'), padx=20, pady=6, relief='flat', command=self.do_math)
        self.check_btn.grid(row=1, column=0, pady=15)

        self.result_lbl = Label(self, text='', font=('Arial Black', 16), bg='#1e293b')
        self.message_lbl = Label(self, text='', font=('Arial', 14, 'bold'), pady=10)

    def do_math(self):
        self.result_lbl.grid_forget()
        self.message_lbl.grid_forget()

        sensor = backend.IndustirialSensor()
        self.temperature = sensor.count_Temperature()
        
        self.result_lbl.config(text=f'Current Temperature: {self.temperature}°C', fg='white')
        self.result_lbl.grid(row=2,column=0,sticky='we',pady=20)

        if self.temperature >= 100:
            self.message_lbl.config(text=f"🚨 ALERT: OVERHEAT ({self.temperature}°C)", bg="#b91c1c", fg="white")
            self.message_lbl.grid(column=0, row=3, sticky='we', pady=20, padx=40)
        elif 80 <= self.temperature < 100:
            self.message_lbl.config(text=f"⚠️ CAUTION: APPROACHING LIMIT ({self.temperature}°C)", bg="#eab308", fg="black")
            self.message_lbl.grid(column=0, row=3, sticky='we', pady=20, padx=40)
        elif self.temperature < 80:
            self.message_lbl.config(text=f"❄️ LOW TEMP: STABLE ({self.temperature}°C)", bg="#1d4ed8", fg="white")
            self.message_lbl.grid(column=0, row=3, sticky='we', pady=20, padx=40)

class Count_resistance(Frame): 
    def __init__(self, parent):
        super().__init__(parent, bg='#1e293b') 
        
        self.columnconfigure(0, weight=1)
        
        self.error_lbl = Label(self, text='Error: You have to enter at least two resistors', fg='#f87171', bg='#7f1d1d', font=('Arial', 14, 'bold'))
        
        self.title_lbl = Label(self, text='Enter Resistors separated by comma', font=('Arial Black', 15), bg='#1e293b', fg='#94a3b8')
        self.title_lbl.grid(row=0, column=0, sticky='we', pady=20)

        self.resistors_ent = Entry(self, font=('Arial', 14), width=25, bg='#334155', fg='white', insertbackground='white', relief='solid')
        self.resistors_ent.grid(row=1, column=0, pady=15)
        
        self.calc_btn = Button(self, text="Calculate Total Resistance", command=self.check_count_resistance, font=('Arial', 14, 'bold'), bg='#256eb0', fg='white', padx=20, pady=6, relief='flat')
        self.calc_btn.grid(row=2, column=0, pady=15)

        self.series_lbl = Label(self, fg='#4ade80', font=('Arial Black', 15), bg='#1e293b')
        self.parallel_lbl = Label(self, fg='#22d3ee', font=('Arial Black', 15), bg='#1e293b')

    def check_count_resistance(self):
        self.error_lbl.grid_forget()
        self.series_lbl.grid_forget()
        self.parallel_lbl.grid_forget()

        raw_input = self.resistors_ent.get()

        if raw_input.strip() == "":
            self.error_lbl.grid(row=4, column=0, sticky='we', pady=10)
            return

        try:
            input_list = raw_input.split(',')
            resistances = [float(r.strip()) for r in input_list if r.strip() != ""]
        except ValueError:
            self.error_lbl.config(text="Error: Please enter numbers only!")
            self.error_lbl.grid(row=4, column=0, sticky='we', pady=10)
            return

        if len(resistances) < 2:
            self.error_lbl.config(text="Error: You have to enter at least two resistors")
            self.error_lbl.grid(row=4, column=0, sticky='we', pady=10)
            return

        calc = backend.Cercuit_Resistance(resistances)
        series_res = calc.count_Totall_series()
        parallel_res = calc.count_Parallel()

        self.series_lbl.config(text=f"Total Series = {series_res} Ω")
        self.series_lbl.grid(row=5, column=0, pady=8)

        self.parallel_lbl.config(text=f"Total Parallel = {parallel_res} Ω")
        self.parallel_lbl.grid(row=6, column=0, pady=10)