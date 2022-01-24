import csv

fields=["name","class","section:a"]

f1=open("records.csv")
csvwriter=csv.Dictwriter(f1,field)