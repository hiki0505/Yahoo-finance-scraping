import sqlite3
import flask
import time
import pandas as pd

# conn = sqlite3.connect(':memory:')

conn = sqlite3.connect('Finances.db')
c = conn.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS historical (
            Date text,
            Open real,
            High real,
            Low real,
            Close real,
            Adj Close real,
            Volume integer
            )""")
conn.commit()

app = flask.Flask(__name__)
app.config["DEBUG"] = True

ticker = 'DOCU'  # title of the company
current_date = int(time.time())
period1 = 0  # Starting date. 0 - means the oldest date
period2 = current_date
interval = '1d'  # Can be 1d, 1m or 1wk

query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

# storing data into dataframe
df = pd.read_csv(query_string)

# converting to sql and save
df.to_sql('historical', conn, if_exists='replace', index=False)

conn.close()

# convert data to json format to be able to represent it in web app
result = df.to_json(orient='records')

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Извлечение финансовых данных с сайта finance.yahoo.com</h1>
<p>Это веб-приложение предназначено для извлечения и вывода на экран финансовых данных за всё время заданной компании</p>'''


# A route to return all of the data in finance history of the company.
@app.route('/api/v7/finances/historical/all', methods=['GET'])
def historical_data():
    return result


app.run()
