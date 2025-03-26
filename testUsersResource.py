import requests

#правильные
first = requests.get('http://127.0.0.1:5000/api/v2/users/1').json()
second = requests.get('http://127.0.0.1:5000/api/v2/users').json()
third = requests.delete('http://127.0.0.1:5000/api/v2/users/1').json()
user = {
    'surname': 'surname',
    'name': 'name',
    'age': 1,
    'position': 'position',
    'speciality': 'speciality',
    'address': 'address',
    'email': 'email',
    'hashed_password': 'hashed_password'
}
fourth = requests.post('http://127.0.0.1:5000/api/v2/users/1', json=user).json()
print(first)
print(second)
print(third)
print(fourth)

# get неверно
get_wrong = requests.get('http://127.0.0.1:5000/api/v2/users/999').json()
print(get_wrong)

#delete неверно
delete_wrong = requests.delete('http://127.0.0.1:5000/api/v2/users/999').json()
print(delete_wrong)

#post неверно
user = dict()
post_wrong = requests.post('http://127.0.0.1:5000/api/v2/users', json=user).json()
print(post_wrong)