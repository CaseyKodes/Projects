import maze

class Game():
    '''Holds the game solving logic. Initialize with a fully initialized maze'''
    def __init__(self, maze):
        self._maze = maze

    # Creating simple methods (like the next two) to abstract core parts 
    #   of your algorithm helps increase the readability of your code.
    #   You will find these two useful in your solution.

    def _is_move_available(self, row, col, path):
        '''If (row, col) is already in the solved path then it is not available'''
        '''and (row, col) can not be a wall'''
        return (row, col) not in path

    def _is_puzzle_solved(self, row, col):
        '''Is the given row,col the finish square?'''
        return self._maze.get_finish() == (row, col)

    ########################################################
    # TODO - Main recursive method. Add your algorithm here.
    def find_route(self, currow, curcol, curscore = 0, curpath = None):

        # only used to be able to call the function with less in the pass area
        if curpath is None: 
            curpath = list
        
        # initalizing max path and score to be written over
        maxscore = -1
        maxpath = []

        # base case if position is at finish 
        if self._is_puzzle_solved(currow, curcol): 
            return (curscore, curpath)

        # when at the start adds the statr position to the path 
        # does not change curscore becasue the value at the start position is 0
        if self._maze.get_start() not in curpath:
            curscore =  self._maze.make_move(currow, curcol, curpath)

        # a value for each move, up,down,left,right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        for d in directions: #iterate through all possible moves
            temp_path = curpath.copy() # creates a copy of the path 

            # checks if ove is in bounds, if move lands on a wall, or if move lands on a position already in path
            if self._is_move_available(currow+d[0], curcol+d[1], temp_path) and self._maze.is_move_in_maze(currow+d[0], curcol+d[1]) and not self._maze.is_wall(currow+d[0], curcol+d[1]):
                newscore = curscore + self._maze.make_move(currow+d[0], curcol+d[1], temp_path) # adds value at new position to score, and updates path
                score, newpath = self.find_route(currow+d[0], curcol+d[1], newscore, temp_path) 

                if score > maxscore: # write over maxscore and path when a higher scoring path is obtained
                    maxscore = score
                    maxpath = newpath

        return maxscore, maxpath

# This block of code will be useful in debugging your algorithm. But you still need
#  to create unittests to thoroughly testing your code.
if __name__ == '__main__':
    # Here is how you create the maze. Pass the row,col size of the grid.
    grid = maze.Maze(4, 4)
    # You have TWO options for initializing the Value and Walls squares.
    # (1) init_random() and add_random_walls()
    #     * Useful when developing your algorithm without having to create 
    #         different grids
    #     * But not easy to use in testcases because you cannot preditably
    #         know what the winning score and path will be each run
    # (2) _set_maze()
    #     * You have to create the grid manually, but very useful in testing
    #       (Please see the test_game.py file for an example of _set_maze())
    grid.init_random(0,9) # Initialze to a random board
    grid.add_random_walls(0.5)   # Make a certian percentage of the maze contain walls

    # AFTER you have used one of the two above methods of initializing 
    #   the Values and Walls, you must set the Start Finish locations. 
    start = (0,2)
    finish = (1,1)
    grid.set_start_finish(start, finish)

    '''grid._set_maze([["*", 1,  "*",  1,  1],
                    [2,   5,  "*", "*", 2],
                    [3,  "*", "*", "*", 8],
                    [9,  "*",  4,   7,  3],
                    [1,   3,   1,  "*", 2]])
    start = (0,1)
    grid.set_start_finish(start, (0,3))'''

    # Printing the starting grid for reference will help you in debugging.
    print(grid)           # Print the maze for visual starting reference

    # Now instatiate your Game algorithm class
    game = Game(grid)     # Pass in the fully initialize maze grid

    # Now initiate your recursize solution to solve the game!
    # Start from the start row, col... zero score and empty winning path
    score, path = game.find_route(start[0], start[1], 0, list())
    print(f"The winning score is {score} with a path of {path}")
