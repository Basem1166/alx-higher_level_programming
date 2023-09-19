#!/usr/bin/python3
def best_score(a_dictionary):
    return (a_dictionary.keys(max(a_dictionary.values())) if a_dictionary else None)
mydic={"John": 12, "Alex": 8, "Bob": 14, "Mike": 14, "Molly": 16}
print(best_score(mydic))