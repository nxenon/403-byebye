# 403 ByeBye
[![Tool Category](https://badgen.net/badge/Tool/Bypasser/black)](https://github.com/nxenon/403-byebye)
[![APP Version](https://badgen.net/badge/Version/v1.1.0/red)](https://github.com/nxenon/403-byebye)
[![Python Version](https://badgen.net/badge/Python/3.x/blue)](https://www.python.org/download/releases/3.0/)
[![License](https://badgen.net/badge/License/GPLv2/purple)](https://github.com/nxenon/403-byebye/blob/master/LICENSE)

Bypass 403 Forbidden Errors
 - Still working on it.

Features:
- Header Bypass Technique

# Usage
    python3 403-byebye.py --show-examples
    python3 403-byebye.py --url https://www.example.com/a/page/which/has/403/error

# Installation
    git clone https://github.com/nxenon/403-byebye.git
    cd 403-byebye
    pip install -r requirements.txt
    python3 403-byebye.py --help

# Help
     nxenon@nxenon:~$ python3 403-byebye.py --help
      _  _    ___ ____    ____             ____
     | || |  / _ \___ \  |  _ \           |  _ \  Version: 1.1.0
     | || |_| | | |__) | | |_) |_   _  ___| |_) |_   _  ___
     |__   _| | | |__ <  |  _ <| | | |/ _ \  _ <| | | |/ _ \
        | | | |_| |__) | | |_) | |_| |  __/ |_) | |_| |  __/
        |_|  \___/____/  |____/ \__, |\___|____/ \__, |\___|
                                 __/ |            __/ |
                                |___/            |___/
    
    Arguments:
      --url                       target URL
      --methods                   methods for request (Available: GET,POST) [default GET]
      --use-json                  use Json Content-Type for POST Request instead of x-www-form-urlencoded
      --add-payload               add Bypass-Value(payload) for replacing in headers [default 127.0.0.1]
      --add-data                  add POST data or GET parameter for Request
      --add-cookie                add cookie for request
      --add-extra-header          add extra header for request
      --set-proxy                 set proxy for requests [http, https](when proxy is set timeout sets to None)
      --verbose                   verbose output
      --timeout                   timeout in seconds [Default 3.0]
      --no-color                  print output without color
      --show-examples             show some examples for using this tool
      --help                      show this help message
