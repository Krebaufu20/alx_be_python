def display_menu():
    print("\nShopping list Manager")
    print("1. Add item")
    print("2. Remove item")
    print("3. View items")
    print("4. Exit")



    def main():
        shopping_list = []


        while True:
            display_menu()
            choice = input("Enter your choice: ").strip()

            if choice == '1':
                item = input("Enter the item to add: ").strip()
                if item:
                    shopping_list.append(item)
                    print(f"Item '{item}' added to the shopping list.")
                else:
                    print("Item cannot be empty.")
           
           

            elif choice == '2':
                item = input("Enter the item to remove: ").strip()
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"Item '{item}' removed from the shopping list.")
                else:
                    print(f"Item '{item}' not found in the shopping list.")
                


            elif choice == '3':
             if shopping_List:
                    print("Shopping list:")
                    for i, item in enumerate(shopping_list, start=1):
                        print(f"{i}. {item}")
                    else:
                        print("Shopping list is empty.")

                        

            elif choice == '4':
                print("Goodbye!")
                break


            else:
                print("Invalid choice. Please try again.")



                if __name__ == "__main__":
                  main()
                