code = """import json, pandas as pd

# load repo list
path = var_call_6ghUCeTpzkBHxS6cHTSx5sFH
with open(path,'r') as f:
    repos = json.load(f)
repo_names = sorted({r['repo_name'] for r in repos if r.get('repo_name')})

# write to parquet for duckdb to read
import pyarrow as pa
import pyarrow.parquet as pq
arr = pa.array(repo_names, type=pa.string())
table = pa.Table.from_arrays([arr], names=['repo_name'])
file_path = '/tmp/repos_shell_apache.parquet'
pq.write_table(table, file_path)

print('__RESULT__:')
print(json.dumps({'parquet_path': file_path, 'repo_count': len(repo_names)}))"""

env_args = {'var_call_6ghUCeTpzkBHxS6cHTSx5sFH': 'file_storage/call_6ghUCeTpzkBHxS6cHTSx5sFH.json', 'var_call_4iFh2crZvLUOEQwJDlI9kBiX': [{'commit_message_count': '0'}], 'var_call_A23H3QLYqusLjok9f1O9FRca': 'file_storage/call_A23H3QLYqusLjok9f1O9FRca.json', 'var_call_e1Y9P7LNo7LAxH0xemEIxUAa': [{'repo_cnt': '114972'}]}

exec(code, env_args)
