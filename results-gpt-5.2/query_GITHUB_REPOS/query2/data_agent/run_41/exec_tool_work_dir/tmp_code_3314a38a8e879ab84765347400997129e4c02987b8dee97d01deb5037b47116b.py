code = """import json, pandas as pd

# Load swift contents rows (may be stored as json file path)
path_or_data = var_call_aAGYOPLIqaQeJ1bwtzhgPYw4
if isinstance(path_or_data, str):
    with open(path_or_data, 'r') as f:
        rows = json.load(f)
else:
    rows = path_or_data

df = pd.DataFrame(rows)
# keep non-binary swift files with duplication count in description
s = df['repo_data_description'].fillna('').str.lower()
df = df[s.str.contains('non-binary') & s.str.contains('times')].copy()
# extract first integer before 'times'
df['times'] = df['repo_data_description'].str.extract(r'([0-9]+)\s+times', expand=False).astype(float)
# uniquely determined by ID: compute per-id max times (should be constant)
id_max = df.groupby('id', as_index=False)['times'].max()
max_times = id_max['times'].max()
most_ids = set(id_max.loc[id_max['times']==max_times, 'id'])
# pick repository for one of those ids: use first occurrence in df
pick = df[df['id'].isin(most_ids)].sort_values(['times','sample_repo_name','sample_path'], ascending=[False, True, True]).iloc[0]
answer = {
    'repo_name': pick['sample_repo_name'],
    'file_id': pick['id'],
    'sample_path': pick['sample_path'],
    'copies_times': int(pick['times'])
}
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_liTCwrYaUXpBJPB6aSAglGsl': [], 'var_call_TCYqVXO7QWPeZZ2g2DPbVN4A': 'file_storage/call_TCYqVXO7QWPeZZ2g2DPbVN4A.json', 'var_call_cEJUYtj7C2lgiwU62KC3KGfY': [], 'var_call_aAGYOPLIqaQeJ1bwtzhgPYw4': 'file_storage/call_aAGYOPLIqaQeJ1bwtzhgPYw4.json', 'var_call_f7IVQ7YgbR3pbVcWRGvZZkEs': [], 'var_call_o4qO4xPcZDYOWC41ociL9ar8': [], 'var_call_hG2Onxvg5vcZ3cCLkt2GwRS0': [{'id': 'b03a39b4e07f98073fcf2fbe945bf1291cbfeca7', 'sample_repo_name': 'kostiakoval/WatchKit-Apps', 'sample_path': '5- Shared-CoreData/SharedKit/Record.swift', 'repo_data_description': 'With a file size of 290 bytes and sample mode 33188, this non-binary file is duplicated 8 times.'}, {'id': '3909cba31dd8c36766ee8efd9299c75a7e9f8721', 'sample_repo_name': 'slavapestov/swift', 'sample_path': 'validation-test/compiler_crashers_fixed/27617-swift-markasobjc.swift', 'repo_data_description': 'A 277-byte non-binary file appearing 8 times, with sample mode code 33188.'}, {'id': 'f7a67dcc0bda7a58e7e1a37d483bfd06e5ff9208', 'sample_repo_name': 'gmertk/BusyNavigationBar', 'sample_path': 'BusyNavigationBar/Example/AppDelegate.swift', 'repo_data_description': 'This file has a size of 2161 bytes, is non-binary, and appears 9 times with sample mode 33188.'}, {'id': '15492da9a0490415a84fa6c1a7957e473ebfa4db', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/25255-swift-typechecker-checkinheritanceclause.swift', 'repo_data_description': 'With a file size of 240 bytes and sample mode 33188, this non-binary file is duplicated 10 times.'}, {'id': '41d65e7ae98cc15b6e5eacfd11568e1a851b6add', 'sample_repo_name': 'practicalswift/swift-compiler-crashes', 'sample_path': 'crashes-duplicates/26498-swift-sourcefile-lookupcache-lookupvalue.swift', 'repo_data_description': 'A 218-byte non-binary file appearing 10 times, with sample mode code 33188.'}], 'var_call_79X3GoPnkH5MA7g7OZcw3a5i': []}

exec(code, env_args)
