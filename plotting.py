import matplotlib.pyplot as plt
import csv

year_2013 = open('2013.csv')
year_2014 = open('2014.csv')
year_2015 = open('2015.csv')
year_2016 = open('2016.csv')

year_files = [year_2013, year_2014, year_2015, year_2016]

nationalities = ['Mexic','Xina','Argentina','Filipines']
neighborhood = ['1. el Raval']
offset = 6

#for each nationality
for i,n in enumerate(nationalities):
    pop_per_nat = []

    #get the data for each year
    for year in range(2013, 2017):
        with open(str(year)+".csv") as f:
            csv_reader = csv.DictReader(f)
            for row in csv_reader:

                #find the neighborhood we are working on
                if row['Barris'] == neighborhood[0]:

                    #getting the population for that year in that neighborhood
                    pop_per_nat.append(row[n])

    plt.bar([x+ i*offset for x in range(2013,2017)], pop_per_nat)
    plt.figure(i)