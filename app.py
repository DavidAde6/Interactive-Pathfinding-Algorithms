from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    grid = []
    for i in range(10):
        inner_grid = []
        for j in range(10):
            inner_grid.append([i, j])
        grid.append(inner_grid)

    return render_template('index.html', grid=grid)

if __name__ == "__main__":
    app.run(debug=True)
    
