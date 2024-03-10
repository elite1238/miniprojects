import pickle
import datetime

def year():
    year=input("Enter year:")
    count=0
    while count==0:
     while len(year)!=4:
       year=input("Enter a valid year:")
     if year[0]=="0":
      year=input("enter valid year:")
     else:
      for i in year:
         if i not in["1","2","3","4","5","6","7","8","9","0"]:
            year=input("Enter a valid year:")
            break
      else:
       count=1
    else:
     return year
def month():
    month=input("Enter month(by number,FOR EXAMPLE:for january input 1): ")
    while True:
       if month in ["1","2","3","4","5","6","7","8","9","10","11","12"]:
           break
       else:
            month=input("Enter a valid month(by number,FOR EXAMPLE:for january input 1): ")
    return month
def date():
    date=input("Enter date:")
    a=0
    while True:
        if date.isdigit():
            if int(date)>0 and int(date)<32:
                break
            else:
                a=1
        else:
            a=1
        if a==1:
            date=input("Enter valid date:")
            a=0
    return date
def amount(zx):
    a=zx
    b=0
    while True:
      for i in a:
         if i in ["1","2","3","4","5","6","7","8","9","0","."]:
            pass
         else:
             b+=1
      if b!=0:
          a=input("Enter a proper integer or floating point number:")
          b=0
      else:
          break
    return a
def deposit():
    global totalbalance,totaldeposit,depositinfo_lst
    depositmoney=input("Enter the amount which you wish to add to your Main Balance :")
    for j in depositmoney:
        if j not in ["1","2","3","4","5","6","7","8","9","0","."]:
            depositmoney=input("enter valid deposit money:")
            break
    depositmoney=float(depositmoney)
    totalbalance=totalbalance+depositmoney
    pickle.dump(totalbalance, open("totalbalance","wb"))
    totaldeposit=totaldeposit+depositmoney
    pickle.dump(totaldeposit, open("totaldeposit","wb"))
    depositinfo_dic={"date":e.day,"Month":e.month,"year":e.year,"time":timenow,"amount deposit":depositmoney}
    depositinfo_lst.append(depositinfo_dic)
    pickle.dump(depositinfo_lst, open("depositinfolist","wb"))
    print(depositmoney,"has been deposited into your main balance.")
    print("Now your main balance is:",totalbalance)
def balance():
    print("Main balance is:",totalbalance)
def enteringexpense():
    global totalexpense,expenseinfo_lst,totalbalance
    expensemoney=input("Enter the amount which you spent on your recent expense: ")
    for j in expensemoney:
        if j not in ["1","2","3","4","5","6","7","8","9","0","."]:
            expensemoney=input("enter valid deposit money:")
            break
    expensemoney=float(expensemoney)
    expensename=input("Enter the name for the above expense to store it: ")
    totalexpense=totalexpense+expensemoney
    pickle.dump(totalexpense, open("totalexpense","wb"))
    expenseinfo_dic={"date":e.day,"Month":e.month,"year":e.year,"time":timenow,"expense":expensename,"expense amount":expensemoney}
    expenseinfo_lst.append(expenseinfo_dic)
    pickle.dump(expenseinfo_lst, open("expenseinfolist","wb"))
    totalbalance=totalbalance-expensemoney
    pickle.dump(totalbalance, open("totalbalance","wb"))
    print("your expenses have been saved")
    print("Now your main balance is:",totalbalance)
def deposithistory():
    if depositinfo_lst==[]:
        print("NO DEPOSITS")
    else:
        print("DEPOSITS ARE")
        for i in depositinfo_lst:
            print(i)
        print("Total amount deposited is:",totaldeposit)
def expensehistory():
    if expenseinfo_lst==[]:
        print("NO EXPENSES RECORDED")
    else:
        print("EXPENSES ARE")
        for i in expenseinfo_lst:
            print(i)
        print("Total expense amount is:",totalexpense)
