from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

# set direction possibles
facing_directions = {"e": "w", "w":"e", "n": "s", "s": "n"}
# set Player starting room
starting_room = player.current_room
# dictionary to track visited rooms
visited = {}
# list for storing reverse directions
reversed_direction = []
# set initial graph with starting room
current_room = starting_room

# Find un-explored direction
def move_quest(current_room):
		curr_room = current_room.id
		room_exits = visited[curr_room]

    # Check all coordinates and return a direction not yet evaluated
		for direction in room_exits:
			if room_exits[direction] == '?' and current_room.get_room_in_direction(direction).id not in visited:
				return direction
		return None
# Check for unexplored rooms exits
def search_unexplored_exits():
    while True:
        back_direction = reversed_direction.pop()
        traversal_path.append(back_direction)
        player.travel(back_direction)
        next_room = player.current_room

     # Find any "?" exits in room. If found, return it
        if '?' in visited[next_room.id].values():
            return next_room

#set up initial traversl graph
if current_room.id not in visited:
    curr_exits = current_room.get_exits()

    #track un visited exits with a dict
    exits ={}
    for xt in curr_exits:
        exits[xt] ="?"
        visited[current_room.id] = exits

while len(visited) < len(world.rooms):
    # next direction
    next_direction = move_quest(current_room)
    # Check if at a dead-end. If yes, look for exits = ?
    if next_direction is None:
        # look for valid exits by backtracking
        new_room = search_unexplored_exits()
        current_room = new_room

    else:
        # Add direction to the path and move into the next room
        player.travel(next_direction)
        traversal_path.append(next_direction)

        # Track reverse direction so we can backtrack if needed
        reversed_direction.append(facing_directions[next_direction])
        previous_room = current_room
        # set current room to the new room
        current_room = player.current_room

    # Update visted dict
    new_exits = {}
    for xt in current_room.get_exits():
        new_exits[xt] = "?"
        visited[current_room.id] = new_exits

        #set previous direction to the new room
        visited[previous_room.id][next_direction] = current_room.id

        # set the new room direction
        visited[previous_room.id][next_direction] = current_room.id
       

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
