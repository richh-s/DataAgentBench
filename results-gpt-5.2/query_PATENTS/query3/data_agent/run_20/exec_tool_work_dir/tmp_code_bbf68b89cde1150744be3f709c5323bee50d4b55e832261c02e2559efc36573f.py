code = """import json, pandas as pd
from pathlib import Path

def load_records(var):
    if isinstance(var, str) and var.endswith('.json'):
        return json.loads(Path(var).read_text())
    return var

recs = load_records(var_call_FLfVs8tLVEb0QVkhBKPDySh1)
# keep only UC assignee rows
uc_recs = [r for r in recs if isinstance(r.get('Patents_info',''), str) and 'owned by UNIV CALIFORNIA' in r['Patents_info']]

out = {
    'uc_publications_count_in_sample': len(uc_recs),
    'sample_uc_patents_info': [r['Patents_info'] for r in uc_recs[:5]],
    'has_citations': [len(json.loads(r['citation'])) if r.get('citation') else 0 for r in uc_recs[:5]]
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_ddOAz8PfD2fDDJqV0zfHDxg7': ['publicationinfo'], 'var_call_wkNZLGn5gJAtTodjHGp1kZtw': ['cpc_definition'], 'var_call_zI3m4l4umjvRlgbTMTKiwULz': [], 'var_call_FLfVs8tLVEb0QVkhBKPDySh1': 'file_storage/call_FLfVs8tLVEb0QVkhBKPDySh1.json'}

exec(code, env_args)
