code = """import json
# load the pairs list from var_call_RVR5xX7fhAI9VXGTFOxqHAol
path = var_call_RVR5xX7fhAI9VXGTFOxqHAol
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)
pairs = data.get('pairs', [])
# load the cpc definitions from var_call_P6X6VasBz5xUXvg5Sw4XUvSU
path_defs = var_call_P6X6VasBz5xUXvg5Sw4XUvSU
with open(path_defs, 'r', encoding='utf-8') as f:
    defs = json.load(f)
# make a mapping
mapping = {d['symbol']: d.get('titleFull','') for d in defs}
# produce final list of (assignee, full title)
final = []
for p in pairs:
    assignee = p['assignee']
    code = p['primary_cpc']
    title = mapping.get(code)
    if not title:
        title = ''
    final.append({'assignee': assignee, 'cpc': code, 'titleFull': title})
# dedupe by assignee and title
seen = set()
unique = []
for f in final:
    key = (f['assignee'], f['cpc'], f['titleFull'])
    if key not in seen:
        seen.add(key)
        unique.append(f)
print('__RESULT__:')
print(json.dumps(unique))"""

env_args = {'var_call_JkzVcUe9mStTDG8g0enUZ82T': 'file_storage/call_JkzVcUe9mStTDG8g0enUZ82T.json', 'var_call_mN0bvvlQgMe2C2VNhr5mLXV6': 'file_storage/call_mN0bvvlQgMe2C2VNhr5mLXV6.json', 'var_call_65VdEqZzcrDGysYV4E5QhCUt': 'file_storage/call_65VdEqZzcrDGysYV4E5QhCUt.json', 'var_call_godfpDa7ee2D983skuWmCPYL': 'file_storage/call_godfpDa7ee2D983skuWmCPYL.json', 'var_call_dr8fTvP2uZg23tRiHdmgebAk': 'file_storage/call_dr8fTvP2uZg23tRiHdmgebAk.json', 'var_call_RVR5xX7fhAI9VXGTFOxqHAol': 'file_storage/call_RVR5xX7fhAI9VXGTFOxqHAol.json', 'var_call_C4H42g7pqoQUVa5BCFz7GNTc': ['A01D45/006', 'A01H1/04', 'A01H6/825', 'A01K67/0275', 'A01K67/0278', 'A61B1/0014', 'A61B1/018', 'A61B1/041', 'A61B17/32002', 'A61B5/0066', 'A61B5/0084', 'A61B5/0215', 'A61B5/14532', 'A61B5/746', 'A61F2/0077', 'A61F2/4611', 'A61F2/86', 'A61K31/4985', 'A61K31/7088', 'A61K31/713', 'A61K35/22', 'A61K35/28', 'A61K35/545', 'A61K38/02', 'A61K38/1858', 'A61K47/12', 'A61K47/542', 'A61K49/1875', 'A61K8/9794', 'A61K9/0014', 'A61L27/58', 'A61M1/287', 'A61N1/36031', 'A61N1/36034', 'A61N1/36046', 'A61N1/36071', 'A61N1/37205', 'A61N1/3787', 'A61P1/16', 'A61P17/14', 'A61P35/00', 'B01L3/5085', 'B07C5/3422', 'B23K26/032', 'B23P15/007', 'B32B5/18', 'B82Y20/00', 'C04B38/0009', 'C07D233/86', 'C07D487/04', 'C07F9/005', 'C07H21/00', 'C07K14/195', 'C07K14/395', 'C07K14/405', 'C07K14/47', 'C07K14/70521', 'C07K14/71', 'C07K14/7151', 'C07K16/1027', 'C07K16/22', 'C07K16/241', 'C07K16/244', 'C07K16/2896', 'C07K16/40', 'C07K9/00', 'C08B15/04', 'C08G61/04', 'C08G61/126', 'C08J9/0066', 'C08J9/30', 'C09K11/06', 'C10L1/026', 'C12M35/02', 'C12N15/102', 'C12N15/1058', 'C12N15/11', 'C12N15/111', 'C12N15/113', 'C12N15/1137', 'C12N15/63', 'C12N15/74', 'C12N15/81', 'C12N15/8201', 'C12N15/8213', 'C12N15/8255', 'C12N15/86', 'C12N15/87', 'C12N15/907', 'C12N9/22', 'C12P7/42', 'C12Q1/001', 'C12Q1/48', 'C12Q1/68', 'C12Q1/6806', 'C12Q1/6816', 'C12Q1/6869', 'C12Q1/6883', 'C12Q1/6886', 'C12Q1/689', 'C23C14/564', 'C30B11/003', 'C30B25/02', 'C30B29/403', 'D01D5/0069', 'E04H9/021', 'F04B43/14', 'F25B21/00', 'G01B11/2518', 'G01N1/42', 'G01N21/6486', 'G01N21/763', 'G01N27/414', 'G01N30/88', 'G01N33/0001', 'G01N33/58', 'G01N33/68', 'G01N33/6845', 'G01N33/6854', 'G01N33/6869', 'G01N33/6896', 'G01S17/89', 'G01S19/24', 'G01S19/256', 'G01S7/4815', 'G01V1/01', 'G01V3/12', 'G05B1/01', 'G06F17/30598', 'G06F3/043', 'G06T7/55', 'G07D7/12', 'G09G3/344', 'G16B20/20', 'G16H40/40', 'G16H50/50', 'H01L21/0262', 'H01L21/02647', 'H01L21/76838', 'H01L31/103', 'H01L33/12', 'H01L33/22', 'H01L33/32', 'H01L33/58', 'H01M10/48', 'H01M12/06', 'H01M4/0419', 'H01M4/13', 'H01M4/131', 'H01M4/134', 'H01M4/5815', 'H01M6/02', 'H01M6/18', 'H01M8/0232', 'H01M8/2425', 'H01S5/1032', 'H03H7/30', 'H04B7/026', 'H04J13/10', 'H05K3/105', 'H10K85/113'], 'var_call_P6X6VasBz5xUXvg5Sw4XUvSU': 'file_storage/call_P6X6VasBz5xUXvg5Sw4XUvSU.json', 'var_call_N5Pa7yDBEQhRLVE54tpLhccY': 'file_storage/call_N5Pa7yDBEQhRLVE54tpLhccY.json'}

exec(code, env_args)
