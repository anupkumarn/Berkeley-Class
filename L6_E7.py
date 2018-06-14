# Pie Chart
import pylab as  plb 

plb.figure('How do we get to work:')
plb.axes([0.035,0.035,0.9,0.9])

l = 'Car', 'Truck', 'Boat', 'Dingle', 'Train', 'Plane', 'Bus', 'Rocket', 'Tram', 'Other'
b = plb.round_(plb.random(10), decimals=2)
c = ['blue', 'red', 'green', 'gray', 'yellowgreen', 
     'gold', 'lightskyblue', 'lightcoral','cyan','orange']
e = (0,0,0,0,0,0,0,0.2,0,0)   #'explode' the 8th slice only - 'Rocket'

plb.cla() 
plb.pie(b, explode = e, labels = l, colors = c, radius = 0.75,
         autopct='%1.2f%%', shadow=True, startangle=25)

#we set the aspect ration to 'equal' so the pie is drawn in a circle
plb.axis('equal')
plb.xticks(()); plb.yticks(())
plb.pause(2)