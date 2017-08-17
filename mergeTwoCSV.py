import csv

outputfile = "usequity_1_1.csv"
outputfile = open(outputfile,"w")
csvwriter = csv.writer(outputfile)

header = ['Id','SecType','Exch','Ticker','Cusip','Sedol','Isin']

csvwriter.writerow(header)

count = 0
with open("usequity.csv","rb") as f:
        reader = csv.reader(f,delimiter=":")
        for line in reader:
                line_len =  len(line)-1
                #print line[line_len]
                if line[line_len].strip() != 'None':
                        #print line[0]
                        with open("secmaster.20170503.1.csv") as g:
                                reader_g = csv.reader(g,delimiter="|")
                                for line_g in reader_g:
                                        #print line[0],"===",line_g[6]
                                        if line[0].strip() == line_g[6]:
                                                row_list = [line_g[0],line_g[1],line_g[5],line_g[6],line_g[7],line_g[8],line_g[9]]
                                                print row_list
                                                csvwriter.writerow(row_list)
                                                del row_list[:]
                        count+=1
        print count
