from __future__ import annotations
from collections import deque
from dataclasses import dataclass
from pathlib import Path
import time
import matplotlib.pyplot as plt


# INPUT_FILE = Path(SCRIPT_DIR, "input/sample_input.txt")
INPUT_FILE = '12.txt'

@dataclass(frozen=True)
class Point():
    """ Point class, which knows how to return a list of all adjacent coordinates """    
    x: int
    y: int
    
    def neighbours(self) -> list[Point]:
        """ Return all adjacent orthogonal (not diagonal) Points """
        return [Point(self.x+dx, self.y+dy) for dx in range(-1, 2)
                                            for dy in range(-1, 2)
                                            if abs(dy) != abs(dx)]

class Grid():
    """ 2D grid of point values. """
       
    def __init__(self, grid_array: list[str]) -> None:
        """ Generate Grid instance from 2D array. 
        This works on a deep copy of the input data, so as not to mutate the input. """                                         
        self.array = grid_array  # Store a deep copy of input data
        self.x_size = len(self.array[0])
        self.y_size = len(self.array)
        self.start = self._get_point_for_elevation("S")
        self.goal = self._get_point_for_elevation("E")
        
    def _all_points(self) -> list[Point]:
        points = [Point(x, y) for x in range(self.x_size) for y in range(self.y_size)]
        return points
    
    def all_lowest_elevation_points(self) -> set[Point]:
        low_points = {point for point in self._all_points() 
                        if self.array[point.y][point.x] == "a"
                        or self.array[point.y][point.x] == "S"}
        return low_points
    
    def _get_point_for_elevation(self, x: str) -> Point:
        assert x in ("S", "E"), "Specified point must be Start or End!"
        for row_num, row in enumerate(self.array):
            if x in row:
                return Point(row.index(x), row_num)
    
    def elevation_at_point(self, point: Point) -> int:
        if point not in (self.start, self.goal):
            return ord(self.array[point.y][point.x])
        
        if point == self.start:
            return ord("a")

        if point == self.goal:
            return ord("z")
    
    def _point_in_grid(self, point: Point) -> bool:
        if (0 <= point.x < self.x_size and 0 <= point.y < self.y_size):
            return True
        
        return False
    
    def _valid_neighbours(self, location:Point):
        current_elevation = self.elevation_at_point(location)
        
        for neighbour in location.neighbours():
            if self._point_in_grid(neighbour):
                if self.elevation_at_point(neighbour) <= current_elevation + 1:
                    yield neighbour

    def get_breadcrumbs(self, end: Point) -> dict[Point, Point]:
        points_to_assess: deque[Point] = deque()
        points_to_assess.append(end)

        came_from = {}
        came_from[end] = None
        
        # BFS with no goal
        while points_to_assess:     # They should only ever be valid points
            current = points_to_assess.popleft()
            
            for neighbour in self._valid_neighbours(current):
                if neighbour not in came_from:   # We will need to assess this point
                    points_to_assess.append(neighbour)
                    came_from[neighbour] = current
        
        return came_from
    
    @staticmethod
    def create_path(breadcrumbs: dict[Point, Point], start: Point, goal: Point):
        path = []
        current = goal
        while current != start: 
            path.append(current)
            if current in breadcrumbs:
                current = breadcrumbs[current]
            else:
                return None
            
        return path

    def __repr__(self) -> str:
        return "\n".join("".join(map(str, row)) for row in self.array)     

def main():
    with open(INPUT_FILE, mode="rt") as f:
        data = f.read().splitlines()
        
    grid = Grid(data)
    breadcrumbs = grid.get_breadcrumbs(grid.start)
    
    # Part 1
    path = grid.create_path(breadcrumbs, grid.start, grid.goal)
    
    print(f"Part 1: {len(path)}")
    render_as_plt(grid, path)
    
    # Part 2  
    best_path = path
    for goal in grid.all_lowest_elevation_points():
        if goal in breadcrumbs:
            path = grid.create_path(breadcrumbs, goal, grid.goal)
            if path:
                if len(path) < len(best_path):
                    best_path = path
    
    print(f"Part 2: {(len(best_path)-1)}")
    render_as_plt(grid, best_path)

        
def render_as_plt(grid, path):
    
    x_vals = [point.x for point in grid._all_points()]
    y_vals = [point.y for point in grid._all_points()]
    
    path_x = [point.x for point in path]
    path_y = [point.y for point in path]
    
    axes = plt.gca()
    axes.set_aspect('equal')
    axes.set_xlim(min(x_vals)-1, max(x_vals)+1)
    axes.set_ylim(min(y_vals)-1, max(y_vals)+1)
    #axes.invert_yaxis()
    
    axes.scatter(x_vals, y_vals, marker="o", s=5, color="grey")
    axes.scatter(path_x, path_y, marker="o", s=5, color="red")
    plt.show()

if __name__ == "__main__":
    t1 = time.perf_counter()
    main()
    t2 = time.perf_counter()
    print(f"Execution time: {t2 - t1:0.4f} seconds")
