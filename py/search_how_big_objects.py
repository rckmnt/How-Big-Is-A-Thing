from google import google

num_page = 3

objs = ["bike", "Airplane", "car", "Alarm Clock", "Albatross"]

thing = "bike"

for obj in objs:
    search_results = google.search("How big is a " + obj + "?", num_page)

    for i, result in enumerate(search_results):
        if i < 3:
            print('\n')
            print(obj.capitalize() + ' ' + str(result.index + 1) + ' ---------')
            print(result.description)
