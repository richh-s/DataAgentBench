code = """import json
# Load stockinfo records
with open(var_call_HAt9M4wuI99epIwp2jtvWXhA, 'r') as f:
    stockinfo_records = json.load(f)
# Build symbol -> company name mapping from stockinfo
sym_to_name = {r['Symbol']: r['Company Description'] for r in stockinfo_records}

# Map of symbol to the var_call key holding its count
symbol_key_map = {
    'AGMH':'var_call_KZKnEkyPEU6Cc1LTzmiDRnXq',
    'ALACU':'var_call_b7EKKNWDAxaOwHTf2JMoMJpL',
    'AMHC':'var_call_ocVwhbFA9MlDfvhQmMgc76UY',
    'ANDA':'var_call_hq53pE2bqP3KW8MDqSk9Rgqo',
    'APEX':'var_call_EUk3XT7KQ9ZjFuAED18R39Bb',
    'BCLI':'var_call_9uwUWi4g5n2b1u6Q81KtGrRe',
    'BHAT':'var_call_mjokjFPOpVbd4sOL8NDyHo3n',
    'BIOC':'var_call_tldwKHJlrSscjXWTl5GRTMoj',
    'BKYI':'var_call_sJFgWJoNW1P3rRsLXEEzwKMe',
    'BLFS':'var_call_1isLy9gPbYHGoscr3YctttgR',
    'BOSC':'var_call_u9fYrHojoBWe35pgww8pQBtl',
    'BOTJ':'var_call_ptTGeCnNsgPSNd1oDrNjA29k',
    'BWEN':'var_call_TMZ3spqYue9Iwaskx75fXUbM',
    'CBAT':'var_call_h5Nh4NqYyoIWXzM8NC7PCViY',
    'CCCL':'var_call_VH4WV0xks2UbFFwM3ENpehke',
    'CDMOP':'var_call_X0IXumjETXAQ07rTUfV1qo91',
    'CEMI':'var_call_YJZFE9prCIq8zXbnBaPEbgmU',
    'CFBK':'var_call_uVkntWRDwKmz993CRSo0KHQq',
    'CFFA':'var_call_TrqGnWVjJlqQas8DSNbZUM1B',
    'CLRB':'var_call_KJjxGoYNezQ4EegOjOpZQLRR',
    'CORV':'var_call_yvS4041ylgKhiyqRs68SEIO4',
    'CPAAU':'var_call_Qgo4hK7brdiiRQvBgFQaFbHy',
    'CPAH':'var_call_rmz1kgtNGjX2BoEqgMsU3Zps',
    'CUBA':'var_call_ZK9aJjBDcXdWRYXyzWzaV1j4',
    'CVV':'var_call_TOMACUXw2LamEp0azyw00hh7',
    'DZSI':'var_call_LhPsfB6TOtncn8uGeN7fliOp',
    'ELSE':'var_call_Hw2oOKtyS38tmWrhS4MMU8FV',
    'EXPC':'var_call_Bb2tTpH2Z8yjVG9RmRXqKYsK',
    'EYEG':'var_call_VOC7Hvp9jqFO8PjlHkBd4bBR',
    'FAMI':'var_call_YjsVnKYo2gKfoBnAfIccYJ8T',
    'FNCB':'var_call_0M65pc1aqYZteeUk8eglxLXD',
    'FSBW':'var_call_dHv6qNIzlyz9DTB2qz3H503l',
    'FTFT':'var_call_rykP9zQBoU4SE1LSgUL10ZgX',
    'GDYN':'var_call_2uMYLbCWpPdylapNDxayyvfo',
    'GLG':'var_call_8dD31YJSpWaYk7cJOsvKGRmN',
    'GRNVU':'var_call_MpFJENjALzJsiU8kualP7GCd',
    'GTEC':'var_call_Zp4qF2B5UtHOOJJqOtseyObu',
    'HCCOU':'var_call_FKhrzi6e9l2YGC4NPOL7QYX6',
    'HNNA':'var_call_YEh63uqZnNK78Lk5B1mv28ar',
    'HQI':'var_call_wG3wvzyACArJLoKWIzXF0mHN',
    'HRTX':'var_call_MVJQHL3jBwYqcHdj8wui6Z3K',
    'IDEX':'var_call_S2950JHk4SA4s5fVSdjvckeN',
    'IGIC':'var_call_F1HcbjwACYnXARjaYdWp25HL',
    'IOTS':'var_call_evuh2WS35udMJRuvxnbOo0QG',
    'ISNS':'var_call_ZzwPX8LCNc8nQE64xmH4H39K',
    'ITI':'var_call_zbVHydFH4Vqu1PSZiwfPpIoU',
    'LACQ':'var_call_t5Hx9nAX2oL5Ebrq3v9sTVbE',
    'MBCN':'var_call_XyqFj2HcB0WrkJNHc21wZlBw',
    'MBNKP':'var_call_meeh5gcrzP6wtsQMF8cRvi4M',
    'MCEP':'var_call_SnNVvDKH6uMJd0cGjLUscC9m',
    'MLND':'var_call_mPoew4vzS9hapN0Z9V8ZqZcM',
    'MMAC':'var_call_gUdU4j4ljT674MCwCvBJbW8k',
    'MNCLU':'var_call_eqvNPeMx4omdrlRMvmK1KbI7',
    'MNPR':'var_call_KlEBUfEYhsPlLQ0PZpjw8ofP',
    'NVEE':'var_call_iAIRlwUK1UZbyeJZ65KCwz4F',
    'NXTD':'var_call_upjGSGAUFMOxoDjwdrbujoFB',
    'OPOF':'var_call_QetFoJqO0sSaiz4mAgGW4seA',
    'OPTT':'var_call_baZGPQl0Kj9OJEeKbbATUO3W',
    'ORGO':'var_call_lORPLZRcR4vKTtJdWjKKlnOh',
    'ORSNU':'var_call_iqLhbfcEbldBZYwpt4pMvYqA',
    'OTEL':'var_call_kNgzQzLlga1zMIPLjtp7cFc0',
    'PBFS':'var_call_2d2NKfQzXRU81oWH0hK83Vg5',
    'PBTS':'var_call_LUhv8w2siiPztkgNl5Kc1gPi',
    'PCSB':'var_call_ywZK2t5YhoKG5Rab31NN88uj',
    'PECK':'var_call_yycQXwMzgVQNc6huP5l5kKuk',
    'PEIX':'var_call_sho1S19uQFJZKev1qDIpYDGh',
    'PFIE':'var_call_xHzBIoGDmCMPOMq10bX6Z0UN',
    'PLIN':'var_call_ZsuwHkai2sLOq5bG0fIALR0E',
    'POPE':'var_call_ku0vQqO66YzgIiGEJmQrpHXM',
    'QRHC':'var_call_67MUkesx1ndkLwwTNBEihuAp',
    'SES':'var_call_yBvc1lYu4GUEAPGgH8twc5Jw',
    'SHSP':'var_call_1l0J0zczm9B6V9mplrjZAYFj',
    'SNSS':'var_call_ydTOzmChyVRdPa1OeFQJO50j',
    'SSNT':'var_call_XGOXOfY3YXq3Mf6hVYFf9hen',
    'STKS':'var_call_NL4ltcOHBOFPgtPAqoruXaie',
    'TGLS':'var_call_9poTEMiZonLKYWfRJ7fzXZuX',
    'TMSR':'var_call_OZoTLUDedwDS9Iv8JAWDuNdw',
    'VERB':'var_call_DPVJsSSHYFpicTeazz3uPnSQ',
    'VMD':'var_call_57rdEgETFuG2H2YLHljGaPFo',
    'VRRM':'var_call_1QRXDCKrm6e7ThWECmDbyvNn',
    'VTIQW':'var_call_mYIdKfbJBGsq0M5lj84Xw2ml',
    'VVPR':'var_call_KWzztHOoETBdycrTTtdCEY3G',
    'WHLM':'var_call_9Lua3dfwEWTBvOyHh0uYEUCR',
    'WHLR':'var_call_pooFTuUT36ZYwyzp7BeCl6jB',
    'XBIOW':'var_call_mmPZxfuKTwwG2lFy5Jm6Cbni',
    'XPEL':'var_call_FCx6nWRWIG09E6AHrReXSIJO'
}

# Retrieve counts
symbol_counts = {}
for sym, varname in symbol_key_map.items():
    try:
        cnt_rec = globals().get(varname)
        if isinstance(cnt_rec, str):
            # sometimes stored as a string with newline, try to json load
            try:
                parsed = json.loads(cnt_rec)
                cnt = int(parsed[0]['cnt'])
            except Exception:
                cnt = 0
        else:
            # expected list like [{"cnt": "N"}]
            if cnt_rec and isinstance(cnt_rec, list) and 'cnt' in cnt_rec[0]:
                cnt = int(cnt_rec[0]['cnt'])
            else:
                cnt = 0
    except Exception:
        cnt = 0
    symbol_counts[sym] = cnt

# Find top 5 symbols by count
top5 = sorted(symbol_counts.items(), key=lambda x: x[1], reverse=True)[:5]
# Map to company names (use description if available, otherwise symbol)
result_names = []
for sym, cnt in top5:
    name = sym_to_name.get(sym, sym)
    result_names.append(name)

print("__RESULT__:")
print(json.dumps(result_names))"""

