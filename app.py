from flask import Flask, jsonify
import mysql.connector
import datetime

app = Flask(__name__)

@app.route('/fetch_data')
def fetch_data():
    try:
        cnx = mysql.connector.connect(user='username', password='password', host='hostname', database='database')
        cursor = cnx.cursor()
        ten_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=10)
        query = 'SELECT * FROM data_table WHERE timestamp > %s'
        cursor.execute(query, (ten_minutes_ago,))
        data = cursor.fetchall()
        return jsonify(data)
    except mysql.connector.Error as err:
        return jsonify(err)

if __name__ == '__main__':
    app.run()

