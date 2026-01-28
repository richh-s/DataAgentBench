code = """import json, re

def load_records(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pi = load_records(var_call_9B3rBOJMhRnL0c2knMve20Am)

pat_name = re.compile(r"\b([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b")
pat_forks = re.compile(r"(\d[\d,]*)\s+forks?\b", re.IGNORECASE)

cnt_name=cnt_forks=cnt_both=0
examples=[]
for rec in pi:
    s=rec.get('Project_Information') or ''
    nm=pat_name.search(s)
    fm=pat_forks.search(s)
    if nm: cnt_name += 1
    if fm: cnt_forks += 1
    if nm and fm:
        cnt_both += 1
        if len(examples)<5:
            examples.append({'s': s, 'name': nm.group(1), 'forks': fm.group(1)})

print('__RESULT__:')
print(json.dumps({'n': len(pi), 'cnt_name': cnt_name, 'cnt_forks': cnt_forks, 'cnt_both': cnt_both, 'examples': examples}))"""

env_args = {'var_call_TyKo4w4PFjsjBMRx6p9huDCN': 'file_storage/call_TyKo4w4PFjsjBMRx6p9huDCN.json', 'var_call_Tqlka6yRDyF2ECJ6dmMSBY7j': 'file_storage/call_Tqlka6yRDyF2ECJ6dmMSBY7j.json', 'var_call_sgeHDZIFraeMQbE4GAAfgvfM': 'file_storage/call_sgeHDZIFraeMQbE4GAAfgvfM.json', 'var_call_94aZZ4ZZzjyHL8DPIpCBn7vH': {'matched_projects': 5289, 'parsed_projectinfo': 0, 'top5': []}, 'var_call_fk0nI4Y3bxKhZ3pa7NVhE0RA': {'pat1': [], 'pat2': [], 'pat3': []}, 'var_call_fhPEOrXZRAKgtLlGP1vfg46O': {'sample': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'fork_index': 129, 'context': ' 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized too', 'numforks': ['5782']}, 'var_call_0H43sefQL4ARBKxbCa2euieE': {'projects_cols': ['ProjectName'], 'projects_n': 5289, 'pi_cols': [], 'pi_n': 0}, 'var_call_9B3rBOJMhRnL0c2knMve20Am': 'file_storage/call_9B3rBOJMhRnL0c2knMve20Am.json'}

exec(code, env_args)
