PUPPETDB_HOST = '172.28.128.3'
PUPPETDB_PORT = 8081
PUPPETDB_SSL_VERIFY = False
PUPPETDB_KEY = '/home/vmazzi/Documents/learning/puppetboard/certs/puppetdb/key.pem'
PUPPETDB_CERT = '/home/vmazzi/Documents/learning/puppetboard/certs/puppetdb/cert.pem'
PUPPETDB_TIMEOUT = 20
DEV_LISTEN_HOST = '127.0.0.1'
DEV_LISTEN_PORT = 5000
UNRESPONSIVE_HOURS = 2
ENABLE_QUERY = True
LOCALISE_TIMESTAMP = True
LOGLEVEL = 'info'
REPORTS_COUNT = 10
OFFLINE_MODE = False
GRAPH_FACTS = ['architecture',
               'domain',
               'lsbcodename',
               'lsbdistcodename',
               'lsbdistid',
               'lsbdistrelease',
               'lsbmajdistrelease',
               'netmask',
               'osfamily',
               'puppetversion',
               'processorcount']