#create for multiple accounts and username and password
def searchexpense():
            print("** INSTRUCTIONS** \
                \n This feature will show u the expense history based on the values u enter below")
            display=input("Enter '1' if u want to search by year             \
                             \nEnter '2' if u want to search by month         \
                             \nEnter '3' if u want to search by date           \
                             \nEnter '4' if u want to search by expense amount  \
                             \nEnter '5' if u want to search by expense object   \
                             \nEnter '6' if u want to search by only month        \
                             \nEnter '7' if u want to search by only date          \
                             \n***ENTERHERE:" )
            ar="no"
            while ar=="no":

             if display in["1","2","3","4","5","6","7"]:
                ar="yes"
                pass
             else:
                print("**ENTER A PROPER NUMBER**")
                display=input("Enter '1' if u want to search by year         \
                             \nEnter '2' if u want to search by month         \
                             \nEnter '3' if u want to search by date           \
                             \nEnter '4' if u want to search by expense amount  \
                             \nEnter '5' if u want to search by expense object   \
                             \nEnter '6' if u want to search by only month        \
                             \nEnter '7' if u want to search by only date          \
                             \n***ENTERHERE:" )
            if display=="1":
                y=0
                searchyear=int(year())
                for x in expenseinfo_lst:
                    if x["year"]==searchyear:
                        print(x)
                        y+=1
                if y==0:
                    print("**NO EXPENSE FOR THE ENTERED YEAR**")
            elif display=="2":
                y=0
                searchyear=int(year())
                searchmonth=int(month())
                for x in expenseinfo_lst:
                    if x["year"]==searchyear:
                        if x["Month"]==searchmonth:
                            print(x)
                            y+=1
                if y==0:
                    print("**NO EXPENSE FOR THE ENTERED YEAR AND MONTH**")
            elif display=="3":
                y=0
                searchyear=int(year())
                searchmonth=int(month())
                searchdate=int(date())
                for x in expenseinfo_lst:
                    if x["year"]==searchyear:
                        if x["Month"]==searchmonth:
                            if x["date"]==searchdate:
                                print(x)
                                y+=1
                if y==0:
                    print("**NO EXPENSES FOR THE ENTERES YEAR,MONTH AND DATE**")
            elif display=="4":
                a=0
                zx=input("Enter search amount")
                searchmoney=float(amount(zx))
                for x in expenseinfo_lst:
                    if x["expense amount"]==searchmoney:
                        print(x)
                        a+=1
                if a==0:
                    print("**NO EXPENSE RECORDED FOR THE ENTERED AMOUNT**")
            elif display=="5":
                searchobj=input("Enter the name of your expense that you wish to search for: ")
                p=0
                for x in expenseinfo_lst:
                    if x["expense"]==searchobj:
                        print(x)
                        p+=1
                if p==0:
                    print("NO SUCH EXPENSE EXISITS")
            elif display=="6":
                searchmonth=int(month())
                l=0
                for x in expenseinfo_lst:
                    if x["Month"]==searchmonth:
                        print(x)
                        l+=1
                if l==0:
                    print("NO EXPENSE FOR THE GIVEN MONTH")
            elif display=="7":
                searchdate=int(date())
                l=0
                for x in expenseinfo_lst:
                    if x["date"]==searchdate:
                        print(x)
                        l+=1
                if l==0:
                    print("NO EXPENSE FOR THE GIVEN DATE")
