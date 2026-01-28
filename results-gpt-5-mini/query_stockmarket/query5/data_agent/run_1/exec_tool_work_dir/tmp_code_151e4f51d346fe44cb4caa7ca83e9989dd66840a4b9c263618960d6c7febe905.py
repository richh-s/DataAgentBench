code = """import json
# collect all var_call_* keys that include results
keys = [
 'var_call_o8w8mqCeZcjdjzDHsGoKkQcX','var_call_vkOHhv9z8XgSda6W8DWX1x0O','var_call_kXUVPZuwvNrKi10PTh3JkRHf','var_call_WTVScKBemyYsO3xsEdiBDIeQ',
 'var_call_IHiXEI4HqkTI340MI5NFQ70I','var_call_AScWe9vSkix49f3WK8L6gO7P','var_call_w52WaQmEaIJVw9BdnuTYLFDE','var_call_FWEFuHPcZ8WUgE0WrAAUFnqH',
 'var_call_ZXDJWb8dfhDhgUDhAsEjFabj','var_call_1OGQzt1TKCzFXHtld13XNv4K','var_call_YasOZ7YYBcBHCkCi2L0uR9sG','var_call_EUqZS8yuPJXNS7SsbpuGjFQO',
 'var_call_scbRZNgjO6eQrqOjcNSCwST4','var_call_wKIP7ZefyeX34a4Rf94xshNz','var_call_iY8y7BcSIzyE1uuWB2h1B9sM','var_call_dWR2dhQNALnn94YioPfYOu6f',
 'var_call_jGBJxJ3Dg6B4GsJXETYZIZfG','var_call_vZhZEVhozT6gaFbMx1FMe9Op','var_call_yENkn3KFT0JlHwiX8WgPLUOK','var_call_xRQt6cZMaxhsxBEQ5dZ4Wspi',
 'var_call_rgzLHnSiTw5R299clBCuKffJ','var_call_z2lyvGf6Yu9AXabSPIJk1ZWW','var_call_ga1ptFW8fgmt27o9N0TwnOOB','var_call_s4OE2HaXm3W6lvYDZMdtGHsa',
 'var_call_vZsrCn9uofBdRvZmptvf7kho','var_call_21FCOTjuNPjLe7e7ui4qKYNd','var_call_wDERUh0KHGV88Q1hJbtxUqUl','var_call_00s6y92PdAtc06s8an6Bty8s',
 'var_call_WUIL7gU5EOU9MaT46hJhYPv8','var_call_O9w2T4pjnDWv3ZUskUTyjpLt','var_call_O9w2T4pjnDWv3ZUskUTyjpLt','var_call_O9w2T4pjnDWv3ZUskUTyjpLt'
]
# But easier: gather all variables in globals matching prefix var_call_
import sys
vars = globals()
res = {}
for k,v in vars.items():
    if k.startswith('var_call_'):
        try:
            with open(v,'r') as f:
                val = json.load(f)
            # val is list like [{"symbol":..., "cnt": ...}]
            for rec in val:
                symbol = rec['symbol']
                cnt = rec['cnt']
                # convert to float if possible
                try:
                    cntf = float(cnt)
                except:
                    cntf = None
                res[symbol] = cntf
        except Exception as e:
            # skip if not a path or can't open
            pass

# sort and get top 5
sorted_syms = sorted(res.items(), key=lambda x: (x[1] if x[1] is not None else -1), reverse=True)
top5 = [s for s,c in sorted_syms[:5]]

# we also have mapping sym_to_name in earlier execute_python result file var_call_yu2THRxExb7QIgtsCuXUShDA
with open(var_call_yu2THRxExb7QIgtsCuXUShDA) as f:
    mapping = json.load(f)['sym_to_name']

names = [mapping.get(s,'') for s in top5]

output = {'top5_symbols': top5, 'company_names': names, 'counts': [res[s] for s in top5]}
print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_h4lURv0gsFsNbbGeJpA93oUb': 'file_storage/call_h4lURv0gsFsNbbGeJpA93oUb.json', 'var_call_wrrVFEISzbCFFa5DhbWeDDsL': 'file_storage/call_wrrVFEISzbCFFa5DhbWeDDsL.json', 'var_call_yu2THRxExb7QIgtsCuXUShDA': 'file_storage/call_yu2THRxExb7QIgtsCuXUShDA.json', 'var_call_o8w8mqCeZcjdjzDHsGoKkQcX': [{'symbol': 'AGMH', 'cnt': '13.0'}], 'var_call_vkOHhv9z8XgSda6W8DWX1x0O': [{'symbol': 'ALACU', 'cnt': '0.0'}], 'var_call_kXUVPZuwvNrKi10PTh3JkRHf': [{'symbol': 'AMHC', 'cnt': 'nan'}], 'var_call_WTVScKBemyYsO3xsEdiBDIeQ': [{'symbol': 'ANDA', 'cnt': '0.0'}], 'var_call_IHiXEI4HqkTI340MI5NFQ70I': [{'symbol': 'APEX', 'cnt': '15.0'}], 'var_call_AScWe9vSkix49f3WK8L6gO7P': [{'symbol': 'BCLI', 'cnt': '0.0'}], 'var_call_w52WaQmEaIJVw9BdnuTYLFDE': [{'symbol': 'BHAT', 'cnt': '10.0'}], 'var_call_FWEFuHPcZ8WUgE0WrAAUFnqH': [{'symbol': 'BIOC', 'cnt': '21.0'}], 'var_call_ZXDJWb8dfhDhgUDhAsEjFabj': [{'symbol': 'BKYI', 'cnt': '16.0'}], 'var_call_1OGQzt1TKCzFXHtld13XNv4K': [{'symbol': 'BLFS', 'cnt': '0.0'}], 'var_call_YasOZ7YYBcBHCkCi2L0uR9sG': [{'symbol': 'BOSC', 'cnt': '3.0'}], 'var_call_EUqZS8yuPJXNS7SsbpuGjFQO': [{'symbol': 'BOTJ', 'cnt': '0.0'}], 'var_call_scbRZNgjO6eQrqOjcNSCwST4': [{'symbol': 'BWEN', 'cnt': '5.0'}], 'var_call_wKIP7ZefyeX34a4Rf94xshNz': [{'symbol': 'CBAT', 'cnt': '23.0'}], 'var_call_iY8y7BcSIzyE1uuWB2h1B9sM': [{'symbol': 'CCCL', 'cnt': '13.0'}], 'var_call_dWR2dhQNALnn94YioPfYOu6f': [{'symbol': 'CDMOP', 'cnt': '0.0'}], 'var_call_jGBJxJ3Dg6B4GsJXETYZIZfG': [{'symbol': 'CEMI', 'cnt': '3.0'}], 'var_call_vZhZEVhozT6gaFbMx1FMe9Op': [{'symbol': 'CFBK', 'cnt': '0.0'}], 'var_call_yENkn3KFT0JlHwiX8WgPLUOK': [{'symbol': 'CFFA', 'cnt': '0.0'}], 'var_call_xRQt6cZMaxhsxBEQ5dZ4Wspi': [{'symbol': 'CLRB', 'cnt': '14.0'}], 'var_call_rgzLHnSiTw5R299clBCuKffJ': [{'symbol': 'CORV', 'cnt': '10.0'}], 'var_call_z2lyvGf6Yu9AXabSPIJk1ZWW': [{'symbol': 'CPAAU', 'cnt': '0.0'}], 'var_call_ga1ptFW8fgmt27o9N0TwnOOB': [{'symbol': 'CPAH', 'cnt': '16.0'}], 'var_call_s4OE2HaXm3W6lvYDZMdtGHsa': [{'symbol': 'CUBA', 'cnt': '0.0'}], 'var_call_vZsrCn9uofBdRvZmptvf7kho': [{'symbol': 'CVV', 'cnt': '0.0'}], 'var_call_21FCOTjuNPjLe7e7ui4qKYNd': [{'symbol': 'DZSI', 'cnt': '1.0'}], 'var_call_wDERUh0KHGV88Q1hJbtxUqUl': [{'symbol': 'ELSE', 'cnt': '0.0'}], 'var_call_00s6y92PdAtc06s8an6Bty8s': [{'symbol': 'EXPC', 'cnt': '0.0'}], 'var_call_WUIL7gU5EOU9MaT46hJhYPv8': [{'symbol': 'EYEG', 'cnt': '18.0'}], 'var_call_O9w2T4pjnDWv3ZUskUTyjpLt': [{'symbol': 'FAMI', 'cnt': '23.0'}], 'var_call_n1KCKmhuktjWXULpXC2rTqp7': [{'symbol': 'FNCB', 'cnt': '1.0'}], 'var_call_7MhglhpfhcBlP2gbAhL04DJn': [{'symbol': 'FSBW', 'cnt': '0.0'}], 'var_call_vNboIjQF9KshI7S5NtY8bBsw': [{'symbol': 'FTFT', 'cnt': '21.0'}], 'var_call_Wwe9lGyvXqPzpYP39vBBpW7g': [{'symbol': 'GDYN', 'cnt': '0.0'}], 'var_call_IttyL1Qvt0V5F6K7N0FUA32H': [{'symbol': 'GLG', 'cnt': '42.0'}], 'var_call_ERCvVqMwVmcjeTHIH3AZfSHP': [{'symbol': 'GRNVU', 'cnt': '0.0'}], 'var_call_3bB1Qw3TEATaLIyzo7HBm6CI': [{'symbol': 'GTEC', 'cnt': '0.0'}], 'var_call_MZVRJ0HJN4YdcEv65cRO6L6P': [{'symbol': 'HCCOU', 'cnt': '0.0'}], 'var_call_zaR958o8pnJZeCfPwp83kBaZ': [{'symbol': 'HNNA', 'cnt': '0.0'}], 'var_call_LZlnMQMJp4pAxjARxNqNaZwF': [{'symbol': 'HQI', 'cnt': '2.0'}], 'var_call_1dusSQHJBpW1I0dC3TtArBro': [{'symbol': 'HRTX', 'cnt': '1.0'}], 'var_call_TQTRscHYCnY42k6JuR7p20Za': [{'symbol': 'IDEX', 'cnt': '15.0'}], 'var_call_2NFDnjnSbPxXOCWnlNzGnTw8': [{'symbol': 'IGIC', 'cnt': '0.0'}], 'var_call_3YPw8tUqFWT2m8Tr3LM5aEcW': [{'symbol': 'IOTS', 'cnt': '1.0'}], 'var_call_DQIowO9gEJ4R1WFFf4vVfsTv': [{'symbol': 'ISNS', 'cnt': '0.0'}], 'var_call_JhUZXW6Jw4hVOXNB4I4O4zlM': [{'symbol': 'ITI', 'cnt': '0.0'}], 'var_call_4w5ERm792mxhaCUrOHqBx4Ef': [{'symbol': 'LACQ', 'cnt': '0.0'}], 'var_call_A89BfXWgCwUB6H7cBlrR5KK6': [{'symbol': 'MBCN', 'cnt': '0.0'}], 'var_call_jUValyH8wN3wraVxwXnuD9E4': [{'symbol': 'MBNKP', 'cnt': '0.0'}], 'var_call_HNSXaHYciqDTaJsBhdPSJXFD': [{'symbol': 'MCEP', 'cnt': '14.0'}], 'var_call_hEPch0xziYojWpils9EVrVZb': [{'symbol': 'MLND', 'cnt': '3.0'}], 'var_call_acZcb5C5EClYHBO48y2QLB7e': [{'symbol': 'MMAC', 'cnt': '1.0'}], 'var_call_KBTdO3ecyajROLB4eqGrRK4r': [{'symbol': 'MNCLU', 'cnt': '0.0'}], 'var_call_LldnK1zYsAWPFCH8sPiSSpiI': [{'symbol': 'MNPR', 'cnt': '4.0'}], 'var_call_JZuj9rUVUCWcUYsfHtAqLnwD': [{'symbol': 'NVEE', 'cnt': '1.0'}], 'var_call_LgRoorH4W0SjARsAsEc4tCKD': [{'symbol': 'NXTD', 'cnt': '15.0'}], 'var_call_tE4rucI2x7amNUaiK3wTxV5D': [{'symbol': 'OPOF', 'cnt': '0.0'}], 'var_call_Dje51Zz9N0fW98pHE5APuTvr': [{'symbol': 'OPTT', 'cnt': '12.0'}], 'var_call_7oKJOgyNAnVET5DwWPj9pDDH': [{'symbol': 'ORGO', 'cnt': '15.0'}], 'var_call_9Hd17Iw4kFdIcXfIPuaDp6yA': [{'symbol': 'ORSNU', 'cnt': '0.0'}], 'var_call_56yS6pYOU4N2Kd5ZLOz4SJua': [{'symbol': 'OTEL', 'cnt': '1.0'}], 'var_call_JZkMlHq7XmJMQZE1b6oaQKq7': [{'symbol': 'PBFS', 'cnt': '0.0'}], 'var_call_kEEBvp4NDye3eyNtJtmvpBqp': [{'symbol': 'PBTS', 'cnt': '8.0'}], 'var_call_9jtjTF2a2XEDTlJoEWjWEI05': [{'symbol': 'PCSB', 'cnt': '0.0'}], 'var_call_iEwpCgw9vHxJnE5BNPWEnM3E': [{'symbol': 'PECK', 'cnt': '19.0'}], 'var_call_OGXLAB1Qh2N9tizRtPOQ6OoM': [{'symbol': 'PEIX', 'cnt': '12.0'}], 'var_call_N7JR41IIlKGN5Nkpr0oEECMI': [{'symbol': 'PFIE', 'cnt': '2.0'}], 'var_call_kcn9AzgtmBOR0xFVwxTyZjPE': [{'symbol': 'PLIN', 'cnt': '1.0'}], 'var_call_aRLPScKAFyYcVEdtUcMke9yU': [{'symbol': 'POPE', 'cnt': '0.0'}], 'var_call_ETZmewLQjbQwrYzOr2JWYVWX': [{'symbol': 'QRHC', 'cnt': '3.0'}], 'var_call_jQkZ4nm74oar818FsqKiKqAT': [{'symbol': 'SES', 'cnt': '51.0'}], 'var_call_v1rrxJnQ1JLNzo72gvyYQh2K': [{'symbol': 'SHSP', 'cnt': '1.0'}], 'var_call_8f0vD20klqwIJFFi21G6t682': [{'symbol': 'SNSS', 'cnt': '32.0'}], 'var_call_X3DlLVU57YVEh7ZPALxniWco': [{'symbol': 'SSNT', 'cnt': '11.0'}], 'var_call_Zd6egbyf4wfcL0bZPG4vfcYy': [{'symbol': 'STKS', 'cnt': '0.0'}], 'var_call_mrzNqwYcibfmKZxLmrD69g2T': [{'symbol': 'TGLS', 'cnt': '0.0'}], 'var_call_aw68o7qrDX2bDFK5MmtACOua': [{'symbol': 'TMSR', 'cnt': '40.0'}], 'var_call_iastvNrRVsswc7mw8oS83bkk': [{'symbol': 'VERB', 'cnt': '38.0'}], 'var_call_gJyiVreelamb0jYdznJQlouw': [{'symbol': 'VMD', 'cnt': '1.0'}], 'var_call_sva126VdnRg7FGHjadafWfbY': [{'symbol': 'VRRM', 'cnt': '0.0'}], 'var_call_XFw8ugquGyMqFxxLASxpvEji': [{'symbol': 'VTIQW', 'cnt': '6.0'}], 'var_call_7mDRT2Ii8D3uY3QIt19NdAR9': [{'symbol': 'VVPR', 'cnt': '14.0'}], 'var_call_RalvLUHMI80goQdPG7VHYdZk': [{'symbol': 'WHLM', 'cnt': '0.0'}], 'var_call_FEjnPiwSJ3j7IcxEcig6OZYh': [{'symbol': 'WHLR', 'cnt': '15.0'}], 'var_call_YPs2xCxXBTFR1rPXzKTtKoQX': [{'symbol': 'XBIOW', 'cnt': '7.0'}], 'var_call_FXm2FtLOVtngi03AeTjeIZ0O': [{'symbol': 'XPEL', 'cnt': '4.0'}]}

exec(code, env_args)
