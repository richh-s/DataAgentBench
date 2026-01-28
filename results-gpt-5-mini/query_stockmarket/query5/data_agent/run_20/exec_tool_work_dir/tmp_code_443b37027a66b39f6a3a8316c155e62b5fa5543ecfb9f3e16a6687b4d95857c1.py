code = """import json, os
# Collect all var_call_* variables injected into this environment
vars_dict = {k: v for k, v in globals().items() if k.startswith('var_call_')}

counts = {}
mapping = None

for k, v in vars_dict.items():
    # Resolve v: if it's a file path, load JSON from it
    data = None
    if isinstance(v, str) and os.path.exists(v):
        try:
            with open(v, 'r') as f:
                data = json.load(f)
        except Exception:
            # maybe it's a simple string result, skip
            continue
    else:
        data = v

    # Check for mapping structure
    if isinstance(data, dict) and 'mapping' in data and 'symbols' in data:
        mapping = data['mapping']
        # continue to next
        continue

    # If data is a list of query results like [{"symbol": "AGMH", "cnt": "13"}]
    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        first = data[0]
        if 'symbol' in first and 'cnt' in first:
            for rec in data:
                sym = rec.get('symbol')
                try:
                    cnt = int(rec.get('cnt', 0))
                except Exception:
                    # sometimes cnt may be numeric already
                    try:
                        cnt = int(float(rec.get('cnt', 0)))
                    except Exception:
                        cnt = 0
                counts[sym] = counts.get(sym, 0) + cnt

# If mapping still None, try to load the original stockinfo result file
if mapping is None:
    # look for a var_call that contains a list of dicts with 'Symbol' and 'Company Description'
    for k, v in vars_dict.items():
        data = None
        if isinstance(v, str) and os.path.exists(v):
            try:
                with open(v, 'r') as f:
                    data = json.load(f)
            except Exception:
                continue
        else:
            data = v
        if isinstance(data, list) and len(data)>0 and isinstance(data[0], dict) and 'Symbol' in data[0] and 'Company Description' in data[0]:
            mapping = {rec['Symbol']: rec['Company Description'] for rec in data}
            break

# Now get top 5 symbols by count
sorted_syms = sorted(counts.items(), key=lambda x: x[1], reverse=True)
top5 = sorted_syms[:5]

# Prepare final company names list
result = []
for sym, cnt in top5:
    name = None
    if mapping and sym in mapping:
        name = mapping[sym]
    else:
        name = sym
    result.append({"symbol": sym, "company": name, "count": cnt})

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_0E5QaHvjoVMRvwUB85CQmhze': 'file_storage/call_0E5QaHvjoVMRvwUB85CQmhze.json', 'var_call_djPIRwcWq4NijOTf6t11m3o0': 'file_storage/call_djPIRwcWq4NijOTf6t11m3o0.json', 'var_call_7ayJpBJjIgtxiWcxwSbdLBKo': 'file_storage/call_7ayJpBJjIgtxiWcxwSbdLBKo.json', 'var_call_v8BoQ4byq3LbAndnRgRGtWW6': 'file_storage/call_v8BoQ4byq3LbAndnRgRGtWW6.json', 'var_call_9k7cEmQHYN2yAjaZ2Wu7qsw5': 'file_storage/call_9k7cEmQHYN2yAjaZ2Wu7qsw5.json', 'var_call_BzJIn7AOWGZkVhukTvWPbbCm': 'file_storage/call_BzJIn7AOWGZkVhukTvWPbbCm.json', 'var_call_n9XP60mxs6sQqQC66oXBVi0D': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_Nz2EuHUi0pr9vZZxKGbaMab2': [{'symbol': 'AGMH', 'cnt': '13'}], 'var_call_46mss3u0tQbNFnlCP9SzPsir': [{'symbol': 'ALACU', 'cnt': '0'}], 'var_call_JsinfehdznxlhqNE7tj0prRZ': [{'symbol': 'AMHC', 'cnt': '0'}], 'var_call_626gvc0gr6aXnVV1HsAyY03p': [{'symbol': 'ANDA', 'cnt': '0'}], 'var_call_jgD41PkwvxFV9gP2GZch3kNL': [{'symbol': 'APEX', 'cnt': '15'}], 'var_call_k4RylgkwRrhU3sLq7DvExmXV': [{'symbol': 'BCLI', 'cnt': '0'}], 'var_call_XkMO3lLjqEwERmpg70NEm0Bj': [{'symbol': 'BHAT', 'cnt': '10'}], 'var_call_3iSdpIiWSTICATTJlQknNLeG': [{'symbol': 'BIOC', 'cnt': '21'}], 'var_call_XkhYyXroJUetGEBd3NPojjTT': [{'symbol': 'BKYI', 'cnt': '16'}], 'var_call_ZXaksnRQmUsQO9kbNjtqBgEp': [{'symbol': 'BLFS', 'cnt': '0'}], 'var_call_sh0YN988gjh6m9MUDzWOMGnv': [{'symbol': 'BOSC', 'cnt': '3'}], 'var_call_2u0liQJ5Go1QZHU5Hl0IWOG4': [{'symbol': 'BOTJ', 'cnt': '0'}], 'var_call_XUxypRs6mZoTPjOx0mYT9pfF': [{'symbol': 'BWEN', 'cnt': '5'}], 'var_call_B4XtxbIV7KkH0ngpRApddd7g': [{'symbol': 'CBAT', 'cnt': '23'}], 'var_call_E487MWL4GXC3vZp30iOm3Zu5': [{'symbol': 'CCCL', 'cnt': '13'}], 'var_call_tPnfDDsVOdwa1UtM8GZValYd': [{'symbol': 'CDMOP', 'cnt': '0'}], 'var_call_2ZYyw7rz2J18oIgLJ2anKuJr': [{'symbol': 'CEMI', 'cnt': '3'}], 'var_call_VZ3oNTnzVdsluy2Woerih3Jd': [{'symbol': 'CFBK', 'cnt': '0'}], 'var_call_cq6voumNbiDkCvERraOSY4fz': [{'symbol': 'CFFA', 'cnt': '0'}], 'var_call_dT2SMIe3VDOmp9nh3EJXWfp0': [{'symbol': 'CLRB', 'cnt': '14'}], 'var_call_wV7FelYC66lhehcvB9Scqt0P': [{'symbol': 'CORV', 'cnt': '10'}], 'var_call_z2hjL5Wo6LBdr1RPoCthW2bS': [{'symbol': 'CPAAU', 'cnt': '0'}], 'var_call_1gTeYfZmA2MYKSpa81rYLaNb': [{'symbol': 'CPAH', 'cnt': '16'}], 'var_call_bou8mvPYzcPvfE2f8pgy0vzP': [{'symbol': 'CUBA', 'cnt': '0'}], 'var_call_CHMeRBUXxnquR4b9KjybXEao': [{'symbol': 'CVV', 'cnt': '0'}], 'var_call_tUBnjjasbY8SRUwGLmsjGejk': [{'symbol': 'DZSI', 'cnt': '1'}], 'var_call_DjzaGGnR3RZOguUBneMZEcje': [{'symbol': 'ELSE', 'cnt': '0'}], 'var_call_yfz9Acs4gTv7N7hYq2Byv262': [{'symbol': 'EXPC', 'cnt': '0'}], 'var_call_iv5G0iRfrnD82up4ehTTXDOA': [{'symbol': 'EYEG', 'cnt': '18'}], 'var_call_IjOUIWaAioQxBa1ncOzmC9Br': [{'symbol': 'FAMI', 'cnt': '23'}], 'var_call_Uu6xL5o25wwaSwrF99L8Y9Vq': [{'symbol': 'FNCB', 'cnt': '1'}], 'var_call_eVPVIfI0A96pvXlPRY3oEeEz': [{'symbol': 'FSBW', 'cnt': '0'}], 'var_call_FGw2RhrGOKZoLPCGQaLinTo7': [{'symbol': 'FTFT', 'cnt': '21'}], 'var_call_iAI8hfxli82654UBaQC68GKv': [{'symbol': 'GDYN', 'cnt': '0'}], 'var_call_44T0FOpAYEGaOx9M5lXlWSQz': [{'symbol': 'GLG', 'cnt': '42'}], 'var_call_8Mv5AKEQE8SKmWYEqgWzoZr8': [{'symbol': 'GRNVU', 'cnt': '0'}], 'var_call_xy2zH7rkD9dEnxiYLneltDWp': [{'symbol': 'GTEC', 'cnt': '0'}], 'var_call_SccicvqNvfCVL4tm9I8l8Ykq': [{'symbol': 'HCCOU', 'cnt': '0'}], 'var_call_wFLw1jloo2PxbY8TOUYzERYa': [{'symbol': 'HNNA', 'cnt': '0'}], 'var_call_ePpBbKmHX3PVQB2sokowzehB': [{'symbol': 'HQI', 'cnt': '2'}], 'var_call_us2kdRp38iG05erhsFxanKqz': [{'symbol': 'HRTX', 'cnt': '1'}], 'var_call_ymso7jMo0IKTcXYTX3EIOrCf': [{'symbol': 'IDEX', 'cnt': '15'}], 'var_call_ai6XIwTw7m0UOVrpGzHWsIvz': [{'symbol': 'IGIC', 'cnt': '0'}], 'var_call_IWZpiROziYCXVTEmMFqUiYMZ': [{'symbol': 'IOTS', 'cnt': '1'}], 'var_call_sPOKfnzEIg8bQT1hLXfoRNc6': [{'symbol': 'ISNS', 'cnt': '0'}], 'var_call_GLAjTuS1NXksuTiBPHccuM1r': [{'symbol': 'ITI', 'cnt': '0'}], 'var_call_1pZbmIlEVRjbI4Z6PJfo0wWx': [{'symbol': 'LACQ', 'cnt': '0'}], 'var_call_h7wzLkImGZqQpuTcxNV4JWh0': [{'symbol': 'MBCN', 'cnt': '0'}], 'var_call_Wl2gKdFxHVpb1PHJNlvp0vaD': [{'symbol': 'MBNKP', 'cnt': '0'}], 'var_call_RJL8pMsBuEm2H8DkF6eNEaI4': [{'symbol': 'MCEP', 'cnt': '14'}], 'var_call_RuASjV5y9DaJ8FXwMWWGnka1': [{'symbol': 'MLND', 'cnt': '3'}], 'var_call_epEkFyyaI4R69btcVQUfzSUv': [{'symbol': 'MMAC', 'cnt': '1'}], 'var_call_jUb0DTiZ6eL8zfIqhuBjtUEN': [{'symbol': 'MNCLU', 'cnt': '0'}], 'var_call_Z8hyeKfjX75wmONkXvIA9iY2': [{'symbol': 'MNPR', 'cnt': '4'}], 'var_call_PL5l2NQE2mOe0f0rptbo0Wzu': [{'symbol': 'NVEE', 'cnt': '1'}], 'var_call_6soEVbc8qlz6rWc1cglcec6b': [{'symbol': 'NXTD', 'cnt': '15'}], 'var_call_ZNckVsuxVR6iJ0LKTQf6YDLB': [{'symbol': 'OPOF', 'cnt': '0'}], 'var_call_1Vv1qXuPCRFruL28eBC7QgWe': [{'symbol': 'OPTT', 'cnt': '12'}], 'var_call_eHEUJdUgBCGi49leuOpAz1oM': [{'symbol': 'ORGO', 'cnt': '15'}], 'var_call_ITrmLm19ZoI3NZFoBjDIpIDM': [{'symbol': 'ORSNU', 'cnt': '0'}], 'var_call_7sMnukR3oXoHNet4q9dtqMoy': [{'symbol': 'OTEL', 'cnt': '1'}], 'var_call_7efZq86U9X8fBnMLN8OIdg5I': [{'symbol': 'PBFS', 'cnt': '0'}], 'var_call_PxjwTfvFxoWYiDLcPnQosXTq': [{'symbol': 'PBTS', 'cnt': '8'}], 'var_call_XgTJ5Y20e8BLIv5JIuvq3P0W': [{'symbol': 'PCSB', 'cnt': '0'}], 'var_call_XoWsIjNFIG2aAEefSeWmNCdy': [{'symbol': 'PECK', 'cnt': '19'}], 'var_call_APRnv3pxqUCsoY4NhZbwWagK': [{'symbol': 'PEIX', 'cnt': '12'}], 'var_call_umvCBHkZX0y0PC5YYZGGyY0O': [{'symbol': 'PFIE', 'cnt': '2'}], 'var_call_rmfziVM4XI9bgzNoUgBlNe95': [{'symbol': 'PLIN', 'cnt': '1'}], 'var_call_bYNYbbCfIcGJJuaBHsiPevEW': [{'symbol': 'POPE', 'cnt': '0'}], 'var_call_T6kDGN5AO0WgHs1KbwZbL7hs': [{'symbol': 'QRHC', 'cnt': '3'}], 'var_call_lyZGgF76TjPiucW7k33DkPZf': [{'symbol': 'SES', 'cnt': '51'}], 'var_call_EpefuST801UpexIdD3TrKqET': [{'symbol': 'SHSP', 'cnt': '1'}], 'var_call_64Z2au1vCXJ2LMHlhgRnU5D4': [{'symbol': 'SNSS', 'cnt': '32'}], 'var_call_AXUMTmL73rgD5r9gObCoSZMw': [{'symbol': 'SSNT', 'cnt': '11'}], 'var_call_Gf51jJfPS3XKONP4EekwunO2': [{'symbol': 'STKS', 'cnt': '0'}], 'var_call_OnzJXp2ad70yFPYexoMzBvMd': [{'symbol': 'TGLS', 'cnt': '0'}], 'var_call_CMjmASRweQyZvS6SDoLoZjUI': [{'symbol': 'TMSR', 'cnt': '40'}], 'var_call_cDoHbwKd9LWEqyPApKBQOiL3': [{'symbol': 'VERB', 'cnt': '38'}], 'var_call_U6UctyBwqgfMKPgKbZVnP2mL': [{'symbol': 'VMD', 'cnt': '1'}], 'var_call_CGxHZPKeJVfmssclqwulbTGK': [{'symbol': 'VRRM', 'cnt': '0'}], 'var_call_1lykHhOhCNOBK9oRLdJT1wQX': [{'symbol': 'VTIQW', 'cnt': '6'}], 'var_call_IvidZaerDzDu0O1n1WRucC7O': [{'symbol': 'VVPR', 'cnt': '14'}], 'var_call_QTQJUbmbfrN3IQuqaQsoxOLb': [{'symbol': 'WHLM', 'cnt': '0'}], 'var_call_JlkDcIqcOV5fQejW3o45gybe': [{'symbol': 'WHLR', 'cnt': '15'}], 'var_call_N3k4ePS3W5qx18djj9Q75wul': [{'symbol': 'XBIOW', 'cnt': '7'}], 'var_call_4cfzghQytlxVqdKzZAtMGa6c': [{'symbol': 'XPEL', 'cnt': '4'}]}

exec(code, env_args)
