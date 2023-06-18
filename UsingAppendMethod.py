#Using Append method to create list of Countries with letter O

Countries=["Zimbabwe","Hollard","Mozambique","Canada","Portugal"]
CLetterO=[]
myindex=0

for x in Countries:
    if "o" in x:
        CLetterO.insert(myindex,x)
        
print(CLetterO)