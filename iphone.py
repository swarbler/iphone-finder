import os
import colorama
from colorama import Fore, Back

# name of phone (e.g. iPhone 5S, iPhone X, iPhone 13 Pro Max)
# screen size 
#   small/below 6"
#   standard/between 6.1 and 6.3"
#   large/over 6.5"
# material (dual tone, plastic body, metal body, metal frame + glass back)
# shape (curved sides, flat sides)
# biometrics (none, TouchID, FaceID)`   `
# camera bump
#   none (i.e. all iPhone models before 6)
#   single camera bump (main only, i.e. iPhone 6 and onwards)
#   horizontal dual camera bump (main + telephoto, i.e. 7 Plus and 8 Plus)
#   pill-shaped dual camera bump (main + ultrawide, i.e. iPhone X and XS)
#   vertical dual camera bump (main + ultrawide, i.e. iPhone 11, 12, and 16)
#   diagonal dual camera bump (main + ultrawide, i.e. iPhone 13, 14, and 15)
#   triangle triple camera bump (main + ultrawide + telephoto, i.e. iPhone Pro models)
# display notch (bars/bezels, notch, Dynamic Island)
# port (lightning, Lightning, USB-C)
# headphone jack (true/false)
# magsafe (true/false)
# maximum optical zoom (1x/3x/5x)
# action button (true/false)
# camera control (true/false)

properties = ["screen size", "material", "shape", "biometrics", "camera bump", "display notch", "port", "headphone jack", "magsafe", "action button", "camera_control"]

# inits class "Phone"
class Phone:
  def __init__(self, name, properties):
    self.name = name
    self.properties = properties

