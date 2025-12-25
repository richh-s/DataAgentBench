code = """import json
import numpy as np

file_path = locals()['var_function-call-18346563918913497179']
with open(file_path, 'r') as f:
    article_ids = sorted(json.load(f))

diffs = np.diff(article_ids)
max_gap = int(np.max(diffs))
mean_gap = float(np.mean(diffs))
gaps_gt_100 = int(np.sum(diffs > 100))

print("__RESULT__:")
print(json.dumps({"max_gap": max_gap, "mean_gap": mean_gap, "gaps_gt_100": gaps_gt_100}))"""

env_args = {'var_function-call-16407373274121457065': 'file_storage/function-call-16407373274121457065.json', 'var_function-call-18346563918913497179': 'file_storage/function-call-18346563918913497179.json', 'var_function-call-1343490920313838881': 6696, 'var_function-call-8048387330739090729': {'min': 13, 'max': 127570}, 'var_function-call-16270890655966812699': 'Done'}

exec(code, env_args)
