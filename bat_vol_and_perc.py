from machine import Pin, ADC
import time

bat_adc = ADC(Pin(35))        # The battery status ADC object
bat_adc.atten(ADC.ATTN_11DB)           # Full range: 3,3 V
bat_scaling = 3.3 / 4095

while True:
    
    def read_battery_voltage():
        adc_val = bat_adc.read()
        voltage = bat_scaling * adc_val
        return voltage

    print("Batterispænding:", read_battery_voltage())
    volt = read_battery_voltage()

    def bat_perc(volt):
        batt_per = 100 * ((volt - 1.65) / (2.4 - 1.65))
        return batt_per

    bat_perc(volt)
    print(bat_perc(volt))
    time.sleep(1)
    

    