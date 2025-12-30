code = """import json
import pandas as pd

# Load the citation data from the file
with open(locals()['var_function-call-2735270006984904089'], 'r') as f:
    citation_data = json.load(f)

df_citations = pd.DataFrame(citation_data)
df_citations['citation_count'] = pd.to_numeric(df_citations['citation_count'])

paper_titles = df_citations['title'].tolist()

# The next step will query MongoDB for paper venues. I need to print the titles to be used in the next step to avoid exceeding context window limits.
print("__RESULT__:")
print(json.dumps(paper_titles))"""

env_args = {'var_function-call-2735270006984904089': 'file_storage/function-call-2735270006984904089.json'}

exec(code, env_args)
