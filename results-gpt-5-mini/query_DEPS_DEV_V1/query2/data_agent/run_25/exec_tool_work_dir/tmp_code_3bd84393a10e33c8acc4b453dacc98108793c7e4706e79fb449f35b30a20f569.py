code = """import json
# load the top5 result
with open(var_call_yixzkonXndc0Yiu6pxud91Jr, 'r') as f:
    top5 = json.load(f)
# prepare final plain-text answer
lines = [f"{i+1}. {r['project']} — {r['forks']} forks" for i,r in enumerate(top5)]
answer = "Top 5 NPM projects (MIT license, release) by GitHub fork count:\n" + "\n".join(lines)
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_MEq7coGaFeZY1uYdzEuOBVxR': 'file_storage/call_MEq7coGaFeZY1uYdzEuOBVxR.json', 'var_call_DQHCHJPoGMReDnmscL4ipZwY': 'file_storage/call_DQHCHJPoGMReDnmscL4ipZwY.json', 'var_call_2e1tl2asUOd6KA5haPS4xUwV': 'file_storage/call_2e1tl2asUOd6KA5haPS4xUwV.json', 'var_call_MykHHMcZQD5RHNY0zWZurORb': 'file_storage/call_MykHHMcZQD5RHNY0zWZurORb.json', 'var_call_zYwQAi7fCjETMLIuuugYdGa0': 'file_storage/call_zYwQAi7fCjETMLIuuugYdGa0.json', 'var_call_tFD7smh9otcdUy84B2GkmS7e': 'file_storage/call_tFD7smh9otcdUy84B2GkmS7e.json', 'var_call_yixzkonXndc0Yiu6pxud91Jr': [{'project': 'mui-org/material-ui', 'forks': 30522}, {'project': 'moment/moment', 'forks': 7201}, {'project': 'lodash/lodash', 'forks': 7109}, {'project': 'semantic-org/semantic-ui', 'forks': 4955}, {'project': 'react-native-elements/react-native-elements', 'forks': 4623}]}

exec(code, env_args)
