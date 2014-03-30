import csv
winter = csv.reader(open("Modwinter.csv","rb"))
summer = csv.reader(open("Modsummer.csv","rb"))
print "Starting..."
total = 0
for indexstart, row in enumerate(summer):
    for indexcell, cell in enumerate(row):
        if int(float(cell)) > 15 and int(float(cell)) < 27:
            for indexrow, roww in enumerate(winter):
                for indexgrr, grr in enumerate(roww):
                    if int(float(roww[indexrow])) > 15 and int(float(roww[indexrow])) < 27:
                        total = total + 1
print total * 3.6
print "DONE"
