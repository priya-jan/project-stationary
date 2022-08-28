import datetime
import pandas as pd
import matplotlib.pyplot as plt
now=datetime.datetime.now()
dtm=str(now)
print('- - - - - - - - - - - - - - - - -',dtm,'- - - - - - - - - - - - - - - - -')
print('# # # # # # # # # # # # # # # #' ,"WELCOME TO OUR STATIONARY SHOP",'# # # # # # # # # # # # # # # #')
name = input('Enter your name')
mobileno=int(input('Enter number'))
address=input('Enter address')
print('#A section is for books')
print('#B section is for bags of range 400 to 2000')
print('#C section for stationary material like pen,pencil,eraser etc')
print('#D section is for lunches and botltles')
choice=input('Enter what you want')
if choice=='A':
    print('Welcome to the section of book where you will get all type of book')
    txt="/home/priyanshi/Downloads/books.txt"
    book=pd.read_csv(txt)
    print("Show csv file")
    print(book)
    choice=input("Enter your choice which type of books you want")
    if choice=='A':
        print('\t',"We welcome your benign presence in noe books where you will get interesting novel.")
        novel=pd.read_csv("/home/priyanshi/Downloads/novels.txt")
        print("This book will give you knowledge")
        print(novel)
        choice=input("Enter your choice which type of novel do you want.")
        if choice=='A':
            print("Welcome to Section of Science Friction.")
            qty=int(input('enter your quantity'))
            price=250
            t_amount=qty*price
            print("The price of those thing which you have buy",t_amount)
        elif choice=='B':
            print("Welcome to Section of historical books.")
            qty=int(input('enter your quantity'))
            price=300
            t_amount=qty*price
            print("The price of those thing which you have buy",t_amount)
        else:
            
            print("We have much novel only")
    elif choice=='B':
        print("You are in secttion of comic book")
        df=['Tom and jerry','Nya rastaa']
        df1=pd.Series(df,index=['A','B'])
        print(df1)
        choice=input("Enter your choice")
        if choice=='A':
            print("Welcome to Section of Tom and jerry.")
            qty=int(input('enter your quantity'))
            price=300
            t_amount=qty*price
            print("The price of those thing which you have buy",t_amount)
        elif choice=='B':
            print("Welcome to Section of Nya rastaa.")
            qty=int(input('enter your quantity'))
            price=350
            t_amount=qty*price
            print("The price of those thing which you have buy",t_amount)
    elif choice=='C':
        print("Welcome to Section of inspirational book")
        df=['Mahatma Gandhi-A great leader','APJ Abdul Kalam']
        df1=pd.Series(df,index=['A','B'])
        print(df1)
        choice=input("Enter ypur hoice which type ")
        if choice=='A':
            print("Welcome to Section of Mahatma Gandhi.")
            qty=int(input('enter your quantity'))
            price=250
            t_amount=qty*price
            print("The price of those books which you have buy",t_amount)
        elif choice=='B':
            print("Welcome to Section of APJ Abdul Kalam")
            qty=int(input('enter your quantity'))
            price=300
            t_amount=qty*price
    elif choice=='D':
        print('You are in the section of encyclopedia')
        print('We have two type encyclopedia')
        df=['general','subjective']
        df1=pd.Series(df,index=['A','B'])
        print(df1)
        choice=input('Enter which type of encyclpedia you want')
        if choice=='A':
            print('You want gernal encyclopedia')
            print('The price which is given is the full parts of encyclopedia')
            qty=int(input('Enter quantity'))
            price=5780
            tamount=qty*price
            print(tamount)
            print('you will get discount')
            discount=tamount-tamount*10/100
            print(discount)
        elif choice=='B':
            print('You want subject encyclopedia')
            print('The price which is given is the full parts of encyclopedia')
            qty=int(input('Enter quantity'))
            price=6734
            tamount=qty*price
            print(tamount)
            print('you will get discount')
            discount=tamount-tamount*10/100
            print(discount)
            print("The price of those books which you have buy",discount)
    print("Graph")
    data=["Good","Very Good","Nice","Very Nice","Excellent"]
    a=eval(input("what is the rate of liking"))
    plt.bar(data,a)
    plt.xlabel("data")
    plt.ylabel("a")
    plt.show()      
elif choice=='B':
    bag1={'Bag':'Tourist bags','Price':'1500 to 2500'}
    bag2={'Bag':'School bags','Price':'500 to 1500'}
    bag3={'Bag':'Carry bags','Price':'100 to 500'}
    bags=[bag1,bag2,bag3]
    bag=pd.DataFrame(bags,index=['A','B','C'])
    print("These are different type of bags avaible")
    print(bag)
    choice=input("Enter your choice which typeof bags do you want")
    if choice=='A':
        print("You are in section of American tourister")
        qty=int(input("Enter te quantity of bags"))
        price=2500
        amount=qty*price
        print("Amount of things you bought are of R.s:")
        print(amount)
    elif choice=='B':
        print("You are in the section of kristy bags company")
        qty=int(input("Enter the quantity of bags"))
        price=2100
        amount=qty*price
    elif choice=='C':
        print("You are in the secton of baganic company bags")
        qty=int(input("Enter the quantiyt of bags"))
        price=2478
        amount=qty*price
        print("The price of bags of alll type of bags",amount)
    else:
        print("You dont want tourist bags")
    print("Analysis")
    print("How many people like our produdts")
    data=["Good","Very Good","Nice","Very Nice","Excellent"]
    a=eval(input("what is the rate of liking"))
    plt.plot(data,a,'b',linestyle='dashed',linewidth=4)
    plt.xlabel("data")
    plt.ylabel("a")
    plt.show()    
