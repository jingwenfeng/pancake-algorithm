#
# Code written by Jingwen Feng 02/28/2024. All rights reserved.
#
from flask import Flask, render_template, request, redirect, url_for
from a_star import AStar
from ucs import UCS

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('description.html')

@app.route('/simulate', methods=['GET', 'POST'])
def simulate():
    if request.method == 'POST':
        stack_input = request.form.get('stack')
        if stack_input:
            try:
                initial_stack = [int(x) for x in stack_input.split() if x.isdigit()]
                if len(initial_stack) <= 1:
                    raise ValueError("Input must contain more than one number.")
            except ValueError as e:
                return render_template('input.html', error=str(e))
        else:

            initial_stack = [10, 9, 8, 7, 6, 5, 4, 1, 3, 2]

        return redirect(url_for('results', stack=",".join(map(str, initial_stack))))
    return render_template('input.html')

@app.route('/results')
def results():
    stack_query = request.args.get('stack', '10,9,8,7,6,5,4,1,3,2')
    initial_stack = [int(x) for x in stack_query.split(',')]

    astar_solver = AStar(initial_stack)
    astar_solver.search()

    ucs_solver = UCS(initial_stack)
    ucs_solver.search()

    return render_template('results.html',
                           initial_stack=initial_stack,
                           astar_solution=astar_solver.solution(),
                           astar_steps=astar_solver.steps(),
                           astar_time=astar_solver.time(),
                           astar_space=astar_solver.space(),
                           ucs_solution=ucs_solver.solution(),
                           ucs_steps=ucs_solver.steps(),
                           ucs_time=ucs_solver.time(),
                           ucs_space=ucs_solver.space())

if __name__ == '__main__':
    app.run(debug=True)
