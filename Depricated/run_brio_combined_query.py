from rdflib import Graph
import pandas as pd
from caas_jupyter_tools import display_dataframe_to_user

ontology_path = "/mnt/data/BrIO_ontology.owl"
instance_path = "/mnt/data/brio_example_case_corrected.ttl"
query_path = "/mnt/data/brio_competency_questions_combined.rq"

g = Graph()
g.parse(ontology_path, format="turtle")
g.parse(instance_path, format="turtle")

with open(query_path, "r", encoding="utf-8") as f:
    sparql = f.read()

rows = []
for row in g.query(sparql):
    rows.append({str(var): (None if val is None else str(val)) for var, val in row.asdict().items()})

df = pd.DataFrame(rows)
display_dataframe_to_user("Combined competency-question result", df)

print("Combined graph size:", len(g), "triples")
print("Rows returned:", len(df))
print("\nSPARQL query used:\n")
print(sparql)
