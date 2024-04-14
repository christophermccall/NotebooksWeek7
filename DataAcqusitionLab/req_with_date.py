from make_request import Settings
this = Settings(url=input('Enter GET url: \n'), headers=Settings().j_header, directory=input('which directory?(abspath):'), prefix=input('make a file prefix: '), suffix=input('make a file suffix: '))
this.requestor_w_date()
