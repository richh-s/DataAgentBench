code = """import json
candidates = ["UVXY", "SOXL", "SOXS", "NUGT", "DUST", "JNUG", "JDST", "LABU", "LABD", "TECL", "TECS", "FAS", "FAZ", "SPXU", "UPRO", "SDS", "SSO", "TNA", "TZA", "ERX", "ERY", "DRN", "DRV"]
dq = chr(34)
sq = chr(39)
parts = []
for c in candidates:
    # SELECT 'SYM' as Sym FROM "SYM" ...
    p = "SELECT " + sq + c + sq + " as Sym FROM " + dq + c + dq + " WHERE " + dq + "Date" + dq + " LIKE " + sq + "2015-%" + sq + " AND " + dq + "Adj Close" + dq + " > 200"
    parts.append(p)

q = " UNION ALL ".join(parts)
# Replace " with QQ for copy-safety
print("__RESULT__:")
print(json.dumps(q.replace(dq, 'QQ')))"""

env_args = {'var_function-call-3062241635553932877': 'file_storage/function-call-3062241635553932877.json', 'var_function-call-12393690622671255916': 'file_storage/function-call-12393690622671255916.json', 'var_function-call-3212137317014693496': 'file_storage/function-call-3212137317014693496.json', 'var_function-call-15925486148284491953': [{'Date': '2003-09-29'}], 'var_function-call-15136510880994038391': {'count': 1435, 'first_50': ['AAAU', 'AADR', 'ABEQ', 'ACSG', 'ACWF', 'AFK', 'AFLG', 'AFMC', 'AFSM', 'AFTY', 'AGG', 'AGGP', 'AGGY', 'AGQ', 'AGZ', 'AIEQ', 'AIIQ', 'AMLP', 'AMOM', 'AMZA', 'AOA', 'AOK', 'AOM', 'AOR', 'ARGT', 'ARKF', 'ARKK', 'ARKW', 'ARMR', 'ASEA', 'ASHR', 'ASHS', 'ASHX', 'AUSF', 'AVDE', 'AVDV', 'AVEM', 'AVUS', 'AVUV', 'AWAY', 'AWTM', 'AXJL', 'BAB', 'BATT', 'BBC', 'BBP', 'BCD', 'BCI', 'BDCY', 'BDRY']}, 'var_function-call-18155754807473582638': 'test', 'var_function-call-1125376442052737803': 'read p1 ok', 'var_function-call-5306680939791668335': 'AAAU', 'var_function-call-500714716372644272': 'file_storage/function-call-500714716372644272.json', 'var_function-call-14235747490851762301': 'file_storage/function-call-14235747490851762301.json', 'var_function-call-2141735815184184445': [], 'var_function-call-16525422730632307331': 'file_storage/function-call-16525422730632307331.json', 'var_function-call-144372245680024754': ['SPY', 'IVV', 'VOO', 'IWM', 'DIA', 'GLD', 'SLV'], 'var_function-call-4552595684948363843': [], 'var_function-call-15137217305148743863': [{'max("Adj Close")': '193.3121490478516', 'max("Close")': '213.5'}], 'var_function-call-11218963919637969631': ['UVXY', 'SOXL', 'SOXS', 'NUGT', 'DUST', 'JNUG', 'JDST', 'LABU', 'LABD', 'TECL', 'TECS', 'FAS', 'FAZ', 'SPXU', 'UPRO', 'SDS', 'SSO', 'TNA', 'TZA', 'ERX', 'ERY', 'DRN', 'DRV']}

exec(code, env_args)
