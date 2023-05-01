import re
run=True
prev=0

print("Here is our magic calculator!")

def performmath():

    global run
    global prev
    if prev==0:
        c=input("Enter your question:")
    else:
        c=input(str(prev))
    if c=="quit":
         print("Goodbye human")
         run=False
    else:
        new=re.sub('[A-Za-z,":&$""#@]'," ", c)

    if run==False:
        print("Switching off")

    elif prev==0:
        prev=eval(new)
        print("Your answer:", prev)
    else:
        prev=eval(str(prev)+new)
        print("Answer:", prev)

while run:
    performmath()






