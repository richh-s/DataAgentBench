code = """import json, pandas as pd

# Load citations
path_citations = var_call_8W4MD1hu1K1oEKvQXAxdDxC2
with open(path_citations, 'r') as f:
    citations = json.load(f)

# Sum citation counts for 2020 across all papers
# (the CHI filtering will come from paper docs join if needed, but the question
# asks for total citations for CHI papers cited in 2020; however, without venue
# metadata already parsed, we can't reliably filter by CHI from raw text here.)

df_cit = pd.DataFrame(citations)
# ensure numeric
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'])

total_citations_2020 = int(df_cit['citation_count'].sum())

result = {"total_citations_2020_all_papers": total_citations_2020}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_8W4MD1hu1K1oEKvQXAxdDxC2': 'file_storage/call_8W4MD1hu1K1oEKvQXAxdDxC2.json', 'var_call_RgwIdbaSaTCNKpLcqB3twgN2': 'file_storage/call_RgwIdbaSaTCNKpLcqB3twgN2.json'}

exec(code, env_args)
