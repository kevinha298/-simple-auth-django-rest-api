import requests

#Display Token
def display_token():
    url = f'{URL}/api/auth/'
    response = requests.post(url, data = {'username': 'admin', 'password': 'app123'})
    return response.json()

#Get auth token
def get_token():
    url = f'{URL}/api/auth/'
    response = requests.post(url, data={'username': 'admin', 'password': 'app123'})
    return response.json()

#get data
def get_data():
    url = f'{URL}/api/users_list/'
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.get(url, headers = header)
    emp_data = response.json()
    for e in emp_data:
        print(e)

#create new data
def create_new(seq):
    url = f'{URL}/api/users_list/'
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        'employeeID': f'HQ00{seq}', 'employeeName': f'Test user {seq}', 'ranking': 6.8 + seq, 'age': 68 + seq
    }
    response = requests.post(url, data = data, headers = header)
    print(response.text, response.status_code)

#edit data
def edit_data(employeeID, employeeName, ranking, age):
    url = f'{URL}/api/users_list/{employeeID}/'
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        'employeeName': f'{employeeName}', 'ranking': {ranking}, 'age': {age}
    }
    response = requests.put(url, data = data, headers = header)
    print(response.text, response.status_code)

#delete data
def delete_data(employeeID):
    url = f'{URL}/api/users_list/{employeeID}/'
    header = {'Authorization': f'Token {get_token()}'}
    response = requests.delete(url, headers = header)
    print(response.text, response.status_code)

if __name__ == "__main__":
    URL = 'http://127.0.0.1:8000'

    print(display_token())

    get_data()

    for seq in range(1,12):
        create_new(seq)

    employeeID = 8
    employeeName = 'Test user 98' 
    ranking = 8.8
    age = 68
    edit_data(employeeID, employeeName, ranking, age)

    for e in range(20):
        if e > 9:
            delete_data(e)
