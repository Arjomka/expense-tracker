#   _____                                       _____               _             
#  | ____|_  ___ __   ___ _ __  ___  ___  ___  |_   _| __ __ _  ___| | _____ _ __ 
#  |  _| \ \/ / '_ \ / _ \ '_ \/ __|/ _ \/ __|   | || '__/ _` |/ __| |/ / _ \ '__|
#  | |___ >  <| |_) |  __/ | | \__ \  __/\__ \   | || | | (_| | (__|   <  __/ |   
#  |_____/_/\_\ .__/ \___|_| |_|___/\___||___/   |_||_|  \__,_|\___|_|\_\___|_|   
#             |_|                                                                 

#
# Uzdevums:
# Uzrakstīt programmu, kas ļauj
# - ievadīt izdevumus: nosaukumu, summu un kategoriju
# - atspoguļot uz ekrāna visus izdevumus
# - iespēja atlasīt 10 lielākus izdevumus
# - iespēja atlasīt 10 mazākus izdevumus
# - iespēja apskatīt vidējo izdevumu summu
# [!] Programmai jaglabā izdevumu stāvokli kad programma ir izslēgta palaista no jauna
#

expenses = []

# load expenses from expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Python read JSON file)
pass

import json

while True:
    command = input("\nChoose command:")
    if command == "1":
            
            name = input("Enter a transaction name: ")
            sum = int(input("Enter transactions sum: "))
            category = input("Enter transactions category: ")
            expense = {"Transaction name": name, "Transaction sum": sum, "Transactions category": category}
            expenses.append(expense)
            print(expenses)

            pass 
    if command == "2":
         print("Your expenses is: ", expenses)
    if command == "3":
         def sort_10bigest(expenses):
              return int(expenses["Transaction sum"])
         expenses.sort(key=sort_10bigest)
         print(expenses[:10])
    if command == "4":
         def sort_10smalest(expenses):
              return int(expenses["Transaction sum"])
         expenses.sort(key=sort_10smalest, reverse = True)
         print(expenses[:10])
    if command == "5":
         total_sum = 0
         count = 0

         for item in expenses:
              if isinstance(item, (int, float)):
                   total_sum += item
                   count += 1
                   if count > 0:
                        average = total_sum / count
                        print("Average: ", average)
                        
                
            
        
             
        
        
                  
        
    if command == "e":
        print("Exiting...")
        break

# save expenses to expenses.json file here
# https://www.geeksforgeeks.org/read-write-and-parse-json-using-python/ (Writing JSON to a file in Python)
pass

