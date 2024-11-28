import argparse
from itertools import permutations
import math
from draw import draw_path
from test import test_path

class password():
    def __init__(self, rule):
        self.rule = rule
        # Longest distance
        self.longest_length = 0.0
        # List of longest path. The longest path is not unique. 
        self.longest_path = []
        # Your code goes here:

    # Find the longest path
    def find_longest_path(self):
        # Your code goes here:
        vertex_dictionary = {'1': (0, 0), '2': (1, 0), '3': (2, 0),
                             '4': (0, 1), '5': (1, 1), '6': (2, 1),
                             '7': (0, 2), '8': (1, 2), '9': (2, 2)}
        invalid_paths = [[['7', '9'], '8'], [['4', '6'], '5'], [['1', '3'], '2'], [['7', '1'], '4'],
                                  [['8', '2'], '5'], [['9', '3'], '6'], [['7', '3'], '5'], [['9', '1'], '5']]
        possible_passwords = permutations('123456789')

        if self.rule == 1:
            for possible_password in possible_passwords: #try all possible combos
                valid = True
                distance = 0.0

                for i in range(len(possible_password)-1): #checking all points against rule 1
                    point1 = possible_password[i]
                    point2 = possible_password[i+1]

                    for j in range(len(possible_password)):
                        point3 = possible_password[j]

                        if [[point1, point2], point3] in invalid_paths or [[point2, point1], point3] in invalid_paths:
                            valid = False
                            break

                    if not valid:
                        break

                    distance += self.distance(vertex_dictionary[possible_password[i]], vertex_dictionary[possible_password[i+1]])
                if valid:
                    if distance > self.longest_length:
                        self.longest_length = distance
                        self.longest_path = [''.join(possible_password)]
                    elif distance == self.longest_length:
                        self.longest_path.append(''.join(possible_password))
        elif self.rule == 2:
            for possible_password in possible_passwords: #try all possible combos
                valid = True
                distance = 0.0

                for i in range(len(possible_password)-1): #checking all points against rule 1
                    point1 = possible_password[i]
                    point2 = possible_password[i+1]

                    for j in range(i+2, len(possible_password)):
                        point3 = possible_password[j]

                        if [[point1, point2], point3] in invalid_paths or [[point2, point1], point3] in invalid_paths:
                            valid = False
                            break

                    if not valid:
                        break

                    distance += self.distance(vertex_dictionary[possible_password[i]], vertex_dictionary[possible_password[i+1]])
                if valid:
                    if distance > self.longest_length:
                        self.longest_length = distance
                        self.longest_path = [''.join(possible_password)]
                    elif distance == self.longest_length:
                        self.longest_path.append(''.join(possible_password))

    # Calculate distance between two vertices
    # Format of a coordinate is a tuple (x_value, y_value), for example, (1,2), (0,1)
    def distance(self, vertex1, vertex2):
        return math.sqrt((vertex1[0]-vertex2[0])**2 + (vertex1[1]-vertex2[1])**2)

    # Print and save the result
    def print_result(self):
        print("The longest length using rule " + str(self.rule) + " is:")
        print(self.longest_length)
        print()
        print("All paths with longest length using rule " + str(self.rule) + " are:") 
        print(self.longest_path)
        print()
        with open('results_rule'+str(self.rule)+'.txt', 'w') as file_handler:
            file_handler.write("{}\n".format(self.longest_length)) 
            for path in self.longest_path:
                file_handler.write("{}\n".format(path)) 

    # test the result 
    def test(self):
        test_path(self.longest_length, self.longest_path, self.rule)

    # draw first result
    def draw(self):
        if len(self.longest_path) > 0:
            draw_path(self.longest_path[0], self.rule)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='PatternLock')
    parser.add_argument('-rule', dest='rule', required = True, type = int, help='Index of the rule')
    args = parser.parse_args()

    # usage
    # python PatternLock.py -rule 1
    # python PatternLock.py -rule 2
    
    # Initialize the object using rule 1 or rule 2
    run = password(args.rule)
    # Find the longest path
    run.find_longest_path()
    # Print and save the result
    run.print_result()
    # Draw the first longest path
    run.draw()
    # Verify the result 
    run.test()