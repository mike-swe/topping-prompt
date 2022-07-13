def choco_store(sundae_toppings):                 #Function Definition (Choco_Store)!!

     user__name = input("Please enter your name: ") #Username

     print(f"\nHey {user__name.capitalize()} We have the following toppings:\n")   #Welcome text!!

     for topping in sundae_toppings:              #Condition!!

          if topping=="Chocolate":                
                                                  
               print(f"{topping}(free)\n")        

          else:

               print(f"{topping}($1.50)\n")
          
     user__pref = input("Which one would you like? ")

     if user__pref == f"{sundae_toppings[0]}":

          print(f"\nOne {sundae_toppings[0].lower()} sundae for {user__name.lower()} coming right up!!\n")

     elif user__pref =="":
          
          delayed_response = input("\nPlease try again: ")

          if delayed_response == f"{sundae_toppings[0]}":

               print(f"\nOne {sundae_toppings[0].lower()} sundae for {user__name.lower()} coming right up!!\n")

          elif delayed_response == f"{sundae_toppings[1]}":

               print(f"One {sundae_toppings[1].lower()} sundae for {user__name.lower()} coming right up!!\n")

          else:

               print("\nYour purchase has been cancelled, you can order again \nas soon as your ready")
     else:

          print(f"\nOne {sundae_toppings[1].lower()} sundae for {user__name.lower()} coming right up!!.\n")

choco_store(["Chocolate", "Vanilla"])
