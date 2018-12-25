from pathlib import Path
import os, random, time,sys

while True:
    MainDirectory = Path().absolute() #Main.py Directory
    randomFileDirectory = Path(MainDirectory).parents[0] / "Texts" #a parent directory + "texts" folder name >>> like a C:\..\..\Texts 
 
    selectRandomFile = random.choice(os.listdir(randomFileDirectory)) #Random file selection in the "Texts" folder
    text = open(file = os.path.join(randomFileDirectory, selectRandomFile),mode='r').read() #Open the random file


    exitProgram = str(input("{}\nIf you want to exit type 'q' and press Enter. Or press enter directly to continue:".format("-"*80,sep="")))
    if exitProgram == "q":
        sys.exit()

    while str(input('\nWhen you are ready, type "ok" and press Enter:')) != 'ok':
        str(input('\nWhen you are ready, type "ok" and press Enter:'))

    startTime = time.time() #Time Start
    print("-"*40,sep="")
    inputText = str(input('"%s" \n \n Type the words quickly and accurately\n>>>' % text))
    endTime = time.time() #Time Stop


    correctWordCounter = len(set(inputText.split()) & set(text.split())) # & :It means the intersection. Breaks the text into words, finds common expressions and calculates the number of common expressions

    totalTime = endTime - startTime

    print ("\n","*" * 40,"\nResults:""\nTotalTime:",round(totalTime)," Second ||","Correct number of words:", correctWordCounter,"||","\n","*" * 40,sep="")
    
