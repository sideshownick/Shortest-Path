# Shortest-Path
Shortest path routing algorithm.

Reads a file of link data for a distance weighted network and prints the shortest path between any two nodes as a list of intersections.

Based on [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm), as used in Python [NetworkX shortest path function](https://networkx.github.io/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.shortest_path.html#networkx.algorithms.shortest_paths.generic.shortest_path).

## Example Usage (and output):
To calculate shortest route between nodes `J1025` and `X1039` given the input file `exmouth-links.dat`:
```bash
  > python exmouth-links.dat J1025 X1039
  J1025
  J1017
  J1020
  J1021
  J1029
  J1033
  J1034
  J1035
  J1036
  J1038
  X1039
```
Calculation of slowest case tested took `0.0025s` on a Intel® Core™ i7-7500U CPU @ 2.70GHz × 4 with 7.7 GiB RAM running 64-bit Ubuntu 18.04.2 LTS.

## Input file format:
```
startNode  		endNode  		distance
A          		B        		2
B          		C        		4
```
* Note that header line should **not** be used
### Example file contents:
```
J1001 J1002 72
J1001 J1026 795
J1001 J1031 28
J1002 J1001 72
J1002 J1019 161
J1002 J1030 242
J1003 J1011 189
J1003 J1012 593
J1003 J1021 639
...
```
## Requirements
Tested with Python 2.7 or Python 3.

## Test Cases
1. Path between two nodes, time command
```bash
> time python shortest.py exmouth-links.dat J1053 J1037
```
#### Output:
```bash
J1053
J1035
J1036
J1037

real	0m0.030s
user	0m0.019s
sys	0m0.011s
```
2. No path exists
```bash 
> python shortest.py exmouth-links.dat J1001 N1000
```
#### Output:
```bash
No Route Found
```
3. Incorrect key given
```bash
> python shortest.py exmouth-links.dat N1000 N1002

Destination N1002 key not found
```
4. Origin same as destination:
```bash
> python shortest.py exmouth-links.dat J1001 J1001

Origin J1001 same as destination J1001
```
