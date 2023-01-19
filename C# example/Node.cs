namespace TreeGraph;

public class Node
{
    public string Title { get; init; }
    public Node Parent { get; init; }

    public List<Node> Children { get; init; }

    public bool IsLeaf => Children.Count == 0;

    public bool IsRoot => Parent == null;

    public Node(string title, Node parent)
    {
        Title = title;
        Children = new List<Node>();
        Parent = parent;
        if (!IsRoot)
            parent.Children.Add(this);
    }
}