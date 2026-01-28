code = """import json
import re

funding_path = locals()['var_functions.query_db:5']
civic_docs_path = locals()['var_functions.query_db:8']

f = open(funding_path)
funding_records = json.load(f)
f.close()

c = open(civic_docs_path)
civic_docs = json.load(c)
c.close()

print('Funding count:', len(funding_records))
print('Civic docs count:', len(civic_docs))

first_funding = funding_records[0]
print('First funding record:', first_funding)

first_doc = civic_docs[0]
print('First doc keys:', list(first_doc.keys()))

sample_text = first_doc['text']
print('Sample text length:', len(sample_text))
print('Text start:', sample_text[:300])"""

env_args = {'var_functions.list_db:0': ['civic_docs'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
