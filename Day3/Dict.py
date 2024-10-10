#Using dict in python and calling the it 

#progamming_infor={
#    "Bug":"A bug is a type of insect with piercing mouthparts that belongs to the Hemiptera group. Examples of bugs include bedbugs and stinkbugs",
#    "Function":"Here is a definition of a function. A function is a rule which maps a number to another unique number."
#     }

#print(progamming_infor["Bug"])

#To add a key in the dict file 

#progamming_infor["loop"]="A curved shape: A curved shape formed when a long, thin object bends until one part of it almost touches or crosses another part. For example, a loop of string or a loop of a written letter"
 
#print(progamming_infor )

#Creating an empty dict

#progamming_infor = {}
#print(progamming_infor)

#Editing an item in a dict

#progamming_infor["Bug"]="This is just just a bad error code "
#print(progamming_infor)

#using loop in a dict

#for key in progamming_infor:
#    print(key)
#    print(progamming_infor[key])


#Using Nesting in dict

#travel = {
#    "city":{"a":["kumba","buea","limbe"],
#            "Tl":12
#            },
#   
#   "country":{"b":["cameroon","france", "panana"],
#              "ku":5
               
#               }
#     }

#print(travel["city"]["a"][2

from Loop import bid

def final_bidder(bidding_d):
    winner = ""
    highest_bid=0
    for bidder in bidding_d:
        bid_A=bidding_d[bidder]
        if bid_A > highest_bid:
            highest_bid = bid_A
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")
    print(bid)
bibs ={}
continue_bidding = True
while continue_bidding:
    name=input("What is your name:").capitalize()
    price=int(input("Enter your biding price:$ "))
    bibs[name]=price
    Question = input("Are there any other bidders? type 'yes' or 'no'. \n").lower()
    if Question == "no":
        continue_bidding = False
        final_bidder(bibs)
    elif Question == "yes":
        print("\n"*100)
#final        
        

    
    


