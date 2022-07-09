import csv

with open('utilities/loanapp.csv') as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    # print(list(csvReader))
    names = []
    stats = []
    for row in csvReader:
        names.append(row[0])
        stats.append(row[1])

print(names)
print(stats)

Index = names.index('Sam')
print(f"Sam loan statis is {stats[Index]}")

with open('utilities/loanapp.csv','a') as wFile:
    writer = csv.writer(wFile)
    writer.writerow(['Emil','accepted'])