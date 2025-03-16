#!/usr/bin/env python3
import requests
import base64
import json
import time
import RPi.GPIO as GPIO
from subprocess import call

DELAY_LISTENER = 3
DELAY_DEVICE = 2


# GitHub repository details
repo_owner = REDACTED
repo_name = REDACTED

file_path_instructions = REDACTED
#!/usr/bin/env python3
import requests
import base64
import json
import time
import RPi.GPIO as GPIO
from subprocess import call

DELAY_LISTENER = 3
DELAY_DEVICE = 2


# GitHub repository details
repo_owner = "jotigokaraju"
repo_name = "sensescript"

file_path_instructions = "instructions.txt"

# GitHub API URL
api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path_instructions}"
#!/usr/bin/env python3
import requests
import base64
import json
import time
import RPi.GPIO as GPIO
from subprocess import call

DELAY_LISTENER = 3
DELAY_DEVICE = 2


# GitHub repository details
repo_owner = "jotigokaraju"
repo_name = "sensescript"

file_path_instructions = "instructions.txt"

# GitHub API URL
api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path_instructions}"


#HIDE
n = "REDACTED"


step_sleep = 0.001                                                              

step_count = 512 # 5.625*(1/64) per step, 4096 steps is 360 Degrees, Octagonal Disc has 8 sides. 512 steps for 45 Degrees.


# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]


running_list = [[0, 0, 0, 0, 0, 0]]
count = 0
count_end = 0

#Stepper Motor 1
in1 = 2
in2 = 3
in3 = 4
in4 = 14


motor_pins = [in1,in2,in3,in4]
motor1_step_counter = 0                                                                                                                                               


#Stepper Motor 2
in1_2 = 17
in2_2 = 27
in3_2 = 22
in4_2 = 23


#Stepper Motor 3
in1_3 = 10
in2_3 = 9
in3_3 = 11
in4_3 = 25

motor_pins_3 = [in1_3,in2_3,in3_3,in4_3]
motor3_step_counter = 0  

#Stepper Motor 4
in1_4 = 5
in2_4 = 6
in3_4 = 13
in4_4 = 19

motor_pins_4 = [in1_4,in2_4,in3_4,in4_4]
motor4_step_counter = 0


# Braille mapping
braille_mapping = {
    'A': [5, 4],  # Braille Letter A
    'B': [2, 4],  # Braille Letter B
    'C': [6, 5],  # Braille Letter C
    'D': [6, 7],  # Braille Letter D
    'E': [6, 1],  # Braille Letter E
    'F': [2, 5],  # Braille Letter F
    'G': [2, 7],  # Braille Letter G
    'H': [2, 1],  # Braille Letter H
    'I': [1, 5],  # Braille Letter I
    'J': [1, 7],  # Braille Letter J
    'K': [3, 4],  # Braille Letter K
    'L': [0, 4],  # Braille Letter L
    'M': [3, 5],  # Braille Letter M
    'N': [3, 7],  # Braille Letter N
    'O': [3, 1],  # Braille Letter O
    'P': [0, 5],  # Braille Letter P
    'Q': [0, 7],  # Braille Letter Q
    'R': [0, 1],  # Braille Letter R
    'S': [7, 5],  # Braille Letter S
    'T': [7, 7],  # Braille Letter T
    'U': [3, 6],  # Braille Letter U
    'V': [0, 6],  # Braille Letter V
    'W': [1, 0],  # Braille Letter W
    'X': [3, 3],  # Braille Letter X
    'Y': [3, 0],  # Braille Letter Y
    'Z': [3, 2],  # Braille Letter Z
    ',': [1, 4],  # Braille Comma
    ';': [7, 4],  # Braille Semicolon
    ':': [1, 1],  # Braille Colon
    '.': [1, 2],  # Braille Full Stop
    '/': [5, 5],  # Braille Slash
    '-': [5, 6],  # Braille Dash
}

def convert_to_braille(text):
    # List to store the resulting sublists of two letters
    braille_result = []
    
    # Convert text to uppercase to make it case-insensitive
    text = text.upper()
    
    # Temporary list to store the [x1, y1, x2, y2] of two letters
    temp_pair = []
    
    # Iterate through each character in the text
    for char in text:
        if char in braille_mapping:  # If the character is in the mapping
            # Append the braille x, y values for the character
            temp_pair.extend(braille_mapping[char])
            
            # If we have two letters (4 values), add to the result and reset temp_pair
            if len(temp_pair) == 4:
                braille_result.append(temp_pair)
                temp_pair = []
    
    # If there's an odd number of letters, add the last one with [0, 0] padding
    if len(temp_pair) == 2:
        temp_pair.extend([0, 0])  # Pad with [0, 0]
        braille_result.append(temp_pair)
    
    return braille_result





def initialize1():
    # setting up
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)

    # initializing
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
 
