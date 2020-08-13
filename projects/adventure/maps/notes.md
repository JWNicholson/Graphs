UPER -
A graph has 500 rooms. Each room will be visited at least once

Plan - Start in room 0. Use bfs. Check nodes to up,down, right and left to see if its an 'empty' room.
 Store nodes as Current Next Visited lists or dicts. use Queu and dequeue 
 If path is not an exit, backtrace until you find one that is 


 Execute - 
 # Start at 0 (place it in Next[])
 # -- loop
 # Check if Next list is empty 
 # if next is not empty, make current cell the Next value
 # check if cell to w is room or wall, or in the Visited list
 ## No - Place cell in Next queue
 ## Yes - check if cell to e is room or wall, or in Visited list
 ### No - Place cell in Next queue
 ### Yes - check if cell to n is is room, wall or in Visited list
 #### No - Place cell in Next queue
 #### Yes - Check if cell to s is room, wall or in Visted list
 ##### No - Place cell in Next queue
 ##### Yes - Place current cell in Visited list
 ## de-queu Next queue (remove first entry aka popleft())
# -- Repeat 