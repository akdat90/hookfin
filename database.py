from sqlalchemy import create_engine, text

db_connection_engine ="mysql+pymysql://8hftdvowswlulou064sv:pscale_pw_GoNoBnhRdxCaq5Vnr7JwNGRg89lhepOVIV5cBywihY9@aws.connect.psdb.cloud/hookup"

engine = create_engine(db_connection_engine,
                       connect_args={"ssl": {
                         "ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from products"))
  print(result.all())
