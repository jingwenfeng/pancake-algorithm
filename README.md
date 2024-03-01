
#
# Code written by Jingwen Feng 02/28/2024. All rights reserved.
#
1. Searching Problem

State Space S:

The set of all possible arrangements of the pancakes. Each state
s is a permutation of the stack [p1, p2, p3 ... p10]. pi is the size of ith pancake from top. 

Intial State S0:

The original disordered list (permutation) of pancakes. For example:
[3, 6, 7, 2, 5, 4, 9, 10, 1, 8]

Action A: 

The set of action A = [a1, a2, a3 ... a9], where ai is the action that inserted under ith pancake in the stack and used to flip all pancakes above it.
(a10 is just flipping the whole set, so I only set to a9).

Transition Function T: 

T(s,a) -> s' returns new stack (new permutation) of pancakes
Goal s*: permutation [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

Cost Function g(i): 

g(i) = total flips from initial state to state i.



2. Possible Cost Function (Backward Cost)

Ci = total flips from initial state to state i.
If from initial state to state i has actions [ai], 1<i<k
Ci = k


3. Possible Heuristic Function (Forward Cost)

h(n) = Number of pancakes that are not in the correct descending order, ignoring the bottom pancake if it's correctly placed.


4. Coding:

For UCS, f(n) = g(n)
For A*; f(n) = g(n) + h(n)

How to use the code:
In terminal, enter main.py
Do you want to input your own pancake stack? YES/NO:
if YES, enter own set such as '1 2 3 4 5 6 7 8 9 10'
if NO, use default set.
The result show:
A*: solution set, steps, time and space
ucs: solution set, steps, time and space

For set [1 3 5 2 4 6]:

A* 
running time: 0.011997461318969727

Space: 531

UCS:
running Time: 0.010999917984008789

Space: 1278


For set [1 3 4 2]:

A* 
running time:  0.0

Space: 25


UCS:
running Time:  0.0

Space: 17



Coding 2:
Use the webpage:
In terminal run:
pip install flask
then run:
app2.py
click on the http://
enter the set and get result
To exist, enter [Control C]