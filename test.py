from flask import Flask, render_template
from sqlalchemy import create_engine, text

app = Flask(__name__)

DB_USER = 'root'
DB_PASS = 'E^^hnikh1984'
DB_NAME = 'movietest'

engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASS}@localhost/{DB_NAME}")

# Define a route for the home page
@app.route('/')
def index():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM movietest.users"))
        users = result.fetchall()
    return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
