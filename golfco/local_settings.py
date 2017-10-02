# DEBUG = True

ALLOWED_HOSTS = ['golfcoin.club']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'golfco',
        'USER': 'golfco',
        'PASSWORD': '&UITk!lhvd',
        'HOST': '/var/run/mysqld/mysqld.sock',
        'ATOMIC_REQUESTS': True,
    }
}

