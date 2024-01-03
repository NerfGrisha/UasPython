from flask import Flask, jsonify, request, render_template
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="perpustakaan"
)

cursor = mydb.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS buku (
        id INT AUTO_INCREMENT PRIMARY KEY,
        judul VARCHAR(255),
        pengarang VARCHAR(255),
        tahun_terbit INT
    )
""")
mydb.commit()

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    judul = request.form['judul']
    pengarang = request.form['pengarang']
    tahun_terbit = request.form['tahun_terbit']

    sql = "INSERT INTO buku (judul, pengarang, tahun_terbit) VALUES (%s, %s, %s)"
    sql_insert = (judul, pengarang, tahun_terbit)

    cursor.execute(sql, sql_insert)
    mydb.commit()

    respond = jsonify('Data Buku Berhasil Tersimpan!') if cursor.rowcount == 1 else jsonify('Data Buku Gagal Tersimpan!')
    respond.status_code = 200 if cursor.rowcount == 1 else 500

    return respond

@app.route('/edit', methods=['PUT'])
def edit():
    book_id = request.args.get("id")
    judul = request.args.get('judul')
    pengarang = request.args.get('pengarang')
    tahun_terbit = request.args.get('tahun_terbit')

    sql = "UPDATE buku SET judul = %s, pengarang = %s, tahun_terbit = %s WHERE id = %s"
    sql_insert = (judul, pengarang, tahun_terbit, book_id)

    cursor.execute(sql, sql_insert)
    mydb.commit()

    respond = jsonify('Data Buku Berhasil Diubah!') if cursor.rowcount == 1 else jsonify('Data Buku Gagal Diubah!')
    respond.status_code = 200 if cursor.rowcount == 1 else 500

    return respond

@app.route('/delete', methods=['DELETE'])
def delete():
    book_id = request.args.get('id')

    sql = "DELETE FROM buku WHERE id = %s"
    cursor.execute(sql, (book_id,))
    mydb.commit()

    respond = jsonify('Data Buku Berhasil Dihapus!') if cursor.rowcount else jsonify('Data Buku Gagal Dihapus!')
    respond.status_code = 200 if cursor.rowcount else 500

    return respond

@app.route('/showdata', methods=['GET'])
def showdata():
    book_id = request.args.get('id')

    if book_id:
        # If book_id is provided, fetch data for that specific ID
        sql = "SELECT * FROM buku WHERE id = %s"
        cursor.execute(sql, (book_id,))
        book_data = cursor.fetchone()
        respond = jsonify(book_data) if book_data else jsonify('Data Buku tidak ditemukan!')
        respond.status_code = 200 if book_data else 404
    else:
        # If book_id is not provided, fetch all data
        sql = "SELECT * FROM buku"
        cursor.execute(sql)
        all_data = cursor.fetchall()
        respond = jsonify(all_data) if all_data else jsonify('Data Buku tidak ditemukan!')
        respond.status_code = 200 if all_data else 404

    return respond

if __name__ == "__main__":
    app.run(port=8080)
