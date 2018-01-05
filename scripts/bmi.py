#!/usr/bin/python

def gather_info():
    height= float(raw_input ("What is you height? (inches or meters)"))
    weight= float(raw_input ("What is you weight? (kilograms or pounds)"))
    unit = raw_input("Are you measurements in metric of imperial units?").lower().strip()
    return (height,weight,unit)

def calculate_bmi(weight,height,unit='metric'):
    if unit == 'metric':
        bmi =  (weight/(height ** 2))
    else:
        bmi = 703 * (weight/(height ** 2))

    print ("your BMI is %s" % bmi)

while True:
    height,weight,unit = gather_info()
    if unit.startswith('i'):
        calculate_bmi(height=height, weight=weight, unit='imperial')
        break
    elif unit.startswith('m'):
        calculate_bmi(weight, height)
        break
    else:
        print ("Error : Unknow measure system.Please use imperial or metric")

