code = """import json, pandas as pd

# load citations 2018
path_cit = var_call_vnmIwSY1IigYEg6nNO64Zmuc
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
if df_cit.empty:
    out = {"average_citation_count": None, "paper_count": 0}
else:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

# load filenames
path_files = var_call_aZ8KrJgWhhxjIfDu2jt2i8oh
with open(path_files, 'r', encoding='utf-8') as f:
    files = json.load(f)
df_files = pd.DataFrame(files)
df_files['title'] = df_files['filename'].str.replace(r'\.txt$', '', regex=True)

# determine ACM titles via heuristic using title presence in ACM Digital Library filename patterns not possible;
# instead, extract source by opening docs and searching for publisher markers.

# fetch texts for titles in citations 2018 to minimize.
titles = df_cit['title'].dropna().unique().tolist() if not df_cit.empty else []

# Query mongo for those titles and get text
# We'll chunk titles to avoid query limits

import math

acm_titles = set()
chunk_size = 50
all_docs = []
for i in range(0, len(titles), chunk_size):
    chunk = titles[i:i+chunk_size]
    # Build a mongo query string (handled outside python not possible). So we approximate by using filename list intersection only.
    pass

# Since we cannot call query_db inside python, we fall back: assume all papers in paper_docs are ACM? Not acceptable.

out = {"error":"Need paper source (ACM) per paper; requires querying paper_docs text/metadata. Please provide a structured source field or allow additional MongoDB queries filtered by filenames/titles."}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_vnmIwSY1IigYEg6nNO64Zmuc': 'file_storage/call_vnmIwSY1IigYEg6nNO64Zmuc.json', 'var_call_aZ8KrJgWhhxjIfDu2jt2i8oh': 'file_storage/call_aZ8KrJgWhhxjIfDu2jt2i8oh.json'}

exec(code, env_args)
