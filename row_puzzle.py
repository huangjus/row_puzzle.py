# Author: Justin Huang
# GitHub username: huangjus
# Date: 5/9/23
# Description: The function takes a row list and two optional parameters: current_index (defaults to 0) and visited
# (defaults to an empty set), to avoid cycles. It checks three base cases: returns False if current_index is out of
# bounds or has already been visited, returns True if the current_index's value is zero. Otherwise, it adds
# current_index to visited set and makes two recursive calls, one to the right (current_index + row[current_index])
# and one to the left (current_index - row[current_index]). It returns True if either of these recursive calls
# returns True.

def row_puzzle(row, current_index=0, visited=None):
    """
    Check if a given row puzzle is solvable.

    A row puzzle is a list of non-negative integers with a zero in the rightmost square.
    The function starts with a token on the leftmost square, and on each turn, the token can shift
    left or right a number of squares exactly equal to the value in its current square, but is not allowed
    to move off either end. The goal is to get the token to the rightmost square.
    """
    if visited is None:
        visited = set()
    if current_index < 0 or current_index >= len(row) or current_index in visited:
        return False
    if row[current_index] == 0:
        return True
    visited.add(current_index)
    return row_puzzle(row, current_index + row[current_index], visited) \
           or row_puzzle(row, current_index - row[current_index], visited)