# creating objects for each iPhone
iphone_2g = Phone("iPhone (original)", ["3.5-inch", "dual-tone", "ipod", "none", "none", "bezels", "30-pin", "true", "false", "false", "false"])
iphone_3g = Phone("iPhone 3G", ["3.5-inch", "plastic", "ipod", "none", "none", "bezels", "30-pin", "true", "false", "false", "false"])
iphone_3gs = Phone("iPhone 3Gs", ["3.5-inch", "plastic", "ipod", "none", "none", "bezels", "30-pin", "true", "false", "false", "false"])
iphone_4 = Phone("iPhone 4", ["3.5-inch", "glass back", "flat edges", "none", "none", "bezels", "30-pin", "true", "false", "false", "false"])
iphone_4s = Phone("iPhone 4s", ["3.5-inch", "glass back", "flat edges", "none", "none", "bezels", "30-pin", "true", "false", "false", "false"])
iphone_5 = Phone("iPhone 5", ["4-inch", "metal back", "flat edges", "none", "none", "bezels", "lightning", "true", "false", "false", "false"])
iphone_5c = Phone("iPhone 5c", ["4-inch", "plastic", "flat edges", "none", "none", "bezels", "lightning", "true", "false", "false", "false"])
iphone_5s = Phone("iPhone 5s", ["4-inch", "metal back", "flat edges", "TouchID", "none", "bezels", "lightning", "true", "false", "false", "false"])
iphone_6 = Phone("iPhone 6", ["4.7-inch", "metal back", "rounded edges", "TouchID", "single", "bezels", "lightning", "true", "false", "false", "false"])
iphone_6_plus = Phone("iPhone 6 Plus", ["5.5-inch", "metal back", "rounded edges", "TouchID", "single", "bezels", "lightning", "true", "false", "false", "false"])
iphone_6s = Phone("iPhone 6s", ["4.7-inch", "metal back", "rounded edges", "TouchID", "single", "bezels", "lightning", "true", "false", "false", "false"])
iphone_6s_plus = Phone("iPhone 6s Plus", ["5.5-inch", "metal back", "rounded edges", "TouchID", "single", "bezels", "lightning", "true", "false", "false", "false"])
iphone_se_1 = Phone("iPhone SE 1st generation", ["4-inch", "metal back", "flat edges", "TouchID", "none", "bezels", "lightning", "true", "false", "false", "false"])
iphone_7 = Phone("iPhone 7", ["4.7-inch", "metal back", "rounded edges", "TouchID", "single", "bezels", "lightning", "courage", "false", "false", "false"])
iphone_7_plus = Phone("iPhone 7 Plus", ["5.5-inch", "metal back", "rounded edges", "TouchID", "dual_horizontal", "bezels", "lightning", "courage", "false", "false", "false"])
iphone_8 = Phone("iPhone 8", ["4.7-inch", "glass back", "rounded edges", "TouchID", "single", "bezels", "lightning", "courage", "false", "false", "false"])
iphone_8_plus = Phone("iPhone 8 Plus", ["5.5-inch", "glass back", "rounded edges", "TouchID", "dual_horizontal", "bezels", "lightning", "courage", "false", "false", "false"])
iphone_x = Phone("iPhone X", ["5.8-inch", "glass back", "rounded edges", "FaceID", "dual_pill", "notch", "lightning", "courage", "false", "false", "false"])
iphone_xr = Phone("iPhone XR", ["6.1-inch", "glass back", "rounded edges", "FaceID", "single", "notch", "lightning", "courage", "false", "false", "false"])
iphone_xs = Phone("iPhone XS", ["5.8-inch", "glass back", "rounded edges", "FaceID", "dual_pill", "notch", "lightning", "courage", "false", "false", "false"])
iphone_xs_max = Phone("iPhone XS Max", ["6.5-inch", "glass back", "rounded edges", "FaceID", "dual_pill", "notch", "lightning", "courage", "false", "false", "false"])
iphone_11 = Phone("iPhone 11", ["6.1-inch", "glass back", "rounded edges", "FaceID", "dual_vertical", "notch", "lightning", "courage", "false", "false", "false"])
iphone_11_pro = Phone("iPhone 11 Pro", ["5.5-inch", "glass back", "rounded edges", "FaceID", "triple", "notch", "lightning", "courage", "false", "false", "false"])
iphone_11_pro_max = Phone("iPhone 11 Pro Max", ["5.8-inch", "glass back", "rounded edges", "FaceID", "triple", "notch", "lightning", "courage", "false", "false", "false"])
iphone_se_2 = Phone("iPhone SE 2nd generation", ["4.7-inch", "glass back", "rounded edges", "TouchID", "single", "bezels", "lightning", "courage", "false", "false", "false"])
iphone_12_mini = Phone("iPhone 12 Mini", ["5.4-inch", "glass back", "flat edges", "FaceID", "dual_vertical", "notch", "lightning", "courage", "true", "false", "false"])
iphone_12 = Phone("iPhone 12", ["6.1-inch", "glass back", "flat edges", "FaceID", "dual_vertical", "notch", "lightning", "courage", "true", "false", "false"])
iphone_12_pro = Phone("iPhone 12 Pro", ["6.1-inch", "glass back", "flat edges", "FaceID", "triple", "notch", "lightning", "courage", "true", "false", "false"])
iphone_12_pro_max = Phone("iPhone 12 Pro Max", ["6.7-inch", "glass back", "flat edges", "FaceID", "triple", "notch", "lightning", "courage", "true", "false", "false"])
iphone_13_mini = Phone("iPhone 13 Mini", ["5.4-inch", "glass back", "flat edges", "FaceID", "dual_diagonal", "notch", "lightning", "courage", "true", "false", "false"])
iphone_13 = Phone("iPhone 13", ["6.1-inch", "glass back", "flat edges", "FaceID", "dual_diagonal", "notch", "lightning", "courage", "true", "false", "false"])
iphone_13_pro = Phone("iPhone 13 Pro", ["6.1-inch", "glass back", "flat edges", "FaceID", "triple", "notch", "lightning", "courage", "true", "false", "false"])
iphone_13_pro_max = Phone("iPhone 13 Pro Max", ["6.7-inch", "glass back", "flat edges", "FaceID", "triple", "notch", "lightning", "courage", "true", "false", "false"])
iphone_se_3 = Phone("iPhone SE 3rd generation", ["4.7-inch", "glass back", "rounded edges", "TouchID", "single", "bezels", "lightning", "courage", "false", "false", "false"])
iphone_14 = Phone("iPhone 14", ["6.1-inch", "glass back", "flat edges", "FaceID", "dual_diagonal", "notch", "lightning", "courage", "true", "false", "false"])
iphone_14_plus = Phone("iPhone 14 Plus", ["6.7-inch", "glass back", "flat edges", "FaceID", "dual_diagonal", "notch", "lightning", "courage", "true", "false", "false"])
iphone_14_pro = Phone("iPhone 14 Pro Max", ["6.1-inch", "glass back", "flat edges", "FaceID", "triple", "dynamic island", "lightning", "courage", "true", "false", "false"])
iphone_14_pro_max = Phone("iPhone 14 Pro Max", ["6.7-inch", "glass back", "flat edges", "FaceID", "triple", "dynamic island", "lightning", "courage", "true", "false", "false"])
iphone_15 = Phone("iPhone 15", ["6.1-inch", "glass back", "flat edges", "FaceID", "dual_diagonal", "dynamic island", "USB-C", "courage", "true", "false", "false"])
iphone_15_plus = Phone("iPhone 15 Plus", ["6.7-inch", "glass back", "flat edges", "FaceID", "dual_diagonal", "dynamic island", "USB-C", "courage", "true", "false", "false"])
iphone_15_pro = Phone("iPhone 15 Pro", ["6.1-inch", "glass back", "flat edges", "FaceID", "triple", "dynamic island", "USB-C", "courage", "true", "true", "false"])
iphone_15_pro_max = Phone("iPhone 15 Pro Max", ["6.7-inch", "glass back", "flat edges", "FaceID", "triple", "dynamic island", "USB-C", "courage", "true", "true", "false"])
iphone_16 = Phone("iPhone 16", ["6.1-inch", "glass back", "flat edges", "FaceID", "dual_vertical", "dynamic island", "USB-C", "courage", "true", "true", "true"])
iphone_16_plus = Phone("iPhone 16 Plus", ["6.7-inch", "glass back", "flat edges", "FaceID", "dual_vertical", "dynamic island", "USB-C", "courage", "true", "true", "true"])
iphone_16_pro = Phone("iPhone 16 Pro", ["6.3-inch", "glass back", "flat edges", "FaceID", "triple", "dynamic island", "USB-C", "courage", "true", "true", "true"])
iphone_16_pro_max = Phone("iPhone 16 Pro Max", ["6.9-inch", "glass back", "flat edges", "FaceID", "triple", "dynamic island", "USB-C", "courage", "true", "true", "true"])
iphone_16e = Phone("iPhone 16e", ["6.1-inch", "glass back", "flat edges", "FaceID", "single", "notch", "USB-C", "courage", "false", "true", "false"])

