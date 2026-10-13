# Exercise 06: Building anonymous FTP Scanner using ftplib module

[Open the PDF](CN_Exercise_06.pdf)

## Aim

To use ftplib to determine whether an assigned FTP service allows anonymous login.

## Requirements

Python 3.10+; assigned FTP hosts. Local verification uses pyftpdlib as a test server.

## Procedure / algorithm

1. Supply individual lab host addresses and the FTP service port.
2. Connect with ftplib.FTP using a timeout; request anonymous login with a lab contact password.
3. Record a 230 reply as accepted; record a 530 permission reply as rejected.
4. Report network errors separately from rejected authentication and close each connection.

## Complete code / configuration

### [ftp_scanner.py](ftp_scanner.py)

```
"""Check anonymous FTP access on explicitly supplied lab hosts."""
import argparse
import ftplib
import json


def check(host, port=21, timeout=5):
    try:
        with ftplib.FTP() as ftp:
            ftp.connect(host, port, timeout=timeout)
            reply = ftp.login("anonymous", "student@example.invalid")
            return {"host": host, "port": port,
                    "anonymous": True, "reply": reply}
    except ftplib.error_perm as error:
        return {"host": host, "port": port,
                "anonymous": False, "reply": str(error)}
    except (OSError, EOFError, ftplib.Error) as error:
        return {"host": host, "port": port,
                "anonymous": None, "error": str(error)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("hosts", nargs="+")
    parser.add_argument("--port", type=int, default=21)
    args = parser.parse_args()
    for host in args.hosts:
        print(json.dumps(check(host, args.port), sort_keys=True))

```

## Run

```
python Exercise_06/ftp_scanner.py 127.0.0.1 --port 2121
```

## Actual output

```
Actual localhost FTP tests (ephemeral ports):
{"anonymous": true, "host": "127.0.0.1", "port": 58871, "reply": "230 Login successful."}
{"anonymous": false, "host": "127.0.0.1", "port": 58873, "reply": "530 Anonymous access not allowed."}

```

## Expected output

Anonymous-enabled servers return a 230 success reply. Restricted servers return 530. An unreachable host produces a separate connection error.

## Observations

This checks login capability only; it does not enumerate or download server files. Connection failure is not evidence that anonymous access is disabled.

## Result

Anonymous acceptance and rejection were verified against local test FTP servers; remote hosts were not scanned.
