import json
import csv
def convertor():
    #opening json file with data
    with open('data.json') as json_file:
        data = json.load(json_file)
    #all the data is in station object data.json file
    station = data['data']['stations']
    data_file = open('data_file.csv', 'w')
    csv_writer = csv.writer(data_file)
    count = 0

    for x in station:
        if count == 0:
            # Writing headers in CSV file
            header = x.keys()
            csv_writer.writerow(header)
            count += 1

        # Writing data in CSV file
        csv_writer.writerow(x.values())

    data_file.close()

if __name__ == '__main__':
    convertor()
