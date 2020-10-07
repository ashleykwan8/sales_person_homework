"""Generate sales report showing total melons each salesperson sold."""


salespeople = [] #empty list for salespeople
melons_sold = [] #empty list for melons sold 

f = open('sales-report.txt')#oepn the sales-report.txt file
for line in f: #loop through each line of the file
    line = line.rstrip() #strip the whitespace 
    entries = line.split('|') # entries = split each element at the pipe line |

    salesperson = entries[0] #overwrite salesperson as the first element in entries 
    melons = int(entries[2]) #overwrite melons as the second element and change type to int

    if salesperson in salespeople: #check if salesperson is in salespeople list
        position = salespeople.index(salesperson)  #position is the index # of salespeople 
        melons_sold[position] += melons #melons_sold list index + number of melons 
    else:
        salespeople.append(salesperson) #add salesperson to salespeople list
        melons_sold.append(melons) #add melons to melons_sold list 


for i in range(len(salespeople)): #for index of the range of the length of salespeople list 
    print(f'{salespeople[i]} sold {melons_sold[i]} melons') #print salesperson sold number of melons 
