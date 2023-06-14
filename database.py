from sqlalchemy import create_engine, text

db_connection_engine = "mysql+pymysql://vcpz0flra94m63sw0pj7:pscale_pw_FoDx1uXfYdIhtLd5aPvMWg2YWzQkCrhzewa04ZN1WFm@aws.connect.psdb.cloud/hookupfinserve"
engine = create_engine(db_connection_engine,
                       connect_args={"ssl": {
                         "ca": "/etc/ssl/cert.pem"
                       }})

with engine.connect() as conn:
  result = conn.execute(text("select * from products"))
  print(result.all())
