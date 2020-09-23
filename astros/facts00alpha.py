#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get("https://api.open-notify.org/astros.json").json)

    # display the methods available to our new object
    print(f"People in space: {r['number']}")
    print(f"{['people'][0]['name']} on the {r['people'][0]['craft']}")
print (f"{['people'][1]['name']} on the {r['people'][0]['craft']}")

main()

