code = """import json
pairs = var_call_hnoMu4RctFqGfBIeNxvwBgh6['pairs']
titles = {r['symbol']: r['titleFull'] for r in var_call_IgZe8kevDXIUP3ScSARhydWl}
rows = []
for p in pairs:
    rows.append({'citing_assignee': p['assignee'], 'cpc_subclass': p['subclass'], 'cpc_subclass_titleFull': titles.get(p['subclass'])})
# sort
rows = sorted(rows, key=lambda x:(x['citing_assignee'], x['cpc_subclass']))
print('__RESULT__:')
print(json.dumps(rows))"""

env_args = {'var_call_k78O5d6VNqdn0Sfz6lA2VsNN': ['publicationinfo'], 'var_call_UHXYP2c9u4mFCPdfMa4PRvxZ': ['cpc_definition'], 'var_call_uMQByuYhjtuOxhdCT5ngThYN': 'file_storage/call_uMQByuYhjtuOxhdCT5ngThYN.json', 'var_call_396wJYrPDq6PXFHSZ4rbfbIB': {'uc_pub_count': 114}, 'var_call_KIulsuDhrhljSEmQ6G6f2zBr': 'file_storage/call_KIulsuDhrhljSEmQ6G6f2zBr.json', 'var_call_hnoMu4RctFqGfBIeNxvwBgh6': {'pair_count': 3, 'assignee_count': 3, 'subclass_count': 3, 'subclasses': ['C30B', 'G01V', 'H01L'], 'pairs': [{'assignee': 'CALIFORNIA INST OF TECHN', 'subclass': 'G01V'}, {'assignee': 'CRYSTAL IS INC', 'subclass': 'C30B'}, {'assignee': 'SCHOWALTER LEO J', 'subclass': 'H01L'}]}, 'var_call_IgZe8kevDXIUP3ScSARhydWl': [{'symbol': 'C30B', 'titleFull': 'SINGLE-CRYSTAL GROWTH; UNIDIRECTIONAL SOLIDIFICATION OF EUTECTIC MATERIAL OR UNIDIRECTIONAL DEMIXING OF EUTECTOID MATERIAL; REFINING BY ZONE-MELTING OF MATERIAL; PRODUCTION OF A HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; SINGLE CRYSTALS OR HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; AFTER-TREATMENT OF SINGLE CRYSTALS OR A HOMOGENEOUS POLYCRYSTALLINE MATERIAL WITH DEFINED STRUCTURE; APPARATUS THEREFOR'}, {'symbol': 'G01V', 'titleFull': 'GEOPHYSICS; GRAVITATIONAL MEASUREMENTS; DETECTING MASSES OR OBJECTS; TAGS'}, {'symbol': 'H01L', 'titleFull': 'SEMICONDUCTOR DEVICES NOT COVERED BY CLASS H10'}]}

exec(code, env_args)
