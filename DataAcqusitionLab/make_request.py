import json
from urllib.request import urlopen
from pprintpp import pprint
from urllib3 import Retry
from urllib3.exceptions import MaxRetryError
from api_key import key
import urllib3

# url_in = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/?/locationcategoryid=name&limit=1000&offset='
# file_prefix_in = 'loctations_'
# file_suffix_in = '.json'
# start_stop_step_in =0 ,0 ,0
# headers_in = {
#     'Content-Type': 'application/json',
#     'token': key
# }


class Settings:
    def __init__(self, url=None, headers=None, parameters=None, start=None, stop=None, step=1000, directory=None, prefix=None, suffix=None):
        self.url = url
        self.s_s_s = start, stop, step
        self.pre = prefix
        self.suf = suffix
        self.directory = directory
        self.header = headers
        self.parameters = parameters # learn how to utilize this later
        self.j_header = {
            'Content-Type': 'application/json',
            'token': key
        }


    def requestor(self):

        start, stop, step = self.s_s_s
        try:
            retries = Retry(
                total=10,  # Total number of allowed retries
                backoff_factor=0.5,  # Factor by which retry delays increase
                status_forcelist=[500, 502, 503, 504]  # HTTP status codes to retry
            )
            http = urllib3.PoolManager(retries=retries)
            count = 0
            for j_set in range(start, stop, step):
                response = http.request('GET', f'{self.url}&limit={step}&offset={str(j_set)}', headers=self.header)
                if response.status == 200:
                    data = json.loads(response.data.decode('utf-8'))
                    j_obj = json.dumps(data, indent=4)
                    with open(f'{self.directory}/{self.pre}{count}{self.suf}', 'w') as f:
                        f.write(j_obj)
                        count += 1
                else:
                    print(f"Error: Unable to fetch data. Status Code: {response.status}")
        except MaxRetryError as e:
            print(f"Error: Maximum retries exceeded. {e}")


    def requestor_w_date(self):

        start, stop, step = self.s_s_s
        try:
            retries = Retry(
                total=10,  # Total number of allowed retries
                backoff_factor=0.5,  # Factor by which retry delays increase
                status_forcelist=[500, 502, 503, 504]  # HTTP status codes to retry
            )
            http = urllib3.PoolManager(retries=retries)
            count = 0
            start_date = int(input('between(start date): \n'))
            end_date = int(input('and(end date): \n'))
            limit = int(input('stop at:(year)'))
            while start_date <= limit:
                response = http.request('GET', f'{self.url}&startdate={start_date}-01-01&enddate={end_date}-01-01&limit=1000&offset=1', headers=self.header)
                if response.status == 200:
                    data = json.loads(response.data.decode('utf-8'))
                    j_obj = json.dumps(data, indent=4)
                    with open(f'{self.directory}/{self.pre}{start_date}_to_{end_date}{self.suf}', 'w') as f:
                        f.write(j_obj)
                        count += 1
                        start_date += 10
                        end_date += 10
                else:
                    print(f"Error: Unable to fetch data. Status Code: {response.status}")
        except MaxRetryError as e:
            print(f"Error: Maximum retries exceeded. {e}")


    # def requestor(self,url, headers, start_stop_step, file_prefix, file_suffix, directory):
    #
    #     start, stop, step = start_stop_step
    #     try:
    #         retries = Retry(
    #             total=10,  # Total number of allowed retries
    #             backoff_factor=0.5,  # Factor by which retry delays increase
    #             status_forcelist=[500, 502, 503, 504]  # HTTP status codes to retry
    #         )
    #         http = urllib3.PoolManager(retries=retries)
    #         count = 0
    #         for j_set in range(start, stop, step):
    #             response = http.request('GET', f'{url}&limit={step}&offset={str(j_set)}', headers=headers)
    #             if response.status == 200:
    #                 data = json.loads(response.data.decode('utf-8'))
    #                 j_obj = json.dumps(data, indent=4)
    #                 with open(f'{directory}/{file_prefix}{count}{file_suffix}', 'w') as f:
    #                     f.write(j_obj)
    #                     count += 1
    #             else:
    #                 print(f"Error: Unable to fetch data. Status Code: {response.status}")
    #     except MaxRetryError as e:
    #         print(f"Error: Maximum retries exceeded. {e}")


    def meta_requestor(self):
        #  start, stop, step = start_stop_step
        try:
            retries = Retry(
                total=10,  # Total number of allowed retries
                backoff_factor=0.5,  # Factor by which retry delays increase
                status_forcelist=[500, 502, 503, 504]  # HTTP status codes to retry
            )
            http = urllib3.PoolManager(retries=retries)
            response = http.request('GET', f'{self.url}&limit=1&offset=1', headers=self.header)
            if response.status == 200:
                data = json.loads(response.data.decode('utf-8'))
                meta = data['metadata']
                print('{')
                for key,value in meta['resultset'].items():
                    print(f"    '{key}': {value}")
                print('}')
            else:
                print(f"Error: Unable to fetch data. Status Code: {response.status} \n")
                print('trying secondary method...\n')
                http = urllib3.PoolManager(retries=retries)
                response = http.request('GET', f'{self.url}', headers=self.header)
                if response.status == 200:
                    data = json.loads(response.data.decode('utf-8'))
                    print('Success!\n')
                    meta = data['metadata']
                    print('{')
                    for key, value in meta['resultset'].items():
                        print(f"    '{key}': {value}")
                    print('}')

        except MaxRetryError as e:
            print(f"Error: Maximum retries exceeded. {e}")



# come back and finish this later
# need to iterate through url
# locate limit= (insert new limit here)
# def auto_ss_requestor(url, headers, file_prefix, file_suffix, directory):
#     ruleset = meta_requestor(url, headers)
#     s_s_s = ()
#     for key in ruleset.values():
#         for values in key.values():
#             s_s_s += values,
#     (start, stop, step) = s_s_s #new limit = stop
#                                 # new offset will be ub
#     step = 1000
#     try:
#         retries = Retry(
#             total=10,  # Total number of allowed retries
#             backoff_factor=0.5,  # Factor by which retry delays increase
#             status_forcelist=[500, 502, 503, 504]  # HTTP status codes to retry
#         )
#         http = urllib3.PoolManager(retries=retries)
#         count = 0
#         for j_set in range(start, stop, step):
#             response = http.request('GET', f'{url}&limit={step}&offset={str(j_set)}', headers=headers)
#             if response.status == 200:
#                 data = json.loads(response.data.decode('utf-8'))
#                 j_obj = json.dumps(data, indent=4)
#                 with open(f'{directory}/{file_prefix}{count}{file_suffix}', 'w') as f:
#                     f.write(j_obj)
#                     count += 1
#             else:
#                 print(f"Error: Unable to fetch data. Status Code: {response.status}")
#     except MaxRetryError as e:
#         print(f"Error: Maximum retries exceeded. {e}")











# url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/?/locationcategoryid=name&limit=1000&offset='

# meta_url = https://www.ncdc.noaa.gov/cdo-web/api/v2/locations


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