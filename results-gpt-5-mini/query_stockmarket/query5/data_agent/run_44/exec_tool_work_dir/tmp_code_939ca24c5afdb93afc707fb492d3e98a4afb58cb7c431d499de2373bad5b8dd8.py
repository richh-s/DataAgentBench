code = """import json
# collect all query results keys from the multi_tool_use output stored in previous step
# keys are available in the environment as var_call_... from the multi_tool_use result above
keys = [
 'var_call_QEHXwvYsCrm7bV8VDouIOZEQ','var_call_q42vqmVvFXBXpm4EXiUOUM79','var_call_WN0sPUplKFrsh6Ecj5Xx2s3z',
 'var_call_Xf1o4basz9N7NmcVNj27Hwli','var_call_jrJuV17CvfTEmwuLRnw2mTGT','var_call_uXzGlp0rZ0Cr484kRerkbcKn',
 'var_call_vsYb6f1GvVpus9GGd7LAKLr7','var_call_04N3KwApoSZNAElx1LHfXcuj','var_call_0CshlOJNl9kCmC99e8KTzfEC',
 'var_call_p4vVyM53JHEItbsd21FpKksk','var_call_3iQlqEYAPDmVB6BYTueTR0OM','var_call_QY3eAe5UoDbpvXwkafXfCj6d',
 'var_call_DSvS6D3qJY425DbEZF2Mqxto','var_call_F327gYCHdQoubdAwOaPRo3JF','var_call_M2xXKR4lX7MppxGZw7hNttSC',
 'var_call_eshjOeHcVIJLcZWWQFJBSOl2','var_call_qLX4KTg9gQTNvkEP9VvnZZpE','var_call_e19KJbPnf0BLq6VEgx0aU7ZR',
 'var_call_DVhD2a6cac8Mfd5QOp3U8fNW','var_call_RLtFDEWA1QnfFLs2WGnNmw1c','var_call_UqSxYipXQNbmfCg1Y7dh9H8u',
 'var_call_LR4JofGrKERwkRYVLv6weysc','var_call_NpSvAjzds0HlfHkKHT38oFO0','var_call_YC1VqfW6NIrEhLD7kmxE1Myw',
 'var_call_ihT3T0HbPCpdgkcMWsEnpdzq','var_call_35Kg6G9oDaw0MaIWd2sTKnYw','var_call_qBOKyv9JqB8SDOZiaLWChZrT',
 'var_call_y7cCAu6KXp6Tm8dxd5KzRcf2','var_call_ZMn3kpMZwOMZGumkM0vik9gd','var_call_7Trr0IG91SjugyVx0ro7B66Q',
 'var_call_DBR19pCd8lPAtIQoIwrFToCL','var_call_TrqLs87JewWxWVupf7ko6vPH','var_call_NcawRBgmZI6spfNAV3zl4Jeb',
 'var_call_C1jGUzBVWT9htPkmQMWOMtSG','var_call_caQGYzLUZlUvhd3pRI0KZNuA','var_call_MQs9uOYyEP9qomLVxxGxO9dM',
 'var_call_yIg7PFO66rAA337qQplNarhG','var_call_TChOnDefYJskwnm6JDeURFT3','var_call_QzZopb2cMD4u5t7zyE9IQs63',
 'var_call_gvqQADm1tLaZzddq5ClRm47L','var_call_tqCCLQuO4Jc7sMFnFgSq16KG','var_call_f53qMrq5rWTsZmg4a42u1sx4',
 'var_call_UVuvkdRXS9emgNW3eTlofeVI','var_call_xJth2457SlgZ1m4AzXGn3ZTM','var_call_GUBn45TZ8Y13L5dw7Dyh3ZIo',
 'var_call_OXJ57CtjWnX3g7H7Fe6IifQy','var_call_Z1ARyUouLb9sBhYzmMdBa5qm','var_call_Ha9LFy2Q94KZEpTjMUkMejTV',
 'var_call_OiNKAvYSt3d1ksQR4HAv7J4a','var_call_OYrGbpSOG6S8HvfK6mAGsgtK','var_call_GSSlIti8QgK4kYg9fl83GdNU',
 'var_call_6tUQLqJuKLaoYmv5BwMvslSX','var_call_zlpEvte8QlLdbaYyaUbZvhmQ','var_call_kxRMJ6Na2DUHa66K8AL5zazI',
 'var_call_2XwEkSMlj1ywAqgxJAoOLh0g','var_call_nDd4QYzvLUvLjWHT50bxyzsH','var_call_P7MAkTUg3CF9HEABZ4lh5JGd',
 'var_call_jKQpji4fO1lniyDO8JHY4NJu','var_call_HiaaOHZxSunT0ieXN5Hdxm8D','var_call_KfDMqwsbztQhqdhyJDq8izqJ',
 'var_call_JGL2rd3KUQD6LzbcgotCy1jZ','var_call_vpGT7ecbj8fZgcyHJDD6iwrH','var_call_NYZY1GUrEWbQ7ySAv8eILlNh',
 'var_call_MmisjCHZpKdUqZm6TdPJNFcI','var_call_E87DMMBSJCI7oMnWT6POwURO','var_call_Ah9JFYVecMHEvD5mQWzC8EzB',
 'var_call_XArvjf8vl6OtYGlXo3Ybc5iQ','var_call_OFwLQwfYCpLHwPrt0j911bQK','var_call_mNan7m1Uf4gQpXwrnQqlhQbB',
 'var_call_RxbKdxhvt3Pl9vhQaH0K9XiX','var_call_D8bVrMIY7r7IVtrcnccgJE8p','var_call_3HzqaOeDvpxpGIvyamXVKveT',
 'var_call_uQEvo0NAg76b23m87sQANKNn','var_call_uQEvo0NAg76b23m87sQANKNn','var_call_s9CZ42ATThAkInqVLvQCeivk',
 'var_call_s9CZ42ATThAkInqVLvQCeivk','var_call_PMmSgnvk7rup4czW86eNwY3q','var_call_FNejCeoCV016jrJAHVZxYae8',
 'var_call_toKWWtu3P7vTyFoJAvFyQRuj','var_call_Z3NjOrinFj1gGXSbkABbILPX','var_call_k9vPwczL1NpCaBynDpw7pTcx',
 'var_call_VVhQlqcY6xFwAGru1R0dXiIa','var_call_VVhQlqcY6xFwAGru1R0dXiIa','var_call_WajePypWi0AwaktGVthGVZ9h',
 'var_call_C1c9qyEGXJdF3m10lhBGhm7O','var_call_oiUjucLRyhIr3EfOTCjitHR6','var_call_vpGT7ecbj8fZgcyHJDD6iwrH',
 'var_call_NYZY1GUrEWbQ7ySAv8eILlNh','var_call_MmisjCHZpKdUqZm6TdPJNFcI','var_call_E87DMMBSJCI7oMnWT6POwURO',
 'var_call_Ah9JFYVecMHEvD5mQWzC8EzB','var_call_RxbKdxhvt3Pl9vhQaH0K9XiX','var_call_D8bVrMIY7r7IVtrcnccgJE8p'
]
# Deduplicate keys
keys = list(dict.fromkeys(keys))

records = []
for k in keys:
    try:
        with open(globals()[k], 'r') as f:
            data = json.load(f)
        records.extend(data)
    except Exception as e:
        # some keys may not be present or readable
        pass

# convert cnt to int and sort
for r in records:
    r['cnt'] = int(float(r['cnt']))

records_sorted = sorted(records, key=lambda x: x['cnt'], reverse=True)
# take top 5
top5 = records_sorted[:5]
print('__RESULT__:')
print(json.dumps(top5))"""

