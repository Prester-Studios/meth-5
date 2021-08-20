
import time
import math

access = False
account = "Nothing"

registered = ['Roblox', 'Thanker']
passwords = ['9wfa=d1das', '$sro0poe1']


def check_input(user_input):
  for x in registered:
    if str(user_input) == x:
      print("Passed First Control.")
      return "Available"


def getpassword(password):
  for x in passwords:
    if x == password:
      return x

print("What's your username?")
print("If you've not received a account personally from the creator,")
print("please select a Guest account by entering: Guest")
print("")
print("Case Sensitive.")

inputted = input()
print("")

acc = ""

availability = check_input(inputted)

if availability == "Available":
  print("Passed Third Control.")
  print("Enter the password of you account.")
  pass_input = input()
  password = getpassword(pass_input)
  if str(pass_input) == str(password):
    account = inputted
    access = True
    print("Login Success!")
  else:
    print("Login Failed!")
    print("Do you want to continue as a guest account?")
    print("1 means yes and 2 means no.")
    print("")
    answer = input()
    if str(answer) == "1":
      access = True
      account = "Guest"
elif str(inputted) == "Guest":
  access = True
  account = "Guest"
else:
  print("Failed at Second Report.")
print("")
if account == "Nothing":
  print("Login Failed: Invalid Account")
else:
  print("Logged in as: " + str(account))

