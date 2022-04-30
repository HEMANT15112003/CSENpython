a = input("enter the word : ")
print(a.upper())

b = input("enter the character : ")
print(b.capitalize())
# upper helps in converting word lower case to upper case 
# capitalize coverts a single character to upper case 
c = input("enter a word : ")
print(c.title())
print(c.lower())
print(c.casefold())

d = "kasyap_dibaru"
print(d.center(50))

e = "brother go out of the the class "
print(e.count("the"))
f = e.find("go")
print(f)
g = input("enter a ascii character : ")
print(g.isascii())
print(g.isidentifier())
print(g.islower())
h = input("enter anything : ")
print(h.isnumeric())
print(h.isalpha())
print(h.isdecimal())
print(h.isalnum())
print("*".join(e))
print(e.split())