if choice=='C':
    print("Welcome to the section of pen,pencil,erasure,etc")
    stationary=pd.read_csv("C:\\Users\\91945\\Documents\\stationary.txt")
    print("CSV file of stationary present in the shop are")
    print(stationary)
    choice=input("Enter your choice in stationary shop")
    if choice=='A':
        print("Welcome to the section of pencil,eraser,sharpner,scale")
        product1={'stationary':['pencil','eraser','sharpner','scale'],
                'price':[5,5,5,5]}
        choice2=pd.DataFrame(product1,index=['A','B','C','D'])
        print(choice2)
        choice=input("Enter your choice which type of stationary you want")
        if choice=='A':
            print("Welcome in the section of pencil")
            qty=int(input("Enter te quantity of penciles you want"))
            price=5
            amount=qty*price
            print(amount)
        if choice=='B':
            print("Welcome in the section of Eraser")
            qty=int(input("Enter te quantity of ereser you want"))
            price=5
            amount=qty*price
            print(amount)
        if choice=='C':
            print("Welcome in the section of sharpner")
            qty=int(input("Enter te quantity of Sharpner you want"))
            price=5
            amount=qty*price
            print(amount)
        if choice=='D':
            print("Welcome in the section of scale")
            qty=int(input("Enter te quantity of Scale you want"))
            price=5
            amount=qty*price
            print(amount)
    if choice=='B':
        print("Welcome to the section of pen pouch")
        qty=int(input("Enter te quantity of pen pouch you want"))
        price=5
        amount=qty*price
        print(amount)
    if choice=='C':
        print("Welcome to the section of pen pouch")
        qty=int(input("Enter te quantity of pen pouch you want"))
        price=25
        amount=qty*price
        print(amount)
    if choice=='D':
        print("Welcome to the section of notebook")
        qty=int(input("Enter te quantity of notebook you want"))
        price=50
        amount=qty*price
        print(amount)
    if choice=='E':
        print("Welcome to the section of project page")
        qty=int(input("Enter te quantity of project packet you want"))
        price=20
        amount=qty*price
        print(amount)
    print("Analysis")
    print("How many people like our produdts")
    data=["Good","Very Good","Nice","Very Nice","Excellent"]
    a=eval(input("what is the rate of liking"))
    plt.plot(data,a,'b',linestyle='dashdot',linewidth=6)
    plt.xlabel("data")
    plt.ylabel("a")
    plt.show()    
elif choice=='D':
    print("Welcome to the section of lunches and bottles of range Rs. 100 to 800")
    product=pd.read_csv("C:\\Users\\91945\\Documents\\choice D.txt")
    print("Show csv file of bottles and lunches")
    print(product)
    choice=input("Enter youe choice of bootles and lunches")
    if choice=='A':
        print("Welcome to the section of lunches")
        lunch1={'lunches':['Plastic lunches','Steal lunches','Vaya'],
                'price':[200,300,600]}
        lunch2=pd.DataFrame(lunch1,index=['A','B','C'])
        print(lunch2)
        choice=input("Enter your choice which type of lunch yu want")
        if choice=='A':
            print("you are in the section of plastic lunches")
            qty=int(input("Enter te quantity of lunches you want"))
            price=200
            amount=qty*price
            print(amount)
        elif choice=='B':
            print("You are in the section of steal lunches")
            qty=int(input("Enter the quantity of lunches of steal that you want"))
            price=300
            amount=qty*price
            print("The price of lunch that you have buy",amount)
        elif choice=='C':
            print("You are in the secton of vaya company of lunch")
            qty=int(input("Enter the quantity of lunch you want"))
            price=600
            amount=qty*price
            print("The price of lunches of all type of lunche you buy are of",amount)
        else:
            print("Sorry we have only three type of lunches mentioned above")
    elif choice=='B':
       print("Welcome to the section of bottles")
       bottle1={'bottles':['plastic bottle','Steal bottles','Milton'],
                'price':[150,250,450]}
       bottle2=pd.DataFrame(bottle1,index=['A','B','C'])
       print(bottle2)
       choice=input("Enter your choice which type of bottles you want")
       if choice=='A':
           print("you are in the section of plastic bottles")
           qty=int(input("Enter te quantity of bottles you want"))
           price=150
           amount=qty*price
           print(amount)
       elif choice=='B':
           print("You are in the section of steal bottles")
           qty=int(input("Enter the quantity of bottles of steal that you want"))
           price=250
           amount=qty*price
           print("The price of bottles that you have buy",amount)
       elif choice=='C':
           print("You are in the section of milton bottles")
           qty=int(input("Enter the quantity of bottles you want"))
           price=450
           amount=qty*price
           print("The price of lunches of all type of bottles you wamt",amount)
       else:
           print("Sorry we have only three type of bottles mentioned above")
    print("Analysis")
    print("How many people like our produdts")
    data=["Good","Very Good","Nice","Very Nice","Excellent"]
    a=eval(input("what is the rate of liking"))
    plt.barh(data,a,color=['red','yellow','c','black','blue'])
    plt.xlabel("data")
    plt.ylabel("a")
    plt.show()

	
