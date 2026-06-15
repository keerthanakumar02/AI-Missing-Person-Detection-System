from flask import Flask, render_template, request, redirect, send_from_directory
import sqlite3
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():

    conn = sqlite3.connect("missing.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM persons")
    total_persons = cursor.fetchone()[0]

    conn.close()

    return render_template(
        "index.html",
        total_persons=total_persons
    )


@app.route('/register', methods=['GET', 'POST'])
def register():

    if request.method == 'POST':

        name = request.form['name']
        age = request.form['age']

        photo = request.files['photo']
        filename = photo.filename

        photo.save(
            os.path.join(app.config['UPLOAD_FOLDER'], filename)
        )

        conn = sqlite3.connect("missing.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO persons(name, age, photo) VALUES (?, ?, ?)",
            (name, age, filename)
        )

        conn.commit()
        conn.close()

        return render_template("success.html", name=name)

    return render_template("register.html")


@app.route('/search')
def search():

    search_name = request.args.get("name", "")

    conn = sqlite3.connect("missing.db")
    cursor = conn.cursor()

    if search_name:
        cursor.execute(
            "SELECT * FROM persons WHERE name LIKE ?",
            ('%' + search_name + '%',)
        )
    else:
        cursor.execute("SELECT * FROM persons")

    persons = cursor.fetchall()

    conn.close()

    return render_template(
        "search.html",
        persons=persons,
        search_name=search_name
    )
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/delete/<int:id>')
def delete(id):

    conn = sqlite3.connect("missing.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM persons WHERE id=?", (id,))

    conn.commit()
    conn.close()

    return redirect('/search')


if __name__ == '__main__':
    app.run(debug=True)
