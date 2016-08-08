# -*- coding: utf-8 -*-

import json

if __name__ == "__main__":
    file_name = "/home/andy/test_json.txt"
    with open (file_name, "rb") as f:
        text = f.read()

    print json.loads(text)