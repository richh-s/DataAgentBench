code = """import json
# Mapping of storage keys to symbols
keys_and_symbols = [
    ("var_call_hZ7vZmQVN6GfzkiRSgY6s74W", "AGMH"),
    ("var_call_yzIdqy0TBkWf6aYrh70ai6S7", "ALACU"),
    ("var_call_9MRG5oCzHw51J95I6Zwbc66p", "AMHC"),
    ("var_call_Y8JzOAPntqHPvAXsDvyyyTVE", "ANDA"),
    ("var_call_jkqX88vulih6n0NyzObFL5jj", "APEX"),
    ("var_call_MB7l5DvGTnP4mEVKQbOErFkq", "BCLI"),
    ("var_call_2xg1k41I111TN5MAiFFzrCed", "BHAT"),
    ("var_call_5O645kIvXSEaTUJ6eftzEO8E", "BIOC"),
    ("var_call_pS9LFUxPNDxlMxY6BzTOYKTi", "BKYI"),
    ("var_call_fjzqcYrRwsljRZfSpiSlrN5A", "BLFS"),
    ("var_call_eV8JywNeHoyV5LDD338LxBs8", "BOSC"),
    ("var_call_BNWCzk5X4hgSHdJBbzKrhav9", "BOTJ"),
    ("var_call_hbzGnLLP0XBiTeddUnEemScw", "BWEN"),
    ("var_call_b9fQ1aE0z8gWwHtoUYfRU2kI", "CBAT"),
    ("var_call_5RTgx8PttqNUdUTzXKx8V6WN", "CCCL"),
    ("var_call_MRRCMFoTtRF0elYzNU40BiLi", "CDMOP"),
    ("var_call_F15b8A0xupKFwMwrs3elsK7s", "CEMI"),
    ("var_call_gmurFlpIxhugCkvwAwpUGjDN", "CFBK"),
    ("var_call_HZHVpxNczDp0YhwP1Bzqgi5d", "CFFA"),
    ("var_call_TJWNrLyXGpWCv01fCmjOwCzd", "CLRB"),
    ("var_call_Ly2UwWLYurBRJcPC1ENOgEnz", "CORV"),
    ("var_call_GfOzS2bkqACLUR3gxeVgjlq6", "CPAAU"),
    ("var_call_yynqoKxfo2vBhy2qC00hO57R", "CPAH"),
    ("var_call_bNRXc0EA6AMmyPKcVYm6kTRM", "CUBA"),
    ("var_call_C8IQGpCNlrD4KGDyW9nEcsfa", "CVV"),
    ("var_call_p3gWVooX5CSOxVA66j0lSggk", "DZSI"),
    ("var_call_VC84AsbLr3z7O9EhPaGTXdsL", "ELSE"),
    ("var_call_rqOXlfT6nngMwAZQFnvBIdHU", "EXPC"),
    ("var_call_Iuy5mo8qXUq1ZjWrSJKdgut2", "EYEG"),
    ("var_call_ZMWvEnSPz4w3SMI0YwvtIsfn", "FAMI"),
    ("var_call_dUGjUD0BXDaZEeBpr61bFJAz", "FNCB"),
    ("var_call_WcBST2DMRkwR3zYQLDX7U39l", "FSBW"),
    ("var_call_ZLieYOCPyJ781cBmYJRvlhCe", "FTFT"),
    ("var_call_D7nZehbcskAkoynb5adXlkF7", "GDYN"),
    ("var_call_S7lNFOLiCvIsSYynm00qj0A1", "GLG"),
    ("var_call_UrTd1gshVVHCApYKNz1rd0VT", "GRNVU"),
    ("var_call_5yj2MdrfngnCHJ0OjQlaUXNi", "GTEC"),
    ("var_call_22FsWG702uL8eZi8XvKEag27", "HCCOU"),
    ("var_call_DNEVRr5dwfi2T9nIzXEZU8GZ", "HNNA"),
    ("var_call_YFGQ7HHRY4MZkeAqOGH2hclH", "HQI"),
    ("var_call_bbmHkfAMO1THvUiUUKtq27Ae", "HRTX"),
    ("var_call_qY0x7ar4iTtJ16LQbcehfdOF", "IDEX"),
    ("var_call_iySU9XVqfWlThOfWj99URDeq", "IGIC"),
    ("var_call_ZXoFHFTP818wOxkTzflzo60Z", "IOTS"),
    ("var_call_QbUEDdVOGs7efbL7uBKHfNQJ", "ISNS"),
    ("var_call_FmRMKQIdFHc0FF8XsMB3FXgW", "ITI"),
    ("var_call_S1G6d0pDkBF1JIBOLjR5qe5n", "LACQ"),
    ("var_call_9lBDP8Disn8gjodpvJnuF1wI", "MBCN"),
    ("var_call_4zg1OgdYHKUXWUpbs42zudvh", "MBNKP"),
    ("var_call_XxGzIEsOx6xptdCfj5pUvzaj", "MCEP"),
    ("var_call_5LdkZOQbHihCulkn8YnSLN7D", "MLND"),
    ("var_call_7E7qZC52rTVchzmIdf4jtSLw", "MMAC"),
    ("var_call_IugR2HwftfXm4o8UNKOYW12I", "MNCLU"),
    ("var_call_KGPdd0ob0Tobzs8pFaRvg9uG", "MNPR"),
    ("var_call_HTNtQpsM7eq66UqSam58BciY", "NVEE"),
    ("var_call_gRXtbnLBDiLmmhsT0ct3ZJD5", "NXTD"),
    ("var_call_Dsaf0an4qaIjlvo0z77SSaSM", "OPOF"),
    ("var_call_El2hp8R47vZSeH2CicARssFO", "OPTT"),
    ("var_call_Z0vhhmJ2bN1OFNF6ckWjOSbB", "ORGO"),
    ("var_call_VXdv6PlWcNJe5SLkMTbH22Zq", "ORSNU"),
    ("var_call_miGH6Te3p7fkBo7AjTsCbo5C", "OTEL"),
    ("var_call_zXU7juKkr4Qvzw46ar8TrvIX", "PBFS"),
    ("var_call_gKHqj2nXz219AhBPQpVKno8Y", "PBTS"),
    ("var_call_AaC0Xw35XZiGyt2YOVtwNEo5", "PCSB"),
    ("var_call_mMUEUO0OlQjeWXF5EuZFRQ71", "PECK"),
    ("var_call_zGB7JhgYhuYlHzYbYHcpX6MA", "PEIX"),
    ("var_call_Z4Xa6HhOD7EEGlhJEyeQ5knW", "PFIE"),
    ("var_call_j9cDY6T3tPVCdjYyaVnGiTD1", "PLIN"),
    ("var_call_iPyfqQfaLLHClBWQCTIHL3iC", "POPE"),
    ("var_call_fCeOzuTJKlAZnmTKRZIw25X9", "QRHC"),
    ("var_call_aGkA2isk9WpofnxHYMotnFeZ", "SES"),
    ("var_call_rucme6fDrhXFIGHimq7bHwsR", "SHSP"),
    ("var_call_MKrZRABpmBAlRBcxDZnryfdw", "SNSS"),
    ("var_call_S0Cnxb8bOoOw6p56QdFYYQla", "SSNT"),
    ("var_call_UkUSOAw7kLA8JNRyxlPYwC5N", "STKS"),
    ("var_call_BCi3mQuGqeuZZkZR8yhOTcRo", "TGLS"),
    ("var_call_JbNzh2hKsg8m1uRsXwcgudMn", "TMSR"),
    ("var_call_n00GOYXzL6kfYH0E8ag9dI8w", "VERB"),
    ("var_call_YzY2Rj7FuC3vwVjLO1K0fog3", "VMD"),
    ("var_call_iwgsZXvhoGmRV4I7zWOPJnS5", "VRRM"),
    ("var_call_NTkNiHGZwGbpPF5T0SSaszas", "VTIQW"),
    ("var_call_0harjpjl6LJHEItSQZvpslM6", "VVPR"),
    ("var_call_WvpEoIrpU0mwEoCAjYfxEqaX", "WHLM"),
    ("var_call_wkAK6ZoumP7AvZgasvW8dCSO", "WHLR"),
    ("var_call_2iX4lkV7hknnzL8gnyCgdUFz", "XBIOW"),
    ("var_call_6ZtLBuxrcaESstYN5REFulvt", "XPEL")
]

counts = []
for key, sym in keys_and_symbols:
    v = globals().get(key)
    cnt = None
    if v is None:
        cnt = None
    else:
        # if v is a string, it's likely a file path to JSON
        if isinstance(v, str):
            try:
                with open(v, 'r') as f:
                    data = json.load(f)
                if isinstance(data, list) and len(data)>0 and 'cnt' in data[0]:
                    cnt = int(data[0]['cnt'])
            except Exception:
                cnt = None
        else:
            try:
                if isinstance(v, list) and len(v)>0 and 'cnt' in v[0]:
                    cnt = int(v[0]['cnt'])
            except Exception:
                cnt = None
    counts.append({'Symbol': sym, 'count': cnt})

# load stockinfo file to map symbols to company description
stockinfo_path = globals().get('var_call_gd5CWdzsZx0rDOMd65g9c3aG')
symbol_to_desc = {}
if isinstance(stockinfo_path, str):
    try:
        with open(stockinfo_path, 'r') as f:
            stockinfo = json.load(f)
        for r in stockinfo:
            symbol_to_desc[r['Symbol']] = r.get('Company Description')
    except Exception:
        stockinfo = []

# filter out None counts
valid = [c for c in counts if c['count'] is not None]
# sort
valid_sorted = sorted(valid, key=lambda x: x['count'], reverse=True)
# take top 5
top5 = valid_sorted[:5]
# prepare output with company descriptions
output = []
for item in top5:
    sym = item['Symbol']
    desc = symbol_to_desc.get(sym)
    output.append({'Symbol': sym, 'Company Description': desc, 'count': item['count']})

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_gd5CWdzsZx0rDOMd65g9c3aG': 'file_storage/call_gd5CWdzsZx0rDOMd65g9c3aG.json', 'var_call_QzqB9vLpeuskhuikHIbwl4Zy': 'file_storage/call_QzqB9vLpeuskhuikHIbwl4Zy.json', 'var_call_VseTpnZF99g6zPGH2Q7jTOml': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_hZ7vZmQVN6GfzkiRSgY6s74W': [{'cnt': '13'}], 'var_call_yzIdqy0TBkWf6aYrh70ai6S7': [{'cnt': '0'}], 'var_call_9MRG5oCzHw51J95I6Zwbc66p': [{'cnt': '0'}], 'var_call_Y8JzOAPntqHPvAXsDvyyyTVE': [{'cnt': '0'}], 'var_call_jkqX88vulih6n0NyzObFL5jj': [{'cnt': '15'}], 'var_call_MB7l5DvGTnP4mEVKQbOErFkq': [{'cnt': '0'}], 'var_call_2xg1k41I111TN5MAiFFzrCed': [{'cnt': '10'}], 'var_call_5O645kIvXSEaTUJ6eftzEO8E': [{'cnt': '21'}], 'var_call_pS9LFUxPNDxlMxY6BzTOYKTi': [{'cnt': '16'}], 'var_call_fjzqcYrRwsljRZfSpiSlrN5A': [{'cnt': '0'}], 'var_call_eV8JywNeHoyV5LDD338LxBs8': [{'cnt': '3'}], 'var_call_BNWCzk5X4hgSHdJBbzKrhav9': [{'cnt': '0'}], 'var_call_hbzGnLLP0XBiTeddUnEemScw': [{'cnt': '5'}], 'var_call_b9fQ1aE0z8gWwHtoUYfRU2kI': [{'cnt': '23'}], 'var_call_5RTgx8PttqNUdUTzXKx8V6WN': [{'cnt': '13'}], 'var_call_MRRCMFoTtRF0elYzNU40BiLi': [{'cnt': '0'}], 'var_call_F15b8A0xupKFwMwrs3elsK7s': [{'cnt': '3'}], 'var_call_gmurFlpIxhugCkvwAwpUGjDN': [{'cnt': '0'}], 'var_call_HZHVpxNczDp0YhwP1Bzqgi5d': [{'cnt': '0'}], 'var_call_TJWNrLyXGpWCv01fCmjOwCzd': [{'cnt': '14'}], 'var_call_Ly2UwWLYurBRJcPC1ENOgEnz': [{'cnt': '10'}], 'var_call_GfOzS2bkqACLUR3gxeVgjlq6': [{'cnt': '0'}], 'var_call_yynqoKxfo2vBhy2qC00hO57R': [{'cnt': '16'}], 'var_call_bNRXc0EA6AMmyPKcVYm6kTRM': [{'cnt': '0'}], 'var_call_C8IQGpCNlrD4KGDyW9nEcsfa': [{'cnt': '0'}], 'var_call_p3gWVooX5CSOxVA66j0lSggk': [{'cnt': '1'}], 'var_call_VC84AsbLr3z7O9EhPaGTXdsL': [{'cnt': '0'}], 'var_call_rqOXlfT6nngMwAZQFnvBIdHU': [{'cnt': '0'}], 'var_call_Iuy5mo8qXUq1ZjWrSJKdgut2': [{'cnt': '18'}], 'var_call_ZMWvEnSPz4w3SMI0YwvtIsfn': [{'cnt': '23'}], 'var_call_dUGjUD0BXDaZEeBpr61bFJAz': [{'cnt': '1'}], 'var_call_WcBST2DMRkwR3zYQLDX7U39l': [{'cnt': '0'}], 'var_call_ZLieYOCPyJ781cBmYJRvlhCe': [{'cnt': '21'}], 'var_call_D7nZehbcskAkoynb5adXlkF7': [{'cnt': '0'}], 'var_call_S7lNFOLiCvIsSYynm00qj0A1': [{'cnt': '42'}], 'var_call_UrTd1gshVVHCApYKNz1rd0VT': [{'cnt': '0'}], 'var_call_5yj2MdrfngnCHJ0OjQlaUXNi': [{'cnt': '0'}], 'var_call_22FsWG702uL8eZi8XvKEag27': [{'cnt': '0'}], 'var_call_DNEVRr5dwfi2T9nIzXEZU8GZ': [{'cnt': '0'}], 'var_call_YFGQ7HHRY4MZkeAqOGH2hclH': [{'cnt': '2'}], 'var_call_bbmHkfAMO1THvUiUUKtq27Ae': [{'cnt': '1'}], 'var_call_qY0x7ar4iTtJ16LQbcehfdOF': [{'cnt': '15'}], 'var_call_iySU9XVqfWlThOfWj99URDeq': [{'cnt': '0'}], 'var_call_ZXoFHFTP818wOxkTzflzo60Z': [{'cnt': '1'}], 'var_call_QbUEDdVOGs7efbL7uBKHfNQJ': [{'cnt': '0'}], 'var_call_FmRMKQIdFHc0FF8XsMB3FXgW': [{'cnt': '0'}], 'var_call_S1G6d0pDkBF1JIBOLjR5qe5n': [{'cnt': '0'}], 'var_call_9lBDP8Disn8gjodpvJnuF1wI': [{'cnt': '0'}], 'var_call_4zg1OgdYHKUXWUpbs42zudvh': [{'cnt': '0'}], 'var_call_XxGzIEsOx6xptdCfj5pUvzaj': [{'cnt': '14'}], 'var_call_5LdkZOQbHihCulkn8YnSLN7D': [{'cnt': '3'}], 'var_call_7E7qZC52rTVchzmIdf4jtSLw': [{'cnt': '1'}], 'var_call_IugR2HwftfXm4o8UNKOYW12I': [{'cnt': '0'}], 'var_call_KGPdd0ob0Tobzs8pFaRvg9uG': [{'cnt': '4'}], 'var_call_HTNtQpsM7eq66UqSam58BciY': [{'cnt': '1'}], 'var_call_gRXtbnLBDiLmmhsT0ct3ZJD5': [{'cnt': '15'}], 'var_call_Dsaf0an4qaIjlvo0z77SSaSM': [{'cnt': '0'}], 'var_call_El2hp8R47vZSeH2CicARssFO': [{'cnt': '12'}], 'var_call_Z0vhhmJ2bN1OFNF6ckWjOSbB': [{'cnt': '15'}], 'var_call_VXdv6PlWcNJe5SLkMTbH22Zq': [{'cnt': '0'}], 'var_call_miGH6Te3p7fkBo7AjTsCbo5C': [{'cnt': '1'}], 'var_call_zXU7juKkr4Qvzw46ar8TrvIX': [{'cnt': '0'}], 'var_call_gKHqj2nXz219AhBPQpVKno8Y': [{'cnt': '8'}], 'var_call_AaC0Xw35XZiGyt2YOVtwNEo5': [{'cnt': '0'}], 'var_call_mMUEUO0OlQjeWXF5EuZFRQ71': [{'cnt': '19'}], 'var_call_zGB7JhgYhuYlHzYbYHcpX6MA': [{'cnt': '12'}], 'var_call_Z4Xa6HhOD7EEGlhJEyeQ5knW': [{'cnt': '2'}], 'var_call_j9cDY6T3tPVCdjYyaVnGiTD1': [{'cnt': '1'}], 'var_call_iPyfqQfaLLHClBWQCTIHL3iC': [{'cnt': '0'}], 'var_call_fCeOzuTJKlAZnmTKRZIw25X9': [{'cnt': '3'}], 'var_call_aGkA2isk9WpofnxHYMotnFeZ': [{'cnt': '51'}], 'var_call_rucme6fDrhXFIGHimq7bHwsR': [{'cnt': '1'}], 'var_call_MKrZRABpmBAlRBcxDZnryfdw': [{'cnt': '32'}], 'var_call_S0Cnxb8bOoOw6p56QdFYYQla': [{'cnt': '11'}], 'var_call_UkUSOAw7kLA8JNRyxlPYwC5N': [{'cnt': '0'}], 'var_call_BCi3mQuGqeuZZkZR8yhOTcRo': [{'cnt': '0'}], 'var_call_JbNzh2hKsg8m1uRsXwcgudMn': [{'cnt': '40'}], 'var_call_n00GOYXzL6kfYH0E8ag9dI8w': [{'cnt': '38'}], 'var_call_YzY2Rj7FuC3vwVjLO1K0fog3': [{'cnt': '1'}], 'var_call_iwgsZXvhoGmRV4I7zWOPJnS5': [{'cnt': '0'}], 'var_call_NTkNiHGZwGbpPF5T0SSaszas': [{'cnt': '6'}], 'var_call_0harjpjl6LJHEItSQZvpslM6': [{'cnt': '14'}], 'var_call_WvpEoIrpU0mwEoCAjYfxEqaX': [{'cnt': '0'}], 'var_call_wkAK6ZoumP7AvZgasvW8dCSO': [{'cnt': '15'}], 'var_call_2iX4lkV7hknnzL8gnyCgdUFz': [{'cnt': '7'}], 'var_call_6ZtLBuxrcaESstYN5REFulvt': [{'cnt': '4'}], 'var_call_08r7LOMy4jrF13Ic1HYVhdp8': []}

exec(code, env_args)
