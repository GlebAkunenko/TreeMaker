namespace TreeGraph;

public static class TreeParser
{
    const char separator = '/';

    public static Tree FromLines(string[] lines)
    {
        string root = lines[0].Split(separator)[0].Trim();
        Tree tree = new Tree(root);

        foreach(string line in lines) {
            string[] nodes = line.Split(separator);
            for (int i = 1; i < nodes.Length; i++)
                tree.AddNode(nodes[i].Trim(), nodes[i - 1].Trim());
        }

        return tree;
    }

    public static Tree FromFile(string fileName)
    {
        return FromLines(File.ReadAllLines(fileName));
    }
}
