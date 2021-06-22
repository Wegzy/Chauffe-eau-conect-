#!/usr/bin/python3.9
#coding: utf-8

from smbus2 import *
import time

SLAVE_ADDRESS = 0x51
bus  = SMBus(1)

"""
    Adresse des registres
"""

SECONDS   = 0x03
MINUTES   = 0x04
HOURS     = 0x05
DAYS      = 0x06
WEEKDAYS  = 0x07
MONTHS    = 0x08
YEARS     = 0x09
CONTROL_1 = 0x00

def Set_time_RTC():
    try:
        
        heures = int(input("Heures : "))
        if ((heures<0) or (heures>24)):
            print("Merci de rentrer une heure entre 0 et 24")
            heures=int('erreur')
                

        minutes = int(input("Minutes : "))
        if (minutes<0) or (minutes>60) :
            print("Merci de rentrer une minute entre 0 et 60")
            minutes=int('erreur')


        secondes = int(00)
            
        print("L'heure va être synchronisée sur : {0} Heures, {1} Minutes, {2} Secondes".format(heures,minutes,secondes))

        heures = bin(heures)
        print(heures)
        minutes = bin(minutes)
        print(minutes)
        secondes = bin(secondes)
        print(secondes)

        bus.write_byte_data(SLAVE_ADDRESS, SECONDS, [secondes,minutes,heures])
        #val = bus.read_byte_data(SLAVE_ADDRESS, CONTROL_1, 9)
        val = bus.read_byte_data(SLAVE_ADDRESS, SECONDS, 4)
        print(val)
        # Récupérer champs

"""
        try:
            rtc_sec   = str(val[x])
            rtc_min   = str(val[x])
            rtc_hours = str(val[x])
            print(heures, minutes, secondes)

            rtc_sec = int(rtc_sec, 2)
            rtc_min = int(rtc_min, 2)
            rtc_hours = int(rtc_hours, 2)

        except:
            print("Problème dans la conversion")

        #print("Il est {0} heures, {1} minutes et {2} secondes".format(rtc_hours,rtc_min,rtc_sec))
"""
    except:
        Set_time_RTC()

Set_time_RTC()