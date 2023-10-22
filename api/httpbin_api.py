from api.client import Client


class HttpBinApi(Client):
    HTML = '/html'
    TXT = '/robots.txt'
    BASE_URL = 'https://httpbin.org'
    TIME = '/delay'

    def list_html(self):
        """
        method: get
        routs: /html
        status: 200
        """

        url = self.BASE_URL + self.HTML
        return self.get(url)

    def get_robots(self):
        """
        method: get
        routs: /robots.txt
        status: 200
        """

        url = self.BASE_URL + self.TXT
        return self.get(url)

    def get_ip(self):
        """
        method: get
        routs: /ip
        status: 200
        """

        url = self.BASE_URL + self.TXT
        return self.get(url)

    def time_out(self, delay=1):
        """
        :method: get
        :routs: /delay/{delay}
        :status: 200
        """

        url = self.BASE_URL + self.TIME + f'/3'
        try:
            return self.get(url, timeout=delay)
        except Exception as ex:
            return False, ex


http_bin_api = HttpBinApi()
