code = """import json
import pandas as pd
import re

swift_repo_names = json.load(open(locals()['var_function-call-11660494627758164746'], 'r'))
non_binary_swift_files = json.load(open(locals()['var_function-call-2584952045628009572'], 'r'))

df_files = pd.DataFrame(non_binary_swift_files)

def extract_copies(description):
    match = re.search(r'copied (\d+) times', description)
    if match:
        return int(match.group(1))
    match = re.search(r'appears (\d+) times', description)
    if match:
        return int(match.group(1))
    match = re.search(r'repeated (\d+) times', description)
    if match:
        return int(match.group(1))
    match = re.search(r'duplicated (\d+) times', description)
    if match:
        return int(match.group(1))
    match = re.search(r'seen (\d+) times', description)
    if match:
        return int(match.group(1))
    return 0

df_files['copies'] = df_files['repo_data_description'].apply(extract_copies)

df_swift_files = df_files[df_files['sample_repo_name'].isin(swift_repo_names)]

if not df_swift_files.empty:
    max_copies_file = df_swift_files.loc[df_swift_files['copies'].idxmax()]
    result = max_copies_file['sample_repo_name']
else:
    result = "No Swift files found with copy information."

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-655609114511562150': 'file_storage/function-call-655609114511562150.json', 'var_function-call-10084207732532201684': [], 'var_function-call-11660494627758164746': 'file_storage/function-call-11660494627758164746.json', 'var_function-call-101813004073253211': 'file_storage/function-call-101813004073253211.json', 'var_function-call-2584952045628009572': 'file_storage/function-call-2584952045628009572.json'}

exec(code, env_args)
