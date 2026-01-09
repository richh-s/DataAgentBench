code = """import json, re

def extract_assignee(patents_info: str):
    if not patents_info:
        return None
    # stop at comma/period; also stop at ' and has pub'
    m = re.search(r"owned by ([^,\.]+)", patents_info, flags=re.IGNORECASE)
    if not m:
        return None
    s=m.group(1).strip()
    s=re.sub(r"\s+and\s+has\s+pub.*$","",s,flags=re.IGNORECASE).strip()
    return s

samples=[
    'In US, the application (number US-202117472182-A) is owned by UNIV CALIFORNIA and has pub. number US-2022074631-A1.',
    'Application (no. US-77231501-A) from US, owned by CALIFORNIA INST OF TECHN, with publication no. US-6559125-B1.'
]
print('__RESULT__:')
print(json.dumps([extract_assignee(x) for x in samples]))"""

env_args = {'var_call_1rYrvyDMz1z3QQtjsFzHstWw': ['publicationinfo'], 'var_call_Ms9eMaShBwv17k0wWTZQFXz7': [], 'var_call_5eTr8UabZxWiZbQfiXRw0lFv': [], 'var_call_47XoEKYUkAFjoJCttXjRK0gU': 'file_storage/call_47XoEKYUkAFjoJCttXjRK0gU.json', 'var_call_C9RLBBJLeuadpJoDEshNxw3R': ['cpc_definition'], 'var_call_5nl6c85ItrHDBnsYe6dKNRfh': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine'}], 'var_call_ufRM2y4QHSgCdLLpWiiplGL4': {'n_citation_links': 75, 'sample': [{'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cited_pub': 'US-4599677-A'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cited_pub': 'US-2015129765-A1'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cited_pub': 'FR-3105380-A1'}, {'citing_assignee': 'UNIV CALIFORNIA and has pub', 'cited_pub': 'US-11466906-B2'}, {'citing_assignee': 'CALIFORNIA INST OF TECHN', 'cited_pub': 'US-4766142-A'}]}}

exec(code, env_args)
