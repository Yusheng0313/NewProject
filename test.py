import pygraphviz as pgv

G = pgv.AGraph(directed=True, strict=False, ranksep=0.2, splines="spline", concentrate=True)

# 设置节点标签
nodeA = "Police\nIntelligence"
nodeB = "Police Station"
nodeC = "Criminal Action"
nodeD = "Incidents"
nodeE = "Police Dockets"
nodeF = "Control Room\nAwareness"
nodeG = "Patroller Information"
nodeH = "Patroller Awareness"


# 添加节点
G.add_nodes_from([nodeA, nodeB, nodeC, nodeD, nodeE, nodeF, nodeG, nodeH],
                 color="#ffffff", fontname="times bold italic")

# 添加边
G.add_edges_from([[nodeA, nodeB], [nodeA, nodeF], [nodeB, nodeC], [nodeC, nodeD],
                  [nodeC, nodeG], [nodeD, nodeE], [nodeD, nodeG], [nodeE, nodeA],
                  [nodeF, nodeA], [nodeF, nodeG], [nodeF, nodeH], [nodeG, nodeF],
                  [nodeH, nodeG]], color="#7F01FF", arrowsize=0.8)

# 导出图形
G.layout()
G.draw("因果关系图.png", prog="dot")


