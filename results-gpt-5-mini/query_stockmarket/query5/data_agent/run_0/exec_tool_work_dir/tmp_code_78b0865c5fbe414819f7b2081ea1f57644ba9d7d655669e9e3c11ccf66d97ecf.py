code = """import json, os
# Snapshot globals to avoid RuntimeError
g = globals().copy()
rows = []
mapping_data = None
for k, v in g.items():
    if not k.startswith('var_call_'):
        continue
    content = None
    # If v is a string and points to a .json file, load it
    if isinstance(v, str) and v.endswith('.json') and os.path.exists(v):
        try:
            with open(v, 'r') as f:
                content = json.load(f)
        except Exception:
            continue
    else:
        # v might already be a list/dict
        content = v
    # detect mapping_data
    if isinstance(content, dict) and 'mapping' in content:
        mapping_data = content
    # detect query result rows
    if isinstance(content, list) and len(content) > 0 and isinstance(content[0], dict):
        rec = content[0]
        if 'symbol' in rec and 'cnt' in rec:
            try:
                cnt = int(rec['cnt'])
            except Exception:
                try:
                    cnt = int(float(rec['cnt']))
                except Exception:
                    continue
            rows.append((rec['symbol'], cnt))

# Aggregate
if rows:
    from collections import defaultdict
    agg = defaultdict(int)
    for s,c in rows:
        agg[s] += c
    items = sorted(agg.items(), key=lambda x: x[1], reverse=True)
    top5 = items[:5]
    result = []
    for sym, cnt in top5:
        name = None
        if mapping_data and isinstance(mapping_data, dict):
            name = mapping_data.get('mapping', {}).get(sym)
        if not name:
            name = sym
        result.append(name)
else:
    result = []

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_0yaHAZkfGrcaXHyke6o3ibIL': 'file_storage/call_0yaHAZkfGrcaXHyke6o3ibIL.json', 'var_call_dKSpiYnifg74W8Lb0g48hfat': 'file_storage/call_dKSpiYnifg74W8Lb0g48hfat.json', 'var_call_8sPApHfmPrpLxFoixe5XxPs2': 'file_storage/call_8sPApHfmPrpLxFoixe5XxPs2.json', 'var_call_uV700ljuzLYOFubuCKWWcprH': [{'symbol': 'AGMH', 'cnt': '13'}], 'var_call_MFhAtsYs4nhDxZiOLx9VeKM3': [{'symbol': 'ALACU', 'cnt': '0'}], 'var_call_u8RMk0u5Tzgd9DSsUmUCILkr': [{'symbol': 'AMHC', 'cnt': '0'}], 'var_call_OnBDLisAGs3EhGt9J1DueWJK': [{'symbol': 'ANDA', 'cnt': '0'}], 'var_call_e5aKwCrOdobNPnmbrsdZHj3E': [{'symbol': 'APEX', 'cnt': '15'}], 'var_call_q7MI6IlZaKgB4deYTp6SKhSA': [{'symbol': 'BCLI', 'cnt': '0'}], 'var_call_453gIulUfqduzYjJhrL5CU0L': [{'symbol': 'BHAT', 'cnt': '10'}], 'var_call_15WaEPs9Hh54VmtxPJmaWX05': [{'symbol': 'BIOC', 'cnt': '21'}], 'var_call_6XxJPoJe0BBZrDHo0d8ereas': [{'symbol': 'BKYI', 'cnt': '16'}], 'var_call_7Dxu5pGry7gj52K0WHAmh6B8': [{'symbol': 'BLFS', 'cnt': '0'}], 'var_call_v8VMmoLn3XXh5ylu8AF2VKHR': [{'symbol': 'BOSC', 'cnt': '3'}], 'var_call_IxC2enqX0xQJehQUKF1hKyzo': [{'symbol': 'BOTJ', 'cnt': '0'}], 'var_call_gTk4LYGNHtHGiSdk8J1gW1qJ': [{'symbol': 'BWEN', 'cnt': '5'}], 'var_call_eiibDUZYJoYvQCvyJ3FAjIJg': [{'symbol': 'CBAT', 'cnt': '23'}], 'var_call_Rp4gTlsCAZ6lQ1uVPWMBiIuT': [{'symbol': 'CCCL', 'cnt': '13'}], 'var_call_e9xit0LWHIVNq3c2jMQxtlWr': [{'symbol': 'CDMOP', 'cnt': '0'}], 'var_call_ZwqtWo2HzC34JV0rRvNs691h': [{'symbol': 'CEMI', 'cnt': '3'}], 'var_call_yJWEoLkLjaZ6HqLmsa4nmobp': [{'symbol': 'CFBK', 'cnt': '0'}], 'var_call_rJrD33p6tQJiCu40fiTmFQIg': [{'symbol': 'CFFA', 'cnt': '0'}], 'var_call_Agu1ONNsN81ewSsLRmXjaoSN': [{'symbol': 'CLRB', 'cnt': '14'}], 'var_call_xjWV2UpB9VN6ZfJRNiyQWrTV': [{'symbol': 'CORV', 'cnt': '10'}], 'var_call_DaYCPh1knoSQJUoFvJ22qehv': [{'symbol': 'CPAAU', 'cnt': '0'}], 'var_call_wqWehNT9Eb2F5ZqSXg2sb9J5': [{'symbol': 'CPAH', 'cnt': '16'}], 'var_call_0FHXlftU4d5gw9yti8zP04XH': [{'symbol': 'CUBA', 'cnt': '0'}], 'var_call_iifFeySBVOez24bGqn8oVBDI': [{'symbol': 'CVV', 'cnt': '0'}], 'var_call_EvhEBSEA6o1UOtKL6XoGxIlV': [{'symbol': 'DZSI', 'cnt': '1'}], 'var_call_btBvtHDawiDW3P50PhN7QzOw': [{'symbol': 'ELSE', 'cnt': '0'}], 'var_call_JcCy0cTHM9Jb93LW0K2EziS2': [{'symbol': 'EXPC', 'cnt': '0'}], 'var_call_AJdcoKoRrjsx1fW3BGut9v0e': [{'symbol': 'EYEG', 'cnt': '18'}], 'var_call_Joc3niXg3wQ4g7Ym5YoRxOeL': [{'symbol': 'FAMI', 'cnt': '23'}], 'var_call_W5MA99KHoZBrSZbWceSzmHkM': [{'symbol': 'FNCB', 'cnt': '1'}], 'var_call_p7JBdiGh7Bm4FpWuDxf2mH45': [{'symbol': 'FSBW', 'cnt': '0'}], 'var_call_1wg9MyRyTK4iWeL5zMlOTZGY': [{'symbol': 'FTFT', 'cnt': '21'}], 'var_call_WIGKK8psIqE8hCdLUwxFWKFR': [{'symbol': 'GDYN', 'cnt': '0'}], 'var_call_G9LdKdpLSh2qYrnwR9GW4zPv': [{'symbol': 'GLG', 'cnt': '42'}], 'var_call_Y9rUtrAtEbz67DhWVPRpIavS': [{'symbol': 'GRNVU', 'cnt': '0'}], 'var_call_QBC7jjWuGSogRgrYeo25OuY5': [{'symbol': 'GTEC', 'cnt': '0'}], 'var_call_kiyEwqnEU45Kl4UWWLiioD7N': [{'symbol': 'HCCOU', 'cnt': '0'}], 'var_call_MUIlREfTZtxIqtfmeOooT7fA': [{'symbol': 'HNNA', 'cnt': '0'}], 'var_call_QqR7r0FWiZGfVsiduuqauZaw': [{'symbol': 'HQI', 'cnt': '2'}], 'var_call_VM0iJ7GtnEj38yebAaZWeGKJ': [{'symbol': 'HRTX', 'cnt': '1'}], 'var_call_gXEKSiIA9bX509Xlyrb2fJ5R': [{'symbol': 'IDEX', 'cnt': '15'}], 'var_call_kZOWpTwFBi9FPrzNhcz14gV2': [{'symbol': 'IGIC', 'cnt': '0'}], 'var_call_1bhMxUxlvHSoLvKK9OfgQfdH': [{'symbol': 'IOTS', 'cnt': '1'}], 'var_call_m6E8hJ43XC5j74MP0pFWLd0Q': [{'symbol': 'ISNS', 'cnt': '0'}], 'var_call_CTZljYUH9WpyX2cJC08rjS3c': [{'symbol': 'ITI', 'cnt': '0'}], 'var_call_sDzu1vRytL8u1VbL4cfS2cKp': [{'symbol': 'LACQ', 'cnt': '0'}], 'var_call_Ub9Ivl0xfYqHRJnK24UQL4Tv': [{'symbol': 'MBCN', 'cnt': '0'}], 'var_call_aRhDFvYAkKOvZ4Sp9p4tl61P': [{'symbol': 'MBNKP', 'cnt': '0'}], 'var_call_O6g3fCMF4YlJggJe4lcxdkvJ': [{'symbol': 'MCEP', 'cnt': '14'}], 'var_call_TcxabhdV5AwL0IujNIQORLxc': [{'symbol': 'MLND', 'cnt': '3'}], 'var_call_dJGchL6ZpQzhKjZt1LvJ9iaq': [{'symbol': 'MMAC', 'cnt': '1'}], 'var_call_YpCmQKwBGkTXiCQuTqKDALF7': [{'symbol': 'MNCLU', 'cnt': '0'}], 'var_call_R7IAagEhMYvNfICnEkfLDX9o': [{'symbol': 'MNPR', 'cnt': '4'}], 'var_call_3cfMfvOqhjPrPu31PDwcuGkN': [{'symbol': 'NVEE', 'cnt': '1'}], 'var_call_V7ZrCivghmrlNBjgi4DSVjRU': [{'symbol': 'NXTD', 'cnt': '15'}], 'var_call_yf6m9h1ytl0ZG17Eidau985p': [{'symbol': 'OPOF', 'cnt': '0'}], 'var_call_vSGaIMDJKUk0iAG3JezDTCJ8': [{'symbol': 'OPTT', 'cnt': '12'}], 'var_call_KSPnUY7bDL3dTx984gV30CyZ': [{'symbol': 'ORGO', 'cnt': '15'}], 'var_call_e1x0x3Ltn0VIQSoVvcOiPKFB': [{'symbol': 'ORSNU', 'cnt': '0'}], 'var_call_3J0O8CDixqEoiSLLwi5ARcW8': [{'symbol': 'OTEL', 'cnt': '1'}], 'var_call_CMK63yUh4dUXMuPwH8R892CV': [{'symbol': 'PBFS', 'cnt': '0'}], 'var_call_MKT1IKJDbnpJfMNqF3StG3DS': [{'symbol': 'PBTS', 'cnt': '8'}], 'var_call_LYufaSLZTbXjVedRSeKVqyzj': [{'symbol': 'PCSB', 'cnt': '0'}], 'var_call_KT3a77uFXNCKCRoCG5ugtOHA': [{'symbol': 'PECK', 'cnt': '19'}], 'var_call_zM8nRhpNG43upSX2GPhlXMej': [{'symbol': 'PEIX', 'cnt': '12'}], 'var_call_tu2WrgfIYXsW1OaHBTCY8ipX': [{'symbol': 'PFIE', 'cnt': '2'}], 'var_call_n0OicB0cQp5StHeimbaxHhmB': [{'symbol': 'PLIN', 'cnt': '1'}], 'var_call_50jmh2o9K1pKz2Rs5uHijYmQ': [{'symbol': 'POPE', 'cnt': '0'}], 'var_call_E6OUCqsAjICT74FvMn5PraFS': [{'symbol': 'QRHC', 'cnt': '3'}], 'var_call_7LhZbFWLTmh51fqAxwRxQbDI': [{'symbol': 'SES', 'cnt': '51'}]}

exec(code, env_args)
