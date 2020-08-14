
def earliest_ancestor(ancestors, starting_node):
    #.................((1,3), 10)
    #dict to hold node families
    node_fam = dict()
 
    #check ancestors parameter,  
    for older in ancestors:
        if older[1] not in node_fam:#looking for dupe node ids(keys)
            print(f"older[0]: ", older[0])
            print(f"older[1]", older[1])
            # if not in node_fam add it as first position,
            node_fam[older[1]] = [older[0]]

            print(f"new older[1]", older[1])
           
            print(f"current dict state: ", node_fam)
            print(f"xxxxxxxxxxxxxxxxxxxxxxxx")
            
        else:
            node_fam[older[1]].append(older[0])

            print(f"appended", older[0])
            print(f"appended dict state: ", node_fam)
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~")

    print(f"node_fam : ", node_fam) 

    # if starting node has no family, return -1 (exit)
    if starting_node not in node_fam:
        return -1
    
    # set the current_gen equal to the parent dict at the starting node
    current_gen = node_fam[starting_node]

    

     #iterate through the  in the current generation and add them to the new generation array and then compare it to the current generation (equal to the starting node of the family dict)
    while True:
        new_gen = []
        for older in current_gen:
            if older in node_fam:
                new_gen = new_gen + node_fam[older]
        
        if len(new_gen) == 0:
            return current_gen[0]
        else:
            current_gen = new_gen

       




    #input data comes from graph of parent>child relationships through multiple generations
    #check input node pairs against neighbors for parents
    # if no parents, return -1
    #otherwise, if older than current oldest, make current oldest THE oldest generation


    #dictionary (or maybe a list and cache) of ancestors

   

    #if the starting node has no family - exit

    

    
   