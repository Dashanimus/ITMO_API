import requests


class Client:

    @staticmethod
    def get(url, timeout=5):
        return requests.request("GET", url, timeout=timeout)

    @staticmethod
    def post(url, headers, payload, timeout=5):
        return requests.request("POST", url, headers=headers, data=payload, timeout=timeout)

    @staticmethod
    def delete(url, timeout=5):
        return requests.request("DELETE", url, timeout=timeout)
