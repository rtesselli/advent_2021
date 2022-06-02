from typing import List, Dict, Text, Set, Tuple
from collections import defaultdict


def parse():
    with open('data/input_12.txt', 'r') as f:
        lines = f.readlines()
    graph = defaultdict(list)
    for line in lines:
        left, right = line.split('-')
        left = left.strip()
        right = right.strip()
        graph[left].append(right)
        graph[right].append(left)
    return graph


def add_step(paths: List[List[Text]], node: Text) -> List[List[Text]]:
    return list(map(lambda path: path + [node], paths))


def to_visit(node: Text, visited: Set[Text]) -> bool:
    return (node.islower() and node not in visited) or node.isupper()


def find_paths(graph: Dict):
    def find_recursive(curr_node: Text, paths: List[List[Text]], visited: Set[Text]) -> List[List[Text]]:
        if curr_node == 'end':
            return add_step(paths, curr_node)
        if all(not to_visit(neighbor, visited) for neighbor in graph[curr_node]):
            return []
        all_new_paths = []
        for neighbor in graph[curr_node]:
            if to_visit(neighbor, visited):
                all_new_paths.extend(find_recursive(neighbor, add_step(paths, curr_node), visited | {curr_node}))
        return all_new_paths

    return find_recursive('start', [[]], set())


def find_paths2(graph: Dict):
    def add_step(paths: Set[Tuple[Text]], node: Text) -> Set[Tuple[Text]]:
        return set(map(lambda path: path + (node,), paths))

    def find_recursive(curr_node: Text, paths: Set[Tuple[Text]], visited: Set[Text],
                       used_double: bool) -> Set[Tuple[Text]]:
        if curr_node == 'end':
            return add_step(paths, curr_node)
        if all(not to_visit(neighbor, visited) for neighbor in graph[curr_node]):
            return set()
        all_new_paths = set()
        for neighbor in graph[curr_node]:
            if to_visit(neighbor, visited):
                all_new_paths = all_new_paths.union(
                    find_recursive(neighbor, add_step(paths, curr_node), visited | {curr_node}, used_double))
                if not used_double and curr_node.islower() and curr_node not in {'start', 'end'}:
                    all_new_paths = all_new_paths.union(
                        find_recursive(neighbor, add_step(paths, curr_node), visited, True))
        return all_new_paths

    return find_recursive('start', {tuple()}, set(), False)


def main():
    graph = parse()
    paths = find_paths(graph)
    print(len(paths))
    paths = find_paths2(graph)
    print(len(paths))


if __name__ == '__main__':
    main()
