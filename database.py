from sqlalchemy import create_engine, text
import os


my_secret = os.environ['link_to_db']
engine = create_engine(
  my_secret, 
  connect_args={
    "ssl": {
      "ssl_ca": "/etc/ssl/cert.pem"
    }
  })

with engine.connect() as conn:
  result = conn.execute(text("select * from products"))
  print(result.all())
