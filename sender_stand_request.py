import configuration
import requests
import data


def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

response = get_docs()
print(response.status_code)


def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH,
                        params={"count":20})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH, headers=data.headers,json=body)


def post_products_kits():
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,json=data.product_kids,headers=data.headers)


response = post_products_kits()


