code = """import json
# load previous python result
res = var_call_7JdSxC1zZikmZBnp7L51QbSu
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_w7ZuVRkYUn4Gu7SpWccSzHVL': 'file_storage/call_w7ZuVRkYUn4Gu7SpWccSzHVL.json', 'var_call_IxA7XUhlcREjW05n5cTzF5ho': 'file_storage/call_IxA7XUhlcREjW05n5cTzF5ho.json', 'var_call_M6Q0rrpmAJZ6OZfdr1nqHru3': 'file_storage/call_M6Q0rrpmAJZ6OZfdr1nqHru3.json', 'var_call_ukDcz9BPczGPF2UTPdFHqhF0': 'file_storage/call_ukDcz9BPczGPF2UTPdFHqhF0.json', 'var_call_7JdSxC1zZikmZBnp7L51QbSu': [{'project': 'mui-org/material-ui', 'forks': 30522}, {'project': 'drovp/types', 'forks': 12282}, {'project': 'dwlib-js/types', 'forks': 12282}, {'project': 'dishhq/typescript', 'forks': 12282}, {'project': 'nestjs/swagger', 'forks': 8824}]}

exec(code, env_args)
