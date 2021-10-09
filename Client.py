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
def create_new(count):
    url = f'{URL}/api/users_list/'
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        'employeeID': f'HQ00{count}', 'name': f'Test user {count}', 'ranking': 6.8 + count, 'age': 68 + count
    }
    response = requests.post(url, data = data, headers = header)
    print(response.text, response.status_code)

#edit data
def edit_data(employeeID):
    url = f'{URL}/api/users_list/{employeeID}/'
    header = {'Authorization': f'Token {get_token()}'}
    data = {
        'name': f'Test user 17', 'ranking': 8.8, 'age': 88
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

    # print(display_token())

    get_data()

    #edit_data(7)

    # create_new()
    # for e in range(10):
    # create_new(e)

    # for e in range(11):
    # if e > 2:
    #     delete_data(e)
