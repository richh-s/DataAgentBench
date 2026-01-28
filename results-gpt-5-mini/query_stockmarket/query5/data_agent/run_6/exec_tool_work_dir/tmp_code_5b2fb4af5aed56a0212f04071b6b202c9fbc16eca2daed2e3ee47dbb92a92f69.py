code = """import json
# Collect results from the parallel calls stored in various keys
keys = [
 'var_call_jjPBxtJCxh1aG7BB2mwNnGqF', 'var_call_bZt2kgjoja1Zop1FWBBEPpGW', 'var_call_RYT2s7vBUf9TyoVr57Tsihy3',
 'var_call_wajOvZvN5klYiPVCLzoAOa9G', 'var_call_t0ejtLIZxpPPWNIjaRd7c0jM', 'var_call_vXGfu6fYlMLKjnkR75nE7QXB',
 'var_call_ssuLl1SToVSGU82FEDGf6QR2', 'var_call_wX037m8aljL7wDbHZzOweVXV', 'var_call_SvI0jDUWNMTVGoSl3DMiz9Qz',
 'var_call_Lo1H564TiPyiHnv7NXxXyNlJ', 'var_call_aIkynSvPfg8fzmhu3vGOlhLK', 'var_call_hnfouY7INTTkH5j8rR1DH0S8',
 'var_call_QSx982hF9Tc0nQkz2zGCsWBa', 'var_call_duwHJgO87ZULmtRRLgGeEMwG', 'var_call_uCyhwdehCTB4zsXOcWBEvDOP',
 'var_call_x0tjlMcxSUmTCM5S9366RqkJ', 'var_call_jPjm7KdiFIEn0Swx6GqWPro1', 'var_call_3ptrLiLSPGnATT52WN9BLUUD',
 'var_call_uopEC2DYo8TstcN4vwskcF2f', 'var_call_96YlnjJfIPtpzgNk3s9qCUdB', 'var_call_cV681ilJbRlpKhSZ3MHmSr40',
 'var_call_24k8LiXudeQPvDDhC6Ug94ty', 'var_call_rvFtVTJSsnEZ61wshDeZBtV4', 'var_call_bSuwXVn2RnCxmQVYe7B9YVkh',
 'var_call_lWp23stq5eFxsnDAshMMWC8f', 'var_call_MJ2HxPWSWcZeRRbysGYNvvT2', 'var_call_pe89X1bF6Q8LmqlDI1KxC1Wh',
 'var_call_P6JQnqwG4PsZvND36gZPmQoq', 'var_call_29LS07zXZfL328KHtN57CMFu', 'var_call_HOV2fW4Hx3szERx7VHaKbt7I',
 'var_call_lpdWg8UhxTczWhfhZ8TEPBBf', 'var_call_PD8KHKw2n8wFI44LKJUEai6M', 'var_call_sR5xWmhL7gQkD6lRUPv0Pti8',
 'var_call_35RGx4LcDjhku475de0G4qgW', 'var_call_XJbt6GwjtQMgd4SBXn1mtjlb', 'var_call_ywC0uh3ez1gvI2HjyX4pXyex',
 'var_call_jeq4F55A3nEYvCVIoYQXdQww', 'var_call_VYRRyflf6yX8WHZZERfa2Wow', 'var_call_YrHEPNHpXLRnyQJNPbNfyaW5',
 'var_call_jCtXzzDKdtVwzv8ADRIHfLNu', 'var_call_0MGt4cJsMdw48hj3O8dp3GJM', 'var_call_N28hA4Qamcv3Ifn4hTONAP48',
 'var_call_a9uFgiwZiCHemftiBQKdc2bZ', 'var_call_JxhxTCyyQNLdNKDUn0Kk95uC'
]

# Map symbols from earlier list
symbols = json.load(open(var_call_UlwTYnxK8aLPvZD04YhbL5xk, 'r'))
symbols = [rec['Symbol'] for rec in symbols]

results = []
for i, key in enumerate(keys):
    try:
        recs = json.load(open(key, 'r'))
        cnt = float(recs[0]['cnt'])
    except Exception as e:
        cnt = None
    sym = symbols[i]
    results.append({'symbol': sym, 'cnt': cnt})

# sort and take top 5
results_sorted = sorted([r for r in results if r['cnt'] is not None], key=lambda x: x['cnt'], reverse=True)
top5 = results_sorted[:5]

print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_Ad4UsH2M8L6uC8cGxj7jUQRQ': 'file_storage/call_Ad4UsH2M8L6uC8cGxj7jUQRQ.json', 'var_call_SiXzvTbfmBNhOMQ5JDOIG3NS': 'file_storage/call_SiXzvTbfmBNhOMQ5JDOIG3NS.json', 'var_call_UlwTYnxK8aLPvZD04YhbL5xk': 'file_storage/call_UlwTYnxK8aLPvZD04YhbL5xk.json', 'var_call_RatI87gZt8WuvleV5cCRcxxH': {'n_symbols': 86, 'first_20': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB']}, 'var_call_jjPBxtJCxh1aG7BB2mwNnGqF': [{'cnt': '13.0'}], 'var_call_bZt2kgjoja1Zop1FWBBEPpGW': [{'cnt': '0.0'}], 'var_call_RYT2s7vBUf9TyoVr57Tsihy3': [{'cnt': '0.0'}], 'var_call_wajOvZvN5klYiPVCLzoAOa9G': [{'cnt': '0.0'}], 'var_call_t0ejtLIZxpPPWNIjaRd7c0jM': [{'cnt': '15.0'}], 'var_call_vXGfu6fYlMLKjnkR75nE7QXB': [{'cnt': '0.0'}], 'var_call_ssuLl1SToVSGU82FEDGf6QR2': [{'cnt': '10.0'}], 'var_call_wX037m8aljL7wDbHZzOweVXV': [{'cnt': '21.0'}], 'var_call_SvI0jDUWNMTVGoSl3DMiz9Qz': [{'cnt': '16.0'}], 'var_call_Lo1H564TiPyiHnv7NXxXyNlJ': [{'cnt': '0.0'}], 'var_call_aIkynSvPfg8fzmhu3vGOlhLK': [{'cnt': '3.0'}], 'var_call_hnfouY7INTTkH5j8rR1DH0S8': [{'cnt': '0.0'}], 'var_call_QSx982hF9Tc0nQkz2zGCsWBa': [{'cnt': '5.0'}], 'var_call_duwHJgO87ZULmtRRLgGeEMwG': [{'cnt': '23.0'}], 'var_call_uCyhwdehCTB4zsXOcWBEvDOP': [{'cnt': '13.0'}], 'var_call_x0tjlMcxSUmTCM5S9366RqkJ': [{'cnt': '0.0'}], 'var_call_jPjm7KdiFIEn0Swx6GqWPro1': [{'cnt': '3.0'}], 'var_call_3ptrLiLSPGnATT52WN9BLUUD': [{'cnt': '0.0'}], 'var_call_uopEC2DYo8TstcN4vwskcF2f': [{'cnt': '0.0'}], 'var_call_96YlnjJfIPtpzgNk3s9qCUdB': [{'cnt': '14.0'}], 'var_call_cV681ilJbRlpKhSZ3MHmSr40': [{'cnt': '10.0'}], 'var_call_24k8LiXudeQPvDDhC6Ug94ty': [{'cnt': '0.0'}], 'var_call_rvFtVTJSsnEZ61wshDeZBtV4': [{'cnt': '16.0'}], 'var_call_bSuwXVn2RnCxmQVYe7B9YVkh': [{'cnt': '0.0'}], 'var_call_lWp23stq5eFxsnDAshMMWC8f': [{'cnt': '0.0'}], 'var_call_MJ2HxPWSWcZeRRbysGYNvvT2': [{'cnt': '1.0'}], 'var_call_pe89X1bF6Q8LmqlDI1KxC1Wh': [{'cnt': '0.0'}], 'var_call_P6JQnqwG4PsZvND36gZPmQoq': [{'cnt': '0.0'}], 'var_call_29LS07zXZfL328KHtN57CMFu': [{'cnt': '18.0'}], 'var_call_HOV2fW4Hx3szERx7VHaKbt7I': [{'cnt': '23.0'}], 'var_call_lpdWg8UhxTczWhfhZ8TEPBBf': [{'cnt': '1.0'}], 'var_call_PD8KHKw2n8wFI44LKJUEai6M': [{'cnt': '0.0'}], 'var_call_sR5xWmhL7gQkD6lRUPv0Pti8': [{'cnt': '21.0'}], 'var_call_35RGx4LcDjhku475de0G4qgW': [{'cnt': '0.0'}], 'var_call_XJbt6GwjtQMgd4SBXn1mtjlb': [{'cnt': '42.0'}], 'var_call_ywC0uh3ez1gvI2HjyX4pXyex': [{'cnt': '0.0'}], 'var_call_jeq4F55A3nEYvCVIoYQXdQww': [{'cnt': '0.0'}], 'var_call_VYRRyflf6yX8WHZZERfa2Wow': [{'cnt': '0.0'}], 'var_call_YrHEPNHpXLRnyQJNPbNfyaW5': [{'cnt': '0.0'}], 'var_call_jCtXzzDKdtVwzv8ADRIHfLNu': [{'cnt': '2.0'}], 'var_call_0MGt4cJsMdw48hj3O8dp3GJM': [{'cnt': '1.0'}], 'var_call_N28hA4Qamcv3Ifn4hTONAP48': [{'cnt': '15.0'}], 'var_call_a9uFgiwZiCHemftiBQKdc2bZ': [{'cnt': '0.0'}], 'var_call_JxhxTCyyQNLdNKDUn0Kk95uC': [{'cnt': '1.0'}]}

exec(code, env_args)
