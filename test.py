temp1 = ['One', 'Two', 'Three', 'Four']
temp2 = ['One', 'Two']
temp3 = [item for item in temp1 if item not in temp2]
print(temp3)