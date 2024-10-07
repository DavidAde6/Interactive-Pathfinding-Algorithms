from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():

    grid = []
    for i in range(10):
        inner_grid = []
        for j in range(10):
            inner_grid.append([i, j])
        grid.append(inner_grid)

    return render_template('index.html', grid=grid)   

@app.route("/bfs", methods=["POST"])
def bfs():
    if request.method == "POST":
        starting_box = request.form["start1"]
        ending_box = request.form["end1"]
        wall_boxes = request.form["wall1"]

        grid = []
        for i in range(10):
            inner_grid = []
            for j in range(10):
                inner_grid.append([i, j])
            grid.append(inner_grid)

        return render_template('bfs.html', grid=grid)

@app.route("/dfs", methods=["GET", "POST"])
def dfs():
    if request.method == "POST":
        starting_box = request.form["start2"]
        ending_box = request.form["end2"]
        wall_boxes = request.form["wall2"]

        grid = []
        for i in range(10):
            inner_grid = []
            for j in range(10):
                inner_grid.append([i, j])
            grid.append(inner_grid)

        return render_template('dfs.html', grid=grid)

if __name__ == "__main__":
    app.run(debug=True)
    
