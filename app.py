from flask import Flask, render_template, request

import numpy as np
import cv2

app = Flask(__name__)

def convertToHtml(result):
    html = """
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    </head>

    <body>
        <div class="container">
           """+result+"""
        </div>


    <script src="https://code.jquery.com/jquery-3.6.3.min.js" integrity="sha256-pvPw+upLPUjgMXY0G+8O0xUf+/Im1MZjXxxgOcBQBXU=" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>

    </body>

    </html>"""
    return html

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST","GET"])
def upload():
    result = ""
    items = []
    if request.method == "POST":
        f = request.files["image"]
        # save with rename file
        imgName = "static/"+ "input.jpg"
        f.save(imgName)
        img = cv2.imread(imgName)

        # blur image
        imgBlur = cv2.GaussianBlur(img, (5, 5), 0)
        cv2.imwrite("static/blur.jpg", imgBlur)
        items.append(["Blur", "static/blur.jpg"])

        # change color
        imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
        cv2.imwrite("static/gray.jpg", imgGray)
        items.append(["Gray", "static/gray.jpg"])

        # edge detection
        imgCanny = cv2.Canny(imgGray, 100, 100)
        cv2.imwrite("static/canny.jpg", imgCanny)
        items.append(["Canny", "static/canny.jpg"])

        result += "<table id='resulttbl' class='table table-striped table-bordered' style='width:100%'>"
        result += "<thead>"
        result += "<tr>"
        result += "<th>Keterangan</th>"
        result += "<th>Gambar</th>"
        result += "</thead>"
        result += "<tbody>"
        for item in items:
            result += "<tr>"
            result += "<td>"+item[0]+"</td>"
            result += "<td><img src='"+item[1]+"' width='200px' height='200px'></td>"
            result += "</tr>"

        result += "</tbody>"
        result += "</table>"

        f = open('templates/result.html', 'w') 
        f.write(convertToHtml(result))

        f.close()
        return render_template("result.html")
    if request.method == "GET":
        return render_template("result.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
