# # Graph with cycles
# # graph = {
# #     "1": ["2", "3"],
# #     "2": ["1", "5"],
# #     "3": ["1", "5", "7"],
# #     "4": ["5"],
# #     "5": ["2", "3", "4", "6"],
# #     "6": ["5", "7"],
# #     "7": ["3", "6"],
# # }
# # Graph without cycles
# # graph = {
# #     "1": ["2"],
# #     "2": ["5"],
# #     "3": ["1","5"],
# #     "4": ["5"],
# #     "5": ["6"],
# #     "6": ["7"],
# #     "7": ["3"],
# #     "8": ["3","5"]
# # }

# # Input
# # Directed graph with cycles
# graph = {
#     "1": ["2"],
#     "2": ["5"],
#     "3": ["1"],
#     "4": ["5"],
#     "5": ["6"],
#     "6": ["7"],
#     "7": ["3"],
#     "8": ["3", "5"],
# }

# # Directed graph with no cycles
# graph = {
#     "1": ["2"],
#     "2": ["5"],
#     "3": ["1"],
#     "4": ["5"],
#     "5": ["6"],
#     "6": ["7"],
#     "7": [],
#     "8": ["3", "5"],
# }


# # Problem 3: Cycle detection in directed graphs

# trace = []                                      # Holds traversal trace
# visited = dict.fromkeys(dict.keys(graph), False)  # Mark all nodes as unvisited

# # Cycle detection


# def search_cycle(parent, current_node):

#     trace.append(current_node)
#     # Add the node to trace
#     # Mark node as visited on each recursive call
#     visited[current_node] = True

#     # loop over neigbours of the current_node
#     for neighbour_vertex in graph[current_node]:
#         if not visited[neighbour_vertex]:     # explore the node if not visited
#             if search_cycle(current_node, neighbour_vertex):
#                 return True

#         # if the node is visited & in the current trace
#         elif trace.count(neighbour_vertex):
#             trace.append(neighbour_vertex)      # cycle detected
#             return True

#     # Remove the node since it is not part of the cycle
#     trace.pop()
#     return False

# # Method to splice list of nodes forming the cycle


# def fetch_cycle_from_trace():
#     # Latest node in the trace will be the starting point of cycle
#     cycle_origin = trace[-1]
#     # First occurence of the node in the trace
#     origin_index = trace.index(cycle_origin)
#     return trace[origin_index:-1]


# # Driver code
# # Initialize cycle_present to false
# cycle_present = False
# # Loop over all univisited nodes to ensure disconnected graphs are tested
# for node in graph.keys():
#     if search_cycle(None, node):                # Root has no parent hence None
#         cycle_present = True
#         break

# if cycle_present:
#     # Print the trace if cycle found
#     print(fetch_cycle_from_trace())
# else:
#     print("No cycles")


 

