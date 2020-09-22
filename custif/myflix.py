#!/usr/bin/env python3

message = 'Which Car should i Actually Drive? '

# wrap connection in a float() to accept decimals as numbers
connection = float(input("what is your preferred activation speed in Mph?"))

# if input value was lower or equal to 0 to 60 in 2.9secs
if connection >= 2.9:
    message = message + 'Lamborghini Aventador can reach speed of 220 Mph and go from 0 to 60 in 2.9 secs.'
elif connection >= 3.4:
    message = message + 'Aston Martin one-77 can reach speed of 220 Mph and go from 0 to 60 in 3.4 secs.'
elif connection >= 2.4:
    message = message + 'Bugatti Veyron Super sport can reach speed of 267 Mph and go from 0 to 60 in 2.4 secs.'
else:
    message = message + 'Maybe a Jet will do.'
print(message)
