code = """import json
# load previous result
data = json.load(open(var_call_HmYwVsetvOZ1SrWOkNrDbW1h, 'r'))
pairs = data.get('pairs', [])
# collect unique cpc codes
codes = sorted({p['cpc_code'] for p in pairs if p.get('cpc_code')})
# build SQL IN clause safely by escaping single quotes
in_list = ','.join("'{}'".format(c.replace("'","''")) for c in codes)
sql = 'SELECT symbol, "titleFull" FROM cpc_definition WHERE symbol IN ({});'.format(in_list)
output = {'sql': sql, 'pairs': pairs, 'codes': codes}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_FWaq87obpvltPwUmTRpRaycV': 'file_storage/call_FWaq87obpvltPwUmTRpRaycV.json', 'var_call_xPULEoxuCI0R7gn4s9WmVLxr': 'file_storage/call_xPULEoxuCI0R7gn4s9WmVLxr.json', 'var_call_tgrM8QNXraQ65lKZy8S0oDdF': 'file_storage/call_tgrM8QNXraQ65lKZy8S0oDdF.json', 'var_call_HmYwVsetvOZ1SrWOkNrDbW1h': 'file_storage/call_HmYwVsetvOZ1SrWOkNrDbW1h.json'}

exec(code, env_args)
