#f string 
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
#   print(fruit+"_fruit")
  print(f"lisa adott gyümölcse: {fruit} ....")
#Listához elem hozzáadás (python add list element)
fruits.append("mango")
print(fruits)



print(fruits)
if "abanana" in fruits:
  fruits.remove("abanana")
else:
    fruits.append("abanana")
print(fruits)