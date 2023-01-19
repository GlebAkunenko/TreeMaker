using System.Xml;

namespace TreeGraph;

public class Tree
{
    private Node _root;
    private Dictionary<string, Node> _nodes;

    public Tree(string root)
    {
        _root = new Node(root, null);
        _nodes = new Dictionary<string, Node>();
        _nodes.Add(root, _root);
    }

    private string GetNodeText(Node node, int tabs)
    {
        string space = "";
        for (int i = 0; i < tabs; i++)
            space += "\t";
        string pic;
        if (node.IsRoot)
            pic = "|__ ";
        else
            pic = node.Parent.Children[^1] == node ? "|__ " : "|-- ";
        return space + pic + node.Title;
    }

    private void PrintNode(Node node, int tabs)
    {
        Console.WriteLine(GetNodeText(node, tabs));
        foreach (Node child in node.Children)
            PrintNode(child, tabs + 1);
    }

    public void Print() => PrintNode(_root, 0);

    public void AddNode(string nodeTitle, string parentTitle)
    {
        if (_nodes.ContainsKey(nodeTitle))
            return;
        Node parent = _nodes[parentTitle];
        Node node = new Node(nodeTitle, parent);
        _nodes[nodeTitle] = node;
    }
}