def initialize2():
    # setting up
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1_2, GPIO.OUT)
    GPIO.setup(in2_2, GPIO.OUT)
    GPIO.setup(in3_2, GPIO.OUT)
    GPIO.setup(in4_2, GPIO.OUT)

    # initializing
    GPIO.output(in1_2, GPIO.LOW)
    GPIO.output(in2_2, GPIO.LOW)
    GPIO.output(in3_2, GPIO.LOW)
    GPIO.output(in4_2, GPIO.LOW)
    
def initialize3():
    # setting up
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1_3, GPIO.OUT)
    GPIO.setup(in2_3, GPIO.OUT)
    GPIO.setup(in3_3, GPIO.OUT)
    GPIO.setup(in4_3, GPIO.OUT)

    # initializing
    GPIO.output(in1_3, GPIO.LOW)
    GPIO.output(in2_3, GPIO.LOW)
    GPIO.output(in3_3, GPIO.LOW)
    GPIO.output(in4_3, GPIO.LOW)
    
def initialize4():
    # setting up
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1_4, GPIO.OUT)
    GPIO.setup(in2_4, GPIO.OUT)
    GPIO.setup(in3_4, GPIO.OUT)
    GPIO.setup(in4_4, GPIO.OUT)

    # initializing
    GPIO.output(in1_4, GPIO.LOW)
    GPIO.output(in2_4, GPIO.LOW)
    GPIO.output(in3_4, GPIO.LOW)
    GPIO.output(in4_4, GPIO.LOW)

motor_pins_2 = [in1_2,in2_2,in3_2,in4_2]
motor2_step_counter = 0 ;

    
#Creating 2 Different Values List for each Motor
values_list_motor1 = [0]
values_list_motor2 = [0]
values_list_motor3 = [0]
values_list_motor4 = [0]
#Pin Numberings for Buttons


GPIO.setwarnings(False)

           

def cleanup1():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    
def cleanup2():
    GPIO.output(in1_2, GPIO.LOW)
    GPIO.output(in2_2, GPIO.LOW)
    GPIO.output(in3_2, GPIO.LOW)
    GPIO.output(in4_2, GPIO.LOW)
    
def cleanup3():
    GPIO.output(in1_3, GPIO.LOW)
    GPIO.output(in2_3, GPIO.LOW)
    GPIO.output(in3_3, GPIO.LOW)
    GPIO.output(in4_3, GPIO.LOW)
    
def cleanup4():
    GPIO.output(in1_4, GPIO.LOW)
    GPIO.output(in2_4, GPIO.LOW)
    GPIO.output(in3_4, GPIO.LOW)
    GPIO.output(in4_4, GPIO.LOW)


