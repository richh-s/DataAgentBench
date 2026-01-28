code = """import json
import pandas as pd

# Load results from previous tool calls (file paths or lists)
data_citations = None
path_citations = var_call_qAFlIQ0iEPQORVMX9cyJgnkf
if isinstance(path_citations, str):
    with open(path_citations, 'r', encoding='utf-8') as f:
        data_citations = json.load(f)
else:
    data_citations = path_citations

data_papers = None
path_papers = var_call_yJzhcR47EeY3z9yLF0I1asmz
if isinstance(path_papers, str):
    with open(path_papers, 'r', encoding='utf-8') as f:
        data_papers = json.load(f)
else:
    data_papers = path_papers

# Convert to DataFrames
df_c = pd.DataFrame(data_citations)
# Ensure citation_count is integer
if 'citation_count' in df_c.columns:
    df_c['citation_count'] = pd.to_numeric(df_c['citation_count'], errors='coerce').fillna(0).astype(int)

# Prepare paper titles and detect ACM source
df_p = pd.DataFrame(data_papers)
# Extract title from filename (remove trailing .txt if present)
if 'filename' in df_p.columns:
    df_p['title'] = df_p['filename'].str.replace(r"\.txt$", '', regex=True)
else:
    df_p['title'] = ''

# Detect ACM source by checking presence of 'ACM' or 'Association for Computing Machinery' in text
def is_acm(text):
    if not isinstance(text, str):
        return False
    txt = text.upper()
    return ('ACM' in txt) or ('ASSOCIATION FOR COMPUTING MACHINERY' in txt)

if 'text' in df_p.columns:
    df_p['is_acm'] = df_p['text'].apply(is_acm)
else:
    df_p['is_acm'] = False

# Merge citations with papers on title
merged = pd.merge(df_c, df_p[['title', 'is_acm']], on='title', how='left')
# Filter for ACM papers
acm_rows = merged[merged['is_acm'] == True]

# Compute statistics
if len(acm_rows) == 0:
    result = {'average_citation': None, 'paper_count': 0, 'total_citations': 0}
else:
    total = int(acm_rows['citation_count'].sum())
    count = int(len(acm_rows))
    avg = total / count
    # Round average to 2 decimal places
    result = {'average_citation': round(avg, 2), 'paper_count': count, 'total_citations': total}

# Print result in required format as a JSON string
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_qAFlIQ0iEPQORVMX9cyJgnkf': 'file_storage/call_qAFlIQ0iEPQORVMX9cyJgnkf.json', 'var_call_yJzhcR47EeY3z9yLF0I1asmz': 'file_storage/call_yJzhcR47EeY3z9yLF0I1asmz.json'}

exec(code, env_args)
