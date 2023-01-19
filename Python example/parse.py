def from_lines(lines : list[str]):
	tree = {}
	def try_add_node(parent, node):
		parent = parent.strip()
		node = node.strip()
		if tree.get(parent):
			if node not in tree[parent]:
				tree[parent].append(node)
		else:
			tree[parent] = [node]

	def add_line(line: str, sep='/'):
		nodes = line.split(sep)
		for i in range(1, len(nodes)):
			try_add_node(nodes[i - 1], nodes[i])

	for line in lines:
		add_line(line)

	return tree

def from_file(file):
	with open(file, 'r', encoding='utf-8') as f:
		tree = from_lines(f.readlines())
	return tree