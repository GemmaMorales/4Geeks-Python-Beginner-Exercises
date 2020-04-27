import random

def get_color(color_number):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")

students = range(1,11)
#print(list(students))

list_10random = []   
for i in range(10):
    list_10random.append(random.randint(1,4))
#print(list_10random)

def get_allStudentColors():  
    for i in list_10random:
        print (get_color(i))
               
#students_and_randnum = zip(students, list_10random) 
#print(list(students_and_randnum))
   
print(get_allStudentColors())        



    #example_color = 1
    #students_array = []
    #your loop here



