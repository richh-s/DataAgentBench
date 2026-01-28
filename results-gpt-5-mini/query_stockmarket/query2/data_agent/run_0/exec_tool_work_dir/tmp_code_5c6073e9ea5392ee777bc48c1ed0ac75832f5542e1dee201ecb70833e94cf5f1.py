code = """import json
symbols = json.load(open(var_call_q7gL9hCr9JspmaMEoJRADFkT))
# Build SELECT statements with HAVING to filter >200
selects = []
for s in symbols:
    # Safe check: skip empty
    if not s or not isinstance(s, str):
        continue
    stmt = f"SELECT '{s}' AS symbol, MAX(\"Adj Close\") AS max_adj FROM \"{s}\" WHERE Date BETWEEN '2015-01-01' AND '2015-12-31' HAVING MAX(\"Adj Close\") > 200"
    selects.append(stmt)

if not selects:
    sql = "SELECT NULL WHERE 1=0;"
else:
    sql = '\nUNION ALL\n'.join(selects) + ';'

print('__RESULT__:')
print(json.dumps(sql))"""

env_args = {'var_call_pioxFm3HMNADNVHF9KBLRTjt': 'file_storage/call_pioxFm3HMNADNVHF9KBLRTjt.json', 'var_call_rL51DkgtzdOWrf1cILYO8Xv8': 'file_storage/call_rL51DkgtzdOWrf1cILYO8Xv8.json', 'var_call_q7gL9hCr9JspmaMEoJRADFkT': 'file_storage/call_q7gL9hCr9JspmaMEoJRADFkT.json', 'var_call_z5Ol2kR9NwYXLOuKVDTQQoWM': ['SPY', 'IVV', 'VOO', 'VGT', 'QQQ', 'DIA', 'VOOG', 'VTI', 'IWM', 'GLD', 'GDX'], 'var_call_pH4prLIZozt6VWwo2idqIyiG': {'count': 1435, 'sample_first_50': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_call_Ipy6b3buxHRlvuOYm9mcf5O5': [{'max_adj': '193.3121490478516'}], 'var_call_Ih1fxQqFg8G4NZiURIVbVT8J': [{'max_adj': '193.5270538330078'}], 'var_call_C2VnxqiL9MF5Bz1EvDDB6bFn': [{'max_adj': '177.17626953125'}], 'var_call_hm9E6jw0E2rG83qw821gawt9': [{'max_adj': '106.7868881225586'}], 'var_call_LlXD0BGULR3asSg8lYIusB3o': [{'max_adj': '110.42893981933594'}], 'var_call_HbHqf5ZqIjexIPiThdgmv2Sr': [{'max_adj': '163.6190185546875'}], 'var_call_X3YTMLeHCOKVqDTvrFH4TUZU': [{'max_adj': '100.61006927490234'}], 'var_call_dlfQZRWaJN6eUdxJwJMUv2Yl': [{'max_adj': '100.54161834716795'}], 'var_call_0Kexk418TV0rd6ZrUTQctUaT': [{'max_adj': '120.37349700927734'}], 'var_call_kbYX7wrs8B9WMBmMwErWacUl': [{'max_adj': '125.2300033569336'}], 'var_call_GiABUL371isen7CXOM6WvBP8': [{'max_adj': '22.22186088562012'}], 'var_call_0JVFt9jakGGlPfG51CIuHDTl': 'file_storage/call_0JVFt9jakGGlPfG51CIuHDTl.json'}

exec(code, env_args)
