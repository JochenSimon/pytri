with open("Pytri2/pytriontology.py", "w") as f:
  f.write("\n")

from Pytri2.ontology import ontologize

with open("Pytri2/pytriontology.pto") as o, open("Pytri2/pytriontology.py", "w") as p:
  p.write("from time import sleep\nfrom .ontology import Concept\nfrom .utils import renamekey, flood\n\n")
  p.write(ontologize(o.read()))
