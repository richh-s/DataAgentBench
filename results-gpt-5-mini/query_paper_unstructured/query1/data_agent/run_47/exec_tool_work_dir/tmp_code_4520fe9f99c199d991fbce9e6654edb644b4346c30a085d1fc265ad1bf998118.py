code = """import json
import pandas as pd

# Load data from storage-provided file paths
with open(var_call_LXXRrV0t6etZNqMXBE56GHFi, 'r', encoding='utf-8') as f:
    papers = json.load(f)
with open(var_call_iwUacCdu76q59LpcAtwE4qqN, 'r', encoding='utf-8') as f:
    citations = json.load(f)

# Create DataFrames
df_papers = pd.DataFrame(papers)
# Extract title from filename by removing trailing .txt
if 'filename' in df_papers.columns:
    df_papers['title'] = df_papers['filename'].str.replace(r"\.txt$", '', regex=True)
else:
    df_papers['title'] = None

# Lowercase text for searching
df_papers['text_low'] = df_papers['text'].str.lower().fillna('')

# Determine which papers are in the 'food' domain by substring match
# Use word boundary to match 'food' as a word, but also match occurrences like 'food,' 'food.'
food_mask = df_papers['text_low'].str.contains(r'\bfood\b') | df_papers['title'].str.lower().str.contains(r'\bfood\b', na=False)
food_titles = set(df_papers.loc[food_mask, 'title'].tolist())

# Load citations into DataFrame
df_cit = pd.DataFrame(citations)
# Ensure citation_count is integer
# Some records may have non-numeric or null; coerce errors to 0
if 'citation_count' in df_cit.columns:
    df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce').fillna(0).astype(int)
else:
    df_cit['citation_count'] = 0

# Filter citation records for titles in food_titles
df_food_cit = df_cit[df_cit['title'].isin(food_titles)]

# Sum total citations
total_citations = int(df_food_cit['citation_count'].sum())

# Prepare result as JSON-serializable string (just the integer)
import json
result_str = json.dumps({"domain": "food", "total_citation_count": total_citations})

print("__RESULT__:")
print(result_str)"""

env_args = {'var_call_A8Bu88kLTnXwnw5v3fbmcpMV': ['paper_docs'], 'var_call_LXXRrV0t6etZNqMXBE56GHFi': 'file_storage/call_LXXRrV0t6etZNqMXBE56GHFi.json', 'var_call_iwUacCdu76q59LpcAtwE4qqN': 'file_storage/call_iwUacCdu76q59LpcAtwE4qqN.json'}

exec(code, env_args)
