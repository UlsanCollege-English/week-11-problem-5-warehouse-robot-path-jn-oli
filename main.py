
## main.py
```python
"""
HW05 — Warehouse Robot Path (Grid BFS)

Implement:
- parse_grid(lines)
- grid_shortest_path(lines)
"""

from collections import deque

def parse_grid(lines):
    """Return (graph, start, target) built from the grid lines.

    Graph keys are "r,c" strings for open cells. Neighbors move 4 directions.
    """
    raise NotImplementedError

def grid_shortest_path(lines):
    """Return a shortest path list of "r,c" from S to T; or None if unreachable."""
    raise NotImplementedError
