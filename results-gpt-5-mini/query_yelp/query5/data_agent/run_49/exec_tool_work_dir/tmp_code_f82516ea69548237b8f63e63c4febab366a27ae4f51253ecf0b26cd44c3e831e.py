code = """import json
var = var_call_unCag2iTyjwaNuh2NypAaGlf
mapping = var['mapping']
# count per state
counts = {}
for bref, st in mapping.items():
    counts[st] = counts.get(st, 0) + 1
# find top state (if tie, pick lexicographically smallest)
max_count = max(counts.values())
top_states = [s for s,c in counts.items() if c==max_count]
top_state = sorted(top_states)[0]
# collect business_refs for top state
brefs_top = [b for b,s in mapping.items() if s==top_state]
out = {'counts': counts, 'max_count': max_count, 'top_state': top_state, 'brefs_top': sorted(brefs_top)}
print("__RESULT__:")
print(json.dumps(out))"""

env_args = {'var_call_ISQoh6iMVYmAnZq1TNJGCAAx': ['checkin', 'business'], 'var_call_qJb8PqPyM64XFVIREQHFZvqM': ['review', 'tip', 'user'], 'var_call_lyuIhu1hJ2dZgWmh4ozVScQN': 'file_storage/call_lyuIhu1hJ2dZgWmh4ozVScQN.json', 'var_call_unCag2iTyjwaNuh2NypAaGlf': {'business_refs': ['businessref_12', 'businessref_16', 'businessref_20', 'businessref_25', 'businessref_26', 'businessref_40', 'businessref_43', 'businessref_44', 'businessref_46', 'businessref_51', 'businessref_54', 'businessref_55', 'businessref_6', 'businessref_64', 'businessref_67', 'businessref_77', 'businessref_82', 'businessref_86', 'businessref_89', 'businessref_91', 'businessref_93', 'businessref_97'], 'mapping': {'businessref_64': 'MO', 'businessref_54': 'FL', 'businessref_91': 'LA', 'businessref_93': 'IL', 'businessref_26': 'FL', 'businessref_89': 'PA', 'businessref_97': 'PA', 'businessref_67': 'PA', 'businessref_51': 'FL', 'businessref_6': 'NV', 'businessref_55': 'FL', 'businessref_77': 'PA', 'businessref_86': 'PA', 'businessref_40': 'PA', 'businessref_44': 'PA', 'businessref_43': 'IN', 'businessref_20': 'FL', 'businessref_25': 'ID', 'businessref_82': 'PA', 'businessref_12': 'AB', 'businessref_16': 'IN', 'businessref_46': 'MO'}}}

exec(code, env_args)
