code = """import json, re
import pandas as pd

# load filenames
path_files = var_call_kTDdrqkBRqXTBZuUxBPQEHnT
with open(path_files, 'r', encoding='utf-8') as f:
    files = json.load(f)

# load citations totals
path_cit = var_call_NEWZSHwtzbngeFnBEoPIUOn0
with open(path_cit, 'r', encoding='utf-8') as f:
    cits = json.load(f)

titles = [d['filename'].replace('.txt','') for d in files]

# heuristic: domain physical activity if title contains activity/exercise/fitness/sedentary/step/wearable? but must be 'physical activity' domain.
# Use keyword filter to approximate; then query mongo for those candidate docs and extract year+domain using regex.
kw = re.compile(r"\b(physical activity|activity tracking|fitness|exercise|step|steps|sedentary|gym|running|wearable|tracker|trackers)\b", re.I)

cand = [t for t in titles if kw.search(t)]

print('__RESULT__:')
print(json.dumps({'candidate_count': len(cand), 'candidates': cand[:200]}))"""

env_args = {'var_call_kTDdrqkBRqXTBZuUxBPQEHnT': 'file_storage/call_kTDdrqkBRqXTBZuUxBPQEHnT.json', 'var_call_NEWZSHwtzbngeFnBEoPIUOn0': 'file_storage/call_NEWZSHwtzbngeFnBEoPIUOn0.json'}

exec(code, env_args)
