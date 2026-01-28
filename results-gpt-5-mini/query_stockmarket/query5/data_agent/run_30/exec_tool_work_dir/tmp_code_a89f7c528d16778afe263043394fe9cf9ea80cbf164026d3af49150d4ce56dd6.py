code = """import json
# access variables from storage
results_vars = [
    var_call_LlBcYWb5xAOMTSR914eBl024,
    var_call_dXMA873trhG83w2ohz4Lbzo6,
    var_call_3ZhsmEVnwFsKe8HJWnWRj4Tm,
    var_call_TNerny0XobV3uQWLZWEpmcCA,
    var_call_0YqDDLt2SRHclvEC5eZLDm2m,
    var_call_Q1zfHKdz1RvhgzqA0nd2ckGa,
    var_call_xi0KdB9bdnNhCptLSZ9FPxcH,
    var_call_NmI6iAmKBGbPgUUjM2FAmDTx,
    var_call_TYwmquHaT2qPvoP2qzbkdfpE,
    var_call_koavP0Powm3o4bjYmVpap1Q2,
    var_call_0jdzJZGYHCoD22q2ZXOSks8F,
    var_call_GVKutYiM3h7ol1uDU2ZQzeuT,
    var_call_s0wGSYrmACXvNwUnifIcADY5,
    var_call_nHmJaRZPApsmQAVIWHO0GBRu,
    var_call_sWucSgRZdXYsauGMSSdyf5vT,
    var_call_dGertTxB8kG3MJ6IysfrxJ6Z,
    var_call_6V2bN4mSGl2UP8sZ3rgumM1I,
    var_call_hibrxXBUYa3vqu6niyF2YP4l,
    var_call_tZRuL11P7Z7iTF1jOM2dmB2M,
    var_call_W13KWjhfbL6ZYcMScyGT2jVH,
    var_call_bpBtGUJz8u0CxZb1l7hBAlaM,
    var_call_lM3oh2F9MW02NWbsRi2lqo2L,
    var_call_F370tvonUzsI9qmsjyMKYJUT,
    var_call_aoVn6beuNah6LkQuEXGwIIpy,
    var_call_3OOHYzQMuwVMwDNDAyKi5PAC,
    var_call_vlgYIRwULLfCYRqThFmDnpZr,
    var_call_mSlKb9l8dsHfa7V4y0UXeGnq,
    var_call_wnE0TpWn15z2OnMrskjqSRkO,
    var_call_N2pkHrMKqi1eodhFAao161AD,
    var_call_Qr4PX8U7Mll5WVUErxfoT5Ow,
    var_call_NVFvBIO9sVJRiB1tK1cMS4Nm,
    var_call_luNSxMsDq3Zji2GTwyvoG2mS,
    var_call_uunlJtyvPnxzQJ1JC9HsoRFM
]
# symbols list from previous execute_python
symbols = var_call_vSqO40PQ9zTfcvZESRSIrBtC['symbols']

# load stockinfo full file to map symbols to company descriptions
with open(var_call_UM52fwnGjM9w8qHHmlixozgo, 'r') as f:
    stockinfo = json.load(f)
mapping = {rec['Symbol']: rec.get('Company Description','') for rec in stockinfo}

counts = []
for i, val in enumerate(results_vars):
    cnt = 0
    try:
        if isinstance(val, str):
            # sometimes it's a JSON string
            try:
                parsed = json.loads(val)
            except Exception:
                parsed = None
            if isinstance(parsed, list) and len(parsed)>0:
                item = parsed[0]
                cnt = int(item.get('cnt') if isinstance(item.get('cnt'), (int,str)) else item.get('cnt'))
            else:
                # try eval-like parsing: strip non-digits
                pass
        elif isinstance(val, list):
            if len(val)>0 and isinstance(val[0], dict):
                cnt = int(val[0].get('cnt',0))
        elif isinstance(val, dict):
            # maybe directly a dict
            cnt = int(val.get('cnt',0))
    except Exception:
        cnt = 0
    counts.append(cnt)

# map counts to symbols
symbol_counts = []
for idx, s in enumerate(symbols[:len(counts)]):
    symbol_counts.append({'symbol': s, 'count': counts[idx], 'company': mapping.get(s, '')})

# sort descending by count
symbol_counts_sorted = sorted(symbol_counts, key=lambda x: x['count'], reverse=True)
# take top 5
top5 = symbol_counts_sorted[:5]
# prepare list of company descriptions (names)
top5_names = [item['company'] if item['company'] else item['symbol'] for item in top5]

print('__RESULT__:')
print(json.dumps(top5_names))"""

