code = """import pandas as pd
import json

with open(locals()['var_function-call-11452238049263839450'], 'r') as f:
    citations_data = json.load(f)

citations_df = pd.DataFrame(citations_data)

# Convert citation_count to numeric, handling potential non-numeric values
citations_df['citation_count'] = pd.to_numeric(citations_df['citation_count'], errors='coerce').fillna(0)

titles = citations_df['title'].tolist()

# Prepare filenames for MongoDB query
mongo_filenames = [f'{title}.txt' for title in titles]

# Create a filter string for MongoDB
filter_str = json.dumps({"filename": {"$in": mongo_filenames}})

# Construct the MongoDB query
mongo_query = f'{{\"collection\": \"paper_docs\", \"filter\": {filter_str}, \"projection\": {{\"filename\": 1, \"text\": 1}}}}'

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-11452238049263839450': 'file_storage/function-call-11452238049263839450.json'}

exec(code, env_args)