def set_start_position(move_amount_motor1, move_amount_motor2, move_amount_motor3, move_amount_motor4, motor1_step_counter, motor2_step_counter, motor3_step_counter, motor4_step_counter):
    '''Set Start Position of Motors. Takes Args: Move Amount.'''
    
    initialize1()
    for index_motor_counter in range(int((step_count)*(move_amount_motor1))):
        for pin_1 in range(0, len(motor_pins)):  
            #Main Code to Output Value and Move Stepper Motor
            GPIO.output( motor_pins[pin_1], step_sequence[motor1_step_counter][pin_1] )
        motor1_step_counter = (motor1_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup1()
    initialize2()
    for index_motor_counter in range(int((step_count)*(move_amount_motor2))):
        for pins_motor2 in range(0, len(motor_pins_2)):
                #Main Code to Output Value and Move Stepper Motor
            GPIO.output( motor_pins_2[pins_motor2], step_sequence[motor2_step_counter][pins_motor2] )
        motor2_step_counter = (motor2_step_counter + 1) % 8
                
        time.sleep(step_sleep)
    cleanup2()
    initialize3()
    for index_motor_counter in range(int((step_count)*(move_amount_motor3))):
        for pins_motor3 in range(0, len(motor_pins_3)):
                #Main Code to Output Value and Move Stepper Motor
            GPIO.output( motor_pins_3[pins_motor3], step_sequence[motor3_step_counter][pins_motor3] )
        motor3_step_counter = (motor3_step_counter + 1) % 8
                
        time.sleep(step_sleep)
    cleanup3()
    initialize4()
    for index_motor_counter in range(int((step_count)*(move_amount_motor4))):
        for pins_motor4 in range(0, len(motor_pins_4)):
                #Main Code to Output Value and Move Stepper Motor
            GPIO.output( motor_pins_4[pins_motor4], step_sequence[motor4_step_counter][pins_motor4] )
        motor4_step_counter = (motor4_step_counter + 1) % 8
                
        time.sleep(step_sleep)
    cleanup4()

def calc_move_amount(values_list, instruction_set, location):
    '''Calculates Amount the Stepper Motor Needs to Move Based on (Values_List,
    instruction_set, and the location of which instructions the motor is using (0 or 1)'''
    
    move_to_position = 0
    
    #Depending on Which Stepper Motor, Read Either the First Data Point or Second Point
    move_to_position = instruction_set[location]
    
    #Add This to the Values_list for Future Use
    values_list.append(move_to_position)
       
    # In calc_move_amount, replace the if block with this:
    if values_list[-1] > values_list[-2]:
        return 8-values_list[-1]+values_list[-2]
    return values_list[-1]-values_list[-2]



        

def move_motors(values_list_motor1, values_list_motor2, values_list_motor3, values_list_motor4, instruction_set, motor1_step_counter, motor2_step_counter, motor3_step_counter, motor4_step_counter):
    # Calculate movement amounts
    move_amount_motor1 = calc_move_amount(values_list_motor1, instruction_set, 0)
    move_amount_motor2 = calc_move_amount(values_list_motor2, instruction_set, 1)
    move_amount_motor3 = calc_move_amount(values_list_motor3, instruction_set, 2)
    move_amount_motor4 = calc_move_amount(values_list_motor4, instruction_set, 3)
    
    # Initialize motors and move them to the new positions
    initialize1()
    for _ in range(step_count * move_amount_motor1):
        for pin in range(4):  # For each pin
            GPIO.output(motor_pins[pin], step_sequence[motor1_step_counter][pin])
        motor1_step_counter = (motor1_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup1()

    initialize2()
    for _ in range(step_count * move_amount_motor2):
        for pin in range(4):
            GPIO.output(motor_pins_2[pin], step_sequence[motor2_step_counter][pin])
        motor2_step_counter = (motor2_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup2()

    initialize3()
    for _ in range(step_count * move_amount_motor3):
        for pin in range(4):
            GPIO.output(motor_pins_3[pin], step_sequence[motor3_step_counter][pin])
        motor3_step_counter = (motor3_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup3()

    initialize4()
    for _ in range(step_count * move_amount_motor4):
        for pin in range(4):
            GPIO.output(motor_pins_4[pin], step_sequence[motor4_step_counter][pin])
        motor4_step_counter = (motor4_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup4()
    
    
#set_start_position(0, 0.125, motor1_step_counter, motor2_step_counter)

    

START = True
while START:

    
    # Get content
    response = requests.get(api_url, headers={"Authorization": f"Bearer {n}"})
    response_data = response.json()

         
    current_content = response_data["content"]
    current_content_decoded = base64.b64decode(current_content).decode("utf-8")

    # Treat the content as a string directly
    current_content_string = current_content_decoded

    # Check if the string content is not just "0"
    if current_content_string.strip() != "0":
        # Process the content as needed
        current_content_list = convert_to_braille(current_content_string.strip())
        
        for instruction_set in current_content_list:
            print(instruction_set)
            move_motors(values_list_motor1, values_list_motor2, values_list_motor3, values_list_motor4, instruction_set, motor1_step_counter, motor2_step_counter, motor3_step_counter, motor4_step_counter)


        set_0_motor1 = 8-values_list_motor1[-1]
        set_0_motor2 = 8-values_list_motor2[-1]
        set_0_motor4 = 8-values_list_motor4[-1]
        set_0_motor3 = 8-values_list_motor3[-1]
        values_list_motor1.append(0)
        values_list_motor2.append(0)
        values_list_motor3.append(0)
        values_list_motor4.append(0)
#         set_start_position(set_0_motor1, set_0_motor2, set_0_motor3, set_0_motor4, motor1_step_counter, motor2_step_counter, motor3_step_counter, motor4_step_counter)
        print(0)
        
        

        
        # Update content
        new_content = "0"

        # Encode new content
        new_content_encoded = base64.b64encode(new_content.encode("utf-8")).decode("utf-8")

        # Prepare data
        data = {
            "message": "Update instructions.txt",
            "content": new_content_encoded,
            "sha": response_data["sha"]
        }

        # Update
        update_response = requests.put(api_url, headers={"Authorization": f"Bearer {n}"}, json=data)

        if update_response.status_code == 200:
            print("Sent!")
        else:
            print(f"Error updating file. Status code: {update_response.status_code}")
                  
    time.sleep(DELAY_LISTENER)

#HIDE
n = "REDACTED"


step_sleep = 0.001                                                              

step_count = 512 # 5.625*(1/64) per step, 4096 steps is 360 Degrees, Octagonal Disc has 8 sides. 512 steps for 45 Degrees.


# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]


running_list = [[0, 0, 0, 0, 0, 0]]
count = 0
count_end = 0

#Stepper Motor 1
in1 = 2
in2 = 3
in3 = 4
in4 = 14


motor_pins = [in1,in2,in3,in4]
motor1_step_counter = 0                                                                                                                                               


#Stepper Motor 2
in1_2 = 17
in2_2 = 27
in3_2 = 22
in4_2 = 23


#Stepper Motor 3
in1_3 = 10
in2_3 = 9
in3_3 = 11
in4_3 = 25

motor_pins_3 = [in1_3,in2_3,in3_3,in4_3]
motor3_step_counter = 0  

#Stepper Motor 4
in1_4 = 5
in2_4 = 6
in3_4 = 13
in4_4 = 19

motor_pins_4 = [in1_4,in2_4,in3_4,in4_4]
motor4_step_counter = 0


# Braille mapping
braille_mapping = {
    'A': [6, 4],  # Braille Letter A
    'B': [2, 4],  # Braille Letter B
    'C': [6, 5],  # Braille Letter C
    'D': [6, 7],  # Braille Letter D
    'E': [6, 1],  # Braille Letter E
    'F': [2, 5],  # Braille Letter F
    'G': [2, 7],  # Braille Letter G
    'H': [2, 1],  # Braille Letter H
    'I': [1, 5],  # Braille Letter I
    'J': [1, 7],  # Braille Letter J
    'K': [3, 4],  # Braille Letter K
    'L': [0, 4],  # Braille Letter L
    'M': [3, 5],  # Braille Letter M
    'N': [3, 7],  # Braille Letter N
    'O': [3, 1],  # Braille Letter O
    'P': [0, 5],  # Braille Letter P
    'Q': [0, 7],  # Braille Letter Q
    'R': [0, 1],  # Braille Letter R
    'S': [7, 5],  # Braille Letter S
    'T': [7, 7],  # Braille Letter T
    'U': [3, 6],  # Braille Letter U
    'V': [0, 6],  # Braille Letter V
    'W': [1, 0],  # Braille Letter W
    'X': [3, 3],  # Braille Letter X
    'Y': [3, 0],  # Braille Letter Y
    'Z': [3, 2],  # Braille Letter Z
    ',': [1, 4],  # Braille Comma
    ';': [7, 4],  # Braille Semicolon
    ':': [1, 1],  # Braille Colon
    '.': [1, 2],  # Braille Full Stop
    '/': [5, 5],  # Braille Slash
    '-': [5, 6],  # Braille Dash
}

def convert_to_braille(text):
    # List to store the resulting sublists of two letters
    braille_result = []
    
    # Convert text to uppercase to make it case-insensitive
    text = text.upper()
    
    # Temporary list to store the [x1, y1, x2, y2] of two letters
    temp_pair = []
    
    # Iterate through each character in the text
    for char in text:
        if char in braille_mapping:  # If the character is in the mapping
            # Append the braille x, y values for the character
            temp_pair.extend(braille_mapping[char])
            
            # If we have two letters (4 values), add to the result and reset temp_pair
            if len(temp_pair) == 4:
                braille_result.append(temp_pair)
                temp_pair = []
    
    # If there's an odd number of letters, add the last one with [0, 0] padding
    if len(temp_pair) == 2:
        temp_pair.extend([0, 0])  # Pad with [0, 0]
        braille_result.append(temp_pair)
    
    return braille_result





def initialize1():
    # setting up
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)

    # initializing
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
 
def initialize2():
    # setting up
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1_2, GPIO.OUT)
    GPIO.setup(in2_2, GPIO.OUT)
    GPIO.setup(in3_2, GPIO.OUT)
    GPIO.setup(in4_2, GPIO.OUT)

    # initializing
    GPIO.output(in1_2, GPIO.LOW)
    GPIO.output(in2_2, GPIO.LOW)
    GPIO.output(in3_2, GPIO.LOW)
    GPIO.output(in4_2, GPIO.LOW)
    
def initialize3():
    # setting up
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1_3, GPIO.OUT)
    GPIO.setup(in2_3, GPIO.OUT)
    GPIO.setup(in3_3, GPIO.OUT)
    GPIO.setup(in4_3, GPIO.OUT)

    # initializing
    GPIO.output(in1_3, GPIO.LOW)
    GPIO.output(in2_3, GPIO.LOW)
    GPIO.output(in3_3, GPIO.LOW)
    GPIO.output(in4_3, GPIO.LOW)
    
def initialize4():
    # setting up
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1_4, GPIO.OUT)
    GPIO.setup(in2_4, GPIO.OUT)
    GPIO.setup(in3_4, GPIO.OUT)
    GPIO.setup(in4_4, GPIO.OUT)

    # initializing
    GPIO.output(in1_4, GPIO.LOW)
    GPIO.output(in2_4, GPIO.LOW)
    GPIO.output(in3_4, GPIO.LOW)
    GPIO.output(in4_4, GPIO.LOW)

motor_pins_2 = [in1_2,in2_2,in3_2,in4_2]
motor2_step_counter = 0 ;

    
#Creating 2 Different Values List for each Motor
values_list_motor1 = [0]
values_list_motor2 = [0]
values_list_motor3 = [0]
values_list_motor4 = [0]
#Pin Numberings for Buttons


GPIO.setwarnings(False)

           

def cleanup1():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    
def cleanup2():
    GPIO.output(in1_2, GPIO.LOW)
    GPIO.output(in2_2, GPIO.LOW)
    GPIO.output(in3_2, GPIO.LOW)
    GPIO.output(in4_2, GPIO.LOW)
    
def cleanup3():
    GPIO.output(in1_3, GPIO.LOW)
    GPIO.output(in2_3, GPIO.LOW)
    GPIO.output(in3_3, GPIO.LOW)
    GPIO.output(in4_3, GPIO.LOW)
    
def cleanup4():
    GPIO.output(in1_4, GPIO.LOW)
    GPIO.output(in2_4, GPIO.LOW)
    GPIO.output(in3_4, GPIO.LOW)
    GPIO.output(in4_4, GPIO.LOW)


def set_start_position(move_amount_motor1, move_amount_motor2, move_amount_motor3, move_amount_motor4, motor1_step_counter, motor2_step_counter, motor3_step_counter, motor4_step_counter):
    '''Set Start Position of Motors. Takes Args: Move Amount.'''
    
    initialize1()
    for index_motor_counter in range(int((step_count)*(move_amount_motor1))):
        for pin_1 in range(0, len(motor_pins)):  
            #Main Code to Output Value and Move Stepper Motor
            GPIO.output( motor_pins[pin_1], step_sequence[motor1_step_counter][pin_1] )
        motor1_step_counter = (motor1_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup1()
    initialize2()
    for index_motor_counter in range(int((step_count)*(move_amount_motor2))):
        for pins_motor2 in range(0, len(motor_pins_2)):
                #Main Code to Output Value and Move Stepper Motor
            GPIO.output( motor_pins_2[pins_motor2], step_sequence[motor2_step_counter][pins_motor2] )
        motor2_step_counter = (motor2_step_counter + 1) % 8
                
        time.sleep(step_sleep)
    cleanup2()
    initialize3()
    for index_motor_counter in range(int((step_count)*(move_amount_motor3))):
        for pins_motor3 in range(0, len(motor_pins_3)):
                #Main Code to Output Value and Move Stepper Motor
            GPIO.output( motor_pins_3[pins_motor3], step_sequence[motor3_step_counter][pins_motor3] )
        motor3_step_counter = (motor3_step_counter + 1) % 8
                
        time.sleep(step_sleep)
    cleanup3()
    initialize4()
    for index_motor_counter in range(int((step_count)*(move_amount_motor4))):
        for pins_motor4 in range(0, len(motor_pins_4)):
                #Main Code to Output Value and Move Stepper Motor
            GPIO.output( motor_pins_4[pins_motor4], step_sequence[motor4_step_counter][pins_motor4] )
        motor4_step_counter = (motor4_step_counter + 1) % 8
                
        time.sleep(step_sleep)
    cleanup4()

def calc_move_amount(values_list, instruction_set, location):
    '''Calculates Amount the Stepper Motor Needs to Move Based on (Values_List,
    instruction_set, and the location of which instructions the motor is using (0 or 1)'''
    
    move_to_position = 0
    
    #Depending on Which Stepper Motor, Read Either the First Data Point or Second Point
    move_to_position = instruction_set[location]
    
    #Add This to the Values_list for Future Use
    values_list.append(move_to_position)
       
    # In calc_move_amount, replace the if block with this:
    if values_list[-1] > values_list[-2]:
        return 8-values_list[-1]+values_list[-2]
    return values_list[-1]-values_list[-2]



        

def move_motors(values_list_motor1, values_list_motor2, values_list_motor3, values_list_motor4, instruction_set, motor1_step_counter, motor2_step_counter, motor3_step_counter, motor4_step_counter):
    # Calculate movement amounts
    move_amount_motor1 = calc_move_amount(values_list_motor1, instruction_set, 0)
    move_amount_motor2 = calc_move_amount(values_list_motor2, instruction_set, 1)
    move_amount_motor3 = calc_move_amount(values_list_motor3, instruction_set, 2)
    move_amount_motor4 = calc_move_amount(values_list_motor4, instruction_set, 3)
    
    # Initialize motors and move them to the new positions
    initialize1()
    for _ in range(step_count * move_amount_motor1):
        for pin in range(4):  # For each pin
            GPIO.output(motor_pins[pin], step_sequence[motor1_step_counter][pin])
        motor1_step_counter = (motor1_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup1()

    initialize2()
    for _ in range(step_count * move_amount_motor2):
        for pin in range(4):
            GPIO.output(motor_pins_2[pin], step_sequence[motor2_step_counter][pin])
        motor2_step_counter = (motor2_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup2()

    initialize3()
    for _ in range(step_count * move_amount_motor3):
        for pin in range(4):
            GPIO.output(motor_pins_3[pin], step_sequence[motor3_step_counter][pin])
        motor3_step_counter = (motor3_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup3()

    initialize4()
    for _ in range(step_count * move_amount_motor4):
        for pin in range(4):
            GPIO.output(motor_pins_4[pin], step_sequence[motor4_step_counter][pin])
        motor4_step_counter = (motor4_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup4()
    
    
#set_start_position(0, 0.125, motor1_step_counter, motor2_step_counter)

    

START = True
while START:

    
    # Get content
    response = requests.get(api_url, headers={"Authorization": f"Bearer {n}"})
    response_data = response.json()

         
    current_content = response_data["content"]
    current_content_decoded = base64.b64decode(current_content).decode("utf-8")

    # Treat the content as a string directly
    current_content_string = current_content_decoded

    # Check if the string content is not just "0"
    if current_content_string.strip() != "0":
        # Process the content as needed
        current_content_list = convert_to_braille(current_content_string.strip())
        
        for instruction_set in current_content_list:
            print(instruction_set)
            move_motors(values_list_motor1, values_list_motor2, values_list_motor3, values_list_motor4, instruction_set, motor1_step_counter, motor2_step_counter, motor3_step_counter, motor4_step_counter)


        set_0_motor1 = 8-values_list_motor1[-1]
        set_0_motor2 = 8-values_list_motor2[-1]
        set_0_motor4 = 8-values_list_motor4[-1]
        set_0_motor3 = 8-values_list_motor3[-1]
        values_list_motor1.append(0)
        values_list_motor2.append(0)
        values_list_motor3.append(0)
        values_list_motor4.append(0)
        set_start_position(set_0_motor1, set_0_motor2, set_0_motor3, set_0_motor4, motor1_step_counter, motor2_step_counter, motor3_step_counter, motor4_step_counter)
        print(0)
        
        

        
        # Update content
        new_content = "0"

        # Encode new content
        new_content_encoded = base64.b64encode(new_content.encode("utf-8")).decode("utf-8")

        # Prepare data
        data = {
            "message": "Update instructions.txt",
            "content": new_content_encoded,
            "sha": response_data["sha"]
        }

        # Update
        update_response = requests.put(api_url, headers={"Authorization": f"Bearer {n}"}, json=data)

        if update_response.status_code == 200:
            print("Sent!")
        else:
            print(f"Error updating file. Status code: {update_response.status_code}")
                  
    time.sleep(DELAY_LISTENER)
# GitHub API URL
api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/contents/{file_path_instructions}"


#HIDE
n = "REDACTED"


step_sleep = 0.001                                                              

step_count = 512 # 5.625*(1/64) per step, 4096 steps is 360 Degrees, Octagonal Disc has 8 sides. 512 steps for 45 Degrees.


# defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
step_sequence = [[1,0,0,1],
                 [1,0,0,0],
                 [1,1,0,0],
                 [0,1,0,0],
                 [0,1,1,0],
                 [0,0,1,0],
                 [0,0,1,1],
                 [0,0,0,1]]


running_list = [[0, 0, 0, 0, 0, 0]]
count = 0
count_end = 0

#Stepper Motor 1
in1 = 2
in2 = 3
in3 = 4
in4 = 14


motor_pins = [in1,in2,in3,in4]
motor1_step_counter = 0                                                                                                                                               


#Stepper Motor 2
in1_2 = 17
in2_2 = 27
in3_2 = 22
in4_2 = 23


#Stepper Motor 3
in1_3 = 10
in2_3 = 9
in3_3 = 11
in4_3 = 25

motor_pins_3 = [in1_3,in2_3,in3_3,in4_3]
motor3_step_counter = 0  

#Stepper Motor 4
in1_4 = 5
in2_4 = 6
in3_4 = 13
in4_4 = 19

motor_pins_4 = [in1_4,in2_4,in3_4,in4_4]
motor4_step_counter = 0


# Braille mapping
braille_mapping = {
    'A': [6, 4],  # Braille Letter A
    'B': [2, 4],  # Braille Letter B
    'C': [6, 5],  # Braille Letter C
    'D': [6, 7],  # Braille Letter D
    'E': [6, 1],  # Braille Letter E
    'F': [2, 5],  # Braille Letter F
    'G': [2, 7],  # Braille Letter G
    'H': [2, 1],  # Braille Letter H
    'I': [1, 5],  # Braille Letter I
    'J': [1, 7],  # Braille Letter J
    'K': [3, 4],  # Braille Letter K
    'L': [0, 4],  # Braille Letter L
    'M': [3, 5],  # Braille Letter M
    'N': [3, 7],  # Braille Letter N
    'O': [3, 1],  # Braille Letter O
    'P': [0, 5],  # Braille Letter P
    'Q': [0, 7],  # Braille Letter Q
    'R': [0, 1],  # Braille Letter R
    'S': [7, 5],  # Braille Letter S
    'T': [7, 7],  # Braille Letter T
    'U': [3, 6],  # Braille Letter U
    'V': [0, 6],  # Braille Letter V
    'W': [1, 0],  # Braille Letter W
    'X': [3, 3],  # Braille Letter X
    'Y': [3, 0],  # Braille Letter Y
    'Z': [3, 2],  # Braille Letter Z
    ',': [1, 4],  # Braille Comma
    ';': [7, 4],  # Braille Semicolon
    ':': [1, 1],  # Braille Colon
    '.': [1, 2],  # Braille Full Stop
    '/': [5, 5],  # Braille Slash
    '-': [5, 6],  # Braille Dash
}

def convert_to_braille(text):
    # List to store the resulting sublists of two letters
    braille_result = []
    
    # Convert text to uppercase to make it case-insensitive
    text = text.upper()
    
    # Temporary list to store the [x1, y1, x2, y2] of two letters
    temp_pair = []
    
    # Iterate through each character in the text
    for char in text:
        if char in braille_mapping:  # If the character is in the mapping
            # Append the braille x, y values for the character
            temp_pair.extend(braille_mapping[char])
            
            # If we have two letters (4 values), add to the result and reset temp_pair
            if len(temp_pair) == 4:
                braille_result.append(temp_pair)
                temp_pair = []
    
    # If there's an odd number of letters, add the last one with [0, 0] padding
    if len(temp_pair) == 2:
        temp_pair.extend([0, 0])  # Pad with [0, 0]
        braille_result.append(temp_pair)
    
    return braille_result





def initialize1():
    # setting up
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1, GPIO.OUT)
    GPIO.setup(in2, GPIO.OUT)
    GPIO.setup(in3, GPIO.OUT)
    GPIO.setup(in4, GPIO.OUT)

    # initializing
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
 
def initialize2():
    # setting up
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1_2, GPIO.OUT)
    GPIO.setup(in2_2, GPIO.OUT)
    GPIO.setup(in3_2, GPIO.OUT)
    GPIO.setup(in4_2, GPIO.OUT)

    # initializing
    GPIO.output(in1_2, GPIO.LOW)
    GPIO.output(in2_2, GPIO.LOW)
    GPIO.output(in3_2, GPIO.LOW)
    GPIO.output(in4_2, GPIO.LOW)
    
def initialize3():
    # setting up
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1_3, GPIO.OUT)
    GPIO.setup(in2_3, GPIO.OUT)
    GPIO.setup(in3_3, GPIO.OUT)
    GPIO.setup(in4_3, GPIO.OUT)

    # initializing
    GPIO.output(in1_3, GPIO.LOW)
    GPIO.output(in2_3, GPIO.LOW)
    GPIO.output(in3_3, GPIO.LOW)
    GPIO.output(in4_3, GPIO.LOW)
    
def initialize4():
    # setting up
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1_4, GPIO.OUT)
    GPIO.setup(in2_4, GPIO.OUT)
    GPIO.setup(in3_4, GPIO.OUT)
    GPIO.setup(in4_4, GPIO.OUT)

    # initializing
    GPIO.output(in1_4, GPIO.LOW)
    GPIO.output(in2_4, GPIO.LOW)
    GPIO.output(in3_4, GPIO.LOW)
    GPIO.output(in4_4, GPIO.LOW)

motor_pins_2 = [in1_2,in2_2,in3_2,in4_2]
motor2_step_counter = 0 ;

    
#Creating 2 Different Values List for each Motor
values_list_motor1 = [0]
values_list_motor2 = [0]
values_list_motor3 = [0]
values_list_motor4 = [0]
#Pin Numberings for Buttons


GPIO.setwarnings(False)

           

def cleanup1():
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    GPIO.output(in3, GPIO.LOW)
    GPIO.output(in4, GPIO.LOW)
    
def cleanup2():
    GPIO.output(in1_2, GPIO.LOW)
    GPIO.output(in2_2, GPIO.LOW)
    GPIO.output(in3_2, GPIO.LOW)
    GPIO.output(in4_2, GPIO.LOW)
    
def cleanup3():
    GPIO.output(in1_3, GPIO.LOW)
    GPIO.output(in2_3, GPIO.LOW)
    GPIO.output(in3_3, GPIO.LOW)
    GPIO.output(in4_3, GPIO.LOW)
    
def cleanup4():
    GPIO.output(in1_4, GPIO.LOW)
    GPIO.output(in2_4, GPIO.LOW)
    GPIO.output(in3_4, GPIO.LOW)
    GPIO.output(in4_4, GPIO.LOW)


def set_start_position(move_amount_motor1, move_amount_motor2, move_amount_motor3, move_amount_motor4, motor1_step_counter, motor2_step_counter, motor3_step_counter, motor4_step_counter):
    '''Set Start Position of Motors. Takes Args: Move Amount.'''
    
    initialize1()
    for index_motor_counter in range(int((step_count)*(move_amount_motor1))):
        for pin_1 in range(0, len(motor_pins)):  
            #Main Code to Output Value and Move Stepper Motor
            GPIO.output( motor_pins[pin_1], step_sequence[motor1_step_counter][pin_1] )
        motor1_step_counter = (motor1_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup1()
    initialize2()
    for index_motor_counter in range(int((step_count)*(move_amount_motor2))):
        for pins_motor2 in range(0, len(motor_pins_2)):
                #Main Code to Output Value and Move Stepper Motor
            GPIO.output( motor_pins_2[pins_motor2], step_sequence[motor2_step_counter][pins_motor2] )
        motor2_step_counter = (motor2_step_counter + 1) % 8
                
        time.sleep(step_sleep)
    cleanup2()
    initialize3()
    for index_motor_counter in range(int((step_count)*(move_amount_motor3))):
        for pins_motor3 in range(0, len(motor_pins_3)):
                #Main Code to Output Value and Move Stepper Motor
            GPIO.output( motor_pins_3[pins_motor3], step_sequence[motor3_step_counter][pins_motor3] )
        motor3_step_counter = (motor3_step_counter + 1) % 8
                
        time.sleep(step_sleep)
    cleanup3()
    initialize4()
    for index_motor_counter in range(int((step_count)*(move_amount_motor4))):
        for pins_motor4 in range(0, len(motor_pins_4)):
                #Main Code to Output Value and Move Stepper Motor
            GPIO.output( motor_pins_4[pins_motor4], step_sequence[motor4_step_counter][pins_motor4] )
        motor4_step_counter = (motor4_step_counter + 1) % 8
                
        time.sleep(step_sleep)
    cleanup4()

def calc_move_amount(values_list, instruction_set, location):
    '''Calculates Amount the Stepper Motor Needs to Move Based on (Values_List,
    instruction_set, and the location of which instructions the motor is using (0 or 1)'''
    
    move_to_position = 0
    
    #Depending on Which Stepper Motor, Read Either the First Data Point or Second Point
    move_to_position = instruction_set[location]
    
    #Add This to the Values_list for Future Use
    values_list.append(move_to_position)
       
    # In calc_move_amount, replace the if block with this:
    if values_list[-1] > values_list[-2]:
        return 8-values_list[-1]+values_list[-2]
    return values_list[-1]-values_list[-2]



        

def move_motors(values_list_motor1, values_list_motor2, values_list_motor3, values_list_motor4, instruction_set, motor1_step_counter, motor2_step_counter, motor3_step_counter, motor4_step_counter):
    # Calculate movement amounts
    move_amount_motor1 = calc_move_amount(values_list_motor1, instruction_set, 0)
    print(move_amount_motor1)
    move_amount_motor2 = calc_move_amount(values_list_motor2, instruction_set, 1)
    print(move_amount_motor2)
    move_amount_motor3 = calc_move_amount(values_list_motor3, instruction_set, 2)
    move_amount_motor4 = calc_move_amount(values_list_motor4, instruction_set, 3)
    print(move_amount_motor3)
    print(move_amount_motor4)
    
    # Initialize motors and move them to the new positions
    initialize1()
    for _ in range(step_count * move_amount_motor1):
        for pin in range(4):  # For each pin
            GPIO.output(motor_pins[pin], step_sequence[motor1_step_counter][pin])
        motor1_step_counter = (motor1_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup1()

    initialize2()
    for _ in range(step_count * move_amount_motor2):
        for pin in range(4):
            GPIO.output(motor_pins_2[pin], step_sequence[motor2_step_counter][pin])
        motor2_step_counter = (motor2_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup2()

    initialize3()
    for _ in range(step_count * move_amount_motor3):
        for pin in range(4):
            GPIO.output(motor_pins_3[pin], step_sequence[motor3_step_counter][pin])
        motor3_step_counter = (motor3_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup3()

    initialize4()
    for _ in range(step_count * move_amount_motor4):
        for pin in range(4):
            GPIO.output(motor_pins_4[pin], step_sequence[motor4_step_counter][pin])
        motor4_step_counter = (motor4_step_counter + 1) % 8
        time.sleep(step_sleep)
    cleanup4()
    
    
#set_start_position(0, 0.125, motor1_step_counter, motor2_step_counter)

    

START = True
while START:

    
    # Get content
    response = requests.get(api_url, headers={"Authorization": f"Bearer {n}"})
    response_data = response.json()

         
    current_content = response_data["content"]
    current_content_decoded = base64.b64decode(current_content).decode("utf-8")

    # Treat the content as a string directly
    current_content_string = current_content_decoded

    # Check if the string content is not just "0"
    if current_content_string.strip() != "0":
        # Process the content as needed
        current_content_list = convert_to_braille(current_content_string.strip())
        
        for instruction_set in current_content_list:
            print(instruction_set)
            move_motors(values_list_motor1, values_list_motor2, values_list_motor3, values_list_motor4, instruction_set, motor1_step_counter, motor2_step_counter, motor3_step_counter, motor4_step_counter)


        set_0_motor1 = 8-values_list_motor1[-1]
        set_0_motor2 = 8-values_list_motor2[-1]
        set_0_motor4 = 8-values_list_motor4[-1]
        set_0_motor3 = 8-values_list_motor3[-1]
        values_list_motor1.append(0)
        values_list_motor2.append(0)
        values_list_motor3.append(0)
        values_list_motor4.append(0)
        set_start_position(set_0_motor1, set_0_motor2, set_0_motor3, set_0_motor4, motor1_step_counter, motor2_step_counter, motor3_step_counter, motor4_step_counter)
        print(0)
        
        

        
        # Update content
        new_content = "0"

        # Encode new content
        new_content_encoded = base64.b64encode(new_content.encode("utf-8")).decode("utf-8")

        # Prepare data
        data = {
            "message": "Update instructions.txt",
            "content": new_content_encoded,
            "sha": response_data["sha"]
        }

        # Update
        update_response = requests.put(api_url, headers={"Authorization": f"Bearer {n}"}, json=data)

        if update_response.status_code == 200:
            print("Sent!")
        else:
            print(f"Error updating file. Status code: {update_response.status_code}")
                  
    time.sleep(DELAY_LISTENER)
