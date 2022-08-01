# 403 ByeBye
[![Tool Category](https://badgen.net/badge/Tool/Bypasser/black)](https://github.com/nxenon/403-byebye)
[![APP Version](https://badgen.net/badge/Version/Beta/red)](https://github.com/nxenon/403-byebye)
[![Python Version](https://badgen.net/badge/Python/3.x/blue)](https://www.python.org/download/releases/3.0/)
[![License](https://badgen.net/badge/License/GPLv2/purple)](https://github.com/nxenon/403-byebye/blob/master/LICENSE)

Hope to Bypass 403 Forbidden Errors :)
 - Still working on it.
 - I'll be glad if you wanna contribute

# Usage
    python3 403-byebye.py --url https://wwww.example.com

# Installation
    git clone git@github.com:nxenon/403-byebye.git
    cd 403-byebye
    pip install -r requirements.txt
    python3 403-byebye.py --script-help

# Help
     nxenon@nxenon:~$ python3 403-byebye.py --script-help
      _  _    ___ ____    ____             ____
     | || |  / _ \___ \  |  _ \           |  _ \  Version: Beta
     | || |_| | | |__) | | |_) |_   _  ___| |_) |_   _  ___
     |__   _| | | |__ <  |  _ <| | | |/ _ \  _ <| | | |/ _ \
        | | | |_| |__) | | |_) | |_| |  __/ |_) | |_| |  __/
        |_|  \___/____/  |____/ \__, |\___|____/ \__, |\___|
                                 __/ |            __/ |
                                |___/            |___/
    
    Arguments:
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
