code = """import json
# Collect all query results stored in keys (from multi tool calls and earlier)
keys = [
 'var_call_bWWt9r8dUGOsuCAUkHJeXnVy','var_call_tP92AXCAYo2llUKWbuufgct5','var_call_F2UqRS74IAD5Zbb0Y5b9aiUF',
 'var_call_6iZrHkSRrqLAF48lJQ7Kwyay','var_call_6Doy9gHr10wzs1iUbcluqHaT','var_call_X9Uvvxh6RByHwcZK4WQTEdKF',
 'var_call_tiA4UFuRHYyi7UfactjaDO2e','var_call_ZoPD2tDxNdhqmKEcokClKR1H','var_call_dUibvS50TnT57D2M40bPFXT1',
 'var_call_RP28qAXgleZYpqEHWwDeGIiX','var_call_q1bgEBlmOXRluuYAvxpMjE7i','var_call_zQpFxtsU5V20OlgrGQawdM91',
 'var_call_EcmGHMG0WMTl3hQYIDgJRjyv','var_call_FLcsqQUxVojHR43Mg8TvrVQd','var_call_NrGJpj37OBVH9s2oBEtpvWvX',
 'var_call_i2GZ3QGhbKqHdsqAeFtq6HVg','var_call_q2HyK7qpgJ8ZIOEaoF2pd7DI','var_call_jBLVOjHvktIadwwXiwsdyPsd',
 'var_call_hAqH60ouCh1bvP5xV4u457fm','var_call_frPuiCEsmumGNLfZvWM1rlhK','var_call_su0nhoWAryH6Aw9ic8uzzS4x',
 'var_call_Ye7mrUNzU3NpzrLxwN00CC5G','var_call_ipFrP3zKx8zgBwxZCnL7Lk75','var_call_7lvjEvGAQlCTDXzOiuYhMtcp',
 'var_call_TZ3onx6ilk7okeiHM8gY4bsf','var_call_D2SldQ4PHXOY99Cuny4UxZCB','var_call_FB6U5F5ekap31ID2Tpq2cmCw',
 'var_call_AFs3jciyZLwWbofbehWP0zFs','var_call_Ik6s0kTRus3tqIidg3fqGKQP','var_call_f6k5mbGG9GqKUQNJZp0zkrh6',
 'var_call_e7kOz5lbP4qlq2q59fugCaVd','var_call_H8rLTphBmcWDkOdIdEHthz0z','var_call_tHQ8EDeJRzNmfMGd96qeAIz5',
 'var_call_QCEHrgcoXpOWyirGvFjkQX9e','var_call_poGRNpI2iHNZomhnt34UCQbu','var_call_80Ar4tNL8KIPZ1saE15baho4',
 'var_call_LhGNggSXWnS41Arv7QIXyXx9','var_call_etH6mVOa06bsjknIL1yTLg9s','var_call_vAhU2RcaUbxTlKrhGJwhHyni',
 'var_call_itG4MJ7zLQeBqJ67bqEvPLdi','var_call_HB5QzPXJw8yRFu11QC9V2clb','var_call_FAOgoBssHSjDcaLTWipehXwJ',
 'var_call_144XT0AJUorvFaadyffkGNyQ','var_call_PLfUzNvp7eFUtV0ZgHCDSsDB','var_call_gux2d2bJ8gLXaS4BgDwEWnr4',
 'var_call_cj7FLubaxSqeVDlPUhwWh2NZ','var_call_D7g0sYeX885Rp2sGLihHFJ0S','var_call_bYZiiWXGU0NJHGAlydapDkog',
 'var_call_7hhxsfJH02GfCM2qFTvBiixJ','var_call_SJlskG7kaWQfrevA7m5sSOD0','var_call_Zc7ZJ3FlAIOgOuUNfQO2VcN4',
 'var_call_s2vUpvjTbNeB5BmjtYS4cIkA','var_call_gFiadXxnTRrgxyBVqyWgVuto','var_call_9XBV5uvofW0nq4JewW7H2CAQ',
 'var_call_6Ozs8elnuPUsHX5cjTrzaqjZ','var_call_77AbjrJsXXaVMtMm89bDpaYV','var_call_RfwXJVrqyd4yfqSjU1a8htua',
 'var_call_ifAnfLc2qyXjJKS6UdCUVHjN','var_call_8yXjrK9nDa4psHcqh0Yb86ue','var_call_isrOtlp9djG7il7gpzvlysk8',
 'var_call_raydtf5wivGQa07wzz8T7uc2','var_call_2ydz0gn4OL9rOhLeEk67KPWY','var_call_L9FRvn0xhYqv64XiJV5cDYbh',
 'var_call_zZWo86F9qdJAOlk4DnFreEiV','var_call_JN5t0gGuRHSOgRQZOcpSPcGc','var_call_hV549LnmSjdyjcGjBucNE1W8',
 'var_call_fcxFuyBRJJASIhYdVW2WWVmS','var_call_RAL4VH4cziQlLiJ88X97YihO','var_call_Kd8S1YMUYKJ416j5fADptDSl',
 'var_call_cpzAMa6BfE4GrzZt3v0gjJIl','var_call_YGROuSAHsDk9PfabBnwlvqyp','var_call_ROEyiMjBezupAUQuj7FxFUYa',
 'var_call_65C2Wbwwa8xzPD24rZhz2yOr','var_call_s7h0Vkiu3QHvOu6Df3rGmRUg','var_call_CtUpMkYKOllLvObPwU2OjnlN',
 'var_call_00oZimszxMVKbspuu3Suj39b','var_call_9k1qPlydc8r6nh9nfoXENnah','var_call_TAM71bje34ldFlAtAymM6cg8',
 'var_call_pYtXrQefjTfri9assa6ABI23','var_call_qKkAAvLfbpOUZCaD3n6xUESD','var_call_m5fnHB9i7Jv01S3NUwfoKWz8',
 'var_call_MyxNteF62nq7wERabBXbudfa','var_call_kXPTxFHLch3pDvFXPBtPZfjp','var_call_41t5t66gbrB2FEaCSZ0YiVZX',
 'var_call_JlvJYqjrkkGJ9cuawqGwiyZq','var_call_gjCz0ehxkc1PkcMAuf6i9XJZ']

results = []
for k in keys:
    if k in globals():
        val = globals()[k]
        # val is string with JSON or list; try to parse if string
        if isinstance(val, str):
            try:
                parsed = json.loads(val)
            except:
                # maybe it's already a python list representation
                try:
                    parsed = eval(val)
                except:
                    parsed = None
        else:
            parsed = val
        if isinstance(parsed, list) and len(parsed)>0 and 'symbol' in parsed[0]:
            for rec in parsed:
                # convert cnt to int
                try:
                    cnt = int(rec.get('cnt',0))
                except:
                    cnt = 0
                results.append({'symbol': rec.get('symbol'), 'cnt': cnt})

# Sort by cnt desc and pick top 5
results_sorted = sorted(results, key=lambda x: x['cnt'], reverse=True)
top5 = results_sorted[:5]

# Need to map symbols to company names using stockinfo data stored in var_call_SmfWzdhbPsHBDa2wDmDRsIFQ
raw1 = var_call_SmfWzdhbPsHBDa2wDmDRsIFQ
if isinstance(raw1, str):
    with open(raw1,'r') as f:
        stockinfo = json.load(f)
else:
    stockinfo = raw1

sym_to_name = {r['Symbol']: r['Company Description'] for r in stockinfo}
for item in top5:
    item['company'] = sym_to_name.get(item['symbol'], '')

import json
print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_SmfWzdhbPsHBDa2wDmDRsIFQ': 'file_storage/call_SmfWzdhbPsHBDa2wDmDRsIFQ.json', 'var_call_nREWCVssDAOxzqViAsZHygLJ': 'file_storage/call_nREWCVssDAOxzqViAsZHygLJ.json', 'var_call_BEkxa2WnkSVGLf69dgQ70zp3': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_bWWt9r8dUGOsuCAUkHJeXnVy': [{'symbol': 'AGMH', 'cnt': '13'}], 'var_call_tP92AXCAYo2llUKWbuufgct5': [{'symbol': 'ALACU', 'cnt': '0'}], 'var_call_F2UqRS74IAD5Zbb0Y5b9aiUF': [{'symbol': 'AMHC', 'cnt': '0'}], 'var_call_6iZrHkSRrqLAF48lJQ7Kwyay': [{'symbol': 'ANDA', 'cnt': '0'}], 'var_call_6Doy9gHr10wzs1iUbcluqHaT': [{'symbol': 'APEX', 'cnt': '15'}], 'var_call_X9Uvvxh6RByHwcZK4WQTEdKF': [{'symbol': 'BCLI', 'cnt': '0'}], 'var_call_tiA4UFuRHYyi7UfactjaDO2e': [{'symbol': 'BHAT', 'cnt': '10'}], 'var_call_ZoPD2tDxNdhqmKEcokClKR1H': [{'symbol': 'BIOC', 'cnt': '21'}], 'var_call_dUibvS50TnT57D2M40bPFXT1': [{'symbol': 'BKYI', 'cnt': '16'}], 'var_call_RP28qAXgleZYpqEHWwDeGIiX': [{'symbol': 'BLFS', 'cnt': '0'}], 'var_call_q1bgEBlmOXRluuYAvxpMjE7i': [{'symbol': 'BOSC', 'cnt': '3'}], 'var_call_zQpFxtsU5V20OlgrGQawdM91': [{'symbol': 'BOTJ', 'cnt': '0'}], 'var_call_EcmGHMG0WMTl3hQYIDgJRjyv': [{'symbol': 'BWEN', 'cnt': '5'}], 'var_call_FLcsqQUxVojHR43Mg8TvrVQd': [{'symbol': 'CBAT', 'cnt': '23'}], 'var_call_NrGJpj37OBVH9s2oBEtpvWvX': [{'symbol': 'CCCL', 'cnt': '13'}], 'var_call_i2GZ3QGhbKqHdsqAeFtq6HVg': [{'symbol': 'CDMOP', 'cnt': '0'}], 'var_call_q2HyK7qpgJ8ZIOEaoF2pd7DI': [{'symbol': 'CEMI', 'cnt': '3'}], 'var_call_jBLVOjHvktIadwwXiwsdyPsd': [{'symbol': 'CFBK', 'cnt': '0'}], 'var_call_hAqH60ouCh1bvP5xV4u457fm': [{'symbol': 'CFFA', 'cnt': '0'}], 'var_call_frPuiCEsmumGNLfZvWM1rlhK': [{'symbol': 'CLRB', 'cnt': '14'}], 'var_call_su0nhoWAryH6Aw9ic8uzzS4x': [{'symbol': 'CORV', 'cnt': '10'}], 'var_call_Ye7mrUNzU3NpzrLxwN00CC5G': [{'symbol': 'CPAAU', 'cnt': '0'}], 'var_call_ipFrP3zKx8zgBwxZCnL7Lk75': [{'symbol': 'CPAH', 'cnt': '16'}], 'var_call_7lvjEvGAQlCTDXzOiuYhMtcp': [{'symbol': 'CUBA', 'cnt': '0'}], 'var_call_TZ3onx6ilk7okeiHM8gY4bsf': [{'symbol': 'CVV', 'cnt': '0'}], 'var_call_D2SldQ4PHXOY99Cuny4UxZCB': [{'symbol': 'DZSI', 'cnt': '1'}], 'var_call_FB6U5F5ekap31ID2Tpq2cmCw': [{'symbol': 'ELSE', 'cnt': '0'}], 'var_call_AFs3jciyZLwWbofbehWP0zFs': [{'symbol': 'EXPC', 'cnt': '0'}], 'var_call_Ik6s0kTRus3tqIidg3fqGKQP': [{'symbol': 'EYEG', 'cnt': '18'}], 'var_call_f6k5mbGG9GqKUQNJZp0zkrh6': [{'symbol': 'FAMI', 'cnt': '23'}], 'var_call_e7kOz5lbP4qlq2q59fugCaVd': [{'symbol': 'FNCB', 'cnt': '1'}], 'var_call_H8rLTphBmcWDkOdIdEHthz0z': [{'symbol': 'FSBW', 'cnt': '0'}], 'var_call_tHQ8EDeJRzNmfMGd96qeAIz5': [{'symbol': 'FTFT', 'cnt': '21'}], 'var_call_QCEHrgcoXpOWyirGvFjkQX9e': [{'symbol': 'GDYN', 'cnt': '0'}], 'var_call_poGRNpI2iHNZomhnt34UCQbu': [{'symbol': 'GLG', 'cnt': '42'}], 'var_call_80Ar4tNL8KIPZ1saE15baho4': [{'symbol': 'GRNVU', 'cnt': '0'}], 'var_call_LhGNggSXWnS41Arv7QIXyXx9': [{'symbol': 'GTEC', 'cnt': '0'}], 'var_call_etH6mVOa06bsjknIL1yTLg9s': [{'symbol': 'HCCOU', 'cnt': '0'}], 'var_call_vAhU2RcaUbxTlKrhGJwhHyni': [{'symbol': 'HNNA', 'cnt': '0'}], 'var_call_itG4MJ7zLQeBqJ67bqEvPLdi': [{'symbol': 'HQI', 'cnt': '2'}], 'var_call_HB5QzPXJw8yRFu11QC9V2clb': [{'symbol': 'HRTX', 'cnt': '1'}], 'var_call_FAOgoBssHSjDcaLTWipehXwJ': [{'symbol': 'IDEX', 'cnt': '15'}], 'var_call_144XT0AJUorvFaadyffkGNyQ': [{'symbol': 'IGIC', 'cnt': '0'}], 'var_call_PLfUzNvp7eFUtV0ZgHCDSsDB': [{'symbol': 'IOTS', 'cnt': '1'}], 'var_call_gux2d2bJ8gLXaS4BgDwEWnr4': [{'symbol': 'ISNS', 'cnt': '0'}], 'var_call_cj7FLubaxSqeVDlPUhwWh2NZ': [{'symbol': 'ITI', 'cnt': '0'}], 'var_call_D7g0sYeX885Rp2sGLihHFJ0S': [{'symbol': 'LACQ', 'cnt': '0'}], 'var_call_bYZiiWXGU0NJHGAlydapDkog': [{'symbol': 'MBCN', 'cnt': '0'}], 'var_call_7hhxsfJH02GfCM2qFTvBiixJ': [{'symbol': 'MBNKP', 'cnt': '0'}], 'var_call_SJlskG7kaWQfrevA7m5sSOD0': [{'symbol': 'MCEP', 'cnt': '14'}], 'var_call_Zc7ZJ3FlAIOgOuUNfQO2VcN4': [{'symbol': 'MLND', 'cnt': '3'}], 'var_call_s2vUpvjTbNeB5BmjtYS4cIkA': [{'symbol': 'MMAC', 'cnt': '1'}], 'var_call_gFiadXxnTRrgxyBVqyWgVuto': [{'symbol': 'MNCLU', 'cnt': '0'}], 'var_call_9XBV5uvofW0nq4JewW7H2CAQ': [{'symbol': 'MNPR', 'cnt': '4'}], 'var_call_6Ozs8elnuPUsHX5cjTrzaqjZ': [{'symbol': 'NVEE', 'cnt': '1'}], 'var_call_77AbjrJsXXaVMtMm89bDpaYV': [{'symbol': 'NXTD', 'cnt': '15'}], 'var_call_RfwXJVrqyd4yfqSjU1a8htua': [{'symbol': 'OPOF', 'cnt': '0'}], 'var_call_ifAnfLc2qyXjJKS6UdCUVHjN': [{'symbol': 'OPTT', 'cnt': '12'}], 'var_call_8yXjrK9nDa4psHcqh0Yb86ue': [{'symbol': 'ORGO', 'cnt': '15'}], 'var_call_isrOtlp9djG7il7gpzvlysk8': [{'symbol': 'ORSNU', 'cnt': '0'}], 'var_call_raydtf5wivGQa07wzz8T7uc2': [{'symbol': 'OTEL', 'cnt': '1'}], 'var_call_2ydz0gn4OL9rOhLeEk67KPWY': [{'symbol': 'PBFS', 'cnt': '0'}], 'var_call_L9FRvn0xhYqv64XiJV5cDYbh': [{'symbol': 'PBTS', 'cnt': '8'}], 'var_call_zZWo86F9qdJAOlk4DnFreEiV': [{'symbol': 'PCSB', 'cnt': '0'}], 'var_call_JN5t0gGuRHSOgRQZOcpSPcGc': [{'symbol': 'PECK', 'cnt': '19'}], 'var_call_hV549LnmSjdyjcGjBucNE1W8': [{'symbol': 'PEIX', 'cnt': '12'}], 'var_call_fcxFuyBRJJASIhYdVW2WWVmS': [{'symbol': 'PFIE', 'cnt': '2'}], 'var_call_RAL4VH4cziQlLiJ88X97YihO': [{'symbol': 'PLIN', 'cnt': '1'}], 'var_call_Kd8S1YMUYKJ416j5fADptDSl': [{'symbol': 'POPE', 'cnt': '0'}], 'var_call_cpzAMa6BfE4GrzZt3v0gjJIl': [{'symbol': 'QRHC', 'cnt': '3'}], 'var_call_YGROuSAHsDk9PfabBnwlvqyp': [{'symbol': 'SES', 'cnt': '51'}], 'var_call_ROEyiMjBezupAUQuj7FxFUYa': [{'symbol': 'SHSP', 'cnt': '1'}], 'var_call_65C2Wbwwa8xzPD24rZhz2yOr': [{'symbol': 'SNSS', 'cnt': '32'}], 'var_call_s7h0Vkiu3QHvOu6Df3rGmRUg': [{'symbol': 'SSNT', 'cnt': '11'}], 'var_call_CtUpMkYKOllLvObPwU2OjnlN': [{'symbol': 'STKS', 'cnt': '0'}], 'var_call_00oZimszxMVKbspuu3Suj39b': [{'symbol': 'TGLS', 'cnt': '0'}], 'var_call_9k1qPlydc8r6nh9nfoXENnah': [{'symbol': 'TMSR', 'cnt': '40'}], 'var_call_TAM71bje34ldFlAtAymM6cg8': [{'symbol': 'VERB', 'cnt': '38'}], 'var_call_pYtXrQefjTfri9assa6ABI23': [{'symbol': 'VMD', 'cnt': '1'}], 'var_call_qKkAAvLfbpOUZCaD3n6xUESD': [{'symbol': 'VRRM', 'cnt': '0'}], 'var_call_m5fnHB9i7Jv01S3NUwfoKWz8': [{'symbol': 'VTIQW', 'cnt': '6'}], 'var_call_MyxNteF62nq7wERabBXbudfa': [{'symbol': 'VVPR', 'cnt': '14'}], 'var_call_kXPTxFHLch3pDvFXPBtPZfjp': [{'symbol': 'WHLM', 'cnt': '0'}], 'var_call_41t5t66gbrB2FEaCSZ0YiVZX': [{'symbol': 'WHLR', 'cnt': '15'}], 'var_call_JlvJYqjrkkGJ9cuawqGwiyZq': [{'symbol': 'XBIOW', 'cnt': '7'}], 'var_call_gjCz0ehxkc1PkcMAuf6i9XJZ': [{'symbol': 'XPEL', 'cnt': '4'}]}

exec(code, env_args)
