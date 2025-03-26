import requests

print(requests.get('http://127.0.0.1:5000/api/jobs').json())
print(requests.get('http://127.0.0.1:5000/api/jobs/1').json())
print(requests.get('http://127.0.0.1:5000/api/jobs/12313').json())
print(requests.get('http://127.0.0.1:5000/api/jobs/string').json())