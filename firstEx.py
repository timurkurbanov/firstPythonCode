
# Remember, we get a string from raw_input, but we need an int to compare it
weather = int(25);

# if the weather is greater than or equal to 25 degrees
if weather >= 25:
    print("Go to the beach!")
# the weather is less than 25 degrees AND greater than 15 degrees
elif weather < 25 and weather > 15:
    print("Go home!")
    # Still warm enough for ice cream!
else:
    print('wear a sweater and dream of beaches')
    # Wear a sweater and dream of beaches.