env_args = {'var_call_HAt9M4wuI99epIwp2jtvWXhA': 'file_storage/call_HAt9M4wuI99epIwp2jtvWXhA.json', 'var_call_HS6IzjI77jyHAo9RyvUv10Of': 'file_storage/call_HS6IzjI77jyHAo9RyvUv10Of.json', 'var_call_huWxBzpZCVMZI3QbJE1sx9X7': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_KZKnEkyPEU6Cc1LTzmiDRnXq': [{'cnt': '13'}], 'var_call_b7EKKNWDAxaOwHTf2JMoMJpL': [{'cnt': '0'}], 'var_call_ocVwhbFA9MlDfvhQmMgc76UY': [{'cnt': '0'}], 'var_call_hq53pE2bqP3KW8MDqSk9Rgqo': [{'cnt': '0'}], 'var_call_EUk3XT7KQ9ZjFuAED18R39Bb': [{'cnt': '15'}], 'var_call_9uwUWi4g5n2b1u6Q81KtGrRe': [{'cnt': '0'}], 'var_call_mjokjFPOpVbd4sOL8NDyHo3n': [{'cnt': '10'}], 'var_call_tldwKHJlrSscjXWTl5GRTMoj': [{'cnt': '21'}], 'var_call_sJFgWJoNW1P3rRsLXEEzwKMe': [{'cnt': '16'}], 'var_call_1isLy9gPbYHGoscr3YctttgR': [{'cnt': '0'}], 'var_call_u9fYrHojoBWe35pgww8pQBtl': [{'cnt': '3'}], 'var_call_ptTGeCnNsgPSNd1oDrNjA29k': [{'cnt': '0'}], 'var_call_TMZ3spqYue9Iwaskx75fXUbM': [{'cnt': '5'}], 'var_call_h5Nh4NqYyoIWXzM8NC7PCViY': [{'cnt': '23'}], 'var_call_VH4WV0xks2UbFFwM3ENpehke': [{'cnt': '13'}], 'var_call_X0IXumjETXAQ07rTUfV1qo91': [{'cnt': '0'}], 'var_call_YJZFE9prCIq8zXbnBaPEbgmU': [{'cnt': '3'}], 'var_call_uVkntWRDwKmz993CRSo0KHQq': [{'cnt': '0'}], 'var_call_TrqGnWVjJlqQas8DSNbZUM1B': [{'cnt': '0'}], 'var_call_KJjxGoYNezQ4EegOjOpZQLRR': [{'cnt': '14'}], 'var_call_yvS4041ylgKhiyqRs68SEIO4': [{'cnt': '10'}], 'var_call_Qgo4hK7brdiiRQvBgFQaFbHy': [{'cnt': '0'}], 'var_call_rmz1kgtNGjX2BoEqgMsU3Zps': [{'cnt': '16'}], 'var_call_ZK9aJjBDcXdWRYXyzWzaV1j4': [{'cnt': '0'}], 'var_call_TOMACUXw2LamEp0azyw00hh7': [{'cnt': '0'}], 'var_call_LhPsfB6TOtncn8uGeN7fliOp': [{'cnt': '1'}], 'var_call_Hw2oOKtyS38tmWrhS4MMU8FV': [{'cnt': '0'}], 'var_call_Bb2tTpH2Z8yjVG9RmRXqKYsK': [{'cnt': '0'}], 'var_call_VOC7Hvp9jqFO8PjlHkBd4bBR': [{'cnt': '18'}], 'var_call_YjsVnKYo2gKfoBnAfIccYJ8T': [{'cnt': '23'}], 'var_call_0M65pc1aqYZteeUk8eglxLXD': [{'cnt': '1'}], 'var_call_dHv6qNIzlyz9DTB2qz3H503l': [{'cnt': '0'}], 'var_call_rykP9zQBoU4SE1LSgUL10ZgX': [{'cnt': '21'}], 'var_call_2uMYLbCWpPdylapNDxayyvfo': [{'cnt': '0'}], 'var_call_8dD31YJSpWaYk7cJOsvKGRmN': [{'cnt': '42'}], 'var_call_MpFJENjALzJsiU8kualP7GCd': [{'cnt': '0'}], 'var_call_Zp4qF2B5UtHOOJJqOtseyObu': [{'cnt': '0'}], 'var_call_FKhrzi6e9l2YGC4NPOL7QYX6': [{'cnt': '0'}], 'var_call_YEh63uqZnNK78Lk5B1mv28ar': [{'cnt': '0'}], 'var_call_wG3wvzyACArJLoKWIzXF0mHN': [{'cnt': '2'}], 'var_call_MVJQHL3jBwYqcHdj8wui6Z3K': [{'cnt': '1'}], 'var_call_S2950JHk4SA4s5fVSdjvckeN': [{'cnt': '15'}], 'var_call_F1HcbjwACYnXARjaYdWp25HL': [{'cnt': '0'}], 'var_call_evuh2WS35udMJRuvxnbOo0QG': [{'cnt': '1'}], 'var_call_ZzwPX8LCNc8nQE64xmH4H39K': [{'cnt': '0'}], 'var_call_zbVHydFH4Vqu1PSZiwfPpIoU': [{'cnt': '0'}], 'var_call_t5Hx9nAX2oL5Ebrq3v9sTVbE': [{'cnt': '0'}], 'var_call_XyqFj2HcB0WrkJNHc21wZlBw': [{'cnt': '0'}], 'var_call_meeh5gcrzP6wtsQMF8cRvi4M': [{'cnt': '0'}], 'var_call_SnNVvDKH6uMJd0cGjLUscC9m': [{'cnt': '14'}], 'var_call_mPoew4vzS9hapN0Z9V8ZqZcM': [{'cnt': '3'}], 'var_call_gUdU4j4ljT674MCwCvBJbW8k': [{'cnt': '1'}], 'var_call_eqvNPeMx4omdrlRMvmK1KbI7': [{'cnt': '0'}], 'var_call_KlEBUfEYhsPlLQ0PZpjw8ofP': [{'cnt': '4'}], 'var_call_iAIRlwUK1UZbyeJZ65KCwz4F': [{'cnt': '1'}], 'var_call_upjGSGAUFMOxoDjwdrbujoFB': [{'cnt': '15'}], 'var_call_QetFoJqO0sSaiz4mAgGW4seA': [{'cnt': '0'}], 'var_call_baZGPQl0Kj9OJEeKbbATUO3W': [{'cnt': '12'}], 'var_call_lORPLZRcR4vKTtJdWjKKlnOh': [{'cnt': '15'}], 'var_call_iqLhbfcEbldBZYwpt4pMvYqA': [{'cnt': '0'}], 'var_call_kNgzQzLlga1zMIPLjtp7cFc0': [{'cnt': '1'}], 'var_call_2d2NKfQzXRU81oWH0hK83Vg5': [{'cnt': '0'}], 'var_call_LUhv8w2siiPztkgNl5Kc1gPi': [{'cnt': '8'}], 'var_call_ywZK2t5YhoKG5Rab31NN88uj': [{'cnt': '0'}], 'var_call_yycQXwMzgVQNc6huP5l5kKuk': [{'cnt': '19'}], 'var_call_sho1S19uQFJZKev1qDIpYDGh': [{'cnt': '12'}], 'var_call_xHzBIoGDmCMPOMq10bX6Z0UN': [{'cnt': '2'}], 'var_call_ZsuwHkai2sLOq5bG0fIALR0E': [{'cnt': '1'}], 'var_call_ku0vQqO66YzgIiGEJmQrpHXM': [{'cnt': '0'}], 'var_call_67MUkesx1ndkLwwTNBEihuAp': [{'cnt': '3'}], 'var_call_yBvc1lYu4GUEAPGgH8twc5Jw': [{'cnt': '51'}], 'var_call_1l0J0zczm9B6V9mplrjZAYFj': [{'cnt': '1'}], 'var_call_ydTOzmChyVRdPa1OeFQJO50j': [{'cnt': '32'}], 'var_call_XGOXOfY3YXq3Mf6hVYFf9hen': [{'cnt': '11'}], 'var_call_NL4ltcOHBOFPgtPAqoruXaie': [{'cnt': '0'}], 'var_call_9poTEMiZonLKYWfRJ7fzXZuX': [{'cnt': '0'}], 'var_call_OZoTLUDedwDS9Iv8JAWDuNdw': [{'cnt': '40'}], 'var_call_DPVJsSSHYFpicTeazz3uPnSQ': [{'cnt': '38'}], 'var_call_57rdEgETFuG2H2YLHljGaPFo': [{'cnt': '1'}], 'var_call_1QRXDCKrm6e7ThWECmDbyvNn': [{'cnt': '0'}], 'var_call_mYIdKfbJBGsq0M5lj84Xw2ml': [{'cnt': '6'}], 'var_call_KWzztHOoETBdycrTTtdCEY3G': [{'cnt': '14'}], 'var_call_9Lua3dfwEWTBvOyHh0uYEUCR': [{'cnt': '0'}], 'var_call_pooFTuUT36ZYwyzp7BeCl6jB': [{'cnt': '15'}], 'var_call_mmPZxfuKTwwG2lFy5Jm6Cbni': [{'cnt': '7'}], 'var_call_FCx6nWRWIG09E6AHrReXSIJO': [{'cnt': '4'}]}

exec(code, env_args)
