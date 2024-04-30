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
    
    for s in csFiles:
         className = os.path.basename(s)
         print(f"Liz -> {className}")
    print(f"Liz: you have {len(csFiles)} C# scripts") 


InitLiz()