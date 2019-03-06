# edit the URI below to add your RDS password and your AWS URL
# The other elements are the same as used in the tutorial
# format: (user):(password)@(db_identifier).amazonaws.com:3306/(db_name)

mode = 'dev' # dev / prod

if mode == 'dev':
	SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

if mode == 'prod':
	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://plantondemand:Fumies9933@rds-flask.cdbbfmyitjua.eu-west-2.rds.amazonaws.com:3306/agricultores'

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_RECYCLE = 3600
WTF_CSRF_ENABLED = True
SECRET_KEY = 'q7xsaGX1vwEYfFRV+GTuZP1ISrE8JL7QlkoIAvVe'
