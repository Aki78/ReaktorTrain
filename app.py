from flask import Flask, jsonify, request
import mysql.connector
import datetime

app = Flask(__name__)

@app.route('/fetch_recent_naughty_pilots')
usr = ""
psw = ""
hst = ""
db = ""
def fetch_recent_naughty_pilots():
    try:
        cnx = mysql.connector.connect(user=usr, password=psw, host=hst, database=db)
        cursor = cnx.cursor()
        ten_minutes_ago = datetime.datetime.now() - datetime.timedelta(minutes=10)
        query = 'SELECT * FROM data_table WHERE timestamp > %s'
        cursor.execute(query, (ten_minutes_ago,))
        data = cursor.fetchall()
        return jsonify(data)
    except mysql.connector.Error as err:
        return jsonify(err)

@app.route('/insert_data', methods=['POST'])
def insert_recent_naughty_pilots():
    try:
        cnx = mysql.connector.connect(user=usr, password=psw, host=hst, database=db)
        cursor = cnx.cursor()
        data = request.json

        query = 'INSERT INTO data_table (col1, col2) VALUES (%s, %s)'
        cursor.execute(query, (data['col1'], data['col2']))

        cnx.commit()

        return jsonify({'status': 'success'})

    except mysql.connector.Error as err:
        return jsonify({'status': 'error', 'message': str(err)})

if __name__ == '__main__':
    app.run()

