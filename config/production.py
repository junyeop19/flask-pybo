from config.default import *
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b't\x91/)\xa8\xf4,\x83_\xd7\xd8\x8c\x13\x11\x94\xc5'