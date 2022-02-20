from flask import Flask, render_template, redirect, send_file, current_app

app = Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home")


@app.route("/music")
def music():
    return render_template('music.html', title="Music")


@app.route("/capstone")
def capstone():
    return redirect("https://www.youtube.com/watch?v=cSDPUYppi0Q")


@app.route("/resume")
# def resume():
#     return redirect("https://drive.google.com/file/d/1BYSEGBtj_gKo4_ecNEJyKXzusUg2aLI8/view?usp=sharing")
def show_static_pdf():
    return send_file('static/public/tarandeep.pdf', download_name='resume.pdf')
    # with open('src/static/public/tarandeep.pdf', 'rb') as static_file:
    #     return send_file(static_file, attachment_filename='tarandeep.pdf')


# this conditional, when running directly, will start debug mode
if __name__ == '__main__':
    app.run(debug=True)
