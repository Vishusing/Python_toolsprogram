import periodictable

Atomic_no = int(input("Enter element Atomic no. :-"))

element = periodictable.elements[Atomic_no]

print('Atomic no: ', element.number)
print('Symbol: ', element.symbol)
print('Name: ', element.name)
print('Atomic mass: ', element.mass)
print('Density: ', element.density)