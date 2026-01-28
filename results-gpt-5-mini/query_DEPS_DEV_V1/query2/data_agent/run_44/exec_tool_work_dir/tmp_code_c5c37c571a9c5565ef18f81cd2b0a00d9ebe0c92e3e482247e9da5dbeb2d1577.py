code = """import json
# Load the top5 result
top5 = json.loads(var_call_p86nMcPgAzmCRCLBFySvqCfI)
# Prepare final plain-text output listing the 5 projects and fork counts
lines = [f"{i+1}. {item['repo']} - forks: {item['forks']}" for i,item in enumerate(top5)]
answer = '\n'.join(lines)
print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_call_eZTWND63B9Ut5HlwIDSFC7V7': 'file_storage/call_eZTWND63B9Ut5HlwIDSFC7V7.json', 'var_call_vYGlZ0TX6a8k7YP3TkaDHMqV': 'file_storage/call_vYGlZ0TX6a8k7YP3TkaDHMqV.json', 'var_call_hE4No6ehI7Zq0OEf0b1kbyrR': 'file_storage/call_hE4No6ehI7Zq0OEf0b1kbyrR.json', 'var_call_fbiTpSQdrZQvcL68NGf3VaXF': 'file_storage/call_fbiTpSQdrZQvcL68NGf3VaXF.json', 'var_call_p86nMcPgAzmCRCLBFySvqCfI': [{'repo': 'mui-org/material-ui', 'forks': 30522, 'info': 'The project mui-org/material-ui on GitHub is a popular open-source library with a remarkable 89,398 stars and 30,522 forks, currently facing 1,688 open issues.'}, {'repo': 'moment/moment', 'forks': 7201, 'info': 'The project moment/moment on GitHub has an open issues count of 305, a stars count of 47549, and a forks count of 7201, making it a popular choice among developers for handling date and time in JavaScript.'}, {'repo': 'semantic-org/semantic-ui', 'forks': 4955, 'info': 'The project semantic-org/semantic-ui is hosted on GitHub and currently has an open issues count of 1076, along with a notable stars count of 51069 and 4955 forks.'}, {'repo': 'react-native-elements/react-native-elements', 'forks': 4623, 'info': 'The project react-native-elements/react-native-elements is a GitHub repository that currently has 116 open issues, 24,814 stars, and 4,623 forks, making it a popular choice for developers looking to enhance their React Native applications.'}, {'repo': 'sveltejs/svelte', 'forks': 4091, 'info': 'The project sveltejs/svelte on GitHub is an active repository with 907 open issues, boasting an impressive 73,499 stars and 4,091 forks.'}]}

exec(code, env_args)
