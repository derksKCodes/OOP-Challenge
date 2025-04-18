from pet import Pet

my_pet = Pet("Buddy")

my_pet.get_status()
my_pet.eat()
my_pet.sleep()
my_pet.play()
print(f"\n{my_pet.name} new status")
my_pet.get_status()

# training my pet
my_pet.train("sit")
my_pet.train("roll over")
my_pet.train("play dead")

#display the tricks
my_pet.show_tricks()
