#wkn=input("enter a day: ")
#match(wkn.lower()):
#    case"monday":
#        print("{} i'm an work".format(wkn))
#   case"tuesday":
#       print("{} i'm an work".format(wkn))
#    case"wednesday":
#        print("{} i'm an work".format(wkn))
#    case"thursday":
#        print("{} i'm an work".format(wkn))
#    case"friday":
#        print("{} i'm an work".format(wkn))
#    case"saturdat":
#        print("{} party day".format(wkn))  
#    case"sunday":
#        print("{} go to church".format(wkn))
#This is a randon pick

n=int(input("What is the number of the day: "))
if n<=0:
    print("{} is invalid".format(n))
else:
    print("#"*30)
    i=2
    while(i<=30):
          print("\t All even numbersis {}".format(i))
          i=i+2
    else:
        print("#"*50) 
 
print('&'*100)

n=int(input("What is the number of the day: "))
if n<=0:
    print("{} is invalid".format(n))
else:
    print("#"*30)
    i=1
    while(i<=30):
          print("\t All odd numbersis {}".format(i))
          i=i+2
    else:
        print("#"*50)
        
print('@'*100)

#USING THE BREAK STATEMENT
note="MENTOR"
val = "MENTOR"
while  val==note:
    if val =="MENTOR":
        break
    print("\t{} ".format(val))