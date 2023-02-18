
def IdDetect():
 sum = 0
 codeid = input("Please enter your ID code: ")

 if len(str(codeid)) == 10:
     sum = sum + int(str(codeid) [0]) * 10
     sum = sum + int(str(codeid) [1]) * 9
     sum = sum + int(str(codeid) [2]) * 8
     sum = sum + int(str(codeid) [3]) * 7
     sum = sum + int(str(codeid) [4]) * 6
     sum = sum + int(str(codeid) [5]) * 5
     sum = sum + int(str(codeid) [6]) * 4
     sum = sum + int(str(codeid) [7]) * 3
     sum = sum + int(str(codeid) [8]) * 2
     remainder = sum % 11
     if remainder >= 2 and (11 - remainder == int(str(codeid) [9])):
         print ("valid ID \n \n")
     elif remainder < 2 and (remainder == int(str(codeid) [9])):
         print ("valid ID \n \n")
     else :
         print ("Invalid ID \n \n")
 else:
  print ("Invalid ID \n \n")


def IdGenerator():
    import random

    Sum = 0
    FourToNine = str(random.randint(100000,999999))
    AreaList = {"1" : "442", "2": "044", "3": "345", "4" : "015"}

    print("Please choose an area from the list below: \n 1) Yazd \n 2) Shemiran \n 3) Gheshm\n 4) TehranGharb \n")

    AreaNumber = input("Please enter the list-number of the area: ")

    if AreaNumber in AreaList :
        FirstThree = (AreaList[AreaNumber])
        Sum = int(str(FirstThree[0])) * 10
        Sum += int(str(FirstThree[1])) * 9
        Sum += int(str(FirstThree[2])) * 8
        Sum += int(str(FourToNine[0])) * 7
        Sum += int(str(FourToNine[1])) * 6
        Sum += int(str(FourToNine[2])) * 5
        Sum += int(str(FourToNine[3])) * 4
        Sum += int(str(FourToNine[4])) * 3
        Sum += int(str(FourToNine[5])) * 2
        remainder = Sum % 11
        if remainder >= 2 :
            ControlNumber = 11 - remainder
            Code = (FirstThree + FourToNine + str(ControlNumber))
            print (f"Your generated National ID Code is {Code} \n \n")
        elif remainder < 2 :
            ControlNumber = remainder
            Code = (FirstThree + FourToNine + str(ControlNumber))
            print (f"Your generated National ID Code is {Code} \n \n")

    else:
        print ("Chosen number was not found in list! \n \n")

print ("1) ID Detector \n2) ID Generator")
answer = input("Which service would you like to use? ")
if answer == "1" or answer.lower().replace(" ", "") == "iddetector":
    IdDetect()
elif answer == "2" or answer.lower().replace(" ", "") == "idgenerator":
    IdGenerator()
else :
    print ("Invalid Input")
