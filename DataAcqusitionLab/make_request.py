import json
from urllib.request import urlopen

from urllib3 import Retry
from urllib3.exceptions import MaxRetryError

from api_key import key
import urllib3

file_prefix = 'loctation_'
file_suffix = '.json'
headers = {
    'Content-Type': 'application/json',
    'token': key,
}
try:
    retries = Retry(
        total=10,  # Total number of allowed retries
        backoff_factor=0.5,  # Factor by which retry delays increase
        status_forcelist=[500, 502, 503, 504]  # HTTP status codes to retry
    )
    http = urllib3.PoolManager(retries=retries)
    count = 0
    j_count = 0
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/?/locationcategoryid=name&limit=1000&offset='
    for j_set in range(1, 38862, 1000):
        response = http.request('GET', f'{url}{str(j_set)}', headers=headers)
        if response.status == 200:
            data = json.loads(response.data.decode('utf-8'))
            j_obj = json.dumps(data, indent=4)
            with open(f'locations_{count}.json', 'w') as f:
                f.write(j_obj)
                count += 1
        else:
            print(f"Error: Unable to fetch data. Status Code: {response.status}")
except MaxRetryError as e:
    print(f"Error: Maximum retries exceeded. {e}")





# url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/?/locationcategoryid=name&limit=1000&offset='

# f = open(f'loctation_{count}.json', 'w')
# json.dump(data['results'], f)
#print(data)
    # f = open(f'loctation_{count}.json', 'w')
    # json.dump(data['results'], f)
    # if count % 1000 == 0 or j_set == 38862:
    #     f.close()
    #     count += 1


    # count = 0
    # if j_set % 2 != 0 and j_set != 1:
    #     j_set -= 1
    # response = http.request('GET', f'{url}{str(j_set)}', headers=headers)
    # data = json.loads(response.data.decode('utf-8'))
    # new_j = f'{file_prefix}{count}{file_suffix}'
    # # print(data['results'])
    # with open(new_j, 'w') as f:
    #       json.dump( data['results'], f)
    # count += 1
    #

    # if response:
    #     for j_obj in data['results']: # ['metadata']['resultset']['offset']:
    #         f = open(f'loctation_{j_set}.json', 'w')
    #         json.dump(j_obj, f)
            # with open(new_j, 'w') as f:
            #     json.dump(j_obj, f)



 # response = http.request('GET', url, headers=headers)
    # data = json.loads(response.data.decode('utf-8'))




#base_url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/'


#encoded_params = urlencode(query_params)


#url = f'{base_url}?{encoded_params}'