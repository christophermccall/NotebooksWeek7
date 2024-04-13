from make_request import Settings
this_meta = Settings(url=input('Enter base url: '), headers=Settings().j_header)
this_meta.meta_requestor()
