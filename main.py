
from expense import convert_expense


print("""
-----------------------------------
 WELCOME TO EXPENSE TRACKER
-----------------------------------
"""
)
total=0
count=0




while True:
    count+=1
    expense=input(f"{[count]} Enter the Expense Amount (or 'done' to finish): ")
    
   
    

    if expense.lower()=="done":
        break

    try:
        expense=convert_expense(expense)

        total=total+expense

    except Exception as error:
        print(f"Error: {error}")

        count-=1


print(
    f"""-------------------------------------
NUMBER OF EXPENSES : {count-1} 
TOTAL EXPENSE AMOUNT :{total:.2f}
-------------------------------------
     """
 )
