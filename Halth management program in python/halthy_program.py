print("\t\t\tHello guys welcome to this program.\n*****This program will make your routin..*****")

#function of time...
def GetTime():
    import datetime
    x = datetime.datetime.now()
    return x

#function to make a file
askName = input(" Enter Your name: ")
def personFile():
    """This function will make a file of the client"""
    try:
        yourFile = open(askName+".txt", "x")
        yourFile.close()
        youExercise = open(askName+"Exercise"+".txt", "x")
        youExercise.close()
        youDiet = open(askName+"Diet"+".txt", "x")
        youDiet.close()
        print("*****Your files are ready.******")
    except:
        print("The file of this name is already exist:")

# checking file is exist or not
askWho = input("Do you want to make file or not: click [y] for yes and [n] for not.")
if askWho == "n":
    print("Your file is already exist, Only you can Write or Retrive:")
else:
    personFile()

#main work of this program
print("Click 1 for wrtie.\nClick 2 for retrive.")
askDo = int(input())

if askDo == 1:
    print("Click 1 for write the Exercise.\nClick 2 for write the Diet.\nClick 3 for write the information about the client.")
    askWhatWrtie = int(input())
    if askWhatWrtie == 1:
        entExerciseWrite = input("Enter the exercise: ")
        with open(askName+"Exercise"+".txt", "a") as writeExe:
           writeExe.write(str([str(GetTime())]) + ":" + entExerciseWrite + "\n")
    elif askWhatWrtie == 2:
        entDietWrite = input("Enter the Diet: ")
        with open(askName+"Diet"+".txt", "a") as writeDiet:
            writeDiet.write(str([str(GetTime())]) + ":"  + entDietWrite + "\n")
    elif askWhatWrtie == 3:
        entInfoWrite = input("Enter the information: ")
        with open(askName+".txt", "a") as writeInfo:
            writeInfo.write(str([str(GetTime())]) + ":"  + entInfoWrite + "\n")
    
elif askDo == 2:
    print("Click 1 for Exercise retrive.\nClick 2 for Diet retrive.\nClick 3 for know the information about the client.")
    askWhatRtv = int(input())
    if askWhatRtv == 1:
        with open(askName+"Exercise"+".txt") as retriveExe:
            # writeExe.write(entExerciseWrite)
            if retriveExe is None:
                print("Your this file is empty.")
            else:
                print(retriveExe.read())
    elif askWhatRtv == 2:
        with open(askName+"Diet"+".txt") as retriveDt:
            # writeDiet.write(entDietWrite)
            if retriveDt is None:
                print("Your this file is empty.")
            else:
                print(retriveDt.read())
    elif askWhatRtv == 3:
        with open(askName+".txt") as retriveInfo:
            if retriveInfo is None:
                print("Your this file is empty.")
            else:
                print(retriveInfo.read())