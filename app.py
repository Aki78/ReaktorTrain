from flask import Flask, jsonify, request
import mysql.connector
import datetime

#TODO
#Optimize memory and speed

#Globals
usr = ""
psw = ""
hst = ""
db = ""
app = Flask(__name__)

@app.route('/fetch_recent_naughty_pilots')
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

@app.route('/insert_naughty_pilots', methods=['POST'])
def insert_recent_naughty_pilots():
    try:
        cnx = mysql.connector.connect(user=usr, password=psw, host=hst, database=db)
        cursor = cnx.cursor()
        data = request.json

        data = request.get_json()
        first_name = data['firstName']
        last_name = data['lastName']
        phone_number = data['phoneNumber']
        create_dt = data['createDt']
        email = data['email']
        datetime = data['datetime']

        # Insert the data into the table
        insert_query = '''
        INSERT INTO {} (firstName, lastName, phoneNumber, createDt, email, datetime)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''.format(table_name)
        cursor.execute(insert_query, (first_name, last_name, phone_number, create_dt, email, datetime))
        cnx.commit()

        # Return a success message
        return jsonify({'message': 'Pilot added successfully'})

    except mysql.connector.Error as err:
        return jsonify({'status': 'error', 'message': str(err)})

if __name__ == '__main__':
    app.run()