def searchdeposit():
            print("** INSTRUCTIONS** \
                \n This feature will show u the deposit history based on the values u enter below")
            display=input("Enter '1' if u want to search by year             \
                             \nEnter '2' if u want to search by month         \
                             \nEnter '3' if u want to search by date           \
                             \nEnter '4' if u want to search by deposit amount  \
                             \nEnter '5' if u want to search by only month       \
                             \nEnter '6' if u want to search by only date         \
                             \nYour Choice: " )
            ar="no"
            while ar=="no":

             if display in["1","2","3","4","5","6",]:
                ar="yes"
                pass
             else:
                print("**ENTER A PROPER NUMBER**")
                display=input("Enter '1' if u want to search by year         \
                             \nEnter '2' if u want to search by month         \
                             \nEnter '3' if u want to search by date           \
                             \nEnter '4' if u want to search by deposit amount  \
                             \nEnter '5' if u want to search by only month        \
                             \nEnter '6' if u want to search by only date          \
                             \n***ENTERHERE:" )
            if display=="1":
                y=0
                searchyear=int(year())
                for x in depositinfo_lst:
                    if x["year"]==searchyear:
                        print(x)
                        y+=1
                if y==0:
                    print("**NO DEPOSIT FOR THE ENTERED YEAR**")
            elif display=="2":
                y=0
                searchyear=int(year())
                searchmonth=int(month())
                for x in depositinfo_lst:
                    if x["year"]==searchyear:
                        if x["Month"]==searchmonth:
                            print(x)
                            y+=1
                if y==0:
                    print("**NO DEPOSIT FOR THE ENTERED YEAR AND MONTH**")
            elif display=="3":
                y=0
                searchyear=int(year())
                searchmonth=int(month())
                searchdate=int(date())
                for x in depositinfo_lst:
                    if x["year"]==searchyear:
                        if x["Month"]==searchmonth:
                            if x["date"]==searchdate:
                                print(x)
                                y+=1
                if y==0:
                    print("**NO EXPENSES FOR THE ENTERES YEAR,MONTH AND DATE**")
            elif display=="4":
                a=0
                zx=input("Enter search amount")
                searchmoney=float(amount(zx))
                for x in depositinfo_lst:
                    if x["amount deposit"]==searchmoney:
                        print(x)
                        a+=1
                if a==0:
                    print("NO SUCH DEPOSIT RECORDED")
            elif display=="5":
                searchmonth=int(month())
                l=0
                for x in depositinfo_lst:
                    if x["Month"]==searchmonth:
                        print(x)
                        l+=1
                if l==0:
                    print("NO DEPOSIT FOR THE GIVEN MONTH")
            elif display=="6":
                searchdate=int(date())
                l=0
                for x in depositinfo_lst:
                    if x["date"]==searchdate:
                        print(x)
                        l+=1
                if l==0:
                    print("NO DEPOSIT FOR THE GIVEN DATE")
                





e = datetime.datetime.now()
timenow=str(e.hour)+":"+str(e.minute)
accountinfo=input("Are you an exisiting user?(YES/NO) \n(For Account Creation Enter 'no'):")
if accountinfo in ["NO","No","nO","no"]:
        totaldeposit=totalbalance=totalexpense=0
        depositinfo_lst=expenseinfo_lst=[]
        pickle.dump(totaldeposit, open("totaldeposit","wb"))
        pickle.dump(depositinfo_lst, open("depositinfolist","wb"))
        pickle.dump(totalbalance, open("totalbalance","wb"))
        pickle.dump(totalexpense, open("totalexpense","wb"))
        pickle.dump(expenseinfo_lst, open("expenseinfolist","wb"))



        totalbalance=input("Enter The Amount which you want to store to your account: ")
        for i in totalbalance:
                if i not in ["1","2","3","4","5","6","7","8","9","0","."]:
                    totalbalance=input("Enter valid account balance! :")
                    break
        totalbalance=float(totalbalance)
        pickle.dump(totalbalance, open("totalbalance","wb"))
while True:
    print("1)Deposit money to main Balance                2)Show total balance")
    print("3)Enter expenses                               4)Show deposit history")
    print("5)Show All Expenses                            6)Search an expense using fliters")
    print("7)Search deposits using fliters                8)Exit")
    check1=int(input("Enter input as (1,2,3,4,5,6,7): "))
    totaldeposit=pickle.load(open("totaldeposit","rb"))
    totalbalance=pickle.load(open("totalbalance","rb"))
    totalexpense=pickle.load(open("totalexpense","rb"))
    depositinfo_lst=pickle.load(open("depositinfolist","rb"))
    expenseinfo_lst=pickle.load(open("expenseinfolist","rb"))
    if   check1==1:
        deposit()
    elif check1==2:
        balance()
    elif check1==3:
        enteringexpense()
    elif check1==4:
        deposithistory()
    elif check1==5:
        expensehistory()
    elif check1==6:
        searchexpense()
    elif check1==7:
        searchdeposit()
    elif check1 ==8:
        print("Bye")
        break
