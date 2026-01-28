code = """import json, re
# Load mapping file produced earlier
mkey = 'var_call_4sbjtOXtdORPt2oBnxRCNCTC'
if mkey in globals():
    mval = globals()[mkey]
    if isinstance(mval, str) and mval.endswith('.json'):
        with open(mval, 'r') as f:
            mapping_data = json.load(f)
    else:
        mapping_data = mval
else:
    mapping_data = {'mapping': {}}
mapping = mapping_data.get('mapping', {})

# collect results from all var_call_ keys
res = []
for k, v in list(globals().items()):
    if not k.startswith('var_call_'):
        continue
    if k in (mkey, 'var_call_g29DMfGZ1F5iPmMFwe0rGJmZ', 'var_call_NxAzjzgAprbtYGql6TUtUGiP'):
        continue
    val = v
    parsed = None
    if isinstance(val, str):
        # Try direct JSON load
        try:
            parsed = json.loads(val)
        except Exception:
            # try to extract JSON array inside the string
            m = re.search(r"(\[\s*\{.*?\}\s*\])", val, flags=re.S)
            if m:
                try:
                    parsed = json.loads(m.group(1))
                except Exception:
                    parsed = None
    else:
        parsed = val
    if not parsed:
        continue
    if isinstance(parsed, list):
        for rec in parsed:
            if isinstance(rec, dict) and 'Symbol' in rec:
                sym = rec.get('Symbol')
                cnt = rec.get('cnt')
                try:
                    cnt = int(cnt)
                except Exception:
                    try:
                        cnt = int(str(cnt))
                    except Exception:
                        continue
                res.append((sym, cnt))

# aggregate
from collections import defaultdict
agg = defaultdict(int)
for s,c in res:
    agg[s] += c

sorted_syms = sorted(agg.items(), key=lambda x: x[1], reverse=True)
top5 = sorted_syms[:5]
# map to company description/name
out = []
for s,c in top5:
    name = mapping.get(s, '')
    out.append({'Symbol': s, 'Company Description': name, 'count': c})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_g29DMfGZ1F5iPmMFwe0rGJmZ': 'file_storage/call_g29DMfGZ1F5iPmMFwe0rGJmZ.json', 'var_call_NxAzjzgAprbtYGql6TUtUGiP': 'file_storage/call_NxAzjzgAprbtYGql6TUtUGiP.json', 'var_call_4sbjtOXtdORPt2oBnxRCNCTC': 'file_storage/call_4sbjtOXtdORPt2oBnxRCNCTC.json', 'var_call_aEHqy1wGYvVbtndyo9NiupWw': 86, 'var_call_Yi00vctOirql49ssfBoXfiJN': [{'Symbol': 'AGMH', 'cnt': '13'}], 'var_call_sDcyXeGEVsuS1eYZLEV5ykXe': [{'Symbol': 'ALACU', 'cnt': '0'}], 'var_call_udUkY511AhyLrrPHsyapj8nC': [{'Symbol': 'AMHC', 'cnt': '0'}], 'var_call_5kFyluWaOSAiyD8oeKF2laeX': [{'Symbol': 'ANDA', 'cnt': '0'}], 'var_call_k66wm3zcFXOFRkm5g5tKgrlP': [{'Symbol': 'APEX', 'cnt': '15'}], 'var_call_a1Bt1XfDTyFH29TFMTd8zlGn': [{'Symbol': 'BCLI', 'cnt': '0'}], 'var_call_J5iZ2l3245i94SiVoCubVv5S': [{'Symbol': 'BHAT', 'cnt': '10'}], 'var_call_iLACR67egaSso6icPq25RUto': [{'Symbol': 'BIOC', 'cnt': '21'}], 'var_call_UWtYHxo27Fa1GAsUCzNlqgNP': [{'Symbol': 'BKYI', 'cnt': '16'}], 'var_call_LlYKf6HSHJ982tRjQeIzMiHW': [{'Symbol': 'BLFS', 'cnt': '0'}], 'var_call_OVTIiFZc5yW2LvHnRGPYaK9x': [{'Symbol': 'BOSC', 'cnt': '3'}], 'var_call_l1fXCMVtWK6rgs2fttCNgim4': [{'Symbol': 'BOTJ', 'cnt': '0'}], 'var_call_Aiep7suhovPtNxtx4Ig6yS5A': [{'Symbol': 'BWEN', 'cnt': '5'}], 'var_call_e32tdAB9xxSC72mHdC2gs1UJ': [{'Symbol': 'CBAT', 'cnt': '23'}], 'var_call_451Cu2TVuMIqV3bcDFyKUSwJ': [{'Symbol': 'CCCL', 'cnt': '13'}], 'var_call_1fnN13sXGUai5BYJAXcqkLZb': [{'Symbol': 'CDMOP', 'cnt': '0'}], 'var_call_25TlI5ngdO34IXvNTm3Lwnaq': [{'Symbol': 'CEMI', 'cnt': '3'}], 'var_call_03SuZdwP9YKr52Pyiw5FiRQg': [{'Symbol': 'CFBK', 'cnt': '0'}], 'var_call_xtO2U24mNe40qdy3poBiD8ku': [{'Symbol': 'CFFA', 'cnt': '0'}], 'var_call_BQ35psyMGJlUJtv1VjvRKKpn': [{'Symbol': 'CLRB', 'cnt': '14'}], 'var_call_AvStvPAUvR6nkEQCSKBM7tIn': [{'Symbol': 'CORV', 'cnt': '10'}], 'var_call_u7qwtWHaWeiKFem9bwnr5uUJ': [{'Symbol': 'CPAAU', 'cnt': '0'}], 'var_call_voZG3HYm7fHwjfYXMMgOJtl0': [{'Symbol': 'CPAH', 'cnt': '16'}], 'var_call_pKJPW6mmukLn2Tz6kod4bq1U': [{'Symbol': 'CUBA', 'cnt': '0'}], 'var_call_E1bvPhitbFW0r67sjdbPsUkJ': [{'Symbol': 'CVV', 'cnt': '0'}], 'var_call_jweWxWXikCSZQ7psg7BIhkhW': [{'Symbol': 'DZSI', 'cnt': '1'}], 'var_call_QqTgGgBNaYJoqHQiSYwufBot': [{'Symbol': 'ELSE', 'cnt': '0'}], 'var_call_OoD5Wm5Kcw37aCOK7hcwoK3N': [{'Symbol': 'EXPC', 'cnt': '0'}], 'var_call_PmhLru9vbkmtov7F5UZNNNLO': [{'Symbol': 'EYEG', 'cnt': '18'}], 'var_call_QcN7wgkSYslTJiAgrWIAjslB': [{'Symbol': 'FAMI', 'cnt': '23'}], 'var_call_Hlk4ngwEk3j2mrkYasGEQwAl': [{'Symbol': 'FNCB', 'cnt': '1'}], 'var_call_YiK5ob7jYKLi17OmaI6dLH3N': [{'Symbol': 'FSBW', 'cnt': '0'}], 'var_call_QGwmEsyojxJ7wi5nSIIzYkrN': [{'Symbol': 'FTFT', 'cnt': '21'}], 'var_call_cavOolstZEAicStGt8waE5DJ': [{'Symbol': 'GDYN', 'cnt': '0'}], 'var_call_9kueyoXH9cMdojSdRZlPwrEj': [{'Symbol': 'GLG', 'cnt': '42'}], 'var_call_nbGUHQPhwdXNTWG9ZgBtVgNa': [{'Symbol': 'GRNVU', 'cnt': '0'}], 'var_call_kzjZfAlhABVyQlIelTyppbwa': [{'Symbol': 'GTEC', 'cnt': '0'}], 'var_call_JUhNCDC1W3dIdwelhxq7LmuL': [{'Symbol': 'HCCOU', 'cnt': '0'}], 'var_call_VYj2X9zvXMPfrNBJp3mm11oX': [{'Symbol': 'HNNA', 'cnt': '0'}], 'var_call_m4oTCDVms87BtszBbAnxFr75': [{'Symbol': 'HQI', 'cnt': '2'}], 'var_call_Aw12wApT6p2nTwIsf7VXvjQP': [{'Symbol': 'HRTX', 'cnt': '1'}], 'var_call_Q3NiXJZtlKRYJwt96JFhwqQ7': [{'Symbol': 'IDEX', 'cnt': '15'}], 'var_call_6h1UpHByu4izV0JMfmX2eKxk': [{'Symbol': 'IGIC', 'cnt': '0'}], 'var_call_XofmfX4TIjxkRBP59CYQtdoM': [{'Symbol': 'IOTS', 'cnt': '1'}], 'var_call_6l69Cd468AKi6ACzCZoNegfM': [{'Symbol': 'ISNS', 'cnt': '0'}], 'var_call_8pAVwY5KvMeIukOyTCI74maf': [{'Symbol': 'ITI', 'cnt': '0'}], 'var_call_4jnubctKlpEd2glSeU42S8Xm': [{'Symbol': 'LACQ', 'cnt': '0'}], 'var_call_yfzJNn66GRcPOOUHaIKtFzrM': [{'Symbol': 'MBCN', 'cnt': '0'}], 'var_call_uxnNYfQXYJin79Yu7dLnTTov': [{'Symbol': 'MBNKP', 'cnt': '0'}], 'var_call_A0lH1QxgxXxHt00nW3FhW77Y': [{'Symbol': 'MCEP', 'cnt': '14'}], 'var_call_73Iti4ZyzIZKIxBhGGF0r2j6': [{'Symbol': 'MLND', 'cnt': '3'}], 'var_call_XLq6Ri4xfN9qfnaGb5ucmPYu': [{'Symbol': 'MMAC', 'cnt': '1'}], 'var_call_QGkQY04WRDK0Sv7OMjJHGxvL': [{'Symbol': 'MNCLU', 'cnt': '0'}], 'var_call_pqmHYG8MYJIkNQT1QMvW29Sb': [{'Symbol': 'MNPR', 'cnt': '4'}], 'var_call_16WxezH95wDK3fxshWn3bt3F': [{'Symbol': 'NVEE', 'cnt': '1'}], 'var_call_1chfMVlh3dJxwB89Etv8ERVi': [{'Symbol': 'NXTD', 'cnt': '15'}], 'var_call_fd76XHGP3ZpkIzwYR8Z4UNlZ': [{'Symbol': 'OPOF', 'cnt': '0'}], 'var_call_6T0OKjC0UBsVjBIU5NsFRHKt': [{'Symbol': 'OPTT', 'cnt': '12'}], 'var_call_yTkQzkjIAItG8VL2Ex39M41m': [{'Symbol': 'ORGO', 'cnt': '15'}], 'var_call_oFSiuLMHkoHMvWKpJWYyuH6v': [{'Symbol': 'ORSNU', 'cnt': '0'}], 'var_call_4J65nTTUPfM5x8dLKsLOiSeR': [{'Symbol': 'OTEL', 'cnt': '1'}], 'var_call_CJhg91BM2ZCzL7uRZld3BEfA': [{'Symbol': 'PBFS', 'cnt': '0'}], 'var_call_19HfRLAgY9aXeux7HjoEc3nQ': [{'Symbol': 'PBTS', 'cnt': '8'}], 'var_call_jCVh8IXmXMGB761weIExNU1s': [{'Symbol': 'PCSB', 'cnt': '0'}], 'var_call_RYXeMXcq7lyKWbUQHDPY73OC': [{'Symbol': 'PECK', 'cnt': '19'}], 'var_call_3RQ0AsAK5tSYcsfXKVdqqScN': [{'Symbol': 'PEIX', 'cnt': '12'}], 'var_call_LfLpDanWrTJz4oZkyLoco6OI': [{'Symbol': 'PFIE', 'cnt': '2'}]}

exec(code, env_args)
