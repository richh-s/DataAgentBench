code = """import json, re
import pandas as pd

path_cit = var_call_Nh0LOFojiFpjyp2IjCPbo5KC
with open(path_cit, 'r', encoding='utf-8') as f:
    cit = json.load(f)
df_cit = pd.DataFrame(cit)
df_cit['citation_count'] = pd.to_numeric(df_cit['citation_count'], errors='coerce')

path_docs = var_call_TkYOofvKk22cgej8ZEtqRcll
with open(path_docs, 'r', encoding='utf-8') as f:
    docs = json.load(f)

def extract_title(fn):
    return re.sub(r'\\.txt$', '', fn)

acm_titles = set()
acm_re = re.compile(r'Copyright\\s+\\d{4}[^\\n]{0,120}\\bACM\\b', re.IGNORECASE)
acm_re2 = re.compile(r'\\bAssociation for Computing Machinery\\b', re.IGNORECASE)

for d in docs:
    text = d.get('text', '') or ''
    if acm_re.search(text) or acm_re2.search(text) or re.search(r'\\bACM\\b', text[:2000], re.IGNORECASE):
        acm_titles.add(extract_title(d.get('filename', '')))

mask = df_cit['title'].isin(acm_titles)
df = df_cit[mask].copy()
avg = float(df['citation_count'].mean()) if len(df) else None
out = {'avg_citation_count': avg, 'acm_papers_count': int(len(df)), 'citation_year': 2018}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_KL8S1BsrEEMTR29oNTBVv4bQ': ['Citations', 'sqlite_sequence'], 'var_call_DMVpawmrN7zgfSjIN8h2iatQ': [{'avg_citations_2018_acm': 'None'}], 'var_call_Nh0LOFojiFpjyp2IjCPbo5KC': 'file_storage/call_Nh0LOFojiFpjyp2IjCPbo5KC.json', 'var_call_QyixNi5FcMSx1KTlpBJSllsE': ['paper_docs'], 'var_call_jfouyfNjXeclY647piUbuW2N': 'file_storage/call_jfouyfNjXeclY647piUbuW2N.json', 'var_call_TkYOofvKk22cgej8ZEtqRcll': 'file_storage/call_TkYOofvKk22cgej8ZEtqRcll.json'}

exec(code, env_args)
