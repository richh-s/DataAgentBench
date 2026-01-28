code = """import json
with open(var_call_L3aEZLGLFlCjzU90qdErzaiv, 'r') as f:
    businesses = json.load(f)

# collect keys
keys = set()
for b in businesses:
    keys.update(b.keys())

# show sample of first 10 business docs
sample = businesses[:10]

out = {'all_keys': sorted(list(keys)), 'sample_first_10': sample}
import json
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_9eED9IMmcC3gBPqLot3GmKf2': ['checkin', 'business'], 'var_call_L3aEZLGLFlCjzU90qdErzaiv': 'file_storage/call_L3aEZLGLFlCjzU90qdErzaiv.json', 'var_call_Eg0pI6raclNDSIJBwTjhmyyt': ['review', 'tip', 'user'], 'var_call_ZS8TTBueUsmVsHL2RjoBDATY': 'file_storage/call_ZS8TTBueUsmVsHL2RjoBDATY.json', 'var_call_PZpjfW4C4KuGXr831uxOL406': {'category': None, 'num_businesses': 0, 'average_rating': None}}

exec(code, env_args)
