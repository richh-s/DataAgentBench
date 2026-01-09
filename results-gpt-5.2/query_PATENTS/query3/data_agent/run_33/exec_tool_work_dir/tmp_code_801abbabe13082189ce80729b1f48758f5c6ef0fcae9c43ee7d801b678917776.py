code = """import json, re

obj = var_call_ExZhvZ0JkwRvzm2ygYfUgMTL
pis=[h['Patents_info'] for h in obj['sample_hits']]

def parse_assignee(pi:str):
    patterns=[
        r'^(.+?)\s+holds\b',
        r'^The\s+US\s+patent\s+filing\s+\(.*?\)\s+is\s+assigned\s+to\s+(.+?)\s+and\s+has\b',
        r'^The\s+US\s+patent\s+application\s+\(.*?\)\s+is\s+held\s+by\s+(.+?)\s+and\s+has\b',
        r'^The\s+US\s+application\s+\(.*?\)\s+is\s+owned\s+by\s+(.+?)\s+and\s+has\b',
    ]
    for pat in patterns:
        m=re.search(pat, pi)
        if m:
            return m.group(1).strip()
    return None

out=[{'pi':pi, 'assignee':parse_assignee(pi)} for pi in pis]
print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_1Shnl7Bkiz3f17tuCVOSAZFt': ['publicationinfo'], 'var_call_XBXGwC9AYNLV0N17OPMqqfgP': ['cpc_definition'], 'var_call_yQnQkwtLe8lcRP9xhFF3YIal': 'file_storage/call_yQnQkwtLe8lcRP9xhFF3YIal.json', 'var_call_zpk1hBmFraNmF010iv5ex2Av': 'file_storage/call_zpk1hBmFraNmF010iv5ex2Av.json', 'var_call_l0AFL45eZ5Jdyp1xkvfBxfcE': {'pairs': [], 'subclasses': []}, 'var_call_WMJvbnsJ7iNdFg81pMCWFYHo': [], 'var_call_POoqrEqcjKIbyAAZthbJ2qkQ': 'file_storage/call_POoqrEqcjKIbyAAZthbJ2qkQ.json', 'var_call_ExZhvZ0JkwRvzm2ygYfUgMTL': {'n_uc_pubs': 112, 'n_rows_checked': 77562, 'n_hits': 4, 'sample_hits': [{'Patents_info': 'The US patent filing (application number US-4007205-A) is assigned to CALIFORNIA INST OF TECHN and has publication number US-2005165588-A1.', 'uc_cited': ['US-6237292-B1'], 'n_uc_cited': 1}, {'Patents_info': 'The US patent application (no. US-201715785968-A) is held by BLOOM ENERGY CORP and has publication no. US-10615444-B2.', 'uc_cited': ['US-6767662-B2'], 'n_uc_cited': 1}, {'Patents_info': 'The US application (ID US-201414520615-A) is owned by CRYSTAL IS INC and has publication no. US-9447521-B2.', 'uc_cited': ['US-2010025717-A1'], 'n_uc_cited': 1}, {'Patents_info': 'SCHOWALTER LEO J holds the US application (number US-2000608-A), with publication number US-9437430-B2.', 'uc_cited': ['US-2010025717-A1'], 'n_uc_cited': 1}]}, 'var_call_Bp3zsBiYpqmvBA6nxHmkwuCp': {'pairs': [], 'subclasses': []}}

exec(code, env_args)
