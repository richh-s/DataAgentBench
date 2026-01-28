code = """import json, os
# Collect all records from var_call_* globals
records = []
for name, val in globals().items():
    if not name.startswith('var_call_'):
        continue
    try:
        if isinstance(val, str) and os.path.exists(val):
            with open(val, 'r') as f:
                loaded = json.load(f)
        else:
            loaded = val
        if isinstance(loaded, list):
            for item in loaded:
                if isinstance(item, dict) and 'symbol' in item and 'cnt' in item:
                    records.append(item)
        elif isinstance(loaded, dict):
            if 'symbol' in loaded and 'cnt' in loaded:
                records.append(loaded)
    except Exception:
        continue

# Convert cnt to int
for r in records:
    try:
        r['cnt'] = int(float(r['cnt']))
    except Exception:
        r['cnt'] = 0

# Aggregate by symbol in case of duplicates
agg = {}
for r in records:
    s = r['symbol']
    cnt = r['cnt']
    agg[s] = agg.get(s, 0) + cnt

# Sort symbols by count desc
sorted_syms = sorted(agg.items(), key=lambda x: x[1], reverse=True)
top5 = sorted_syms[:5]

# Load stockinfo mapping
stockinfo = []
if 'var_call_tItXDldGr2benyc4Ud9wMyCQ' in globals():
    path = globals()['var_call_tItXDldGr2benyc4Ud9wMyCQ']
    if isinstance(path, str) and os.path.exists(path):
        with open(path, 'r') as f:
            stockinfo = json.load(f)

sym_to_name = {entry['Symbol']: entry['Company Description'] for entry in stockinfo}

result = []
for sym, cnt in top5:
    name = sym_to_name.get(sym, None)
    result.append({'symbol': sym, 'count': cnt, 'company': name})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_tItXDldGr2benyc4Ud9wMyCQ': 'file_storage/call_tItXDldGr2benyc4Ud9wMyCQ.json', 'var_call_3GqfoyPVmTjGEwRIfI1A6U1V': 'file_storage/call_3GqfoyPVmTjGEwRIfI1A6U1V.json', 'var_call_4CWcslbtU4Wan6tuyRNTQOfn': 'file_storage/call_4CWcslbtU4Wan6tuyRNTQOfn.json', 'var_call_F5ipAHj5IuVx6yKrTctqRuSO': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_eEzBsR9HQHllIPXjb9lUc9d1': 'file_storage/call_eEzBsR9HQHllIPXjb9lUc9d1.json', 'var_call_QEHXwvYsCrm7bV8VDouIOZEQ': [{'symbol': 'AGMH', 'cnt': '13.0'}], 'var_call_q42vqmVvFXBXpm4EXiUOUM79': [{'symbol': 'ALACU', 'cnt': '0.0'}], 'var_call_WN0sPUplKFrsh6Ecj5Xx2s3z': [{'symbol': 'AMHC', 'cnt': '0.0'}], 'var_call_Xf1o4basz9N7NmcVNj27Hwli': [{'symbol': 'ANDA', 'cnt': '0.0'}], 'var_call_jrJuV17CvfTEmwuLRnw2mTGT': [{'symbol': 'APEX', 'cnt': '15.0'}], 'var_call_uXzGlp0rZ0Cr484kRerkbcKn': [{'symbol': 'BCLI', 'cnt': '0.0'}], 'var_call_vsYb6f1GvVpus9GGd7LAKLr7': [{'symbol': 'BHAT', 'cnt': '10.0'}], 'var_call_04N3KwApoSZNAElx1LHfXcuj': [{'symbol': 'BIOC', 'cnt': '21.0'}], 'var_call_0CshlOJNl9kCmC99e8KTzfEC': [{'symbol': 'BKYI', 'cnt': '16.0'}], 'var_call_p4vVyM53JHEItbsd21FpKksk': [{'symbol': 'BLFS', 'cnt': '0.0'}], 'var_call_3iQlqEYAPDmVB6BYTueTR0OM': [{'symbol': 'BOSC', 'cnt': '3.0'}], 'var_call_QY3eAe5UoDbpvXwkafXfCj6d': [{'symbol': 'BOTJ', 'cnt': '0.0'}], 'var_call_DSvS6D3qJY425DbEZF2Mqxto': [{'symbol': 'BWEN', 'cnt': '5.0'}], 'var_call_F327gYCHdQoubdAwOaPRo3JF': [{'symbol': 'CBAT', 'cnt': '23.0'}], 'var_call_M2xXKR4lX7MppxGZw7hNttSC': [{'symbol': 'CCCL', 'cnt': '13.0'}], 'var_call_eshjOeHcVIJLcZWWQFJBSOl2': [{'symbol': 'CDMOP', 'cnt': '0.0'}], 'var_call_qLX4KTg9gQTNvkEP9VvnZZpE': [{'symbol': 'CEMI', 'cnt': '3.0'}], 'var_call_e19KJbPnf0BLq6VEgx0aU7ZR': [{'symbol': 'CFBK', 'cnt': '0.0'}], 'var_call_DVhD2a6cac8Mfd5QOp3U8fNW': [{'symbol': 'CFFA', 'cnt': '0.0'}], 'var_call_RLtFDEWA1QnfFLs2WGnNmw1c': [{'symbol': 'CLRB', 'cnt': '14.0'}], 'var_call_UqSxYipXQNbmfCg1Y7dh9H8u': [{'symbol': 'CORV', 'cnt': '10.0'}], 'var_call_LR4JofGrKERwkRYVLv6weysc': [{'symbol': 'CPAAU', 'cnt': '0.0'}], 'var_call_NpSvAjzds0HlfHkKHT38oFO0': [{'symbol': 'CPAH', 'cnt': '16.0'}], 'var_call_YC1VqfW6NIrEhLD7kmxE1Myw': [{'symbol': 'CUBA', 'cnt': '0.0'}], 'var_call_ihT3T0HbPCpdgkcMWsEnpdzq': [{'symbol': 'CVV', 'cnt': '0.0'}], 'var_call_35Kg6G9oDaw0MaIWd2sTKnYw': [{'symbol': 'DZSI', 'cnt': '1.0'}], 'var_call_qBOKyv9JqB8SDOZiaLWChZrT': [{'symbol': 'ELSE', 'cnt': '0.0'}], 'var_call_y7cCAu6KXp6Tm8dxd5KzRcf2': [{'symbol': 'EXPC', 'cnt': '0.0'}], 'var_call_ZMn3kpMZwOMZGumkM0vik9gd': [{'symbol': 'EYEG', 'cnt': '18.0'}], 'var_call_7Trr0IG91SjugyVx0ro7B66Q': [{'symbol': 'FAMI', 'cnt': '23.0'}], 'var_call_DBR19pCd8lPAtIQoIwrFToCL': [{'symbol': 'FNCB', 'cnt': '1.0'}], 'var_call_TrqLs87JewWxWVupf7ko6vPH': [{'symbol': 'FSBW', 'cnt': '0.0'}], 'var_call_NcawRBgmZI6spfNAV3zl4Jeb': [{'symbol': 'FTFT', 'cnt': '21.0'}], 'var_call_C1jGUzBVWT9htPkmQMWOMtSG': [{'symbol': 'GDYN', 'cnt': '0.0'}], 'var_call_caQGYzLUZlUvhd3pRI0KZNuA': [{'symbol': 'GLG', 'cnt': '42.0'}], 'var_call_MQs9uOYyEP9qomLVxxGxO9dM': [{'symbol': 'GRNVU', 'cnt': '0.0'}], 'var_call_yIg7PFO66rAA337qQplNarhG': [{'symbol': 'GTEC', 'cnt': '0.0'}], 'var_call_TChOnDefYJskwnm6JDeURFT3': [{'symbol': 'HCCOU', 'cnt': '0.0'}], 'var_call_QzZopb2cMD4u5t7zyE9IQs63': [{'symbol': 'HNNA', 'cnt': '0.0'}], 'var_call_gvqQADm1tLaZzddq5ClRm47L': [{'symbol': 'HQI', 'cnt': '2.0'}], 'var_call_tqCCLQuO4Jc7sMFnFgSq16KG': [{'symbol': 'HRTX', 'cnt': '1.0'}], 'var_call_f53qMrq5rWTsZmg4a42u1sx4': [{'symbol': 'IDEX', 'cnt': '15.0'}], 'var_call_UVuvkdRXS9emgNW3eTlofeVI': [{'symbol': 'IGIC', 'cnt': '0.0'}], 'var_call_xJth2457SlgZ1m4AzXGn3ZTM': [{'symbol': 'IOTS', 'cnt': '1.0'}], 'var_call_GUBn45TZ8Y13L5dw7Dyh3ZIo': [{'symbol': 'ISNS', 'cnt': '0.0'}], 'var_call_OXJ57CtjWnX3g7H7Fe6IifQy': [{'symbol': 'ITI', 'cnt': '0.0'}], 'var_call_Z1ARyUouLb9sBhYzmMdBa5qm': [{'symbol': 'LACQ', 'cnt': '0.0'}], 'var_call_Ha9LFy2Q94KZEpTjMUkMejTV': [{'symbol': 'MBCN', 'cnt': '0.0'}], 'var_call_OiNKAvYSt3d1ksQR4HAv7J4a': [{'symbol': 'MBNKP', 'cnt': '0.0'}], 'var_call_OYrGbpSOG6S8HvfK6mAGsgtK': [{'symbol': 'MCEP', 'cnt': '14.0'}], 'var_call_GSSlIti8QgK4kYg9fl83GdNU': [{'symbol': 'MLND', 'cnt': '3.0'}], 'var_call_6tUQLqJuKLaoYmv5BwMvslSX': [{'symbol': 'MMAC', 'cnt': '1.0'}], 'var_call_zlpEvte8QlLdbaYyaUbZvhmQ': [{'symbol': 'MNCLU', 'cnt': '0.0'}], 'var_call_kxRMJ6Na2DUHa66K8AL5zazI': [{'symbol': 'MNPR', 'cnt': '4.0'}], 'var_call_2XwEkSMlj1ywAqgxJAoOLh0g': [{'symbol': 'NVEE', 'cnt': '1.0'}], 'var_call_nDd4QYzvLUvLjWHT50bxyzsH': [{'symbol': 'NXTD', 'cnt': '15.0'}], 'var_call_P7MAkTUg3CF9HEABZ4lh5JGd': [{'symbol': 'OPOF', 'cnt': '0.0'}], 'var_call_jKQpji4fO1lniyDO8JHY4NJu': [{'symbol': 'OPTT', 'cnt': '12.0'}], 'var_call_HiaaOHZxSunT0ieXN5Hdxm8D': [{'symbol': 'ORGO', 'cnt': '15.0'}], 'var_call_KfDMqwsbztQhqdhyJDq8izqJ': [{'symbol': 'ORSNU', 'cnt': '0.0'}], 'var_call_JGL2rd3KUQD6LzbcgotCy1jZ': [{'symbol': 'OTEL', 'cnt': '1.0'}], 'var_call_vpGT7ecbj8fZgcyHJDD6iwrH': [{'symbol': 'PBFS', 'cnt': '0.0'}], 'var_call_NYZY1GUrEWbQ7ySAv8eILlNh': [{'symbol': 'PBTS', 'cnt': '8.0'}], 'var_call_MmisjCHZpKdUqZm6TdPJNFcI': [{'symbol': 'PCSB', 'cnt': '0.0'}], 'var_call_E87DMMBSJCI7oMnWT6POwURO': [{'symbol': 'PECK', 'cnt': '19.0'}], 'var_call_Ah9JFYVecMHEvD5mQWzC8EzB': [{'symbol': 'PEIX', 'cnt': '12.0'}], 'var_call_XArvjf8vl6OtYGlXo3Ybc5iQ': [{'symbol': 'PFIE', 'cnt': '2.0'}], 'var_call_OFwLQwfYCpLHwPrt0j911bQK': [{'symbol': 'PLIN', 'cnt': '1.0'}], 'var_call_mNan7m1Uf4gQpXwrnQqlhQbB': [{'symbol': 'POPE', 'cnt': '0.0'}], 'var_call_RxbKdxhvt3Pl9vhQaH0K9XiX': [{'symbol': 'QRHC', 'cnt': '3.0'}], 'var_call_D8bVrMIY7r7IVtrcnccgJE8p': [{'symbol': 'SES', 'cnt': '51.0'}], 'var_call_3HzqaOeDvpxpGIvyamXVKveT': [{'symbol': 'SHSP', 'cnt': '1.0'}], 'var_call_uQEvo0NAg76b23m87sQANKNn': [{'symbol': 'SNSS', 'cnt': '32.0'}], 'var_call_s9CZ42ATThAkInqVLvQCeivk': [{'symbol': 'SSNT', 'cnt': '11.0'}], 'var_call_PMmSgnvk7rup4czW86eNwY3q': [{'symbol': 'STKS', 'cnt': '0.0'}], 'var_call_FNejCeoCV016jrJAHVZxYae8': [{'symbol': 'TGLS', 'cnt': '0.0'}], 'var_call_toKWWtu3P7vTyFoJAvFyQRuj': [{'symbol': 'TMSR', 'cnt': '40.0'}], 'var_call_Z3NjOrinFj1gGXSbkABbILPX': [{'symbol': 'VERB', 'cnt': '38.0'}], 'var_call_k9vPwczL1NpCaBynDpw7pTcx': [{'symbol': 'VMD', 'cnt': '1.0'}], 'var_call_VVhQlqcY6xFwAGru1R0dXiIa': [{'symbol': 'VRRM', 'cnt': '0.0'}], 'var_call_WajePypWi0AwaktGVthGVZ9h': [{'symbol': 'VTIQW', 'cnt': '6.0'}], 'var_call_BPgufWRfwngJwn2aZIUjjqY0': [{'symbol': 'VVPR', 'cnt': '14.0'}], 'var_call_krhUI68kcMjWzTKoXZ4VdgnW': [{'symbol': 'WHLM', 'cnt': '0.0'}], 'var_call_C1c9qyEGXJdF3m10lhBGhm7O': [{'symbol': 'WHLR', 'cnt': '15.0'}], 'var_call_oiUjucLRyhIr3EfOTCjitHR6': [{'symbol': 'XBIOW', 'cnt': '7.0'}], 'var_call_cy3DKY4ImWa2LlckAM2vT7L8': [{'symbol': 'XPEL', 'cnt': '4.0'}], 'var_call_plWICZF3sLBH1VFHrfVeMyOZ': []}

exec(code, env_args)
