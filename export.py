'''
Created on 15 May 2015

@author: tech
'''


from urllib.parse import urlencode, quote
import pyqrcode
import sqlite3
import sys

URI_FORMAT = "otpauth://{otp_type}/{label_enc}?{parameters}"


def create_totp_uri(label, issuer, secret):
    """generate a URI from the distinct elements"""

    otp_type = 'totp'
    params = {'issuer': issuer,
              'secret': secret}

    parameters = urlencode(params)
    label_enc = quote(label)

    return URI_FORMAT.format(**locals())


def print_qr_code(uri):
    """print the QR code from the URI"""


    qr_code = pyqrcode.create(uri, error='L')
    terminal_codes = qr_code.terminal(quiet_zone=2, )
    print(terminal_codes)


def get_secrets(database_file):
    """reads the database and extracts the secrets and meta-data"""

    print(database_file)
    conn = sqlite3.connect(database_file)
    cur = conn.cursor()

    cur.execute("""
                    select email, issuer, secret
                    from accounts
                """)

    for label, issuer, secret in cur:
        if issuer is None:
            issuer = ''
        yield(label, issuer, secret)

    cur.close()
    conn.close()


def main(argv):
    if len(argv) != 2:
        print("Supply an authenticator database file")
        return
    
    database_file = argv[1]
    
    for label, issuer, secret in get_secrets(database_file):
        print("\n\nLabel:{}\nIssuer:{}\n".format(label, issuer))
        print_qr_code(create_totp_uri(label, issuer, secret))
        _dummy = input("Hit enter to continue")

if __name__ == '__main__':
    main(sys.argv)
