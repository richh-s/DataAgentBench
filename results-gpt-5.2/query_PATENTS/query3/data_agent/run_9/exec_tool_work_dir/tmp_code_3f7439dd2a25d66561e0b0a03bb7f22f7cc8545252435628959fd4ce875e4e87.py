code = """import json
pairs = var_call_2BAp6B8YoaF36BVZ9EBCdYVj
if isinstance(pairs, str):
    pairs = json.loads(pairs)
raw_pairs = pairs['pairs_preview']

def clean_assignee(a):
    for token in [' and has publication number', ' and has publication no']:
        if token in a:
            a = a.split(token)[0]
    return a.strip()

ass_sc = [(clean_assignee(a), sc) for a, sc in raw_pairs]

titles = {r['symbol']: r['titleFull'] for r in var_call_eGEgFrIR93ISSIuDW5CJtyh8}

out_lines=[]
for a, sc in sorted(ass_sc):
    out_lines.append(a + chr(9) + titles.get(sc, ""))

result = chr(10).join(out_lines)
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_rx5W1jUyQT0P9qEJcsjzjH9I': ['publicationinfo'], 'var_call_fMEsFRgAHptD22vzpbFkWKRE': ['cpc_definition'], 'var_call_mGsSzfpCDmC2t8Guo7pudB7f': 'file_storage/call_mGsSzfpCDmC2t8Guo7pudB7f.json', 'var_call_csblGH9jl1APg8p4TKZUsQ7I': {'uc_pub_count': 114, 'sample_uc_pubnums': ['AU-2003247814-A1', 'AU-2003297741-A1', 'AU-2004253879-A1', 'AU-2005269556-A1', 'AU-2007297661-A1', 'AU-2008349842-A1', 'AU-2010214112-B2', 'AU-2015364602-B2', 'AU-2017356943-A1', 'AU-2019275518-B2']}, 'var_call_o7MjA49BL1WAXlf6NUCFG4d2': 'file_storage/call_o7MjA49BL1WAXlf6NUCFG4d2.json', 'var_call_2BAp6B8YoaF36BVZ9EBCdYVj': {'pair_count': 3, 'assignee_count': 3, 'subclass_count': 3, 'pairs_preview': [['CALIFORNIA INST OF TECHN and has publication number US-2005165588-A1', 'G01V'], ['CRYSTAL IS INC and has publication no', 'C30B'], ['SCHOWALTER LEO J', 'H01L']], 'subclasses': ['C30B', 'G01V', 'H01L']}, 'var_call_eGEgFrIR93ISSIuDW5CJtyh8': [{'symbol': 'G01V', 'titleFull': 'GEOPHYSICS; GRAVITATIONAL MEASUREMENTS; DETECTING MASSES OR OBJECTS; TAGS'}, {'symbol': 'C30B', 'titleFull': 'SINGLE-CRYSTAL GROWTH; UNIDIRECTIONAL SOLIDIFICATION OF EUTECTIC MATERIAL OR UNIDIRECTIONAL DEMIXING OF EUTECTOID MATERIAL; REFINING BY ZONE-MELTING OF MATERIAL; PRODUCTION OF A HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; SINGLE CRYSTALS OR HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; AFTER-TREATMENT OF SINGLE CRYSTALS OR A HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; APPARATUS THEREFOR'}, {'symbol': 'H01L', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}]}

exec(code, env_args)
