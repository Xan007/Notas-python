def my_function(**kid): #DICCIONARIO (key-value)
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(*kids): #LISTA
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")