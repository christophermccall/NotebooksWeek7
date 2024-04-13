from make_request import meta_requestor, Settings
this_meta = Settings(url=input('Enter base url: '))
meta_requestor(this_meta.url, this_meta.j_header)
