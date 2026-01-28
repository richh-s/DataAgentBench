code = """import json, re
with open(var_call_UCPD1RS4AZvlswJyAis5URH1, 'r') as f:
    univ_rows = json.load(f)
with open(var_call_TXF5iLgHVwuGHi0geYBudpqL, 'r') as f:
    citing_rows = json.load(f)

pubnum_pattern = re.compile(r"\b[A-Z]{2}-[A-Z0-9\-]+\b")

univ_pubnums = set()
for r in univ_rows[:200]:
    text = r.get('Patents_info','')
    for m in pubnum_pattern.findall(text):
        if re.search(r"\d", m):
            univ_pubnums.add(m.strip())

# collect some cited pubnums from citing_rows
cited_pubnums = set()
count=0
for r in citing_rows[:200]:
    citation_field = r.get('citation')
    try:
        citations = json.loads(citation_field) if isinstance(citation_field, str) else citation_field
    except:
        citations = []
    for c in citations:
        if isinstance(c, dict) and c.get('publication_number'):
            cited_pubnums.add(c.get('publication_number').strip())

sample_univ = sorted(list(univ_pubnums))[:20]
sample_cited = sorted(list(cited_pubnums))[:20]

out = {'num_univ_rows': len(univ_rows), 'num_citing_rows': len(citing_rows), 'num_univ_pubnums': len(univ_pubnums), 'num_cited_pubnums': len(cited_pubnums), 'sample_univ': sample_univ, 'sample_cited': sample_cited}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_JmtpD4VJGFoecQO8VCX0zY1M': 'file_storage/call_JmtpD4VJGFoecQO8VCX0zY1M.json', 'var_call_UCPD1RS4AZvlswJyAis5URH1': 'file_storage/call_UCPD1RS4AZvlswJyAis5URH1.json', 'var_call_TXF5iLgHVwuGHi0geYBudpqL': 'file_storage/call_TXF5iLgHVwuGHi0geYBudpqL.json', 'var_call_2Md769yXdot8j6FoexQHqNUj': {'mappings': [], 'unique_primary_cpcs': []}}

exec(code, env_args)
