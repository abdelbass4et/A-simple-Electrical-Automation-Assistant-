import random

class Ohm_law:
    def __init__(self, voltage, resistance, current):
        self.voltage = float(voltage) if voltage != '' else None
        self.resistance = float(resistance) if resistance != '' else None
        self.current = float(current) if current != '' else None

    def ohm_law(self):
        if self.voltage is None:
            self.voltage = self.resistance * self.current
            return f"{round(self.voltage, 2)} V"
        
        elif self.current is None:
            self.current = self.voltage / self.resistance
            return f"{round(self.current, 2)} A"
        
        elif self.resistance is None:
            self.resistance = self.voltage / self.current
            return f"{round(self.resistance, 2)} Ω"
            
class IndustirialSensor:
    def __init__(self, Rt=None, The_Scaling_Facor=0.385, Nominal_resistance=100):
        self.Rt = Rt if Rt is not None else random.uniform(111.55, 150.05)
        self.The_Scaling_Facor = 0.385
        self.Nominal_resistance = 100

    def count_Temperature(self):
        Temperature = (self.Rt - 100) / 0.385
        return round(Temperature, 2)    
    
class Cercuit_Resistance:
    def __init__(self, resistors):
        self.resistors = resistors

    def count_Totall_series(self):
        Tottall_series = sum(self.resistors)
        return round(Tottall_series, 2)
    
    def count_Parallel(self):
        small_resistors = []
        for x in self.resistors:
            if x == 0: continue
            resistore = 1 / x
            small_resistors.append(resistore)
        if not small_resistors:
            return 0
        Totall_parallel = 1 / sum(small_resistors)
        return round(Totall_parallel, 2)