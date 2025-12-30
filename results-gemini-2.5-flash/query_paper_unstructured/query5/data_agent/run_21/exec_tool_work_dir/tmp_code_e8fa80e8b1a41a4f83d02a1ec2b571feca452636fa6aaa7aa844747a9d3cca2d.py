code = """import pandas as pd
import json

with open(locals()['var_function-call-11452238049263839450'], 'r') as f:
    citations_data = json.load(f)

citations_df = pd.DataFrame(citations_data)

# Convert citation_count to numeric, handling potential non-numeric values
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'], errors='coerce').fillna(0)

titles = citations_df['title'].tolist()

# Prepare titles for MongoDB query - escape single quotes
mongo_titles = [title.replace("'", "\\'") for title in titles]

# Create a filter string for MongoDB
filter_str = f'"filename": {{"$in": [{{$concat: ["\\"{t}\\", "\\".txt"]}} for t in {json.dumps(mongo_titles)}]}}'

# Construct the MongoDB query. We need to escape any single quotes in the titles for the $concat operation to work correctly.
# Since we are creating a string that will be part of a JSON string for MongoDB, we need to double escape the single quotes.
mongo_query = f'{{\"collection\": \"paper_docs\", \"filter\": {{{filter_str}}}, \"projection\": {{\"filename\": 1, \"text\": 1}}}}'

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-11452238049263839450': 'file_storage/function-call-11452238049263839450.json'}

exec(code, env_args)
