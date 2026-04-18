from pylode import OntDoc, MakeDocco, APP_DIR
import os
from os.path import join, dirname, abspath


TESTS_DIR = dirname(abspath(__file__))
ONTOLOGY_DIR = join(TESTS_DIR)
os.chdir(ONTOLOGY_DIR)
print(ONTOLOGY_DIR)
print(join(ONTOLOGY_DIR, "BrIO.ttl"))
#od=OntDoc(default_language="en",source_info=input_rdf, g=input_rdf)
h = MakeDocco(input_data_file=join(ONTOLOGY_DIR, "BrIO.ttl"))
# generate the HTML doc
h.document(destination=join(ONTOLOGY_DIR, "index.html"))