env_args = {'var_call_UM52fwnGjM9w8qHHmlixozgo': 'file_storage/call_UM52fwnGjM9w8qHHmlixozgo.json', 'var_call_EIIjC7y9LrLLtIr5yfS5xcFp': 'file_storage/call_EIIjC7y9LrLLtIr5yfS5xcFp.json', 'var_call_vSqO40PQ9zTfcvZESRSIrBtC': {'symbols': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'mapping_sample_count': 86}, 'var_call_LlBcYWb5xAOMTSR914eBl024': [{'cnt': '13'}], 'var_call_dXMA873trhG83w2ohz4Lbzo6': [{'cnt': '0'}], 'var_call_3ZhsmEVnwFsKe8HJWnWRj4Tm': [{'cnt': '0'}], 'var_call_TNerny0XobV3uQWLZWEpmcCA': [{'cnt': '0'}], 'var_call_0YqDDLt2SRHclvEC5eZLDm2m': [{'cnt': '15'}], 'var_call_Q1zfHKdz1RvhgzqA0nd2ckGa': [{'cnt': '0'}], 'var_call_xi0KdB9bdnNhCptLSZ9FPxcH': [{'cnt': '10'}], 'var_call_NmI6iAmKBGbPgUUjM2FAmDTx': [{'cnt': '21'}], 'var_call_TYwmquHaT2qPvoP2qzbkdfpE': [{'cnt': '16'}], 'var_call_koavP0Powm3o4bjYmVpap1Q2': [{'cnt': '0'}], 'var_call_0jdzJZGYHCoD22q2ZXOSks8F': [{'cnt': '3'}], 'var_call_GVKutYiM3h7ol1uDU2ZQzeuT': [{'cnt': '0'}], 'var_call_s0wGSYrmACXvNwUnifIcADY5': [{'cnt': '5'}], 'var_call_nHmJaRZPApsmQAVIWHO0GBRu': [{'cnt': '23'}], 'var_call_sWucSgRZdXYsauGMSSdyf5vT': [{'cnt': '13'}], 'var_call_dGertTxB8kG3MJ6IysfrxJ6Z': [{'cnt': '0'}], 'var_call_6V2bN4mSGl2UP8sZ3rgumM1I': [{'cnt': '3'}], 'var_call_hibrxXBUYa3vqu6niyF2YP4l': [{'cnt': '0'}], 'var_call_tZRuL11P7Z7iTF1jOM2dmB2M': [{'cnt': '0'}], 'var_call_W13KWjhfbL6ZYcMScyGT2jVH': [{'cnt': '14'}], 'var_call_bpBtGUJz8u0CxZb1l7hBAlaM': [{'cnt': '10'}], 'var_call_lM3oh2F9MW02NWbsRi2lqo2L': [{'cnt': '0'}], 'var_call_F370tvonUzsI9qmsjyMKYJUT': [{'cnt': '16'}], 'var_call_aoVn6beuNah6LkQuEXGwIIpy': [{'cnt': '0'}], 'var_call_3OOHYzQMuwVMwDNDAyKi5PAC': [{'cnt': '0'}], 'var_call_vlgYIRwULLfCYRqThFmDnpZr': [{'cnt': '1'}], 'var_call_mSlKb9l8dsHfa7V4y0UXeGnq': [{'cnt': '0'}], 'var_call_wnE0TpWn15z2OnMrskjqSRkO': [{'cnt': '0'}], 'var_call_N2pkHrMKqi1eodhFAao161AD': [{'cnt': '18'}], 'var_call_Qr4PX8U7Mll5WVUErxfoT5Ow': [{'cnt': '23'}], 'var_call_NVFvBIO9sVJRiB1tK1cMS4Nm': [{'cnt': '1'}], 'var_call_luNSxMsDq3Zji2GTwyvoG2mS': [{'cnt': '0'}], 'var_call_uunlJtyvPnxzQJ1JC9HsoRFM': [{'cnt': '21'}]}

exec(code, env_args)
