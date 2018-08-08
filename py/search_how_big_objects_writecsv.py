from google import google
import csv

# Test list
objs = ["bike", "Airplane", "car", "Alarm Clock", "Albatross"]

"""
for obj in objs:
    search_results = google.search("How big is a " + obj + "?", num_page)

    for i, result in enumerate(search_results):
        if i < 3:
            print('\n')
            print(obj.capitalize() + ' ' + str(result.index + 1) + ' ---------')
            print(result.description)
"""

# Get things from TXT.
r_objs = 'cleaned_basic_objects_R.txt'
with open(r_objs, 'rb') as f:
    things = []
    reader = csv.reader(f)
    for i, row in enumerate(reader):
        if row[0:2] != '//':
            things.append(row)


# Gets rid of strings

things = [t[0] for t in things]


# File out CSV for Results

fileout = file('object_sizes_google_results_R.csv', 'w')
csv_writer = csv.writer(fileout)

# Google all the things

for thing in things:
    search_results = google.search("How big is a " + thing + "?", 1)
    thing_row = []
    thing_row.append(thing)
    for i, result in enumerate(search_results):
        if i < 3:
            thing_row.append(result.description.encode('utf-8').strip())
    print str(thing_row[0:10])
    csv_writer.writerow(thing_row)
