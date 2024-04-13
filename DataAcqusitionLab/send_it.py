from make_request import requestor, meta_requestor, auto_ss_requestor, Settings

# sample_directory = '/Users/chris/pyprojects/NotebooksWeek7/NOAADailySummaries/data/daily_summaries'
#
# offsets_url = 'https://www.ncei.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:10003&startdate=2018-12-01&enddate=2018-12-31&limit=1000&offset='
#
# base_url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations'
#

# this = Settings(url=input('input GET url \'offset=\' don\'t end with a number!): \n'), stop=int(input('count: ')), step=int(input('limit: ')), directory=input('which directory?(abspath):'), prefix=input('make a file prefix: '), suffix=input('make a file suffix: '))
# this_auto = Settings(url=input('url ending in \'offset=\' : \n'), prefix=input('file prefix'), suffix=input('file suffix'), directory=input('which directory?(abspath):'))
# this_meta = Settings()



#meta_requestor(meta_url_in, this_meta.j_header)
#requestor(this.url, this.j_header, this.s_s_s, this.pre, this.suf, this.directory)
#auto_ss_requestor(this_auto.url, this_auto.j_header, this_auto.pre, this_auto.suf, this_auto.directory)
















# ruleset = meta_requestor(meta_url_in, this_meta.j_header)
# s_s_s = ()
# for key in ruleset.values():
#     for values in key.values():
#         s_s_s += values,
# (start, stop, step) = s_s_s
#
# print(start)
# print(stop)
# print(step)

