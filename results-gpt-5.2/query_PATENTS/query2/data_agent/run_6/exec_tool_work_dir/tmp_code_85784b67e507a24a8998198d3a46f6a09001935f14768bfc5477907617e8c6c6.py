code = """import json, pandas as pd

top_obj = var_call_dYla9MAfJFysBlSmAaMHf1FH
if isinstance(top_obj, dict):
    top = top_obj.get('top', [])
else:
    top = top_obj

titles = var_call_AasABWvg0zejQjRXn0PbTRd8

df_top = pd.DataFrame(top)
df_titles = pd.DataFrame(titles).rename(columns={'symbol':'lvl4'})
merged = df_top.merge(df_titles, on='lvl4', how='left')
merged = merged[['titleFull','lvl4','year','ema']].sort_values(['ema','lvl4'], ascending=[False,True])

lines = []
for _, r in merged.iterrows():
    title = r['titleFull'] if pd.notna(r['titleFull']) else '(title not found)'
    lines.append('%s | %s | best_year=%d | max_ema=%.3f' % (r['lvl4'], title, int(r['year']), float(r['ema'])))

answer = chr(10).join(lines)
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_KtpJrgGjCQAScV8aiuSnhhAo': ['publicationinfo'], 'var_call_PdaBkhXROFG7raA0T0FkaSFu': ['cpc_definition'], 'var_call_OWtkZbNyowygBowaTEKzrfvj': [], 'var_call_OlEoAyjMSjsS9CmUmq6pTKsO': 'file_storage/call_OlEoAyjMSjsS9CmUmq6pTKsO.json', 'var_call_HEE0uTfggdQoTJPVL0IpCFKH': 'file_storage/call_HEE0uTfggdQoTJPVL0IpCFKH.json', 'var_call_TV2JwEGCJ2O6VlwXUjhqETNq': {'error': 'No DE granted H2 2019 records with parsable filing_year/CPC.'}, 'var_call_AaeA2pHkjJXWtyG1xBm7JCt0': 'file_storage/call_AaeA2pHkjJXWtyG1xBm7JCt0.json', 'var_call_dYla9MAfJFysBlSmAaMHf1FH': {'top': [{'lvl4': 'F23L1/00', 'year': 2018, 'ema': 3.0}, {'lvl4': 'F23B50/12', 'year': 2018, 'ema': 3.0}, {'lvl4': 'F23L15/04', 'year': 2018, 'ema': 3.0}, {'lvl4': 'F24B5/023', 'year': 2018, 'ema': 3.0}, {'lvl4': 'F02D41/20', 'year': 2010, 'ema': 3.0}, {'lvl4': 'B29C2049/5868', 'year': 2007, 'ema': 2.0}, {'lvl4': 'B29C49/06', 'year': 2007, 'ema': 2.0}, {'lvl4': 'B29C2049/5817', 'year': 2007, 'ema': 2.0}, {'lvl4': 'A61B1/0018', 'year': 2016, 'ema': 2.0}, {'lvl4': 'B29C2049/4294', 'year': 2007, 'ema': 2.0}], 'symbols': ['A61B1/0018', 'B29C2049/4294', 'B29C2049/5817', 'B29C2049/5868', 'B29C49/06', 'F02D41/20', 'F23B50/12', 'F23L1/00', 'F23L15/04', 'F24B5/023']}, 'var_call_AasABWvg0zejQjRXn0PbTRd8': [{'symbol': 'F24B5/023', 'titleFull': 'Supply of primary air for combustion'}, {'symbol': 'B29C2049/4294', 'titleFull': 'Sealing means'}, {'symbol': 'B29C2049/5817', 'titleFull': 'Pneumatic'}, {'symbol': 'B29C2049/5868', 'titleFull': 'Hydraulic'}, {'symbol': 'F23L1/00', 'titleFull': 'Passages or apertures for delivering primary air for combustion\xa0'}, {'symbol': 'F02D41/20', 'titleFull': 'Output circuits, e.g. for controlling currents in command coils'}, {'symbol': 'F23L15/04', 'titleFull': 'Arrangements of recuperators'}, {'symbol': 'B29C49/06', 'titleFull': 'Injection blow-moulding'}, {'symbol': 'F23B50/12', 'titleFull': 'Combustion apparatus in which the fuel is fed into or through the combustion zone by gravity, e.g. from a fuel storage situated above the combustion zone the fuel being fed to the combustion zone by free fall or by sliding along inclined surfaces, e.g. from a conveyor terminating above the fuel bed'}]}

exec(code, env_args)
