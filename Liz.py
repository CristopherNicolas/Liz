# MIT License, created by Cristopher Faundez.
import os
def InitLiz():
    currentDir= os.getcwd()
    print("Intilizing Liz in directoory : "+ currentDir)
    csFiles = []
    for root ,dirs,files, in os.walk(currentDir):
        for file in files:
            if file.endswith(".cs"):
                csFiles.append(os.path.join(root,file))
    totalLines = 0
    for s in csFiles:
         f = open(s)
         lineCount = len( f.readlines())
         totalLines += lineCount
         className = os.path.basename(s)
         print(f"Liz -> {className} with {lineCount} lines of code!")
    print(f"Liz: you have {len(csFiles)} C# scripts with a total of {totalLines} lines of code") 


InitLiz()