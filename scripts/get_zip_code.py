import geocoder
import csv
f1 = open('../Data/lat_long.csv', 'r')

lines = sum(1 for line in open('../Data/lat_long_zipcode.csv')) - 1
print lines                               
f2 = open('../Data/lat_long_zipcode.csv', 'a')

csvreader = csv.reader(f1, delimiter=",", quotechar='"')
csvwriter = csv.writer(f2, delimiter=",", quotechar='"', quoting = csv.QUOTE_MINIMAL)

for i,row in enumerate(csvreader):
    print row,i
    #break
    if i == 0 :
        continue
    else:
        if int(row[0]) > lines :
            address = " ".join([row[2], "new york" ]) 
            geo_obj = geocoder.google(address)
            row.append(address)
            row.append(geo_obj.postal)
            csvwriter.writerow(row)
         
    print row

      


         
