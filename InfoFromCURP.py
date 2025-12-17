##### Obtaining CURP
## In Mexico there is an identification code called CURP, which is unique for each person living in the country.
## In this script, I will show how a CURP can be generated (in an idealized way).
## The CURP is an 18-character alphanumeric code.

# First, I will need some basic information from you
print("Hello! So, you want to know your CURP. I will need some basic information.")
Name = input("* Name:").upper()
FathersLastName = input("* Father´s last name:").upper()
MothersLastName = input("* Mother´s last name:").upper()
BirthDate = input("* Birth date yymmdd:")
Gender = input("* Male/Female:").upper()
State = input("* Birth state(if you are a foreigner write NE):").upper()
#CURP
#Digit 1: first letter of father´s name
dig1 = FathersLastName[0]
#Digit 2: First vowel of the father´s name
vowels = "AEIOU"
dig2 = ""
for letter in FathersLastName[1:]:
    if letter in vowels:
        dig2 = letter
        break
#Digit 3: First letter of mother´s name
dig3 = MothersLastName[0]
#Digit 4: First letter of name
dig4 = Name[0]
#Digit 5 to 10: Birth date

#Digit 11
if Gender == "FEMALE":
    dig11 = "M" #Because in Mexico female is mujer
else:
    dig11 = "H"
#Digit 12-13: State
if State == "NE":
    dig12_13 = "NE"
else:
    dig12_13 = State[:2]
#Digit 14: Intern consonant father's last name
dig14 = "X"
for letter in FathersLastName[1:]:
    if letter.isalpha() and letter not in vowels:
        dig14 = letter
        break
#Digit 15: Intern consonant Mother´s last name
dig15 = "X"
for letter in MothersLastName[1:]:
    if letter.isalpha() and letter not in vowels:
        dig15 = letter
        break
#Digit 16: Intern consonant Name
dig16 = "X"
for letter in Name[1:]:
    if letter.isalpha() and letter not in vowels:
        dig16 = letter
        break
#Digit 17 and 18: Random digits (they are oficially calculated)
import random
dig17_18 = str(random.randint(0,9))+str(random.randint(0,9))

CURP = dig1 + dig2 + dig3 + dig4 + BirthDate + dig11 + dig12_13 + dig14 + dig15 + dig16 + dig17_18

print("Your CURP is", CURP)
