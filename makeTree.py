class Tree:
	def __init__(self, root):
		self.root = root
		self.tree: dict[str, list[str]] = {root: []}
		self.nodes = []

	def try_add_node(self, parent, node):
		if node in self.nodes:
			return
		if self.tree.get(parent):
			if node not in self.tree[parent]:
				self.tree[parent].append(node)
		else:
			if parent not in self.nodes:
				self.tree[self.root].append(parent)
				self.nodes.append(parent)
			self.tree[parent] = [node]
		self.nodes.append(node)

	def add_branch(self, line: str, sep='/'):
		nodes = line.split(sep)
		for i in range(1, len(nodes)):
			self.try_add_node(nodes[i - 1], nodes[i])

	def remove_node(self, node: str):
		if self.tree.get(node):
			del self.tree[node]
		for t in self.tree:
			if node in self.tree[t]:
				self.tree[t].remove(node)

	def __print_node(self, node, isLast = False, tabs=0):
		space = "\t" * tabs
		pic = ("|-- ", "|__ ")[isLast]
		print(space + pic + node)
		if self.tree.get(node):
			for child in self.tree[node]:
				self.__print_node(child, child == self.tree[node][-1], tabs+1)

	def print(self):
		self.__print_node(self.root, True, 0)

	def __to_lines(self, node: str, tail: str, result: list):
		if self.tree.get(node):
			for child in self.tree[node]:
				self.__to_lines(child, tail+'/'+node, result)
		else:
			result.append(tail+'/'+node)

	def to_lines(self):
		lines = []
		for node in self.tree[root]:
			self.__to_lines(node, root, lines)
		return "\n".join(lines)

	def save(self, file):
		with open(file, 'w', encoding='utf-8') as f:
			f.write(self.to_lines())

	@staticmethod
	def open(file):
		lines = []
		root = ""
		with open(file, 'r', encoding='utf-8') as f:
			lines = f.readlines()
		result = Tree(lines[0].split('/')[0])
		for line in lines:
			result.add_branch(line.strip())
		return result



class Command:
	def __init__(self, title: str, func, args_count):
		self.function = func
		self.title = title
		self.args_count = args_count

	def check(self, text: str):
		return text.lower().startswith(self.title)

	def execute(self, tree, args: list):
		if len(args) != self.args_count:
			print(f"Command '{self.title}' takes {self.args_count} parameters")
			return
		self.function(tree, args)

commands = [
	Command("add node", lambda tree, args: tree.try_add_node(args[0], args[1]), 2),
	Command("remove node", lambda tree, args: tree.remove_node(args[0]), 1),
	Command("print", lambda tree, args: tree.print(), 0),
	Command("show", lambda tree, args: tree.print(), 0),
	Command("save", lambda tree, args: tree.save(args[0]), 1)
]

new = input("Create new tree? (y/n)\n")
tree = None
while new.lower() != 'y' and new.lower() != 'n':
	new = input("Create new tree? y/n")
if new.lower() == 'y':
	root = input("A root name: ")
	tree = Tree(root)
if new.lower() == 'n':
	tree = Tree.open(input("Enter the filename: "))

command = ""
while True:
	command = input()
	if command.lower() == "exit":
		exit(0)
	if command.lower() == 'help':
		print("add <par>: <node1>, <node2>...\n"+
			  "add node    - create new node according to the node name and the parent name\n"+
			  "remove node - remove the node according to the node name\n"+
			  "show        - print the tree\n"+
			  "save        - save the tree to the file")
		continue
	if command.lower().startswith('add'):
		command = command.replace('add', '').strip()
		if command.count(':') != 1:
			print("Syntax error")
			continue
		parent, nodes = map(lambda s: s.strip(), command.split(':'))
		nodes = list(map(lambda s: s.strip(), nodes.split(',')))
		for n in nodes:
			tree.try_add_node(parent, n)
		continue
	for com in commands:
		if com.check(command):
			args = command.replace(com.title, '').strip().split(' ')
			if command.lower() == com.title:
				args = []
			com.execute(tree, args)
			break
	else:
		print("Unknow command. Enter 'help' to see the list")