class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
C1 = TemperatureConverter
print(C1.celsius_to_fahrenheit(45))
