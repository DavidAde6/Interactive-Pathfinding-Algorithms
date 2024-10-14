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
    # All the variables gotten from user
    if request.method == "POST":
        starting_box = request.form["start1"]
        ending_box = request.form["end1"]
        wall_boxes = request.form["wall1"]

        # The grid, each with matching coordinates
        grid = []
        for i in range(10):
            inner_grid = []
            for j in range(10):
                inner_grid.append([i, j])
            grid.append(inner_grid)

        # converting the starting and ending box into lists
        start = [int(starting_box[1]), int(starting_box[4])]
        end = [int(ending_box[1]), int(ending_box[4])]
        explored = []
        wall = []
        
        # formats and adds the values in wall_boxes to explored
        temp = [] # stores temporary boxes in wall
        for i in range(len(wall_boxes)):
            if wall_boxes[i] == "[":
                temp.append(int(wall_boxes[i+1]))
            if wall_boxes[i] == "]":
                temp.append(int(wall_boxes[i-1]))
                explored.append(temp)
                wall.append(temp)
                temp = []
        
        # ok, we have wall, start and end.
        # Create a node, that keeps track of parent node
        class Node:

            def __init__(self, state, parent, action):
                self.state = state
                self.parent = parent
                self.action = action

        class StackFrontier():
            def __init__(self):
                self.frontier = []

            def display(self):
                return self.frontier

            def add(self, node):
                self.frontier.append(node)

            def return_state(self):
                result = []
                for i in self.frontier:
                    result.append(i.state)
                return result

            def empty(self):
                return len(self.frontier) == 0

            def remove(self):
                if self.empty():
                    print("Empty Frontier")
                else:
                    node = self.frontier[0]
                    self.frontier = self.frontier[1:]
                    return node

        #actual code, lets cook

        # Checks for available actions

        def action(s): # takes in node.state, returns list
            result = []
            nearby = [[s[0] - 1, s[1]], [s[0] + 1, s[1]], [s[0], s[1] - 1], [s[0], s[1] + 1]]
            for state in nearby:
                if state[0] >= 0 and state[0] <= 9 and state[1] >= 0 and state[1] <= 9:
                    if state not in explored:
                        result.append(state)
            return result

            
        start_node = Node(start, [], action(start))
        frontier = StackFrontier()
        frontier.add(start_node)

        while True:
            
            if frontier.empty():
                path = ["No solution"]
                break
            
            node = frontier.remove()
            #print(explored[:10])

            if node.state == end:
                path = []
                while node.parent != []:
                    path.append(node.state)
                    node = node.parent
                path.reverse()
                break

            else:
                #print("This runs")
                if node.state not in explored:
                    explored.append(node.state)

                for state in node.action:
                    child = Node(state, node, action(state))
                    #print("State = ", child.state, "Parent = ", child.parent, "Action = ", child.action)
                    if state not in frontier.return_state():
                        frontier.add(child)
                    
        print(path)

        return render_template('bfs.html', grid=grid, path=path, start=start, end=end, wall=wall)

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

        # converting the starting and ending box into lists
        start = [int(starting_box[1]), int(starting_box[4])]
        end = [int(ending_box[1]), int(ending_box[4])]
        explored = []
        wall = []
        
        # formats and adds the values in wall_boxes to explored
        temp = [] # stores temporary boxes in wall
        for i in range(len(wall_boxes)):
            if wall_boxes[i] == "[":
                temp.append(int(wall_boxes[i+1]))
            if wall_boxes[i] == "]":
                temp.append(int(wall_boxes[i-1]))
                explored.append(temp)
                wall.append(temp)
                temp = []
        
        # ok, we have wall, start and end.
        # Create a node, that keeps track of parent node
        class Node:

            def __init__(self, state, parent, action):
                self.state = state
                self.parent = parent
                self.action = action

        class StackFrontier():
            def __init__(self):
                self.frontier = []

            def display(self):
                return self.frontier

            def add(self, node):
                self.frontier.append(node)

            def return_state(self):
                result = []
                for i in self.frontier:
                    result.append(i.state)
                return result

            def empty(self):
                return len(self.frontier) == 0

            def remove(self):
                if self.empty():
                    print("Empty Frontier")
                else:
                    node = self.frontier[-1]
                    self.frontier.pop()
                    return node

        #actual code, lets cook

        # Checks for available actions

        def action(s): # takes in node.state, returns list
            result = []
            nearby = [[s[0] - 1, s[1]], [s[0] + 1, s[1]], [s[0], s[1] - 1], [s[0], s[1] + 1]]
            for state in nearby:
                if state[0] >= 0 and state[0] <= 9 and state[1] >= 0 and state[1] <= 9:
                    if state not in explored:
                        result.append(state)
            return result

            
        start_node = Node(start, [], action(start))
        frontier = StackFrontier()
        frontier.add(start_node)

        while True:
            
            if frontier.empty():
                path = ["No solution"]
                break
            
            node = frontier.remove()
            #print(explored[:10])

            if node.state == end:
                path = []
                while node.parent != []:
                    path.append(node.state)
                    node = node.parent
                path.reverse()
                break

            else:
                #print("This runs")
                if node.state not in explored:
                    explored.append(node.state)

                for state in node.action:
                    child = Node(state, node, action(state))
                    #print("State = ", child.state, "Parent = ", child.parent, "Action = ", child.action)
                    if state not in frontier.return_state():
                        frontier.add(child)
                    
        print(path)

        return render_template('dfs.html', grid=grid, path=path, start=start, end=end, wall=wall)

if __name__ == "__main__":
    app.run(debug=True)
    
