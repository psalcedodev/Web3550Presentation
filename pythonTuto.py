#LINK: http://pythontutor.com/live.html

# single line comment
''' multiline comments ''' 

'''
# Create your Facebook profile
string = "text" or 'text' | Text
integer = 1234567890 | Numbers
boolean = True or False
'''

firstName = "Nate"
lastName = "Del Grande"
relationship = "Married"
location = "Saint George, UT"
occupation = "Student"
age = 24
male = True
female = False

#############################################################
# str() => Convert to string
# int() => Convert to integer | number
# if / elif / else
print("My Facebook profile")
print("Name: " + firstName+ " " + lastName)
print("Age: " + str(age))
#if(male):
if(male == True):
    print("Gender: Male")
elif(male == False & female == False):
    print("Gender: Prefer not to answer")
elif(female == True):
    print("Gender: Female")
else:
    print("Not specified")

#Activity
#print("Relationship Status: " + relationship)
#print("Ocupation: " + occupation)
#############################################################