#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    ## create r, which is our request object
    r = requests.get('https://cat-fact.herokuapp.com/facts')


    ## catfact is our iterable -- that just means it will take on the values found within
    ## r.json()["all"], one after the next-- which happens to be a dictionary
    ## the code within the loop, says, "from that single dictionary
    ## print the value associated with text"
    
    substr = "A cat"
    for cat in r.json()["all"]:
        old_fact = cat.get("text")
        if old_fact.find(substr) != -1:
    new_fact = old_fact.replace(substr, "chad")
            chad_fact_list.append(new_fact)
    for fact in chad_fact_list:
        print(fact)
      # the .get() method returns NONE if key not found
main()

