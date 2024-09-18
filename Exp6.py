def divide_numbers(a, b):
    try:
        result = a / b  
        print("The result of division is:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!") 
    except TypeError:
        print("Error: Invalid input type! Please enter numbers.")  
    finally:
        print("Execution completed.")  


divide_numbers(10, 2)   
divide_numbers(10, 0)   
divide_numbers(10, "a") 
