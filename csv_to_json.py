import argparse
import csv
import json

parser = argparse.ArgumentParser(description = 'converting csv to json')
parser.add_argument("-csv", action = "store", help = 'CSV file path')
parser.add_argument("-json", action = "store", help = 'JSON file path')
args = parser.parse_args()

def csv_to_json(source_file, dest_file ):
    csv_file = open(source_file, 'r')
    json_file = open(dest_file, 'w+')
    reader = csv.DictReader(csv_file)
    json_file.write('[')
    for row in reader:
       del row['password']
       json.dump(row, json_file, indent = 4)
       json_file.write(',')
       json_file.write('\n')
    json_file.write(']')
    print('Converting passed successfull')
    
csv_to_json(source_file = args.csv, dest_file = args.json)

