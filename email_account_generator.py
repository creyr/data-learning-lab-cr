##### 
# This script generates a business-style email address based on user input and formatting rules.
# Author: Claudia Reyes
# Purpose: Python string manipulation practice

##### This company needs to generate business email accounts for their workers


print("In order to give you your new business email account I will need the following information:")

#Variables needed
FamilyName = input("      *Family Name:").upper()
Name = input("        *Name:").upper()
Year = (input("     *You were born in (year):"))
Month = (input("      *Month(número 1-12):"))

letter_1 = FamilyName [0]
letter_2 = FamilyName [1]
letter_3 = FamilyName [2]
letter_4 = Name[0]
letter_5 = Name[1]
email = letter_1 + letter_2 + letter_3 + letter_4 + letter_5 + Year + Month + "@bussiness.account.com"

print("Hello!", Name, FamilyName)

print("Your new business account is", email)
