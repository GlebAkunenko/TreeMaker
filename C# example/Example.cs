using TreeGraph;

Console.Write("Enter the file name: ");
string file = Console.ReadLine();

Tree tree = TreeParser.FromFile(file);
tree.Print();