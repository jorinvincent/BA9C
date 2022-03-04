
class Node:
    def __init__(self, text, children):
        self.parent = text
        self.children = children

def addNewSuffix(suffix):
    i = 0
    n = 0
    while (i < len(suffix)):
        j = 0
        m = 0
        clen = 0
        char = suffix[i]

        while (True):
            carr = nodes[n].children

            if clen == len(carr):
                m = len(nodes)
                nodes.append(Node(suffix[i:], []))
                nodes[n].children.append(m)

                return

            m = carr[clen]

            if (nodes[m].parent[0] == char):
                break

            clen += 1

        suffixcont = nodes[m].parent

        while (j < len(suffixcont)):
            if (suffix[i + j] != suffixcont[j]):
                temp = m
                m = len(nodes)
                nodes.append(Node(suffixcont[:j], [temp]))
                nodes[temp].parent = suffixcont[j:]
                nodes[n].children[clen] = m

                break
            j += 1

        i += j
        n = m



reader = open("input", "r")
writer = open("output", "w")

textlist = reader.readlines()
text = ""

for i in range(0, len(textlist)):
    text = text + textlist[i].strip()



nodes = [Node("", [])]
for s in range(0, len(text)):
    suffix = text[s:]
    addNewSuffix(suffix)

for l in range (2, len(nodes) - 1):
    writer.write(nodes[l].parent)
    writer.write("\n")
writer.write(nodes[len(nodes)- 1].parent)



reader.close()
writer.close()
