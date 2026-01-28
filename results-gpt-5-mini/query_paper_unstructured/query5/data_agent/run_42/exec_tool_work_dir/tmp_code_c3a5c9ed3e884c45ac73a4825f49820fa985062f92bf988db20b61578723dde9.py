code = """import json
import re
import pandas as pd

# Load the query results from storage paths provided by previous tool calls
with open(var_call_wUhxLxFcVguqIU7X1OUE1nAP, 'r', encoding='utf-8') as f:
    citations = json.load(f)
with open(var_call_bLpC6T6gFnPJTLEqwOqSEsjz, 'r', encoding='utf-8') as f:
    paper_docs = json.load(f)

# Build DataFrames
df_citations = pd.DataFrame(citations)
# Ensure citation_count is int
if not df_citations.empty:
    df_citations['citation_count'] = df_citations['citation_count'].astype(int)

df_papers = pd.DataFrame(paper_docs)
# Extract title from filename by removing trailing .txt
df_papers['title'] = df_papers['filename'].str.replace(r"\.txt$", '', regex=True)

# Function to detect if a paper was presented at CHI by inspecting header
chi_patterns = [r"\bCHI\b", r"Proceedings of the SIGCHI Conference", r"SIGCHI Conference", r"ACM CHI"]

def is_chi_paper(text):
    if not isinstance(text, str):
        return False
    header = text[:1500]  # check the beginning of the paper for venue info
    header_upper = header.upper()
    # Look for explicit CHI patterns
    for pat in chi_patterns:
        if re.search(pat, header, flags=re.IGNORECASE):
            return True
    # Some CHI papers include the ACM conference formatting with 'CHI' and year like "CHI '15"
    if re.search(r"CHI\s*'\d{2}", header_upper):
        return True
    if re.search(r"CHI\s*\d{4}", header_upper):
        return True
    return False

# Apply detection
df_papers['is_chi'] = df_papers['text'].apply(is_chi_paper)

# Filter CHI papers
df_chi_papers = df_papers[df_papers['is_chi']].copy()

# Join with citations on title
# Some citation titles may have leading/trailing whitespace
df_citations['title'] = df_citations['title'].str.strip()
df_chi_papers['title'] = df_chi_papers['title'].str.strip()

merged = pd.merge(df_chi_papers[['title']], df_citations, on='title', how='inner')

# Compute total citation count
if merged.empty:
    total_citations = 0
else:
    total_citations = int(merged['citation_count'].sum())

# Prepare per-paper list
papers_list = merged[['title', 'citation_count']].to_dict(orient='records')

result = {
    'total_citations_2020_for_CHI_papers': total_citations,
    'num_papers_counted': len(papers_list),
    'papers': papers_list
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_wUhxLxFcVguqIU7X1OUE1nAP': 'file_storage/call_wUhxLxFcVguqIU7X1OUE1nAP.json', 'var_call_bLpC6T6gFnPJTLEqwOqSEsjz': 'file_storage/call_bLpC6T6gFnPJTLEqwOqSEsjz.json'}

exec(code, env_args)
