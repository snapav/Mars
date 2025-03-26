import requests

# правильный запрос
job = {
    'team_leader': 1,
    'job': '1',
    'colaborators': '1',
    'work_size': '15',
    'is_finished': True
}

print(requests.post('http://127.0.0.1:5000/api/jobs', json=job).json())

# запрос с не всеми необходимыми ключами

job = {
    'team_leader': 1,
    'colaborators': '1'
}

print(requests.post('http://127.0.0.1:5000/api/jobs', json=job).json())

# запрос с пустым объектом
job = dict()
print(requests.post('http://127.0.0.1:5000/api/jobs', json=job).json())

# запрос с полями неправильного типа
job = {
    'team_leader': 'dasdasdqwed',
    'job': 'asdasdd',
    'colaborators': 'dasdasdasd',
    'work_size': 'dqwd',
    'is_finished': 123
}

print(requests.post('http://127.0.0.1:5000/api/jobs', json=job).json())
