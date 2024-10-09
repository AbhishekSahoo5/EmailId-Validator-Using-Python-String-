# Email Validation using string function

email=input("Enter email:   ")   #g@g.in

k,j,d=0,0,0
if len(email)>=6: #1

    if(email[0].isalpha()): #2
        
        if(("@" in email) and (email.count("@")==1)): #3
            
            if((email[-4]==".") ^ (email[-3]==".")): #4
                
                for i in email:
                    
                    if (i==i.isspace()): #5
                        k+=1
                    elif (i.isalpha()): #5
                        if(i.isupper()):
                            j+=1
                    elif (i.isdigit()): #5
                        continue
                    elif (i=="_" or i=="." or i=="@"): #5
                        continue
                    else:
                        d+=1

                if(k!=0 or j!=0 or d!=0):
                    print("Wrong EmailId 5")
                else:
                    print("Right EmailId")
            else:
                print("Wrong EmailId 4")
        else:
            print("Wrong EmailId 3")
    else:
        print("Wrong EmailId 2")
else:
    print("Wrong EmailId 1")
