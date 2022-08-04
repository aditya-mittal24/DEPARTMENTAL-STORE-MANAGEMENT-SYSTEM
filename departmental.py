import pickle
import sys
from tabulate import tabulate
print('THIS IS A DBMS FOR DEPARTMENTAL STORE')
print('Please Enter the database to be accessed')

column_headers=['Product no','Product name','Company','Cost','Discount','Quantity']
name=input('Enter File Name-')

fname=name+'.dat'
def addrecord():
        ch="y"
        print(column_headers)
        while ch=="y":
                f=open(fname,"rb+")
                stu=pickle.load(f)
                pno=int(input("Enter product Number-"))
                pname=input("Enter product Name-")
                comp=input("Enter product Company-")
                cost=int(input("Enter product Cost-"))
                disc=int(input("Enter discount Percentage%-"))
                qty=int(input("Enter product Quantity-"))
                ls=[pno,pname,comp,cost,disc,qty]
                stu.append(ls)
                f.seek(0)
                pickle.dump(stu,f)
                f.close()
                print("Record Added!")
                ch=input("Enter y to add record-")
def show_file():
        f=open(fname,'rb')
        g=pickle.load(f)
        s1=[]
        print('Table in file:')
        for i in g:
                s1.append(i)
        print(tabulate(s1,headers="firstrow",tablefmt="pretty"))
        f.close()
def searchbynumber():
        xi=int(input("Enter Product Number-"))
        f=open(fname,"rb+")
        stu=pickle.load(f)
        for i in stu:
                if i[0]==xi:
                        print("Record Found!")
                        print(i)
                        break
        else:
                print("No records found for this product number!")
        f.close()
def searchbyname():
        xi=input("Enter Product Name-")
        f=open(fname,"rb+")
        stu=pickle.load(f)
        for i in stu:
                if i[1]==xi:
                        print("Record Found!")
                        print(i)
                        break
        else:
                print("No records found for this product name!")
        f.close()
def searchbycompany():
        xi=input("Enter Product Company-")
        f=open(fname,"rb+")
        stu=pickle.load(f)
        for i in stu:
                if i[2]==xi:
                        print("Record Found!")
                        print(i)
                        break
        else:
        	print("No records found for this company!")
        f.close()
def searchrecord():
      ch="y"
      while ch=="y":
            print("1- To search by Product No.")
            print("2- To search by Product Name")
            print("3- To search by Company.")
            c=input("Enter choice 1/2/3-")
            if c=="1":
                  searchbynumber()
            elif c=="2":
                  searchbyname()
            elif c=="3":
                  searchbycompany()
            else:
                  print("Wrong Input.")
            ch=input("Enter y to search again-")
        	
        	
def billing():
        ch="y"
        sum1=0
        sumcp=0
        bill=[["Product: ","Quantity:","Price","Discount","Net Amount","Final Cost"]]
        f=open(fname,'rb+')
        stu=pickle.load(f)
        mn=[]
        print("Available Today:")
        for i in stu:
                s=[i[1],"Rs."+str(i[3]),str(i[4])+"%"]
                mn.append(s)
        print(tabulate(mn,headers="firstrow",tablefmt="pretty"))
        print()
        sm=0
        ds=0
        while ch=="y":
                buyname=input("Enter Product Name -")
                buyquantity=int(input("Enter Quantity You Need-"))
                sm=sm+buyquantity
                for i in stu:
                        if i[1]==buyname:
                                cost=i[3]
                                b=i[5]
                                discount=i[4]
                                ds=ds+discount
                                bq= b-buyquantity
                                while bq<0:
                                        print("Max quantity available-",i[5])
                                        buyquantity=int(input("Enter quantity again-"))
                                        bq= b-buyquantity
                                i[5]=bq
                                costprice=cost*buyquantity
                                finalcost=(cost-(cost)*(discount/100))*buyquantity
                                plist=[buyname,str(buyquantity)+"pcs","Rs."+str(cost),str(discount)+"%","Rs."+str(costprice),"Rs."+str(round(finalcost))]
                                bill.append(plist)
                                sum1=sum1+finalcost
                                sumcp=sumcp+costprice
                                ch=input ("Enter y to continue shopping-")
                                break
                else:
                        print("------Item not available-----")
                        sm=sm-buyquantity
                        ch=input ("Enter y to continue shopping-")
        if sm==0:
                sys.exit()
        totalsum=round(sum1)
        b2=["-------","--------","-------","-------","--------","---------"]
        bl=["TOTAL",str(sm)+"pcs","","","Rs."+str(sumcp),"Rs."+str(totalsum)]
        bill.append(b2)
        bill.append(bl)
        print()
        print("DBMS DEPARTMENTAL STORE")
        print("For enquiry Contact:")
        print("9811XXXXXX")
        print("dbmsshopping@xyzmail.com")
        print()
        print("                 -----YOUR SHOPPING BILL-----   ")
        print(tabulate(bill,headers="firstrow",tablefmt="pretty"))
        
        saving=((sumcp-totalsum)/sumcp)*100
        print()
        print("Net Total-   Rs.",round(sumcp))
        print()
        print("Total Bill-   Rs.",totalsum)
        print()
        print("Congratulations, you saved- "+str(round(saving))+"%")
        print()
        print("--------------------------------------------------------")
        print("Thanks for shopping with us!")
        print("  ")
        print("  ")
        f.seek(0)
        pickle.dump(stu,f)
        f.close()
def removerecord():
      ch="y"
      f=open(fname,"rb+")
      stu=pickle.load(f)
      while ch=="y":
            x=int(input("Enter product no. to be Deleted-"))
            for i in stu:
                  if i[0]==x:
                        print(i)
                        stu.remove(i)
                        print("Record Deleted!")
                        break
            else:
                  print("Record not found.")
            ch=input("Enter y to delete another record-")
      f.seek(0)
      pickle.dump(stu,f)
      f.close()
def modifyrecord():
      ch="y"
      f=open(fname,"rb+")
      stu=pickle.load(f)
      while ch=="y":
            x2=int(input("Enter product no. to Update-"))
            for i in stu:
                  h=i[0]
                  if h==x2:
                        print("Record Found!")
                        i[1]=input("Enter product Name-")
                        i[2]=input("Enter Company-")
                        i[3]=int(input("Enter Cost-"))
                        i[4]=int(input("Enter Discount-"))
                        i[5]=int(input("Enter Product Quantity-"))
                        print("Record Updated!")
                        break
            else:
                  print("Record not found!")
            ch=input("Enter y to update another record-")
      f.seek(0)
      pickle.dump(stu,f)
      f.close()
choice="y"
while choice=="y":
      print("   -------MENU--------   ")
      print()
      print("(1)To add record ")
      print("(2)To show table in file")
      print("(3)To delete record")
      print("(4)To update field")
      print("(5)To search record")
      print("(6)Billing")
      print()
      print("(Entering anything else will exit menu)")
      print('-------------------------------------------------------')
      choice=int(input('Enter Choice-'))
      if choice==1:
            addrecord()
      elif choice==2:
            show_file()
      elif choice==3:
            removerecord()
      elif choice==4:
            modifyrecord()
      elif choice==5:
            searchrecord()
      elif choice==6:
            billing()
      else :
            print('WRONG INPUT!')
      choice="y"
