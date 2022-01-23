import os

from flask import Flask, render_template, request
app= Flask(__name__)

@app.route('/greet', methods=['POST'])
def greet():
    inputName = request.form['myName']

    inputName.split(",")
    strength_score = 0
    
    for character in inputName:
        if character.isalpha():
            if character.isupper():
                strength_score += 5
            else:   
                strength_score += 2
        elif character.isdigit():
            strength_score += 5
        else:
            strength_score += 6

    #gathers points on how long password is
    if len(inputName) < 5:
        strength_score += 10
    elif len(inputName) >= 5 and len(inputName) < 8:
        strength_score += 20
    elif len(inputName) >= 8 and len(inputName) < 11:
        strength_score += 30
    else:
        strength_score += 40

    if strength_score < 25:
        final_score = "Passwordnya Lemah! Tambahkan lebih banyak karakter huruf besar, angka, atau karakter khusus!"
    elif strength_score >=25 and strength_score < 50:
        final_score = "Password Di bawah Rata-rata! Terus tambahkan lebih banyak karakter dan angka!"
    elif strength_score >=50 and strength_score < 75:
        final_score = "Passwordnya Diatas rata-rata! Kata sandi kuat tetapi bisa lebih kuat dengan lebih banyak karakter/ digit!"
    else:    
        final_score = "Passwordnya Bagus sekali! Sandi kuat! Ingatlah untuk menyalin dan menyimpan kata sandi Anda di lokasi yang aman"
    
    inputName ="\n" + inputName + "\n adalah kata sandi yang Anda masukkan, dan itu memiliki kekuatan " + str(strength_score) + "! "
    
    return render_template("home.html",myName=inputName,kalimat=final_score)

@app.route('/') 
def home():
    return render_template("home.html",myName="")

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=True)
    