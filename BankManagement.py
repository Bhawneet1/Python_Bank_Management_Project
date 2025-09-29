
# Bank account creation
# Deposit money
# Withdraw money
# Details
# Update details
# Delete account

import json 
import random
import string 
from pathlib import Path 


class Bank:
  database = 'data.json'
  data = []
    
  try:
      if Path(database).exists():
          with open(database) as fs:
              data = json.loads(fs.read())
      else:
          print("no such file exist ")
  except Exception as err:
      print(f"an exception occured as {err}")
    
  @classmethod
  def __update(cls):
      with open(cls.database,'w') as fs:
          fs.write(json.dumps(Bank.data))

  @classmethod
  def __accountgenerate(cls):
      alpha = random.choices(string.ascii_letters,k = 3)
      num = random.choices(string.digits,k= 3)
      spchar = random.choices("!@#$%^&*",k = 1)
      id = alpha + num + spchar
      random.shuffle(id)
      return "".join(id)



  def Createaccount(self):
      info = {
          "name": input("Tell your name :- "),
          "age" : int(input("tell your age :- ")),
          "email": input("tell your email :- "),
          "pin": int(input("tell your 4 number pin :- ")),
          "accountNo." : Bank.__accountgenerate(),
          "balance" : 0
      }
      if info['age'] < 18  or len(str(info['pin'])) != 4:
          print("sorry you cannot create your account")
      else:
          print("account has been created successfully")
          for i in info:
              print(f"{i} : {info[i]}")
          print("please note down your account number")

          Bank.data.append(info)

          Bank.__update()

  def depositmoney(self):
        accnumber = input("please tell your account number ")
        pin = int(input("please tell your pin aswell "))

        userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

        if userdata == False:
            print("soory no data found")
        
        else:
            amount = int(input("how much you want to deposit "))
            if amount  > 10000 or amount < 0:
                print("sorry the amount is too much you can deposit below 10000 and above 0")

            else:
                userdata[0]['balance'] += amount
                Bank.__update()
                print("Amount deposited successfully ")

            
  def withdrawmoney(self):
      accnumber = input("Enter the account number ")
      pin = int(input("Enter the pin "))

      userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

      if userdata == False:
          print("soory no data found")
      else:
          amount = int(input("please enter amount to be withdrawn "))

          if amount > userdata[0]['balance']:
              print("please enter valid amount")
          else:
              # print(userdata)
              userdata[0]['balance']-=amount
              Bank.__update()
              print("Withdrawn successfully")


  def showdetails(self):
      accnumber = input("please enter your account number ")
      pin = int(input("please enter your pin "))
      
      userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]
      print("Your details are :- \n")
      for i in userdata[0]:# dictionary in list therefore at 0th index 
          print(f"{i} : {userdata[0][i]}")


  def updatedetails(self):
      accnumber = input("please enter your account number ")
      pin = int(input("please enter your pin "))
      
      userdata = [i for i in Bank.data if i['accountNo.'] == accnumber and i['pin'] == pin]

      if userdata == False:
        print("No such user found ")
      else:
          print("you can not change age , account number , balance ")

          print("Fill the details for change or leave it empty for ni change")

          newdata = {
              "name":input("please tell new name or please enter : "),
              "email":input("please tell your new email or please enter to skip : "),
              "pin":input("please tell your new pin or please enter to skip : ")
              # we keep it string as on enter take empty string not in int
          }
          
          if newdata['name'] == "":
              newdata['name'] = userdata[0]['name']

          if newdata['email'] == "":
              newdata['email'] = userdata[0]['email']
          if newdata['pin'] == "":
              newdata['pin'] = userdata[0]['pin']
          
          newdata['age'] = userdata[0]['age']
          newdata['accountNo.'] = userdata[0]['accountNo.']
          newdata['balance'] = userdata[0]['balance']

          if type(newdata['pin']) == str:
              newdata['pin'] = int(newdata['pin'])

          for i in newdata:
              if newdata[i] == userdata[0][i]:
                  continue
              else:
                  userdata[0][i]=newdata[i]
          Bank.__update()
          print("Updated details successfully ")
  
  def Delete(self):
      accnumber = input("please enter your account number ")
      pin = int(input('please enter your pin '))

      userdata = [i for i in Bank.data if i['accountNo.']==accnumber and i['pin'] == pin]

      if userdata == False:
          print("sorry no such data exists ")
      else:
          check = input("press y if you actually want to delete the account or please n to not delete")
          if check == 'n' or check == 'N':             
              print("bypassed")
          else:
              index = Bank.data.index(userdata[0])
              Bank.data.pop(index)
              Bank.__update()

              print("Account deleted successfully")
        
user = Bank()
print("press 1 for creating an account")
print("press 2 for depositing the money in the bank")
print("press 3 for withdrawing the money")
print("press 4 for details")
print("press 5 for updating the details")
print("press 6 for deleting your account")

check = int(input("Tell your response :- "))

if check == 1:
  user.Createaccount()

if check == 2:
  user.depositmoney()

if check == 3:
    user.withdrawmoney()

if check == 4:
    user.showdetails()

if check == 5:
    user.updatedetails()

if check == 6:
    user.Delete()