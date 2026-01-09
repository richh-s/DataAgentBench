code = """import json, pandas as pd, re

def load_tool_result(var):
    if isinstance(var, str) and var.endswith('.json'):
        with open(var, 'r', encoding='utf-8') as f:
            return json.load(f)
    return var

rows = load_tool_result(var_call_qWVzb9uDCrsxsOJgzjrdYL9E)
df = pd.DataFrame(rows)

def clean(s):
    if s is None:
        return ''
    s = str(s)
    if s.lower() in ['none','null','nan']:
        return ''
    return s.strip()

df['title_c'] = df['title'].map(clean)
df['artist_c'] = df['artist'].map(clean)

# try to extract artist-title when artist missing

def extract(title, artist):
    if artist:
        return artist, title
    m = re.match(r'^\s*(.+?)\s*[-–]\s*(.+?)\s*$', title)
    if m:
        return m.group(1).strip(), m.group(2).strip()
    return artist, title

parsed = df.apply(lambda r: extract(r['title_c'], r['artist_c']), axis=1, result_type='expand')
df['artist_p'] = parsed[0].fillna('')
df['title_p'] = parsed[1].fillna('')

# choose most common non-empty title_p/artist_p among these ids
best_title = df.loc[df['title_p']!='','title_p'].value_counts().index[0] if (df['title_p']!='').any() else ''
best_artist = df.loc[df['artist_p']!='','artist_p'].value_counts().index[0] if (df['artist_p']!='').any() else ''

out = {
    'representative_title': best_title,
    'representative_artist': best_artist,
    'examples': df[['track_id','title','artist','album','year']].head(10).to_dict(orient='records')
}
print('__RESULT__:')
print(json.dumps(out, ensure_ascii=False))"""

env_args = {'var_call_gHyKaP3bXtwRZqOGUdbox58X': 'file_storage/call_gHyKaP3bXtwRZqOGUdbox58X.json', 'var_call_DipWTOrnih4S2CyMfJaHM3QF': 'file_storage/call_DipWTOrnih4S2CyMfJaHM3QF.json', 'var_call_97spwcMORMDfP5wLA3S66Djy': {'title': '(unknown title)', 'artist': '(unknown artist)', 'album': None, 'total_revenue_usd': 35223.52, 'track_ids_merged': [304, 1759, 1878, 2241, 3360, 3549, 5091, 5579, 5702, 5714, 5733, 5754, 6595, 6703, 6844, 7448, 7701, 7958, 7966, 8256, 9145, 11174, 11978, 13653, 13660, 13945, 14641, 14865, 14964, 15366, 15917, 17174, 17258, 17370, 17492, 18230, 18306, 18507, 18656]}, 'var_call_qWVzb9uDCrsxsOJgzjrdYL9E': 'file_storage/call_qWVzb9uDCrsxsOJgzjrdYL9E.json'}

exec(code, env_args)
