code = """import json, re, pandas as pd

# Load the query results from storage variables
# var_call_yMAunKb2cQZXazIL6wVfLjBh -> citations query result (likely a filepath)
# var_call_80GrJsga5vXRK5IGMNMUJAVt -> paper_docs query result (likely a filepath)

def load_var(v):
    if isinstance(v, str):
        # assume it's a filepath to a json file
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return v

citations = load_var(var_call_yMAunKb2cQZXazIL6wVfLjBh)
papers = load_var(var_call_80GrJsga5vXRK5IGMNMUJAVt)

# Create dataframes
cdf = pd.DataFrame(citations)
# ensure citation_count numeric
if not cdf.empty:
    cdf['citation_count'] = cdf['citation_count'].astype(int)

pdf = pd.DataFrame(papers)
# extract title from filename
pdf['title'] = pdf['filename'].str.replace(r"\.txt$", '', regex=True)

# Function to detect CHI venue in text
chi_patterns = [r"CHI\s*'", r"Proceedings of the SIGCHI", r"Annual Conference on Human Factors in Computing Systems", r"ACM CHI", r"CHI: '", r"\bSIGCHI\b"]

def is_chi(text):
    if not isinstance(text, str):
        return False
    header = text[:1200]  # look in first part of the document
    for p in chi_patterns:
        if re.search(p, header, flags=re.IGNORECASE):
            return True
    return False

pdf['is_chi'] = pdf['text'].apply(is_chi)

# Merge citations with papers on title
merged = pd.merge(cdf, pdf[['title','is_chi']], on='title', how='left')

# Filter to those that are CHI
chi_cited = merged[merged['is_chi'] == True]

total_citations = int(chi_cited['citation_count'].sum())
num_papers = int(chi_cited.shape[0])

result = {"total_citations_2020_chi": total_citations, "num_papers_cited_in_2020": num_papers}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_yMAunKb2cQZXazIL6wVfLjBh': 'file_storage/call_yMAunKb2cQZXazIL6wVfLjBh.json', 'var_call_80GrJsga5vXRK5IGMNMUJAVt': 'file_storage/call_80GrJsga5vXRK5IGMNMUJAVt.json'}

exec(code, env_args)
