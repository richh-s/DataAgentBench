code = """import json
import pandas as pd

# Load citations
with open(locals()['var_function-call-15672313218616885663'], 'r') as f:
    citations_data = json.load(f)
citations_df = pd.DataFrame(citations_data)

# Load paper docs
# The previous query was stored in a file because it was large.
try:
    with open(locals()['var_function-call-11255294213250427348'], 'r') as f:
        papers_data = json.load(f)
except Exception as e:
    papers_data = []
    print(f"Error loading papers: {e}")

print(f"Loaded {len(citations_df)} citation records for 2018.")
print(f"Loaded {len(papers_data)} paper documents.")

# Check title overlap
if len(papers_data) > 0:
    paper_titles = set(p['filename'].replace('.txt', '') for p in papers_data)
    citation_titles = set(citations_df['title'].unique())
    overlap = paper_titles.intersection(citation_titles)
    print(f"Number of overlapping titles: {len(overlap)}")
    
print("__RESULT__:")
print(json.dumps({"citations_count": len(citations_df), "papers_count": len(papers_data)}))"""

env_args = {'var_function-call-15672313218616885663': 'file_storage/function-call-15672313218616885663.json', 'var_function-call-15672313218616887976': 'file_storage/function-call-15672313218616887976.json', 'var_function-call-11255294213250427348': 'file_storage/function-call-11255294213250427348.json'}

exec(code, env_args)
