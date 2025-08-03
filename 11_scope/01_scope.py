# does python has a block scope ?
#-> there is no block scope in python 

#modifying the global scope 
enemies = 1

def increase_enemies():
    # modifying the global varibale
    global enemies
    enemies+=3
    enemies=2
    print("enemies inside function:{enemies}")


increase_enemies()
print("enemies inside function:{enemies}")