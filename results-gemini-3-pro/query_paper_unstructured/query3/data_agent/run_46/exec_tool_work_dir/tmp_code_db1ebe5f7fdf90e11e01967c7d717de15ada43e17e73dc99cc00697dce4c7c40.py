code = """import json\n\npath = globals()['var_function-call-2998795241881557550']\nwith open(path, 'r') as f:\n    d = json.load(f)\n\ntxt = d[0]['text']\nres = {}\nres['start'] = txt[:500]\nres['end'] = txt[-500:]\nres['has_empirical'] = 'empirical' in txt.lower()\n\n# Check for lines with 'contribution'\nlines_contrib = [l.strip() for l in txt.split('\\n') if 'contribution' in l.lower()]\nres['lines_contrib'] = lines_contrib[:5] # limit to 5\n\nprint('__RESULT__:')\nprint(json.dumps(res))"""

env_args = {'var_function-call-2278250218217025444': ['paper_docs'], 'var_function-call-2278250218217023235': ['Citations', 'sqlite_sequence'], 'var_function-call-2998795241881557550': 'file_storage/function-call-2998795241881557550.json'}

exec(code, env_args)