# all Phone objects in a list
iphone_list = [
    iphone_2g,
    iphone_3g,
    iphone_3gs,
    iphone_4,
    iphone_4s,
    iphone_5,
    iphone_5c,
    iphone_5s,
    iphone_6,
    iphone_6_plus,
    iphone_6s,
    iphone_6s_plus,
    iphone_se_1,
    iphone_7,
    iphone_7_plus,
    iphone_8,
    iphone_8_plus,
    iphone_x,
    iphone_xr,
    iphone_xs,
    iphone_xs_max,
    iphone_11,
    iphone_11_pro,
    iphone_11_pro_max,
    iphone_se_2,
    iphone_12_mini,
    iphone_12,
    iphone_12_pro,
    iphone_12_pro_max,
    iphone_13_mini,
    iphone_13,
    iphone_13_pro,
    iphone_13_pro_max,
    iphone_se_3,
    iphone_14,
    iphone_14_plus,
    iphone_14_pro,
    iphone_14_pro_max,
    iphone_15,
    iphone_15_plus,
    iphone_15_pro,
    iphone_15_pro_max,
    iphone_16,
    iphone_16_plus,
    iphone_16_pro,
    iphone_16_pro_max,
    iphone_16e,
]

def list_all_properties():
    for i in range(len(properties)): # iterates over each property
        print(properties[i]) # prints property title

        for j in iphone_list: # iterates over every phone
            print(f"---> {j.name} : {j.properties[i]}") # prints phone and its property

def find_phone():
    phone_found = False
    correct_phone = "iPhone"
    current_phone_list = iphone_list

    while not phone_found: # repeat until phone is found
        for i in range(1, len(properties) - 1): # iterates every property except screen size
            available_input = [current_phone_list[0].properties[i]]
            
            for j in range(len(current_phone_list) - 1): # adds all selectable properties to available input
                if not current_phone_list[j].properties[i] in available_input: # append if unique
                    available_input.append(current_phone_list[j].properties[i]) 
            
            if len(available_input) != 1: # if there is more than one available input
                if i != 1: # does not appear on first question
                    print(Fore.GREEN + "current phones")
                    for c in current_phone_list: # displays every possible input
                        print(Fore.CYAN + f"--> {c.name}")
                print(Fore.BLUE + properties[i].upper()) # prints property name in UPPERCASE
                for a in available_input: # displays every possible input
                    print(Fore.LIGHTBLUE_EX + f"--> {a}")
                
                user_input = "" 
                
                while not user_input in available_input: # waits for user to input
                    user_input = input(Fore.YELLOW + "enter: ")

                for b in range(len(current_phone_list) - 1, -1, -1): # iterates in reverse to avoid conflicts with list indexes (janky, I know)
                    if user_input.lower().strip() != current_phone_list[b].properties[i].lower().strip(): # if property is different to user's input
                        print(f"{Fore.RED}{current_phone_list[b].name} REMOVED!") # REMOVED
                        current_phone_list.pop(b) # pops it out of the list
            
                input("\npress enter to continue...")

            if len(current_phone_list) == 1: # only one phone left 
                phone_found = True


            os.system("cls") # clears screen
        
        phone_found = True # when all properties have been used up

    print(Fore.MAGENTA + "Your iPhone could be one of the following:")
    for m in current_phone_list:
        print(f"-> {m.name}: {m.properties[0]} screen size") # indicates screen size to differentiate against models with the same properties (e.g. iPhone 12 Mini vs 12)
    input("\npress enter to exit the program...")

find_phone()

