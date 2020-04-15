#creating class for customer
class Customer:
  def __init__(mysillyobject,Id,first_name,last_name, phonenumber,email):
    mysillyobject.Id = Id
    mysillyobject.first_name = first_name
    mysillyobject.last_name = last_name
    mysillyobject.phonenumber = phonenumber
    mysillyobject.email = email

#function for customer details 
  def showCustomer(abc):
    print("\n")
    print("---Customer Details---")
    print("Customer's id: ",  abc.Id)
    print("Customer's first name: " + abc.first_name)
    print("Customer's last name: " + abc.last_name)
    print("Phone number: ", abc.phonenumber)
    print("email: ", abc.email)

#creating class for order
class order:
    def __init__(mysillyobject,order_Id,item,price,total):
        mysillyobject.order_Id =order_Id
        mysillyobject.item = item
        mysillyobject.price= price
        mysillyobject.total = total

 #function for order details        
    def showOrder(wendy):
        print("\n")
        print("--- ORDERS----")
        print("order id: ",  wendy.order_Id)
        print("item: " + wendy.item)
        print("price: " , wendy.price)
        print("total: ", wendy.total)

#creating class for merchant details    
class merchant:
    def __init__(mysillyobject,merchant_Id,merchant_name):
        mysillyobject.merchant_Id =merchant_Id
        mysillyobject.merchant_name = merchant_name
        
#function for merchant details 
    def showMerchant(nathaniel):
        print("\n")
        print("--- Merchant Details----")
        print("Merchant id: ",  nathaniel.merchant_Id)
        print("Merchant name: " + nathaniel.merchant_name)

#creating class for order
class order:
    def __init__(mysillyobject,order_Id,item,price,total):
        mysillyobject.order_Id =order_Id
        mysillyobject.item = item
        mysillyobject.price= price
        mysillyobject.total = total

  #function for order details      
    def showOrder(wendy):
        print("\n")
        print("--- ORDERS----")
        print("order id: ",  wendy.order_Id)
        print("item: " + wendy.item)
        print("price: " , wendy.price)
        print("total: ", wendy.total)

#creating class for product    
class product:
    def __init__(mysillyobject,product_Id,product_name,expiry_date):
        mysillyobject.product_Id = product_Id
        mysillyobject.product_name = product_name
        mysillyobject.expiry_date = expiry_date
        
#function for order details   
    def showProduct(wenat):
        print("\n")
        print("--- Product Details----")
        print("product id: ",  wenat.product_Id)
        print("Product name: " + wenat.product_name)
        print("Product expiry: "+ wenat.expiry_date)

#creating class for user
class user:
    def __init__(mysillyobject,user_Id,user_name,title):
        mysillyobject.user_Id = user_Id
        mysillyobject.user_name = user_name
        mysillyobject.title = title
        
#function for user details   
    def showUser(forever):
        print("\n")
        print("--- User Details----")
        print("User Id: ",  forever.user_Id)
        print("User name: " + forever.user_name)
        print("User's Title : "+ forever.title)       
      
  #creating class for transaction    
class transaction:
    def __init__(mysillyobject,transaction_Id,transaction_date,transaction_time):
        mysillyobject.transaction_Id = transaction_Id
        mysillyobject.transaction_date = transaction_date
        mysillyobject.transaction_time = transaction_time
        
#function for transaction details
    def showTransaction(Omega):
        print("\n")
        print("--- Transaction Details----")
        print("Transaction id: ",  Omega.transaction_Id)
        print("Date: " + Omega.transaction_date)
        print("Time: ", Omega.transaction_time)   


#calling all functions and passing arguments to parameters
p1 = Customer(934 , "John","mintah", 36, "nathanielmishio@yahoo.com")
p1.showCustomer()

p2 = order(1,"Kiss condom",3.5,3.5)
p2.showOrder()

p3 = merchant(392,"wendyPharmaceuticals")
p3.showMerchant()

p4 = product(332392,"Kiss condom","12-12-20")
p4.showProduct()

p5 = user(233,"Amarteyley","Branch-manager")
p5.showUser()

p6 = transaction(1,"12/03/2020","12:14:05")
p6.showTransaction()