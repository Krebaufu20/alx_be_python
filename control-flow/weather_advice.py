weather = input("Enter the weather (sunny, rainy, snowy): ").strip().lower()
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Dont't forget your umbrella and raincoat.")
elif weather == "cold":
    print('Make sure to wear a warm coat and a scarf.')
else:
    print("Sorry, I dont't have recommendations for this weather.")
