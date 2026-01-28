code = """import json
from pathlib import Path
# var_call_ZMbRMIcspGSPND5NJgLD3lUI is provided by the previous query_db call and contains the path to the JSON file
p = Path(var_call_ZMbRMIcspGSPND5NJgLD3lUI)
records = json.loads(p.read_text())
# Normalize UpstreamPublishedAt and parse VersionInfo.Ordinal if present
for r in records:
    try:
        r['UpstreamPublishedAt'] = float(r.get('UpstreamPublishedAt') or 0)
    except:
        r['UpstreamPublishedAt'] = 0.0
    # parse ordinal
    try:
        vi = json.loads(r.get('VersionInfo') or '{}')
        r['_ordinal'] = int(vi.get('Ordinal') or -1)
    except:
        r['_ordinal'] = -1
# Keep only System == 'NPM'
records = [r for r in records if r.get('System') == 'NPM']
# Group by Name and select the record with max UpstreamPublishedAt, tie-breaker by _ordinal
latest = {}
for r in records:
    name = r['Name']
    key = (r['UpstreamPublishedAt'], r['_ordinal'])
    if name not in latest or key > (latest[name]['UpstreamPublishedAt'], latest[name]['_ordinal']):
        latest[name] = r
# Build list of (Name, Version)
pairs = [{'Name': v['Name'], 'Version': v['Version']} for v in latest.values()]
# For safety sort by Name
pairs = sorted(pairs, key=lambda x: x['Name'].lower())
out = json.dumps(pairs)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_ZMbRMIcspGSPND5NJgLD3lUI': 'file_storage/call_ZMbRMIcspGSPND5NJgLD3lUI.json'}

exec(code, env_args)
