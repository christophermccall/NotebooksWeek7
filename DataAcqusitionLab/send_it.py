from make_request import requestor, Settings


directory = '/Users/chris/pyprojects/NotebooksWeek7/DataAcqusitionLab/new_js'
url_in = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/?/locationcategoryid=name&limit=1000&offset='

this = Settings('locations_', '.json', 1, 38862, 1000)


requestor(url_in, this.s_s_s, this.pre, this.suf, this.j_header, directory)
