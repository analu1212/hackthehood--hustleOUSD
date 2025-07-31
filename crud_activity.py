cookbook = []

def create(recipie): 
    cookbook.append(recipie)
    print(cookbook)

create("brownies")
create("cake")
create("banana bread")

def read(index):
   item = cookbook[index]
print(item)

read(2)

def update(index, recipie):
    cookbook[index] = recipie
    print(cookbook)

update(0, "bear")
