code = """import json
# Load the result from earlier aggregation (stored under var_call_cXLTUSeTsstcdjd4JW5c7C8R)
path = var_call_cXLTUSeTsstcdjd4JW5c7C8R
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

lines = []
for i, rec in enumerate(data, start=1):
    lines.append(str(i) + ". " + rec.get('ProjectName', '') + " - " + str(rec.get('Forks', 0)) + " forks")

answer = "Top 5 NPM projects with MIT license and marked as release by GitHub fork count:\n" + "\n".join(lines)

print("__RESULT__:")
print(json.dumps(answer))"""

env_args = {'var_call_tYSqXN27S3qNNzfXJjqkaExN': 'file_storage/call_tYSqXN27S3qNNzfXJjqkaExN.json', 'var_call_iz4384JLpjQN4hA64l5XRruR': 'file_storage/call_iz4384JLpjQN4hA64l5XRruR.json', 'var_call_pWrhDs21fM26iU5y23P5sPp5': 'file_storage/call_pWrhDs21fM26iU5y23P5sPp5.json', 'var_call_WMTArFAC4jwQYN050yX5gqFM': 'file_storage/call_WMTArFAC4jwQYN050yX5gqFM.json', 'var_call_cXLTUSeTsstcdjd4JW5c7C8R': [{'ProjectName': 'mui-org/material-ui', 'Forks': 30522, 'Project_Information': 'The project mui-org/material-ui on GitHub is a popular open-source library with a remarkable 89,398 stars and 30,522 forks, currently facing 1,688 open issues.'}, {'ProjectName': 'semantic-org/semantic-ui', 'Forks': 4955, 'Project_Information': 'The project semantic-org/semantic-ui is hosted on GitHub and currently has an open issues count of 1076, along with a notable stars count of 51069 and 4955 forks.'}, {'ProjectName': 'dreampie/semantic-ui', 'Forks': 4955, 'Project_Information': 'The project semantic-org/semantic-ui is hosted on GitHub and currently has an open issues count of 1076, along with a notable stars count of 51069 and 4955 forks.'}, {'ProjectName': 'react-native-elements/react-native-elements', 'Forks': 4623, 'Project_Information': 'The project react-native-elements/react-native-elements is a GitHub repository that currently has 116 open issues, 24,814 stars, and 4,623 forks, making it a popular choice for developers looking to enhance their React Native applications.'}, {'ProjectName': 'sveltejs/svelte', 'Forks': 4091, 'Project_Information': 'The project sveltejs/svelte on GitHub is an active repository with 907 open issues, boasting an impressive 73,499 stars and 4,091 forks.'}]}

exec(code, env_args)
