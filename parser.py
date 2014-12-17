class Node(object):
    def __init__(self):
        self.regex = None
        self.prim_value = None
        self.left = None
        self.right = None
        self.child = None
    def __str__(self):
        if self.regex == None:
            return "None"
        elif self.regex == "prim":
            return "prim(\"" + self.prim_value + "\")"
        elif self.regex == "seq" or self.regex == "alt":
            return self.regex + "(" + str(self.left) + ", " + str(self.right) + ")"
        else:
            return self.regex + "(" + str(self.child) + ")"

def parse(tokens, trail_prim = ""):
    node = Node()
    i = len(tokens) - 1
    
    #check if there is a trailing prim, concatenate onto existing stack or return collected prims
    if not is_rep_mod(tokens[i]) and tokens[i] != ")" and in_alt_node(i, tokens) < 0:
        trail_prim = tokens[i] + trail_prim
        if i == 0:
            node.regex = "prim"
            node.prim_value = trail_prim
        else:
            node = parse(tokens[:i], trail_prim)
    
    #add trailing prim back on if it exists
    elif trail_prim != "":
        prim = Node()
        prim.regex = "prim"
        prim.prim_value = trail_prim
        node.regex = "seq"
        node.left = parse(tokens)
        node.right = prim

    #redundant parenthesis
    elif tokens[i] == ")" and front(i, tokens) == 0:
        node = parse(tokens[1:i])

    #standalone rep mod
    elif front(i, tokens) == 0:
        node.regex = rep_str[tokens[i]]
        node.child = parse(tokens[:i])

    #seq
    elif in_alt_node(i, tokens) < 0:
        split = front(i, tokens)
        node.regex = "seq"
        node.left = parse(tokens[:split])
        node.right = parse(tokens[split:])

    #with alts
    else:
        alt = Node()
        alt.regex = "alt"
        i_left = in_alt_node(i, tokens)
        start = first_alt(i, tokens)
        alt.right = parse(tokens[i_left + 2:])
        alt.left = parse(tokens[start:i_left+1])

        if start == 0:
            node = alt
        else:
            node.regex = "seq"
            node.left = parse(tokens[:start])
            node.right = alt
    return node

#dict of repetition symbol string names
rep_str = {"*":"kleene", "+":"plus", "?":"ques"}

#given index of closing parens, returns matching open parens index
def matching_open(i, seq):
    count = 1
    while count != 0:
        i -= 1
        if seq[i] == ")":
            count += 1
        elif seq[i] == "(":
            count -= 1
    return i

#given character, determines if it is either *, +, or ?
def is_rep_mod(token):
    return token == "*" or token == "+" or token == "?"

#given end of grouping, returns index of beginning of grouping
def front(i, seq):
    offset = 0
    if is_rep_mod(seq[i]):
        offset = 1
    i -= offset
    if seq[i] == ")":
        count = 1
        while count != 0:
            i -= 1
            if seq[i] == ")":
                count += 1
            elif seq[i] == "(":
                count -= 1
        return i
    return i

#given index and sequence, returns index of other side of alt or 0
def in_alt_node(i, seq):
    i = front(i, seq)
    if seq[i - 1] == "|":
        return i - 2
    else:
        return -1

#given index to right side of alt, returns index of beginning of whole alt chain
def first_alt(i, seq):
    i = in_alt_node(i, seq)
    while True:
        if in_alt_node(i, seq) < 0:
            break
        else:
            i = in_alt_node(i, seq)
    return front(i, seq)
