code = """import json, re
s = "The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community."
print('__RESULT__:')
print(json.dumps({
 'name': re.search(r"([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)", s).group(1),
 'forks': re.search(r"(\d[\d,]*)\s+fork", s, flags=re.I).group(1)
}))"""

env_args = {'var_call_TyKo4w4PFjsjBMRx6p9huDCN': 'file_storage/call_TyKo4w4PFjsjBMRx6p9huDCN.json', 'var_call_Tqlka6yRDyF2ECJ6dmMSBY7j': 'file_storage/call_Tqlka6yRDyF2ECJ6dmMSBY7j.json', 'var_call_sgeHDZIFraeMQbE4GAAfgvfM': 'file_storage/call_sgeHDZIFraeMQbE4GAAfgvfM.json', 'var_call_94aZZ4ZZzjyHL8DPIpCBn7vH': {'matched_projects': 5289, 'parsed_projectinfo': 0, 'top5': []}, 'var_call_fk0nI4Y3bxKhZ3pa7NVhE0RA': {'pat1': [], 'pat2': [], 'pat3': []}, 'var_call_fhPEOrXZRAKgtLlGP1vfg46O': {'sample': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'fork_index': 129, 'context': ' 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized too', 'numforks': ['5782']}, 'var_call_0H43sefQL4ARBKxbCa2euieE': {'projects_cols': ['ProjectName'], 'projects_n': 5289, 'pi_cols': [], 'pi_n': 0}, 'var_call_9B3rBOJMhRnL0c2knMve20Am': 'file_storage/call_9B3rBOJMhRnL0c2knMve20Am.json', 'var_call_V1EEaPPUwy93WV58iLuImciS': {'n': 770, 'cnt_name': 0, 'cnt_forks': 0, 'cnt_both': 0, 'examples': []}, 'var_call_37obKOhzGRggWbI1wDbzM9Gd': {'s': 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'name_match': False, 'fork_match': False}, 'var_call_qryh7OOJL6zdzVXjWVTL1Ff1': {'nm': None, 'fm': None, 'all': ['leaflet/leaflet']}}

exec(code, env_args)
