code = """import json, os
# load stockinfo records
stockinfo = []
if 'var_call_CXV6AFYuhWf4cZ3SzcFw0jYo' in globals():
    path = globals()['var_call_CXV6AFYuhWf4cZ3SzcFw0jYo']
    try:
        with open(path,'r') as f:
            stockinfo = json.load(f)
    except Exception:
        stockinfo = []
# gather query results from all var_call_ keys
results = []
for k, v in list(globals().items()):
    if not k.startswith('var_call_'):
        continue
    # skip the stockinfo key we already loaded
    if k == 'var_call_CXV6AFYuhWf4cZ3SzcFw0jYo':
        continue
    val = v
    data = None
    # if it's a path to a file
    if isinstance(val, str):
        # try to open as file
        if os.path.exists(val):
            try:
                with open(val,'r') as f:
                    data = json.load(f)
            except Exception:
                # try to parse the string as json
                try:
                    data = json.loads(val)
                except Exception:
                    data = None
        else:
            try:
                data = json.loads(val)
            except Exception:
                data = None
    else:
        data = val
    if not data:
        continue
    # data may be a list of dicts or a single dict
    if isinstance(data, dict):
        data = [data]
    if not isinstance(data, list):
        continue
    for item in data:
        if not isinstance(item, dict):
            continue
        # normalize keys
        keys = {kk.lower(): kk for kk in item.keys()}
        if 'symbol' in keys:
            sym = item[keys['symbol']]
        else:
            continue
        # try possible cnt keys
        cnt = None
        for candidate in ['cnt','count','value']:
            if candidate in keys:
                cnt = item[keys[candidate]]
                break
        # if cnt not found, try any numeric field
        if cnt is None:
            # find first numeric-like value besides symbol
            for kk, vv in item.items():
                if kk.lower()=='symbol':
                    continue
                if isinstance(vv, (int, float)):
                    cnt = vv
                    break
                # try parseable string
                if isinstance(vv, str):
                    try:
                        num = float(vv)
                        cnt = num
                        break
                    except Exception:
                        continue
        if cnt is None:
            continue
        try:
            cntf = float(cnt)
        except Exception:
            continue
        results.append({'Symbol': sym, 'cnt': cntf})
# aggregate counts
symbol_counts = {}
for r in results:
    symbol_counts[r['Symbol']] = symbol_counts.get(r['Symbol'], 0.0) + r['cnt']
# get top 5 symbols
top5 = sorted(symbol_counts.items(), key=lambda x: x[1], reverse=True)[:5]
# map to company description
sym_to_desc = {rec['Symbol']: rec.get('Company Description','') for rec in stockinfo}
output = []
for sym, cnt in top5:
    desc = sym_to_desc.get(sym, '')
    output.append({'Symbol': sym, 'Company Description': desc, 'count': int(cnt)})
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_CXV6AFYuhWf4cZ3SzcFw0jYo': 'file_storage/call_CXV6AFYuhWf4cZ3SzcFw0jYo.json', 'var_call_tXOtpY1HEpiyPlku0M5AGz86': 'file_storage/call_tXOtpY1HEpiyPlku0M5AGz86.json', 'var_call_RMWFFIuAO9KY40ynDKwwz33N': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_uIAk5lJonkY4Jsi65hz8eUdb': 'file_storage/call_uIAk5lJonkY4Jsi65hz8eUdb.json', 'var_call_FqDZQfrv6jR5AaFcUBxPfuZN': [{'Symbol': 'AGMH', 'cnt': '13.0'}], 'var_call_lv8plQ7JOHPk45z34tecJPB2': [{'Symbol': 'ALACU', 'cnt': '0.0'}], 'var_call_yt8sWGQj23GrorOxKRoDpdaL': [{'Symbol': 'AMHC', 'cnt': '0.0'}], 'var_call_V3tw1tYJiUQ6FSRtQuIEj47l': [{'Symbol': 'ANDA', 'cnt': '0.0'}], 'var_call_ffJjR3mBUpbzNlsMuNE04mY4': [{'Symbol': 'APEX', 'cnt': '15.0'}], 'var_call_yrMTZNw6oqXkLqYG549ddmmY': [{'Symbol': 'BCLI', 'cnt': '0.0'}], 'var_call_xSjr36WSpLigndUPie7R0FoX': [{'Symbol': 'BHAT', 'cnt': '10.0'}], 'var_call_yd9eZZbZGBrjYqZFYipiI8EZ': [{'Symbol': 'BIOC', 'cnt': '21.0'}], 'var_call_3WV12a5GgKIPBZIXyFBpukIF': [{'Symbol': 'BKYI', 'cnt': '16.0'}], 'var_call_9l2GY2fBemnT7S4BMbPwnuBW': [{'Symbol': 'BLFS', 'cnt': '0.0'}], 'var_call_oFDPAtXmLEEIJxv8uQ7Rci8D': [{'Symbol': 'BOSC', 'cnt': '3.0'}], 'var_call_4LCKI0EFgLi2eQKSWvYUpFqK': [{'Symbol': 'BOTJ', 'cnt': '0.0'}], 'var_call_ww4s4A3cnHK3KDfneMfyCbCu': [{'Symbol': 'BWEN', 'cnt': '5.0'}], 'var_call_omNEtazJR2ddhapDFpPFIJGQ': [{'Symbol': 'CBAT', 'cnt': '23.0'}], 'var_call_9h64F2GD2TApCtncIKhdRh3F': [{'Symbol': 'CCCL', 'cnt': '13.0'}], 'var_call_uCcPAx3u9kBx0JXZsyMRASnH': [{'Symbol': 'CDMOP', 'cnt': '0.0'}], 'var_call_XQSyT2mZRbPWSS5oAPEQIPCW': [{'Symbol': 'CEMI', 'cnt': '3.0'}], 'var_call_crUWXV9QRgF6BVzevdielW2v': [{'Symbol': 'CFBK', 'cnt': '0.0'}], 'var_call_bzL9EzJJbHLckbnbGkSIYk7d': [{'Symbol': 'CFFA', 'cnt': '0.0'}], 'var_call_MzXqr1y1YWhMB6sg8YR4N1WK': [{'Symbol': 'CLRB', 'cnt': '14.0'}], 'var_call_ZpfbBfTLgAMp0J9jJNhtCzaL': [{'Symbol': 'CORV', 'cnt': '10.0'}], 'var_call_3gGDY5q1P1tHtxowAvff40On': [{'Symbol': 'CPAAU', 'cnt': '0.0'}], 'var_call_pwBXQBRHbRntHrYfd0fTjnJy': [{'Symbol': 'CPAH', 'cnt': '16.0'}], 'var_call_4lhzLvUWwnZnwTKZmAMPz2qj': [{'Symbol': 'CUBA', 'cnt': '0.0'}], 'var_call_RiLsq0g7ZfXxMP3rWhcubVZQ': [{'Symbol': 'CVV', 'cnt': '0.0'}], 'var_call_sDTZaRM9FQZTLabkaB3FOtBo': [{'Symbol': 'DZSI', 'cnt': '1.0'}], 'var_call_dIqBdI1Gpm8eitnqKy82L3sc': [{'Symbol': 'ELSE', 'cnt': '0.0'}], 'var_call_2ahf6uez6ZF6BMI8W6VRqsoX': [{'Symbol': 'EXPC', 'cnt': '0.0'}], 'var_call_GwrUpk8GOO8iyvw5RBEvGoWa': [{'Symbol': 'EYEG', 'cnt': '18.0'}], 'var_call_qta5Z9BU78swGZ1mwSPGu3c9': [{'Symbol': 'FAMI', 'cnt': '23.0'}], 'var_call_HF04rpUCU0mW0QlRKBQSNx70': [{'Symbol': 'FNCB', 'cnt': '1.0'}], 'var_call_0WEgNwE4rpCWuvWHG0uOY1ZL': [{'Symbol': 'FSBW', 'cnt': '0.0'}], 'var_call_UFAynQs9DKl2SXbBARSkGEHE': [{'Symbol': 'FTFT', 'cnt': '21.0'}], 'var_call_zwq6L15g4UuMBb1IXz0zm6X1': [{'Symbol': 'GDYN', 'cnt': '0.0'}], 'var_call_UF6xZcYWspwSyoXEaSL0onV2': [{'Symbol': 'GLG', 'cnt': '42.0'}], 'var_call_ck9i5iceCy3nn8EpiD18Z1Xc': [{'Symbol': 'GRNVU', 'cnt': '0.0'}], 'var_call_qLYMlTerD7Rh5lJRZZRKRFsH': [{'Symbol': 'GTEC', 'cnt': '0.0'}], 'var_call_Bufi2CC1SQ3XraNdKhVUwxz2': [{'Symbol': 'HCCOU', 'cnt': '0.0'}], 'var_call_F3yTd8yF4mRRK1nJwvckodw8': [{'Symbol': 'HNNA', 'cnt': '0.0'}], 'var_call_DfQod4uimWujOZRqbQQ4bjbh': [{'Symbol': 'HQI', 'cnt': '2.0'}], 'var_call_k2jCXJpRkq2gXGrMOTUA0UFx': [{'Symbol': 'HRTX', 'cnt': '1.0'}], 'var_call_IsCuEIPSLy2kriApVXgO3553': [{'Symbol': 'IDEX', 'cnt': '15.0'}], 'var_call_39uAB9Iiti9YZfFbZ9jdpNmJ': [{'Symbol': 'IGIC', 'cnt': '0.0'}], 'var_call_jA2XcrZ7rxB6KolLkpNihWxF': [{'Symbol': 'IOTS', 'cnt': '1.0'}], 'var_call_HZ4dCeyvU6dZJJJy4A230HKF': [{'Symbol': 'ISNS', 'cnt': '0.0'}], 'var_call_QfJUEgRjiwFojEgLRsJTnkN5': [{'Symbol': 'ITI', 'cnt': '0.0'}], 'var_call_1YAWZpXBxMTKhWkcM8tK1L7X': [{'Symbol': 'LACQ', 'cnt': '0.0'}], 'var_call_LsBmJxLHRwCE8UK8yjVb83bz': [{'Symbol': 'MBCN', 'cnt': '0.0'}], 'var_call_YCAE3W1qxYm8JrSzdJt2BXzj': [{'Symbol': 'MBNKP', 'cnt': '0.0'}], 'var_call_HgAu4PexAUtPFk9jB5ECrri6': [{'Symbol': 'MCEP', 'cnt': '14.0'}], 'var_call_nMaQA85ICt8GRFw6pLoOu6OV': [{'Symbol': 'MLND', 'cnt': '3.0'}], 'var_call_Qb8YyPTqutzdxelX221esz3r': [{'Symbol': 'MMAC', 'cnt': '1.0'}], 'var_call_TzyfAm3vpUWg4uFNU3nCZcZj': [{'Symbol': 'MNCLU', 'cnt': '0.0'}], 'var_call_o6b1N6W2lMj0LnQ54y2cEBNC': [{'Symbol': 'MNPR', 'cnt': '4.0'}], 'var_call_y1WrurFZwjSxjeWs2sxPVQmv': [{'Symbol': 'NVEE', 'cnt': '1.0'}], 'var_call_D5JiLiquGVAQ7KnXQgykKdaO': [{'Symbol': 'NXTD', 'cnt': '15.0'}], 'var_call_eiee5jfGvBQf1tjThsYN5o40': [{'Symbol': 'OPOF', 'cnt': '0.0'}], 'var_call_uzSdgYNoCDZUZ5lQnN0L83IK': [{'Symbol': 'OPTT', 'cnt': '12.0'}], 'var_call_Pv0JHwVrfTC78zmCm1RtGaVV': [{'Symbol': 'ORGO', 'cnt': '15.0'}], 'var_call_pNP0UkHCT8qCNXCl2UK54OAH': [{'Symbol': 'ORSNU', 'cnt': '0.0'}], 'var_call_rHNCWKfyBOWsyvFEeaZIJ22E': [{'Symbol': 'OTEL', 'cnt': '1.0'}], 'var_call_X9Pu1bzMfMBGLlaE39D0MZ9N': [{'Symbol': 'PBFS', 'cnt': '0.0'}], 'var_call_j5eQ6ZWfgAktToHxt95TDf6e': [{'Symbol': 'PBTS', 'cnt': '8.0'}], 'var_call_sztaplgA1byLtH2ZRMZUmyL8': [{'Symbol': 'PCSB', 'cnt': '0.0'}], 'var_call_QvFYxqP1uW7rbdJis4yBuLnN': [{'Symbol': 'PECK', 'cnt': '19.0'}], 'var_call_bxdvSYeE0lNAzFPUL3dftMdY': [{'Symbol': 'PEIX', 'cnt': '12.0'}], 'var_call_1LVw27ENJqpjxRUwGDyJhRAT': [{'Symbol': 'PFIE', 'cnt': '2.0'}], 'var_call_f4vgs09T8TKOQghSOi6sgZkn': [{'Symbol': 'PLIN', 'cnt': '1.0'}], 'var_call_UrATvE8EWONOhMdO0OTle5HP': [{'Symbol': 'POPE', 'cnt': '0.0'}], 'var_call_lFevXayQYiDmgmr9tl7FAW8j': [{'Symbol': 'QRHC', 'cnt': '3.0'}], 'var_call_q9FGl2jNuHTNHSsq1ZEby7Sp': [{'Symbol': 'SES', 'cnt': '51.0'}], 'var_call_qZcXqPPDC8iy8xsj0dCsHqkO': [{'Symbol': 'SHSP', 'cnt': '1.0'}], 'var_call_vSfuFr6bBxoym5ePX6B1XYsb': [{'Symbol': 'SNSS', 'cnt': '32.0'}], 'var_call_SGJuiOJPJWKqBdYhnn4K5Uw7': [{'Symbol': 'SSNT', 'cnt': '11.0'}], 'var_call_ONGDMeRlW9jApZbTplDeyrMX': [{'Symbol': 'STKS', 'cnt': '0.0'}], 'var_call_eYZGtUWjZKbXPaXJsWi0UYZ0': [{'Symbol': 'TGLS', 'cnt': '0.0'}], 'var_call_GQtEcZ7Ol11gQNOJFt2iCdxC': [{'Symbol': 'TMSR', 'cnt': '40.0'}], 'var_call_gOZWdSU8W2FpXk2STzemfhWl': [{'Symbol': 'VERB', 'cnt': '38.0'}], 'var_call_CrtWa23iJSghYF9GvVAvi9G7': [{'Symbol': 'VMD', 'cnt': '1.0'}], 'var_call_y3vHNju6NxQp6hJcd6jVMPiJ': [{'Symbol': 'VRRM', 'cnt': '0.0'}], 'var_call_VtVj0UKdwWCJ9cD1KBOXQTZ6': [{'Symbol': 'VTIQW', 'cnt': '6.0'}], 'var_call_5YxYa7R6sCrBtpqyBgoOGamp': [{'Symbol': 'VVPR', 'cnt': '14.0'}], 'var_call_oTuvybNWqSuyZSyC9ckb1kD9': [{'Symbol': 'WHLM', 'cnt': '0.0'}], 'var_call_06n5OjFaFEwrGwU7zzygGYH7': [{'Symbol': 'WHLR', 'cnt': '15.0'}], 'var_call_Jdua7NDAavdwVHWuwUSgYtt0': [{'Symbol': 'XBIOW', 'cnt': '7.0'}], 'var_call_lBUyAG85GzzkF6LzRrS2RdAW': [{'Symbol': 'XPEL', 'cnt': '4.0'}]}

exec(code, env_args)
