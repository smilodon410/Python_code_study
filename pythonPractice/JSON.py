import json
# data = '''
# {
#     "name":"Hong",
#     "phone":{
#         "type":"intl",
#         "number":"+82 10 6404 6832"
#     },
#     "email":{
#         "hide":"yes"
#     }
# }'''
#
# info = json.loads(data)
# print('Name:', info["name"])
# print('Hide:', info["email"]["hide"])

# input = '''
# [
#     {"id":"001",
#     "x":"2",
#     "name":"Hong"
#     },
#     {"id":"009",
#     "x":"7",
#     "name":"Yoon"
#     }
# ]'''
#
# info = json.loads(input)
# print(info)
# print('User count: ', len(info))
# print('')
# for item in info:
#     print('Name: ', item['name'])
#     print('ID: ', item["id"])
#     print('Attribute: ', item['x'])
#     print('')