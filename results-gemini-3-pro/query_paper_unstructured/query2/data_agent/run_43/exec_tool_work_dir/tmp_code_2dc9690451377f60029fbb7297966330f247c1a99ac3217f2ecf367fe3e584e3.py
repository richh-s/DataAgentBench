code = """import json
import pandas as pd

# Load the citation results
# The previous tool call result is in a file because it was large.
# The key for the citation result was var_function-call-11418660847891976964
with open('var_function-call-11418660847891976964', 'r') as f:
    citations_data = json.load(f)

df_citations = pd.DataFrame(citations_data)
print(f"Number of citation records in 2018: {len(df_citations)}")
print(df_citations.head())

# Prepare list of filenames
filenames = [title + ".txt" for title in df_citations['title'].tolist()]
print(f"Number of unique titles: {len(set(filenames))}")

print("__RESULT__:")
print(json.dumps({"count": len(df_citations), "sample_filename": filenames[0] if filenames else None}))"""

env_args = {'var_function-call-11418660847891976964': 'file_storage/function-call-11418660847891976964.json', 'var_function-call-11418660847891976809': 'file_storage/function-call-11418660847891976809.json'}

exec(code, env_args)
