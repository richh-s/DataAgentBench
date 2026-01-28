code = """import json, re, pandas as pd

def load_records(obj):
    if isinstance(obj, str) and obj.endswith('.json'):
        with open(obj, 'r', encoding='utf-8') as f:
            return json.load(f)
    return obj

cit2020 = load_records(var_call_gHdyYv8nDCX66JueEv8pApKV)
docs = load_records(var_call_TN6wQ2rOLjmqxP2vq28WhaBv)

# Build set of titles cited in 2020
cit_df = pd.DataFrame(cit2020)
cit_df['citation_count'] = pd.to_numeric(cit_df['citation_count'], errors='coerce').fillna(0).astype(int)

# Extract likely venue from text (first ~5000 chars) using patterns
venue_patterns = [
    (re.compile(r"\bCHI\s*'\d{2}\b", re.IGNORECASE), 'CHI'),
    (re.compile(r"\bCHI\s*\d{4}\b", re.IGNORECASE), 'CHI'),
    (re.compile(r"\bSIGCHI\b", re.IGNORECASE), 'CHI'),
    (re.compile(r"\bACM\s+CHI\b", re.IGNORECASE), 'CHI'),
]

def is_chi(text):
    if not text:
        return False
    head = text[:6000]
    # Exclude obvious other venues like UbiComp unless CHI explicitly appears as venue marker
    for pat, v in venue_patterns:
        if pat.search(head):
            return True
    # sometimes citation line: "Proceedings of the SIGCHI Conference on Human Factors in Computing Systems"
    if re.search(r"Proceedings of the SIGCHI Conference on Human Factors in Computing Systems", head, re.IGNORECASE):
        return True
    return False

chi_titles = []
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    if is_chi(d.get('text','')):
        chi_titles.append(title)

chi_set = set(chi_titles)

chi_cit_df = cit_df[cit_df['title'].isin(chi_set)].copy()

total = int(chi_cit_df['citation_count'].sum())

# Also provide breakdown by paper
breakdown = chi_cit_df.sort_values(['citation_count','title'], ascending=[False, True])
records = breakdown.to_dict(orient='records')

out = {
    "total_citation_count_2020_for_CHI_papers": total,
    "num_CHI_papers_cited_in_2020": int(breakdown.shape[0]),
    "per_paper_citation_counts_2020": records
}
print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_gHdyYv8nDCX66JueEv8pApKV': 'file_storage/call_gHdyYv8nDCX66JueEv8pApKV.json', 'var_call_dWo31i4OuVARm8e5SY9WeYbY': 'file_storage/call_dWo31i4OuVARm8e5SY9WeYbY.json', 'var_call_TN6wQ2rOLjmqxP2vq28WhaBv': 'file_storage/call_TN6wQ2rOLjmqxP2vq28WhaBv.json'}

exec(code, env_args)
