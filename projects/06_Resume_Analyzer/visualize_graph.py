from graph import graph

png_data = graph.get_graph().draw_mermaid_png()

with open("resume_graph.png", "wb") as f:
    f.write(png_data)

print("Graph saved as resume_graph.png")