code = """import json
# read result
res = var_call_Fu4ZNdrOEB4bB2NvNSKnszHQ
# prepare final plain text answer
lines = []
for r in res:
    lines.append(f"{r['ProjectName']}: {r['Forks']} forks")
ans = "\n".join(lines)
print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_Tg084gBAp439zBv6nyGVDZv7': ['packageinfo'], 'var_call_JC9jizmvdS8ELnpNsf7ahvqd': ['project_info', 'project_packageversion'], 'var_call_TiqTJ2qgioCLSYHkIik7ZSys': 'file_storage/call_TiqTJ2qgioCLSYHkIik7ZSys.json', 'var_call_wlXtcY4UuYpOaXxovR9Mjzpi': 'file_storage/call_wlXtcY4UuYpOaXxovR9Mjzpi.json', 'var_call_zgk2eTfGFhkYDiYaitJ8dius': 'file_storage/call_zgk2eTfGFhkYDiYaitJ8dius.json', 'var_call_nEOU6Ai0AzaSOEKqCfkdZI6n': 'file_storage/call_nEOU6Ai0AzaSOEKqCfkdZI6n.json', 'var_call_Fu4ZNdrOEB4bB2NvNSKnszHQ': [{'ProjectName': 'mui-org/material-ui', 'Forks': 30522, 'Project_Information': 'The project mui-org/material-ui on GitHub is a popular open-source library with a remarkable 89,398 stars and 30,522 forks, currently facing 1,688 open issues.'}, {'ProjectName': 'moment/moment', 'Forks': 7201, 'Project_Information': 'The project moment/moment on GitHub has an open issues count of 305, a stars count of 47549, and a forks count of 7201, making it a popular choice among developers for handling date and time in JavaScript.'}, {'ProjectName': 'lodash/lodash', 'Forks': 7109, 'Project_Information': 'The project lodash/lodash on GitHub has an open issues count of 24, a stars count of 57779, and a forks count of 7109, making it a popular utility library for JavaScript developers.'}, {'ProjectName': 'semantic-org/semantic-ui', 'Forks': 4955, 'Project_Information': 'The project semantic-org/semantic-ui is hosted on GitHub and currently has an open issues count of 1076, along with a notable stars count of 51069 and 4955 forks.'}, {'ProjectName': 'react-native-elements/react-native-elements', 'Forks': 4623, 'Project_Information': 'The project react-native-elements/react-native-elements is a GitHub repository that currently has 116 open issues, 24,814 stars, and 4,623 forks, making it a popular choice for developers looking to enhance their React Native applications.'}]}

exec(code, env_args)
