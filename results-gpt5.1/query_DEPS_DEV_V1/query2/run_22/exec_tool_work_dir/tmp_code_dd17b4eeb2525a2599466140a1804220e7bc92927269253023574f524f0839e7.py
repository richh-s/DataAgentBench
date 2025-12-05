code = """import json, re, pandas as pd

# Load full results from JSON files
import_path1 = var_call_f3ZxlgsO9sRgRCph5CsslUmJ
import_path2 = var_call_hUZ83BwrFX1D6ewse5BPyReL
import_path3 = var_call_BUkVvioQpDOs4nTuBOpFzru1

with open(import_path1, 'r') as f:
    package_rows = json.load(f)
with open(import_path2, 'r') as f:
    proj_pkg_rows = json.load(f)
with open(import_path3, 'r') as f:
    proj_info_rows = json.load(f)

# DataFrames
pkg_df = pd.DataFrame(package_rows)
ppv_df = pd.DataFrame(proj_pkg_rows)
info_df = pd.DataFrame(proj_info_rows)

# Filter to NPM + MIT + IsRelease already done in SQL; just ensure System=NPM
pkg_df = pkg_df[pkg_df['System'] == 'NPM']

# Join packageinfo with project_packageversion on System, Name, Version
merged = pkg_df.merge(ppv_df, on=['System', 'Name', 'Version'], how='inner')

# Keep only GitHub projects
merged = merged[merged['ProjectType'] == 'GITHUB']

# Extract project name and metrics from Project_Information
# Example text: "The project leaflet/leaflet on GitHub ... 38715 stars, and 5782 forks"

project_metrics = []
pattern = re.compile(r"project\s+([^\s]+/[^\s]+).*?([0-9,]+)\s+stars.*?([0-9,]+)\s+forks", re.IGNORECASE)

for row in info_df['Project_Information']:
    text = row
    m = pattern.search(text)
    if not m:
        continue
    name = m.group(1).strip()
    stars = int(m.group(2).replace(',', ''))
    forks = int(m.group(3).replace(',', ''))
    project_metrics.append({'ProjectName': name, 'Stars': stars, 'Forks': forks})

metrics_df = pd.DataFrame(project_metrics).drop_duplicates(subset=['ProjectName'])

# Map metrics to merged data via ProjectName
merged_with_metrics = merged.merge(metrics_df, on='ProjectName', how='inner')

# Among all NPM MIT release packages, find distinct projects and their fork counts
project_agg = merged_with_metrics.groupby('ProjectName', as_index=False)['Forks'].max()

# Top 5 by Forks
top5 = project_agg.sort_values('Forks', ascending=False).head(5)

result = top5.to_dict(orient='records')

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_f3ZxlgsO9sRgRCph5CsslUmJ': 'file_storage/call_f3ZxlgsO9sRgRCph5CsslUmJ.json', 'var_call_hUZ83BwrFX1D6ewse5BPyReL': 'file_storage/call_hUZ83BwrFX1D6ewse5BPyReL.json', 'var_call_BUkVvioQpDOs4nTuBOpFzru1': 'file_storage/call_BUkVvioQpDOs4nTuBOpFzru1.json'}

exec(code, env_args)