env_args = {'var_call_tItXDldGr2benyc4Ud9wMyCQ': 'file_storage/call_tItXDldGr2benyc4Ud9wMyCQ.json', 'var_call_3GqfoyPVmTjGEwRIfI1A6U1V': 'file_storage/call_3GqfoyPVmTjGEwRIfI1A6U1V.json', 'var_call_4CWcslbtU4Wan6tuyRNTQOfn': 'file_storage/call_4CWcslbtU4Wan6tuyRNTQOfn.json', 'var_call_F5ipAHj5IuVx6yKrTctqRuSO': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_eEzBsR9HQHllIPXjb9lUc9d1': 'file_storage/call_eEzBsR9HQHllIPXjb9lUc9d1.json', 'var_call_QEHXwvYsCrm7bV8VDouIOZEQ': [{'symbol': 'AGMH', 'cnt': '13.0'}], 'var_call_q42vqmVvFXBXpm4EXiUOUM79': [{'symbol': 'ALACU', 'cnt': '0.0'}], 'var_call_WN0sPUplKFrsh6Ecj5Xx2s3z': [{'symbol': 'AMHC', 'cnt': '0.0'}], 'var_call_Xf1o4basz9N7NmcVNj27Hwli': [{'symbol': 'ANDA', 'cnt': '0.0'}], 'var_call_jrJuV17CvfTEmwuLRnw2mTGT': [{'symbol': 'APEX', 'cnt': '15.0'}], 'var_call_uXzGlp0rZ0Cr484kRerkbcKn': [{'symbol': 'BCLI', 'cnt': '0.0'}], 'var_call_vsYb6f1GvVpus9GGd7LAKLr7': [{'symbol': 'BHAT', 'cnt': '10.0'}], 'var_call_04N3KwApoSZNAElx1LHfXcuj': [{'symbol': 'BIOC', 'cnt': '21.0'}], 'var_call_0CshlOJNl9kCmC99e8KTzfEC': [{'symbol': 'BKYI', 'cnt': '16.0'}], 'var_call_p4vVyM53JHEItbsd21FpKksk': [{'symbol': 'BLFS', 'cnt': '0.0'}], 'var_call_3iQlqEYAPDmVB6BYTueTR0OM': [{'symbol': 'BOSC', 'cnt': '3.0'}], 'var_call_QY3eAe5UoDbpvXwkafXfCj6d': [{'symbol': 'BOTJ', 'cnt': '0.0'}], 'var_call_DSvS6D3qJY425DbEZF2Mqxto': [{'symbol': 'BWEN', 'cnt': '5.0'}], 'var_call_F327gYCHdQoubdAwOaPRo3JF': [{'symbol': 'CBAT', 'cnt': '23.0'}], 'var_call_M2xXKR4lX7MppxGZw7hNttSC': [{'symbol': 'CCCL', 'cnt': '13.0'}], 'var_call_eshjOeHcVIJLcZWWQFJBSOl2': [{'symbol': 'CDMOP', 'cnt': '0.0'}], 'var_call_qLX4KTg9gQTNvkEP9VvnZZpE': [{'symbol': 'CEMI', 'cnt': '3.0'}], 'var_call_e19KJbPnf0BLq6VEgx0aU7ZR': [{'symbol': 'CFBK', 'cnt': '0.0'}], 'var_call_DVhD2a6cac8Mfd5QOp3U8fNW': [{'symbol': 'CFFA', 'cnt': '0.0'}], 'var_call_RLtFDEWA1QnfFLs2WGnNmw1c': [{'symbol': 'CLRB', 'cnt': '14.0'}], 'var_call_UqSxYipXQNbmfCg1Y7dh9H8u': [{'symbol': 'CORV', 'cnt': '10.0'}], 'var_call_LR4JofGrKERwkRYVLv6weysc': [{'symbol': 'CPAAU', 'cnt': '0.0'}], 'var_call_NpSvAjzds0HlfHkKHT38oFO0': [{'symbol': 'CPAH', 'cnt': '16.0'}], 'var_call_YC1VqfW6NIrEhLD7kmxE1Myw': [{'symbol': 'CUBA', 'cnt': '0.0'}], 'var_call_ihT3T0HbPCpdgkcMWsEnpdzq': [{'symbol': 'CVV', 'cnt': '0.0'}], 'var_call_35Kg6G9oDaw0MaIWd2sTKnYw': [{'symbol': 'DZSI', 'cnt': '1.0'}], 'var_call_qBOKyv9JqB8SDOZiaLWChZrT': [{'symbol': 'ELSE', 'cnt': '0.0'}], 'var_call_y7cCAu6KXp6Tm8dxd5KzRcf2': [{'symbol': 'EXPC', 'cnt': '0.0'}], 'var_call_ZMn3kpMZwOMZGumkM0vik9gd': [{'symbol': 'EYEG', 'cnt': '18.0'}], 'var_call_7Trr0IG91SjugyVx0ro7B66Q': [{'symbol': 'FAMI', 'cnt': '23.0'}], 'var_call_DBR19pCd8lPAtIQoIwrFToCL': [{'symbol': 'FNCB', 'cnt': '1.0'}], 'var_call_TrqLs87JewWxWVupf7ko6vPH': [{'symbol': 'FSBW', 'cnt': '0.0'}], 'var_call_NcawRBgmZI6spfNAV3zl4Jeb': [{'symbol': 'FTFT', 'cnt': '21.0'}], 'var_call_C1jGUzBVWT9htPkmQMWOMtSG': [{'symbol': 'GDYN', 'cnt': '0.0'}], 'var_call_caQGYzLUZlUvhd3pRI0KZNuA': [{'symbol': 'GLG', 'cnt': '42.0'}], 'var_call_MQs9uOYyEP9qomLVxxGxO9dM': [{'symbol': 'GRNVU', 'cnt': '0.0'}], 'var_call_yIg7PFO66rAA337qQplNarhG': [{'symbol': 'GTEC', 'cnt': '0.0'}], 'var_call_TChOnDefYJskwnm6JDeURFT3': [{'symbol': 'HCCOU', 'cnt': '0.0'}], 'var_call_QzZopb2cMD4u5t7zyE9IQs63': [{'symbol': 'HNNA', 'cnt': '0.0'}], 'var_call_gvqQADm1tLaZzddq5ClRm47L': [{'symbol': 'HQI', 'cnt': '2.0'}], 'var_call_tqCCLQuO4Jc7sMFnFgSq16KG': [{'symbol': 'HRTX', 'cnt': '1.0'}], 'var_call_f53qMrq5rWTsZmg4a42u1sx4': [{'symbol': 'IDEX', 'cnt': '15.0'}], 'var_call_UVuvkdRXS9emgNW3eTlofeVI': [{'symbol': 'IGIC', 'cnt': '0.0'}], 'var_call_xJth2457SlgZ1m4AzXGn3ZTM': [{'symbol': 'IOTS', 'cnt': '1.0'}], 'var_call_GUBn45TZ8Y13L5dw7Dyh3ZIo': [{'symbol': 'ISNS', 'cnt': '0.0'}], 'var_call_OXJ57CtjWnX3g7H7Fe6IifQy': [{'symbol': 'ITI', 'cnt': '0.0'}], 'var_call_Z1ARyUouLb9sBhYzmMdBa5qm': [{'symbol': 'LACQ', 'cnt': '0.0'}], 'var_call_Ha9LFy2Q94KZEpTjMUkMejTV': [{'symbol': 'MBCN', 'cnt': '0.0'}], 'var_call_OiNKAvYSt3d1ksQR4HAv7J4a': [{'symbol': 'MBNKP', 'cnt': '0.0'}], 'var_call_OYrGbpSOG6S8HvfK6mAGsgtK': [{'symbol': 'MCEP', 'cnt': '14.0'}], 'var_call_GSSlIti8QgK4kYg9fl83GdNU': [{'symbol': 'MLND', 'cnt': '3.0'}], 'var_call_6tUQLqJuKLaoYmv5BwMvslSX': [{'symbol': 'MMAC', 'cnt': '1.0'}], 'var_call_zlpEvte8QlLdbaYyaUbZvhmQ': [{'symbol': 'MNCLU', 'cnt': '0.0'}], 'var_call_kxRMJ6Na2DUHa66K8AL5zazI': [{'symbol': 'MNPR', 'cnt': '4.0'}], 'var_call_2XwEkSMlj1ywAqgxJAoOLh0g': [{'symbol': 'NVEE', 'cnt': '1.0'}], 'var_call_nDd4QYzvLUvLjWHT50bxyzsH': [{'symbol': 'NXTD', 'cnt': '15.0'}], 'var_call_P7MAkTUg3CF9HEABZ4lh5JGd': [{'symbol': 'OPOF', 'cnt': '0.0'}], 'var_call_jKQpji4fO1lniyDO8JHY4NJu': [{'symbol': 'OPTT', 'cnt': '12.0'}], 'var_call_HiaaOHZxSunT0ieXN5Hdxm8D': [{'symbol': 'ORGO', 'cnt': '15.0'}], 'var_call_KfDMqwsbztQhqdhyJDq8izqJ': [{'symbol': 'ORSNU', 'cnt': '0.0'}], 'var_call_JGL2rd3KUQD6LzbcgotCy1jZ': [{'symbol': 'OTEL', 'cnt': '1.0'}], 'var_call_vpGT7ecbj8fZgcyHJDD6iwrH': [{'symbol': 'PBFS', 'cnt': '0.0'}], 'var_call_NYZY1GUrEWbQ7ySAv8eILlNh': [{'symbol': 'PBTS', 'cnt': '8.0'}], 'var_call_MmisjCHZpKdUqZm6TdPJNFcI': [{'symbol': 'PCSB', 'cnt': '0.0'}], 'var_call_E87DMMBSJCI7oMnWT6POwURO': [{'symbol': 'PECK', 'cnt': '19.0'}], 'var_call_Ah9JFYVecMHEvD5mQWzC8EzB': [{'symbol': 'PEIX', 'cnt': '12.0'}], 'var_call_XArvjf8vl6OtYGlXo3Ybc5iQ': [{'symbol': 'PFIE', 'cnt': '2.0'}], 'var_call_OFwLQwfYCpLHwPrt0j911bQK': [{'symbol': 'PLIN', 'cnt': '1.0'}], 'var_call_mNan7m1Uf4gQpXwrnQqlhQbB': [{'symbol': 'POPE', 'cnt': '0.0'}], 'var_call_RxbKdxhvt3Pl9vhQaH0K9XiX': [{'symbol': 'QRHC', 'cnt': '3.0'}], 'var_call_D8bVrMIY7r7IVtrcnccgJE8p': [{'symbol': 'SES', 'cnt': '51.0'}], 'var_call_3HzqaOeDvpxpGIvyamXVKveT': [{'symbol': 'SHSP', 'cnt': '1.0'}], 'var_call_uQEvo0NAg76b23m87sQANKNn': [{'symbol': 'SNSS', 'cnt': '32.0'}], 'var_call_s9CZ42ATThAkInqVLvQCeivk': [{'symbol': 'SSNT', 'cnt': '11.0'}], 'var_call_PMmSgnvk7rup4czW86eNwY3q': [{'symbol': 'STKS', 'cnt': '0.0'}], 'var_call_FNejCeoCV016jrJAHVZxYae8': [{'symbol': 'TGLS', 'cnt': '0.0'}], 'var_call_toKWWtu3P7vTyFoJAvFyQRuj': [{'symbol': 'TMSR', 'cnt': '40.0'}], 'var_call_Z3NjOrinFj1gGXSbkABbILPX': [{'symbol': 'VERB', 'cnt': '38.0'}], 'var_call_k9vPwczL1NpCaBynDpw7pTcx': [{'symbol': 'VMD', 'cnt': '1.0'}], 'var_call_VVhQlqcY6xFwAGru1R0dXiIa': [{'symbol': 'VRRM', 'cnt': '0.0'}], 'var_call_WajePypWi0AwaktGVthGVZ9h': [{'symbol': 'VTIQW', 'cnt': '6.0'}], 'var_call_BPgufWRfwngJwn2aZIUjjqY0': [{'symbol': 'VVPR', 'cnt': '14.0'}], 'var_call_krhUI68kcMjWzTKoXZ4VdgnW': [{'symbol': 'WHLM', 'cnt': '0.0'}], 'var_call_C1c9qyEGXJdF3m10lhBGhm7O': [{'symbol': 'WHLR', 'cnt': '15.0'}], 'var_call_oiUjucLRyhIr3EfOTCjitHR6': [{'symbol': 'XBIOW', 'cnt': '7.0'}], 'var_call_cy3DKY4ImWa2LlckAM2vT7L8': [{'symbol': 'XPEL', 'cnt': '4.0'}]}

exec(code, env_args)
