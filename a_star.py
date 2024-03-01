#
# Code written by Jingwen Feng 02/28/2024. All rights reserved.
#
import time
from typing import List

class PancakeStack:
    def __init__(self, stack: List[int], g=0, action=None, parent=None):
        self.stack = stack
        self.parent = parent
        self.action = action
        self.g = g

    def flip(self, i: int) -> 'PancakeStack':
        new_stack = self.stack[:i] + self.stack[i:][::-1]
        #print('flip:' + str(new_stack))
        return PancakeStack(new_stack, self.g + 1, i, self)

    def is_goal(self) -> bool:
        return self.stack == sorted(self.stack, reverse=True)

    def __repr__(self):
        return f"{self.stack} (g={self.g})"

class AStar:
    def __init__(self, initial_stack: List[int]):
        self.initial_stack = initial_stack
        self.solution_actions = []
        self.solution_steps = []
        self.execution_time = 0
        self.space_used = 0

    def heuristic(self, stack: List[int]) -> int:
        sum = 0
        for i in range(1, len(stack)):
            if stack[i] > stack[i - 1]:
                sum += 1
        return sum


    def find_lowest_f_score_node(self, nodes):
        lowest_node = min(nodes, key=lambda x: x.g + self.heuristic(x.stack))
        nodes.remove(lowest_node)
        return lowest_node

    def search(self):
        start_time = time.time()
        nodes = [PancakeStack(self.initial_stack)]
        explored = set()
        while nodes:
            current_node = self.find_lowest_f_score_node(nodes)
            #print('check 1')
            #print(current_node)\
            #self.reconstruct_path(current_node)


            if current_node.is_goal():
                #print("a")
                self.execution_time = time.time() - start_time
                self.reconstruct_path(current_node)
                self.space_used = len(explored) + len(nodes)
                self.solution_actions.append('END')
                return
            else:
                #print(" check b")
                explored.add(tuple(current_node.stack))

                for i in range(0, len(current_node.stack) - 1):
                    child = current_node.flip(i)
                    child_tuple = tuple(child.stack)

                    #print(child.stack)

                    if child_tuple not in explored and child not in nodes:
                       # print('check point')
                        nodes.append(child)
                    if child.is_goal():
                        self.reconstruct_path(child)
                        # print("c")
                        self.execution_time = time.time() - start_time
                        # self.reconstruct_path(current_node)
                        self.space_used = len(explored) + len(nodes)
                        self.solution_actions.append('END')
                        return





        self.execution_time = time.time() - start_time
        self.space_used = len(explored) + len(nodes)

    def reconstruct_path(self, node: PancakeStack):
        if node.action is None:
            return
        else:
            # print(str(node.action) + ':' + str(node.stack))
            path = []
            while node:
                path.append(node.stack)
                self.solution_actions.append(f'a_{node.action}')
                node = node.parent

            path.reverse()
            self.solution_actions.reverse()
            self.solution_steps = path

    def solution(self):
        return self.solution_actions

    def steps(self):
        return self.solution_steps

    def time(self):
        return self.execution_time

    def space(self):
        return self.space_used
