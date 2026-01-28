code = """import json
import pandas as pd

# Load variables from storage
with open(var_call_4EFqrNYfrs8yFpChOBcDWvsl, 'r', encoding='utf-8') as f:
    data_citations = json.load(f)
with open(var_call_2yhsNBZQnu2ffxQCZqh7e4hH, 'r', encoding='utf-8') as f:
    data_papers = json.load(f)

# DataFrames
df_cit = pd.DataFrame(data_citations)
df_p = pd.DataFrame(data_papers)

# Samples
cit_titles_sample = df_cit['title'].head(50).tolist()
file_names_sample = df_p['filename'].head(50).tolist()

# Check exact intersection of titles (without .txt)
df_p['title'] = df_p['filename'].str.replace(r"\.txt$", '', regex=True)
intersection = set(df_cit['title']).intersection(set(df_p['title']))

# Check CHI occurrence in texts (case-insensitive, word boundary)
df_p['text'] = df_p['text'].fillna('')
df_p['chi_match'] = df_p['text'].str.contains(r"\bCHI\b", case=False, regex=True)
chi_titles = df_p[df_p['chi_match']]['title'].head(50).tolist()
num_chi = int(df_p['chi_match'].sum())
num_papers = int(len(df_p))
num_citations = int(len(df_cit))
num_intersection = int(len(intersection))

result = {
    'num_papers_in_mongo': num_papers,
    'num_citation_records_2020': num_citations,
    'num_titles_intersection': num_intersection,
    'intersection_sample': list(intersection)[:30],
    'num_chi_detected_in_texts': num_chi,
    'chi_titles_sample': chi_titles[:30],
    'cit_titles_sample_first_50': cit_titles_sample,
    'file_names_sample_first_50': file_names_sample
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_4EFqrNYfrs8yFpChOBcDWvsl': 'file_storage/call_4EFqrNYfrs8yFpChOBcDWvsl.json', 'var_call_JJ4mKnI7jt2F0rjjoG3g96oU': ['paper_docs'], 'var_call_2yhsNBZQnu2ffxQCZqh7e4hH': 'file_storage/call_2yhsNBZQnu2ffxQCZqh7e4hH.json', 'var_call_CyA4TwHOpP9WArQOHRRwUJJa': {'total_citations': 0, 'num_papers': 0}}

exec(code, env_args)
