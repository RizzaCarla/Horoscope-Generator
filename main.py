# Zodiac Sign Website

# -----Imports-----
import os
import re
import pymongo
from zodiac_sign_identifier import ZodiacSignIdentifier
from flask import Flask, render_template, redirect, url_for, request, flash


# -----------------
client = pymongo.MongoClient("mongodb+srv://zsADMIN:zsPASSWORD@cluster0.ara46.mongodb.net/ZodiacSignDatabase?retryWrites=true")
db = client["ZodiacSignDatabase"]
collection = db["ZodiacSign"]

UPLOAD_FOLDER = "C:\\PycharmProjects\\Zodiac_Sign\\Templates\\images"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/', methods=['GET', 'POST'])
def zodiacfinder():
    if request.method == 'POST':
        month = request.form['month_input']
        month = month.lower()
        date = request.form['date_input']
        date = re.findall(r'[0-9]+$', date)
        if len(date) == 0 or len(month) == 0:
            return render_template('/home.html', error="Invalid Entry. Empty field.")
        user = ZodiacSignIdentifier(month, *date)
        user_zodiac_sign = user.zodiac_sign_generator()
        if "valid" in user_zodiac_sign:
            return render_template('/home.html', error=user_zodiac_sign)
        return redirect(url_for('zodiacsign', zodiacsign=user_zodiac_sign))
    else:
        return render_template('/home.html')


@app.route('/<zodiacsign>')
def zodiacsign(zodiacsign):
    zodiacsign = zodiacsign.lower()
    full_filename = os.path.join(app.config["UPLOAD_FOLDER"], f'{zodiacsign}.png')
    print(full_filename)
    description = collection.find_one({"sign": zodiacsign}, {"_id": 0, "sign": 0})
    zodiacsign = zodiacsign.capitalize()
    if description is not None:
        description = description["description"]
    return render_template("zodiacsign.html", zodiacsign=zodiacsign, description=description)

if __name__ == "__main__":
    app.run(debug=True)
