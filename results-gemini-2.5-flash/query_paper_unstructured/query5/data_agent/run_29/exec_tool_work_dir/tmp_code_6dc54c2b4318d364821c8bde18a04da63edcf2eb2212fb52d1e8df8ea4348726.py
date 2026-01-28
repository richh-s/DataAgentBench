code = """import json
import pandas as pd

with open(locals()['var_function-call-9866274534013825103'], 'r') as f:
    citation_data = json.load(f)

citation_df = pd.DataFrame(citation_data)
citation_titles = citation_df['title'].tolist()

query_parts = []
for title in citation_titles:
    escaped_title = title.replace("'", "\'").replace(""", "\"") # Escape single and double quotes
    query_parts.append(f"{{\"filename\": \"{escaped_title}.txt\"}}")

# Construct the MongoDB query using $or to match any of the titles
mongo_query = f"{{\"$or\": [{", ".join(query_parts)}]}}"

print("__RESULT__:")
print(json.dumps(mongo_query))"""

env_args = {'var_function-call-9866274534013825103': 'file_storage/function-call-9866274534013825103.json'}

exec(code, env_args)
