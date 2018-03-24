from config import Config
from KeyVaultWrapper import KeyVaultWrapper
from OpenSSLWrapper import OpenSSLWrapper

from OpenSSL import crypto
import os
import time

hostname = os.uname()[1]

cfg = Config()
openssl = OpenSSLWrapper()

def load_data():
    kvwrapper = KeyVaultWrapper()

    kvwrapper.get_secret_to_file(cfg.vault_uri, 'root-ca', '', 'root_ca.pem')
    kvwrapper.get_secret_to_file(cfg.vault_uri, 'intermediate-ca', '', 'intermediate_ca.pem')

    kvwrapper.get_certificate_and_key_to_file(
        vault_uri = cfg.vault_uri,
        cert_name = hostname,
        cert_version = '',
        key_filename = 'new.key',
        cert_filename = 'new.pem')

while True:
    try:
        load_data()
    except:
        time.sleep(5)
        continue
    else:
        break