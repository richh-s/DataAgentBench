code = """import json, re, pandas as pd
from pathlib import Path

# Load project_info
file_path = Path(var_call_DSrvYdgGF98ChmJNTfYygw9r)
project_info_records = json.loads(file_path.read_text())
pi_df = pd.DataFrame(project_info_records)

# Extract repo name, stars from Project_Information using regex
repo_pattern = re.compile(r"project ([^\s]+/[^\s]+)")
stars_pattern = re.compile(r"(\d[\d,]*) stars")

def parse_row(text):
    repo = None
    m = repo_pattern.search(text)
    if m:
        repo = m.group(1)
    m2 = stars_pattern.search(text)
    stars = None
    if m2:
        stars = int(m2.group(1).replace(',', ''))
    return repo, stars

pi_df['repo'], pi_df['stars'] = zip(*pi_df['Project_Information'].map(parse_row))
pi_df = pi_df.dropna(subset=['repo','stars'])

# Load join summary from previous step to know that merged exists (but we re-load for full join)
file_path_pkg = Path(var_call_9InKmcugfYrRQK1YePU2sPLH)
package_records = json.loads(file_path_pkg.read_text())
file_path_ppv = Path(var_call_nvbQQd5FtL0OtrvGmbYH7WuB)
ppv_records = json.loads(file_path_ppv.read_text())

pkg_df = pd.DataFrame(package_records)[['System','Name','Version']].drop_duplicates()
ppv_df = pd.DataFrame(ppv_records)
ppv_df = ppv_df[ppv_df['ProjectType']=='GITHUB']
latest_pkg = pkg_df.sort_values('Version').groupby('Name', as_index=False).tail(1)
merged = latest_pkg.merge(ppv_df, on=['System','Name','Version'], how='inner')

# Map ProjectName to stars via repo
merged = merged.merge(pi_df[['repo','stars']], left_on='ProjectName', right_on='repo', how='left')
merged = merged.dropna(subset=['stars'])

# For each package Name, take the max stars across its projects
pkg_popularity = merged.groupby(['Name','Version'], as_index=False)['stars'].max()

# Take top 5 by stars
top5 = pkg_popularity.sort_values('stars', ascending=False).head(5)

result = top5.to_dict(orient='records')
result_json = json.dumps(result)
print("__RESULT__:")
print(result_json)"""

env_args = {'var_call_9InKmcugfYrRQK1YePU2sPLH': 'file_storage/call_9InKmcugfYrRQK1YePU2sPLH.json', 'var_call_M9iyqf5KGXNrVqJpgc6g5FVf': ['project_info', 'project_packageversion'], 'var_call_nvbQQd5FtL0OtrvGmbYH7WuB': 'file_storage/call_nvbQQd5FtL0OtrvGmbYH7WuB.json', 'var_call_uOF3GYDZCIxmJ9E5xzBfpGeN': {'num_latest_packages': 16614, 'num_joined': 31822, 'sample_projects': ['renddslow/dunsany', 'rvagg/prr', 'div-js/core', 'richmccartney/design-system-monorepo', 'twopg/music', 'dizmo/context', 'drmyersii/dictionary.js', 'substack/jsonify', 'substack/tty-browserify', 'dizmo/context-tree2json', 'mathe42/vite-plugin-serviceworker', 'divedylan/sardine', 'ebizltd/ebiz-kit', 'kaiser-io/kaiserin-storybook', 'easrng/sparkle', 'substack/https-browserify', 'yandex-cloud/sentenizer', 'div-js/cli', 'djplaner/trimester-date', 'dxcli/lint']}, 'var_call_DSrvYdgGF98ChmJNTfYygw9r': 'file_storage/call_DSrvYdgGF98ChmJNTfYygw9r.json'}

exec(code, env_args)
