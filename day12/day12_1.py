cave_system = {}

with open("caves.txt", "r") as raw_map:
    lines = [line.strip() for line in raw_map.readlines()]


for line in lines:
    node = tuple(line.split("-"))
    reverse_node = tuple(reversed(node))

    bidirectional_node = [node] + [reverse_node]

    for nodes in bidirectional_node:
        if nodes[0] not in cave_system.keys():
            cave_system[nodes[0]] = {nodes[1]: 1}
        else:
            cave_system[nodes[0]].update({nodes[1]: 1})


def find_all_paths(caves, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in caves:
        return []
    paths = []
    for node in caves[start]:
        #    if node not in path:
        if (node.islower() and node not in path) or node.isupper():
            newpaths = find_all_paths(caves, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths


all_paths = find_all_paths(cave_system, "start", "end")

print(f"All available paths are: {len(all_paths)}")
