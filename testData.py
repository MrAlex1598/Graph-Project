# dijkstra
demo = {1: [(2, 10), (3, 3), (5, 6)],
        2: [(1, 0)],
        3: [(2, 4), (5, 2)],
        4: [(3, 4), (5, 3)],
        5: [(2, 0), (6, 1)],
        6: [(1, 2), (2, 1)]}

# quadruplet (destination, (min, max, cost))
flots = {
    "S1": [("S2", (0, 2, 1)), ("T1", (0, 3, 1))],
    "S2": [("T1", (0, 2, 1)), ("T2", (0, 1, 1)), ("T3", (0, 1, 1))],
    "S3": [("S2", (0, 2, 1)), ("T3", (0, 3, 1))],
    "T1": [("T2", (0, 2, 1)), ("T4", (0, 7, 1))],
    "T2": [("T4", (0, 2, 1)), ("T5", (0, 1.5, 1))],
    "T3": [("T2", (0, 3, 1)), ("T5", (0, 1, 1))],
    "T4": [("R", (0, 8, 1))],
    "T5": [("R", (0, 4, 1))],
    "E": [("S1", (0, 5, 1)), ("S2", (0, 4, 1)), ("S3", (0, 3, 1))],
    "R": []
}


flotsCours = {
    1: [(2,2),(4,6)],
    2: [(3,-2)],
    3: [(2,5), (4, 5)],
    4: [(1,-4), (2, -1)]
}