code = """import json
# load final result
res = var_call_0t7RaG9thAOB63huteBM9Uao
# ensure output format minimal
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_OEReunzHmE74cZY4WNSIkfET': ['packageinfo'], 'var_call_o5zSgoYFYlDqAiCwnnXLwH5B': ['project_info', 'project_packageversion'], 'var_call_sYGEyX5JrMt2dOgtF3WlNf4f': 'file_storage/call_sYGEyX5JrMt2dOgtF3WlNf4f.json', 'var_call_6wivde3LLZKivV7PoIz7h2oI': 'file_storage/call_6wivde3LLZKivV7PoIz7h2oI.json', 'var_call_hOu0eUEw9QMltxlq4dHpjw1h': 'file_storage/call_hOu0eUEw9QMltxlq4dHpjw1h.json', 'var_call_RvxZemrM7Zy6YgWKjluTo5QN': 'file_storage/call_RvxZemrM7Zy6YgWKjluTo5QN.json', 'var_call_x1IMOYdf6h3JXSJiZRuUt4FV': 'file_storage/call_x1IMOYdf6h3JXSJiZRuUt4FV.json', 'var_call_0t7RaG9thAOB63huteBM9Uao': [{'ProjectName': 'mui-org/material-ui', 'Forks': 30522, 'Licenses': ['MIT'], 'Name': '@docly/web', 'Version': '0.1.371'}, {'ProjectName': 'moment/moment', 'Forks': 7201, 'Licenses': ['MIT'], 'Name': '@dollarshaveclub/cli>1.12.0>moment', 'Version': '2.22.2'}, {'ProjectName': 'react-native-elements/react-native-elements', 'Forks': 4623, 'Licenses': ['MIT'], 'Name': '@dplus/themed', 'Version': '0.0.2'}, {'ProjectName': 'sveltejs/svelte', 'Forks': 4091, 'Licenses': ['MIT'], 'Name': '@dylanvann/svelte', 'Version': '3.25.3'}, {'ProjectName': 'tailwindcss/tailwindcss', 'Forks': 3848, 'Licenses': ['MIT'], 'Name': '@dumc11/tailwindcss', 'Version': '0.4.0'}]}

exec(code, env_args)
