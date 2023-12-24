from flask import Flask, render_template, request, redirect, url_for
import os
import mysql.connector

app = Flask(__name__)

# Replace these with your MySQL database credentials
db_host = 'localhost'
db_user = 'root'
db_password = ''
db_name = 'mybook'

# Create a MySQL connection
connection = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = connection.cursor()

# Create the 'address_book' table if it doesn't exist
create_table_query = '''
CREATE TABLE IF NOT EXISTS address_book (
    id INT AUTO_INCREMENT PRIMARY KEY,
    address_book_name VARCHAR(255),
    firstname VARCHAR(255),
    secondname VARCHAR(255),
    addressline1 VARCHAR(255),
    addressline2 VARCHAR(255),
    addressline3 VARCHAR(255),
    city VARCHAR(255),
    state VARCHAR(255),
    zip VARCHAR(255),
    homephe VARCHAR(255),
    workphe VARCHAR(255),
    mobile VARCHAR(255),
    email VARCHAR(255),
    email2 VARCHAR(255),
    notes TEXT
)
'''
cursor.execute(create_table_query)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    data = {
        'addressbookname': request.form['addressbookname'],
        'firstname': request.form['firstname'],
        'secondname': request.form['secondname'],
        'addressline1': request.form['addressline1'],
        'addressline2': request.form['addressline2'],
        'addressline3': request.form['addressline3'],
        'city': request.form['city'],
        'state': request.form['state'],
        'zip': request.form['zip'],
        'homephe': request.form['homephe'],
        'workphe': request.form['workphe'],
        'mobile': request.form['mobile'],
        'email': request.form['email'],
        'email2': request.form['email2'],
        'notes': request.form['notes']
    }

    save_to_database(data)

    return redirect(url_for('index'))

def save_to_database(data):
    insert_query = '''
    INSERT INTO address_book (
        address_book_name, firstname, secondname, addressline1, addressline2,
        addressline3, city, state, zip, homephe, workphe, mobile, email, email2, notes
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    '''

    cursor.execute(insert_query, (
        data['addressbookname'], data['firstname'], data['secondname'],
        data['addressline1'], data['addressline2'], data['addressline3'],
        data['city'], data['state'], data['zip'], data['homephe'],
        data['workphe'], data['mobile'], data['email'], data['email2'], data['notes']
    ))

    connection.commit()

if __name__ == '__main__':
    app.run(debug=True)
