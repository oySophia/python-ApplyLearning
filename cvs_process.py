#coding=utf-8
#/usr/bin/python

import csv

def csv_process(file_name):
    out = open("write2example.csv", "wb")#, newline='')
    csv_writer = csv.writer(out, dialect="excel")
    with open(file_name, 'r') as f:
        csv_reader = csv.reader(f)
        #print csv_reader
        n = 0
        for row in csv_reader:
            if n == 0:
                #data_header = next(csv_reader)
                data_header = row
                print row
                data_header.append("extra_info")
                data_header.append("test")
                csv_writer.writerow(data_header)
                n = n + 1
                continue
            n = n + 1
            print row
            print row[1]
            write_row = row
            write_row.append("testing")
            csv_writer.writerow(write_row)
        print n
    #print "in the csv_process"

if __name__ == '__main__':
    csv_process("examp1.csv")
    print "in the main func"