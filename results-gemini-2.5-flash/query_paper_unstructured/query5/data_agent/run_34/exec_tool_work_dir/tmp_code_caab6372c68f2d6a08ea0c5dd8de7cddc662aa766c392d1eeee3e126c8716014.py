code = """import pandas as pd
import json

with open(locals()['var_function-call-8422589621512163175'], 'r') as f:
    citations_2020 = json.load(f)

df_citations = pd.DataFrame(citations_2020)

# Convert citation_count to numeric, handling potential errors
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'], errors='coerce')

# Drop rows where citation_count could not be converted (e.g., if it was not a number)
df_citations.dropna(subset=['citation_count'], inplace=True)

# Prepare titles for MongoDB query
paper_titles = df_citations['title'].tolist()

# MongoDB queries cannot be directly executed in execute_python, so I need to return the list of titles
# and then use a tool for MongoDB query.

print("__RESULT__:")
print(json.dumps(paper_titles))"""

env_args = {'var_function-call-8422589621512163175': 'file_storage/function-call-8422589621512163175.json'}

exec(code, env_args)
