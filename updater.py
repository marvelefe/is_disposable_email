#!usr/bin/env python3

from os import path
from urllib.request import urlopen


current_dir = path.abspath(path.dirname(__file__))
path_to_file = path.join(current_dir, 'disposable_email_address',
                         '_domains.py')


def update_domains_file():
    host = 'https://raw.githubusercontent.com/'
    src_path = 'akhilharihar/disposable-email-domains-node/master/index.json'
    src = host + src_path

    print('getting domains from internet.')

    try:
        with urlopen(src) as jc:
            emails = jc.read().decode()
    except Exception as e:
        print("error: {}".format(e.code),
              "message: {}".format(e.msg), sep='\n')

        return False

    with open(path_to_file, 'w') as pf:
        data = "domains = " + emails
        pf.write(data)

    print('updated disposable email domains list')


def clear_domains_file():
    with open(path_to_file, 'w') as pf:
        data = "domains = []"
        pf.write(data)


if __name__ == "__main__":
    clear_domains_file()
    update_domains_file()
