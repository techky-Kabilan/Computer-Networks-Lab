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
