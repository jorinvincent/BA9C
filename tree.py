
class Node:
    def __init__(self, text, children):
        self.parent = text
        self.children = children



reader = open("input", "r")
writer = open("output", "w")

textlist = reader.readlines()
text = ""

for i in range(0, len(textlist)):
    text = text + textlist[i].strip()

nodes = [Node("", [])]
for s in range(0, len(text)):
    suffix = text[s:]

for l in range (2, len(nodes) - 1):
    writer.write(nodes[l].parent)
    writer.write("\n")
writer.write(nodes[len(nodes)- 1].parent)

reader.close()
writer.close()
