from make_request import Settings
this = Settings(url=input('Enter GET url: \n'), headers=Settings().j_header, start=int(input('offset: ')), stop=int(input('count: ')), step=int(input('limit: ')), directory=input('which directory?(abspath):'), prefix=input('make a file prefix: '), suffix=input('make a file suffix: '))
this.requestor()
