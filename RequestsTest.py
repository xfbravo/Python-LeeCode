import requests
resp=requests.get('https://apis.tianapi.com/guonei/index?key=c45275f5f710527333e15e867c35acf1&nums=10')
def print_dict(data):
    if type(data) is dict:
        for key, value in data.items():
            print(key + ":" ,end=" ")
            if type(value) is dict or type(value) is list:
                print()
                print_dict(value)
            else:
                print(value)
    elif type(data) is list:
        for item in data:
            if type(item) is dict:
                print_dict(item)
            else:
                print(item)
    else:
        print(data)
if resp.status_code == 200:
    data_model=resp.json()
    print_dict(data_model)
    # for key,value in data_model.items():
    #     print(key,value,sep=':')
    # for news in data_model['result']['newslist']:
    #     print(news['title'])
    #     print(news['url'])
    #     print('-'*60)