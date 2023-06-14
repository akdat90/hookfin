from flask import Flask,render_template

app = Flask(__name__,template_folder='template')

PRODUCTS = [
  {
    'id': 1,
    'Product Name': 'Long term Investing',
    'price': '20000'
  },
  {
    'id': 2,
    'Product Name': 'Short term Investing',
    'price': '15000'
  },
  {
    'id': 3,
    'Product Name': 'Ultra term Investing',
    'price': '10000'
  }
]


@app.route("/")

def fin_services():
  return render_template("home.html", company_name="Hookup Finserve", products = PRODUCTS)

@app.route("/products")
def show_products():
  return render_template("productpage.html")

@app.route("/blog")
def show_blog():
  return render_template("blog.html")
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)