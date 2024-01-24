from decimal import Decimal
from os import system
def menu():
    """This function displays the menu and also returns items of the dictionary as a list"""
    menu_card={ 'Margherita': 6,
                'Vegetarian': 7,
                'Chicken Tikka': 8,
                'Paneer Special': 9,
                'Meat Lover': 10,
                'Hawaiian': 11,
                'Cheese Burst': 12,
                'BBQ Chicken': 7,
                'Spicy Sausage': 9,
                'Veggie Delight': 8}
    i=0
    for key,value in menu_card.items():
        i+=1
        print(f"{i}.{key} : £{value}")
        
    
    menu_items=list(menu_card.items())
    return menu_items

def choice(menu_items):
    """This function asks user to enter their choice and checks if it is valid or not."""
    while True:
        total=float()
        try:
            user_input=int(input("Enter your choice: "))
            if 1 <= user_input <= len(menu_items):
                total=total+ menu_items[user_input-1][1]
                choosen=menu_items[user_input-1][0]
                return total,choosen
                break
            else:
                print("\nInvalid input! Please enter a number between 1 and 10")
        except ValueError:
            print("\nInvalid input! Please enter a number.")

def topping(total):
        """this function is used to adds extra toppings 
        at the additional rate of £2 to the pizza when user wants to add more toppings."""
        while True:
            try:
                topping_choice=input("Is topping Required?: ").lower()
                if topping_choice=="y":
                    toppings=["Mozzarella Cheese","Tomatos","Green olives","Black olives","Mushroom"]
                    for i in range(len(toppings)):
                        print(f"{i+1}.{toppings[i]}")
                    topping_choice=int(input("Which topping do you want? :"))
                    if 1<=topping_choice<=len(toppings):
                        total+=2
                        choosen=toppings[topping_choice-1]
                        return total,choosen,2

                    else:
                        print("\nInvalid input! Please enter a valid option.")
                    break
                
                elif topping_choice=="n":
                    return total,"No Toppings",0
                    break
                else:
                    print("Invalid Input! ")
            except ValueError:
                print("\nInvalid input! Please enter a valid option.\n")

                
def calculate_Price(pizza):
    """This function asks the number of pizzas ordered and calculates 
    the price of pizza after the type of pizza is confirmed"""
    while True:
        try:
            number=int(input("How many pizzas ordered? "))
        
            if number<0:
                print("\tPlease enter a positive integer")
            else:
                total_price=Decimal(number*pizza)
                break
        except ValueError:
            print("\tPlease enter a number!")
    return total_price,number


def delivery_Charge(total,number):
    """This function adds £2.50 to the total price for delivery"""
    while True:
        choice=input("Is delivery required? ")
        delivery=choice.upper()
        if delivery=="Y" and number<5:
            charge=Decimal(2.50)
            total+=charge
            return total,charge
            break
        elif delivery=="Y" and number>=5:
            return total,0
            break
        elif delivery=="N":
            return total,0
            break
        else:
                print ("\tPlease enter Y or N")
    

def tuesday_Special(total,delivery_charged):
    """This function applies a 50% discount on Tuesdays"""
    while True:
        day=input("Is it tuesday? ")
        weekday=day.upper()
        if weekday=="Y" and delivery_charged!=0:
            tuesday_discount=(total-Decimal(2.50))/Decimal(2)
            total-=tuesday_discount
            return total,tuesday_discount
            break
        elif weekday=="Y" and delivery_charged==0:
            tuesday_discount=total/Decimal(2)
            total-=tuesday_discount
            return total,tuesday_discount
            break
        elif weekday=="N":
            return total,0
            break
        else:
            print("\tPlease answer 'Y' or 'N'.")
    

def app_Order(final_amount):
    """This function provides a discount of 25% on the final price if the order is
    placed using the new BPP App"""
    while True:
        source=input("Did the customer use the app? ")
        if source.upper()=="Y":
            app_discount=final_amount*Decimal(0.25)
            final_discount=Decimal(final_amount-app_discount)
            return final_discount,app_discount
            break
        elif source.upper()=="N":
            return final_amount,0
            break
        else:
            print("\ttPlease answer 'Y' or 'N'.")

def bill(pizza,topping,topping_price,number,delivery,tuesday,app,total):
    """This function displays a formatted bill after the calculation is completed"""
    system("cls")
    print("*-*-*-*-*-*-*-*-*-*-*-Bill*-*-*-*-*-*-*-*-*-*-*-")
    print(f"Pizza Ordered\t\t\t: {pizza}\nTopping\t\t\t\t: {topping},£{topping_price}\nNumber of Pizzas\t\t: {number}")
    print(f"Delivery Charge\t\t\t: £{delivery}\nTuesday Special Discount(50%)\t: -£{tuesday}\nApp Usage Discount(25%)\t\t: -£{app}")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print(f"Total\t\t\t\t: {total}")


#The main program starts here
print("\tBPP Pizza Calculator")
print("\t====================\n")
items=menu()
per_pizza_price,pizza_choosen=choice(items)
price_with_topping,topping_added,topping_cost=topping(per_pizza_price)
multiple_pizza_price,number_of_pizza=calculate_Price(price_with_topping)
price_after_delivery,delivery_charge=delivery_Charge(multiple_pizza_price,number_of_pizza)
after_tuesday_discount,tuesday_discount_provided=tuesday_Special(price_after_delivery,delivery_charge)
final_amount,app_usage_discount=app_Order(after_tuesday_discount)

bill(pizza_choosen,topping_added,topping_cost,number_of_pizza,delivery_charge,tuesday_discount_provided,app_usage_discount,final_amount)

