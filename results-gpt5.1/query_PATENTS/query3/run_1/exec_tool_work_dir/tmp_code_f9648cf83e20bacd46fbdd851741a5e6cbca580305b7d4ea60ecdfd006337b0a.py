code = """import json, pandas as pd
from pathlib import Path

cpc_defs = json.loads(Path(var_call_SPAySaerO1DM0O2cd4CwBovH).read_text())

mapping = {r['symbol']: r['titleFull'] for r in cpc_defs}
assignee_codes = json.loads(var_call_h1dfrEX7n45YNbqi7HgQtEIC)

result_list = []
for assignee, codes in assignee_codes.items():
    for code in codes:
        title = mapping.get(code, '')
        result_list.append({'assignee': assignee, 'cpc_symbol': code, 'cpc_titleFull': title})

out = json.dumps(result_list)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_VyvxqGiKX2mHqW0HCBUffhJJ': [], 'var_call_5IdcQmOBSdzDr5RwJDg5NzW9': 'file_storage/call_5IdcQmOBSdzDr5RwJDg5NzW9.json', 'var_call_h1dfrEX7n45YNbqi7HgQtEIC': {'UNKNOWN': ['A61B5/0031', 'A61B5/0035', 'A61B5/0066', 'A61B5/1128', 'A61K31/155', 'A61K31/352', 'A61K31/4184', 'A61K31/734', 'A61K31/737', 'A61K35/28', 'A61K35/30', 'A61K38/02', 'A61K38/14', 'A61K39/0011', 'A61K39/15', 'A61K45/06', 'A61K48/00', 'A61K51/065', 'A61L27/3633', 'A61L27/3865', 'A61L27/58', 'A61N1/36021', 'A61N1/3605', 'A61N7/02', 'A61P17/14', 'A61P35/00', 'B01L3/50273', 'B01L3/502761', 'B01L3/5085', 'B25J13/084', 'C07D233/86', 'C07D235/02', 'C07D473/18', 'C07D487/04', 'C07H19/16', 'C07H21/00', 'C07K14/435', 'C07K14/47', 'C07K14/4711', 'C07K14/51', 'C07K16/00', 'C08B15/04', 'C08B37/0024', 'C08G61/02', 'C08J9/30', 'C08L1/02', 'C08L5/08', 'C09C1/3676', 'C09D105/00', 'C12N15/102', 'C12N15/1037', 'C12N15/81', 'C12N15/8255', 'C12N15/86', 'C12N5/0621', 'C12N5/0647', 'C12N9/1085', 'C12Q1/48', 'C12Q1/485', 'C12Q1/6883', 'C30B29/403', 'F16K99/0059', 'F25B21/00', 'G01N27/44791', 'G01N33/48721', 'G01N33/58', 'G01N33/6854', 'G01N33/6869', 'G01N33/6893', 'G01N35/00', 'G01R33/421', 'G01V3/12', 'H01L21/0262', 'H01L21/76838', 'H01M8/0232', 'H01M8/1226', 'H03H7/30', 'H04B7/0413', 'H04J13/10', 'H04L1/0048', 'H04L12/28', 'H04L63/0245']}, 'var_call_SPAySaerO1DM0O2cd4CwBovH': 'file_storage/call_SPAySaerO1DM0O2cd4CwBovH.json'}

exec(code, env_args)
