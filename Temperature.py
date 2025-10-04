Temperature = float(input(" Please Enter Temperature : "))

if Temperature >= 30:
    print("It's a hot day. Stay hydrated!")
elif 20 <= Temperature <= 29:
    print("It's a warm day. Enjoy the weather!")
elif 10 <= Temperature <= 19:
    print("It's a cool day. Wear a jacket!")
else:
    print("It's a cold day. Stay warm!")