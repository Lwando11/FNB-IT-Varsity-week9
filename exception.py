try:
    print(b)
    
#except:
   # print("This except will run and print than try b")
except NameError:  
    print("This except will run")
except:
    print("When theres two except the second one will print run")
    
    
finally:
    print("This will run properly with except name error")    
    
    
def process_payment(amount):
    try:
        amount = float(amount)
        print(f"Payment of R{amount:.2f} processed.")
    except ValueError:
        print("Invalid amount entered. Please provide a number.")

process_payment("29.99")  
process_payment("twenty")  


def check_user_status():
    try:
        print(user_status)  #Look carefully check_user_status variable was not used 
    except NameError:
        print("Oops! 'user_status' hasn't been set yet.")
    finally:
        print("Check complete. Moving on...")

check_user_status()
