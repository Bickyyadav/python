capitals :{
    "france":"heor",
    "yadav":"bicky"
}

#Nested list of dictionary

travel_log={
    "france":["paris","lilli","Dijiioi"],
    "travel":{
        "nums_times_travel":8,
        "cities_visited":["paris","lilli","Dijiioi"]
    }
}
print(travel_log["france"][1])

#nested list 
nested_list=["A","B",["C","D"]]
print(nested_list[2][0])

print(travel_log["travel"]["cities_visited"][1])