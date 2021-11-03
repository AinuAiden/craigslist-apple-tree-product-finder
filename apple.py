from craigslist import CraigslistForSale as fs

fs_search = fs(site='madison',
          category='grd', #Garden Catagory
          filters={
    'query': 'apple',
    'bundle_duplicates': True,
    'max_price':100
    })

results=[]

for result in fs_search.get_results(sort_by='newest'):
    results.append(result)
    print(result["name"])


