"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] #empty list for salespeople
melons_sold = [] #empty list for melons sold 

f = open('sales-report.txt')#oepn the sales-report.txt file
for line in f: #loop through each line of the file
    line = line.rstrip() #strip the whitespace 
    entries = line.split('|') # entries = split each element at the pipe line |

    salesperson = entries[0] #overwrite salesperson as the first element in entries 
    melons = int(entries[2]) #overwrite melons as the second element and change type to int

    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
