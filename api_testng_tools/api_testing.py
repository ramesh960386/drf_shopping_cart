import requests


headers = {
    'Authorization': 'Token c0efa4be06a92f8b60dc4f818b30eb468041fdd7'
}


def getToken(username, password):
    url = f"http://127.0.0.1:8000/api-token-auth/ username={username} password={password}"
    r = requests.post(url)
    print(r)


def get_all_resources():
    url = 'http://localhost:8000/api/cart-items/'
    # PARAMS = {'address':location}
    # r = requests.get(url = URL, params = PARAMS)
    r = requests.get(url=url, headers=headers)
    print(r.json())


def post_resource():
    url = 'http://localhost:8000/api/cart-items/'
    data = {
        "product_name": "POCO Mobile",
        "product_price": 2000.0,
        "product_quantity": 20
    }
    # r = requests.get(url, headers=headers)
    r = requests.post(url=url, headers=headers, data = data)

    print(r.json())


def get_single_resource(id):
    url = f'http://localhost:8000/api/cart-items/{id}'
    r = requests.get(url=url, headers=headers)
    print(r.json())


def put_single_resource(id):
    data = {
        "product_name": "Jio Mobile",
        "product_price": 2500.0,
        "product_quantity": 20
    }
    url = f'http://localhost:8000/api/cart-items/{id}'
    r = requests.put(url=url, headers=headers, data=data)
    print(r.json())


def delete_single_resource(id):
    url = f'http://localhost:8000/api/cart-items/{id}'
    r = requests.delete(url=url, headers=headers)
    print(r.json())


if __name__ == "__main__":
    get_all_resources()
    # post_resource()
    # get_single_resource(8)
    # put_single_resource(7)
    # delete_single_resource(9)