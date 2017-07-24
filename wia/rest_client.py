import requests
import logging

from wia import Wia

# TODO: Return error and response in object

'''
wia_post:
    args:
        path:   string specifying url path
        kwargs: variable-length dict which can
                contain data for post request
'''
def post(path, kwargs):
    url = generate_url(path)
    headers = generate_headers()

    if 'file' in kwargs:
        kwargsCopy = dict(kwargs)
        del kwargsCopy['file']
        r = requests.post(url, data=kwargsCopy, headers=headers, files={'file': kwargs['file']})
    else:
        r = requests.post(url, json=kwargs, headers=headers)
    try:
        jsonResponse = r.json()
    except ValueError:
        pass
    return jsonResponse

'''
wia_put:
    args:
        path:   string specifying url path
        kwargs: variable-length dict which can
                contain data for put request
'''
def put(path, **kwargs):
    url = generate_url(path)
    headers = generate_headers()
    data = kwargs
    r = requests.put(url, json=data, headers=headers)
    return r.json()

'''
wia_get:
    args:
        path:   string specifying url path
        kwargs: variable-length dict which can
                contain query params
'''
def get(path, **kwargs):
    url = generate_url(path)
    headers = generate_headers()

    r = requests.get(url, headers=headers, params=kwargs)
    return r.json()

'''
wia_delete:
    args:
        path: string specifying url path
'''
def delete(path):
    url = generate_url(path)
    headers = generate_headers()

    r = requests.delete(url, headers=headers)
    return r

def generate_url(path):
    if path is None:
        path = ''

    url = Wia().rest_config['protocol'] + '://' + Wia().rest_config['host'] + '/' + Wia().rest_config['basePath'] + '/' + path

    logging.debug('URL: %s', url)

    return url

def generate_headers():
    headers = {}

    if Wia().access_token is not None:
        headers['Authorization'] = 'Bearer ' + Wia().access_token

    if Wia().app_key is not None:
        headers['x-app-key'] = Wia().app_key

    logging.debug('Headers: %s', headers)

    return headers
