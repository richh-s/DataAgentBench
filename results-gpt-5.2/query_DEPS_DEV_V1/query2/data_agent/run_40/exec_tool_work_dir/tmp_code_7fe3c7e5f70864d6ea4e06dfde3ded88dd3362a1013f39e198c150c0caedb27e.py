code = """import json, re

def load_maybe_path(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

pi = load_maybe_path(var_call_FhD4S8krAStrLmiGyy7r2oUI)
name_pat_cs = re.compile(r"\bproject\s+(?:named\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b")
name_pat_ci = re.compile(r"\bproject\s+(?:named\s+)?([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)\b", re.IGNORECASE)

cnt_cs=0; cnt_ci=0
for rec in pi[:5000]:
    t = rec.get('Project_Information')
    if not isinstance(t,str):
        continue
    if name_pat_cs.search(t):
        cnt_cs += 1
    if name_pat_ci.search(t):
        cnt_ci += 1

print('__RESULT__:')
print(json.dumps({'cnt_cs': cnt_cs, 'cnt_ci': cnt_ci, 'checked': 5000}))"""

env_args = {'var_call_ZE9KN9DOlI7j7zVOCa3r3FqT': 'file_storage/call_ZE9KN9DOlI7j7zVOCa3r3FqT.json', 'var_call_ww7i2MXMtA5uvgeQwPLi9f81': 'file_storage/call_ww7i2MXMtA5uvgeQwPLi9f81.json', 'var_call_FhD4S8krAStrLmiGyy7r2oUI': 'file_storage/call_FhD4S8krAStrLmiGyy7r2oUI.json', 'var_call_VhucjoAshOLRzdU24ovCtJHi': [], 'var_call_t1kUjKcXcmnAzEy8sgbAN9kG': [], 'var_call_djVKSWnPW9SczZVTuvT0971t': ['The project lberrocal/npm-packages-template is hosted on GitHub and currently has 0 open issues, 0 stars, and 0 forks.', 'The project leaflet/leaflet on GitHub is a popular open-source library that currently has 521 open issues, 38715 stars, and 5782 forks, making it a widely recognized tool in the developer community.', 'The project leaflet/leaflet.fullscreen on GitHub currently has 29 open issues, 417 stars, and 118 forks, making it a noteworthy contribution to the Leaflet ecosystem.', 'The project leaflet/leaflet.markercluster is hosted on GitHub and currently has an open issues count of 130, along with a stars count of 3761 and forks count of 988.', 'The project leandrowd/react-responsive-carousel on GitHub has garnered significant attention, with a total of 2,534 stars and 636 forks, while currently having 23 open issues.'], 'var_call_KnPghQKbzV3OsIYnqbwQTgD3': {'matched_projects': 5289, 'parsed_projects': 0, 'top5': []}, 'var_call_SMXWvC5ViWe6WCeGi3ngpwr3': {'proj_names': 5289, 'names_in_pi': 0, 'intersection': 0, 'intersection_sample': []}}

exec(code, env_args)
