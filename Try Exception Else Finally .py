while True:
   try:
       age=int(input("Enter Age"))
   except ValueError as es:
          print(f"You Enter Age in  Wrong Format!! {es}")
   except:
       print("Unknown Error!")
   else:
        if age>18:
             print("You Are Adult")
        else:
             print("You Are Teen Ager")
        break
   finally:
           print("Cool")

