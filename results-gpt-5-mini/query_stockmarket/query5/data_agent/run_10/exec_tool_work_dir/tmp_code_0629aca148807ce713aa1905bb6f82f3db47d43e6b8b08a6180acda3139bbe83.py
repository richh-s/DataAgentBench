code = """import json
# Gather counts from the stored keys produced by the many query_db calls
# Keys list manually compiled from the previous responses
keys = [
 'var_call_f7WgYmDT7nRouowbcnPq2vfv', 'var_call_NzvmHc1yIZzaJq0wpuRwhRmz', 'var_call_mDH5ycMz3dPnEiIe2D8oHfPc', 'var_call_3MXtpgJeZ2PdgOFlvUQ1RPnM', 'var_call_l9YeJ6UR8Fu3hV5WQAQ9uUk6',
 'var_call_NU0ppfrxG3iPkM9n7C7PNscQ', 'var_call_8wNVzVgf95hlJZUYp4RNfNoq', 'var_call_ym3dTHOUhpmbSc7bHnkGmlsv', 'var_call_QdfgE35RFOInR7CoylJzb5tl', 'var_call_rpLScoJA1WaNVK7XCo6zkaYd',
 'var_call_86bZgnnoBJm2wine3ZG1nuk3', 'var_call_ZCJ2UkEb9TaauqcCjbgVU5W7', 'var_call_5WRKFN4gZMUV2GyqKeZd2H3D', 'var_call_Bk5cE3Z9xGjNbYntQKCmvRj1', 'var_call_V186Yr4Da2UHgiJnugcDnJNZ',
 'var_call_LVBN9DsCEe6JRafVvlIAovfj', 'var_call_ze1B1LjaRN8Q4hQ8rRPMOkoQ', 'var_call_bUSIWp4ejXx2Y0V6fjmhjV7H', 'var_call_15OQ8QTz4Nsi24npqBn0tKs5', 'var_call_5fKj8cnMpvhQdDZgzDWDmArb',
 'var_call_zGY6fLjDwwsEZLzMHSDxOiOA', 'var_call_Rk88rAeHMFikaTgymj1toTHe', 'var_call_hYEJOxhEZCqGdBREdzPZiLlT', 'var_call_YshrBhRd6nCDbqyiszj1b9sa', 'var_call_zrUttd9wARugDWbXcl73YTQt',
 'var_call_o9Vzz52Qh0j5URtWdkAMsnXS', 'var_call_ksa8pYzWVNa47doTeDI1TjAH', 'var_call_EyG8PgjnQmaGfAAjB73vVXtM', 'var_call_VxaKmG7pqOZ2xIW0JjmXTlpl', 'var_call_98zJ3m6sVVJNbvqwpsJZ5lUO',
 'var_call_JJfDDvwC5HMrO7OnibpRGAut', 'var_call_DUydAr1RY2uJjiPnwiPiiqxz', 'var_call_t0BgA4FPw5KcPha2c7mvXFeU', 'var_call_rZaEjVBTLVnb7tqjDwtFa9Yv', 'var_call_o5FCrAX1AQJoK5ity2Q6mc5Y',
 'var_call_L9fdedZpNzVzR0wK4rFKMPMD', 'var_call_6zr8u0Mi7yIhoZhUUa3GrLQ4', 'var_call_CHxD1bbFOmX3FznLyD63FmFd', 'var_call_eT3iV7x66HKrE7rtBnlQKZor', 'var_call_QXlUpnDKIhiAAQeUUpOkxbxK',
 'var_call_7x9EFXQOVARkI2MEvJj1P2IA', 'var_call_1uMe8MXwKanTqPmi2Cd6ZgRa', 'var_call_SLiZNqJ7TWAQMETv6NcEu6jE', 'var_call_b8gE8fka1H4puOzzqLxu6jYG', 'var_call_APdhsdqtvmQBEGY5nS2HUpnN',
 'var_call_ueLJuI5kH6RRpv5gQF7riOp5', 'var_call_KaIv4j6ui4QYBvu1ZYzBaQbn', 'var_call_otZyi3xLnLubilee2Gd0qwYt', 'var_call_YbSHxFlc4xoCSvf3XETGsbZJ', 'var_call_i0A9eTU3Z8NUFJnh61YAtFLo',
 'var_call_PF4GYpHUIWVTox1kDbp5hWJp', 'var_call_riHOapRQsuE5OX4GsMPspBpX', 'var_call_YGinEsXSQMVtIyffZe6LxWe6', 'var_call_eVSwfdtXapdjYTJId1lmzhVU', 'var_call_6FEnOwbaLin0QziDq98b3jWS',
 'var_call_aNssxzCzvctssfVtGDiGZ78s', 'var_call_TaEIxsgfrX9ZiEzEa4kUGCto', 'var_call_CeTXJaQEJA7fkZ2E9syUhCQR', 'var_call_gCy1aMkHWwSmMNfIwIcNGRBU', 'var_call_2XdOFMUTHujUHnD9PkKagrVN',
 'var_call_7vFlTctqGm3JvZSEv6Yu19OQ', 'var_call_RcQ2stlxNCaCePgLaTnHTj7x', 'var_call_68Uxqo1HyEwmtgPtxXKsmuRA', 'var_call_b50jAMqXyIxXWxJ1UuoAbI5x', 'var_call_x9PD8ZZXoHenBXMM4Pj5oiA6',
 'var_call_jK8ig78fhQqC3MEL9UyhFD1B', 'var_call_S9l3exeXBknqECEY3MsmeHo0', 'var_call_aFAh13BbuNaRkSRxTuVtYhbB', 'var_call_nyKMNIeXW7BRH4kbrGVdQNlu', 'var_call_Dvj3idqrkoho2aKZDbpeXSPR',
 'var_call_nBXhLJl8bXg3grTlRNiseL6m', 'var_call_0K2UxQ1NZmQblil7SEZyQgRP', 'var_call_Mj9w8yoz6ovbbuOmBGt7PPZV', 'var_call_bE99QAmKjiOFsDPqNKqOFUOp', 'var_call_m9rlyOABIfWhomsm46DCQEAD',
 'var_call_E29zKgrDcS18tCYz4uSVnGBU', 'var_call_NueshWWduHBNeMcJ847TvqaX', 'var_call_wl7t8Z3JxHClo0muy1BlH6zw', 'var_call_ng77uX2dVuj07FGqoxKiGP9v', 'var_call_mScJPS5ieKVZDbQMrXMseLo7',
 'var_call_HOngRNYxqxYY43uKDjowHZbU', 'var_call_gTn362NG8K9lOSjcfRIe3Bi9', 'var_call_3DiAprutAampsLNCkviuKiyo', 'var_call_nlvUTrF09EOqneBWYlyvbw4G', 'var_call_Cw4wLoXcwiFPIUuNmg7sS6tS'
]

# Map symbols to the keys in order of when queries were run (we need the symbol list in same order)
symbols_order = [
 'AGMH','ALACU','AMHC','ANDA','APEX','BCLI','BHAT','BIOC','BKYI','BLFS',
 'BOSC','BOTJ','BWEN','CBAT','CCCL','CDMOP','CEMI','CFBK','CFFA','CLRB',
 'CORV','CPAAU','CPAH','CUBA','CVV','DZSI','ELSE','EXPC','EYEG','FAMI',
 'FNCB','FSBW','FTFT','GDYN','GLG','GRNVU','GTEC','HCCOU','HNNA','HQI',
 'HRTX','IDEX','IGIC','IOTS','ISNS','ITI','LACQ','MBCN','MBNKP','MCEP',
 'MLND','MMAC','MNCLU','MNPR','NVEE','NXTD','OPOF','OPTT','ORGO','ORSNU',
 'OTEL','PBFS','PBTS','PCSB','PECK','PEIX','PFIE','PLIN','POPE','QRHC',
 'SES','SHSP','SNSS','SSNT','STKS','TGLS','TMSR','VERB','VMD','VRRM',
 'VTIQW','VVPR','WHLM','WHLR','XBIOW','XPEL'
]

# Build symbol->count dict
sym_counts = {}
for sym,key in zip(symbols_order, keys):
    val = globals().get(key)
    if val is None:
        # try reading file if exists
        try:
            with open(key, 'r') as f:
                val = json.load(f)
        except Exception:
            val = None
    # val should be list like [{"cnt": "13"}]
    if isinstance(val, list) and len(val)>0 and 'cnt' in val[0]:
        try:
            cnt = int(val[0]['cnt'])
        except:
            cnt = 0
    else:
        cnt = 0
    sym_counts[sym] = cnt

# Find top 5 symbols by count
top5 = sorted(sym_counts.items(), key=lambda x: x[1], reverse=True)[:5]
# We need company names from stockinfo_records (from earlier file var_call_wJvVknT3N8zlKck366Iwh6Cj)
with open(var_call_wJvVknT3N8zlKck366Iwh6Cj, 'r') as f:
    stockinfo_records = json.load(f)
sym_to_name = {rec['Symbol']: rec['Company Description'] for rec in stockinfo_records}

result = [{'Symbol': s, 'Company Description': sym_to_name.get(s,''), 'Count': c} for s,c in top5]
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_wJvVknT3N8zlKck366Iwh6Cj': 'file_storage/call_wJvVknT3N8zlKck366Iwh6Cj.json', 'var_call_50uryvni7Ci1ykukhix6ImaP': 'file_storage/call_50uryvni7Ci1ykukhix6ImaP.json', 'var_call_rfbNBTSzxjxWdM59EorwdL5a': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_f7WgYmDT7nRouowbcnPq2vfv': [{'cnt': '13'}], 'var_call_NzvmHc1yIZzaJq0wpuRwhRmz': [{'cnt': '0'}], 'var_call_mDH5ycMz3dPnEiIe2D8oHfPc': [{'cnt': '0'}], 'var_call_3MXtpgJeZ2PdgOFlvUQ1RPnM': [{'cnt': '0'}], 'var_call_l9YeJ6UR8Fu3hV5WQAQ9uUk6': [{'cnt': '15'}], 'var_call_NU0ppfrxG3iPkM9n7C7PNscQ': [{'cnt': '0'}], 'var_call_8wNVzVgf95hlJZUYp4RNfNoq': [{'cnt': '10'}], 'var_call_ym3dTHOUhpmbSc7bHnkGmlsv': [{'cnt': '21'}], 'var_call_QdfgE35RFOInR7CoylJzb5tl': [{'cnt': '16'}], 'var_call_rpLScoJA1WaNVK7XCo6zkaYd': [{'cnt': '0'}], 'var_call_86bZgnnoBJm2wine3ZG1nuk3': [{'cnt': '3'}], 'var_call_ZCJ2UkEb9TaauqcCjbgVU5W7': [{'cnt': '0'}], 'var_call_5WRKFN4gZMUV2GyqKeZd2H3D': [{'cnt': '5'}], 'var_call_Bk5cE3Z9xGjNbYntQKCmvRj1': [{'cnt': '23'}], 'var_call_V186Yr4Da2UHgiJnugcDnJNZ': [{'cnt': '13'}], 'var_call_LVBN9DsCEe6JRafVvlIAovfj': [{'cnt': '0'}], 'var_call_ze1B1LjaRN8Q4hQ8rRPMOkoQ': [{'cnt': '3'}], 'var_call_bUSIWp4ejXx2Y0V6fjmhjV7H': [{'cnt': '0'}], 'var_call_15OQ8QTz4Nsi24npqBn0tKs5': [{'cnt': '0'}], 'var_call_5fKj8cnMpvhQdDZgzDWDmArb': [{'cnt': '14'}], 'var_call_zGY6fLjDwwsEZLzMHSDxOiOA': [{'cnt': '10'}], 'var_call_Rk88rAeHMFikaTgymj1toTHe': [{'cnt': '0'}], 'var_call_hYEJOxhEZCqGdBREdzPZiLlT': [{'cnt': '16'}], 'var_call_YshrBhRd6nCDbqyiszj1b9sa': [{'cnt': '0'}], 'var_call_zrUttd9wARugDWbXcl73YTQt': [{'cnt': '0'}], 'var_call_o9Vzz52Qh0j5URtWdkAMsnXS': [{'cnt': '1'}], 'var_call_ksa8pYzWVNa47doTeDI1TjAH': [{'cnt': '0'}], 'var_call_EyG8PgjnQmaGfAAjB73vVXtM': [{'cnt': '0'}], 'var_call_VxaKmG7pqOZ2xIW0JjmXTlpl': [{'cnt': '18'}], 'var_call_98zJ3m6sVVJNbvqwpsJZ5lUO': [{'cnt': '23'}], 'var_call_JJfDDvwC5HMrO7OnibpRGAut': [{'cnt': '1'}], 'var_call_DUydAr1RY2uJjiPnwiPiiqxz': [{'cnt': '0'}], 'var_call_t0BgA4FPw5KcPha2c7mvXFeU': [{'cnt': '21'}], 'var_call_rZaEjVBTLVnb7tqjDwtFa9Yv': [{'cnt': '0'}], 'var_call_o5FCrAX1AQJoK5ity2Q6mc5Y': [{'cnt': '42'}], 'var_call_L9fdedZpNzVzR0wK4rFKMPMD': [{'cnt': '0'}], 'var_call_6zr8u0Mi7yIhoZhUUa3GrLQ4': [{'cnt': '0'}], 'var_call_CHxD1bbFOmX3FznLyD63FmFd': [{'cnt': '0'}], 'var_call_eT3iV7x66HKrE7rtBnlQKZor': [{'cnt': '0'}], 'var_call_QXlUpnDKIhiAAQeUUpOkxbxK': [{'cnt': '2'}], 'var_call_7x9EFXQOVARkI2MEvJj1P2IA': [{'cnt': '1'}], 'var_call_1uMe8MXwKanTqPmi2Cd6ZgRa': [{'cnt': '15'}], 'var_call_SLiZNqJ7TWAQMETv6NcEu6jE': [{'cnt': '0'}], 'var_call_b8gE8fka1H4puOzzqLxu6jYG': [{'cnt': '1'}], 'var_call_APdhsdqtvmQBEGY5nS2HUpnN': [{'cnt': '0'}], 'var_call_ueLJuI5kH6RRpv5gQF7riOp5': [{'cnt': '0'}], 'var_call_KaIv4j6ui4QYBvu1ZYzBaQbn': [{'cnt': '0'}], 'var_call_otZyi3xLnLubilee2Gd0qwYt': [{'cnt': '0'}], 'var_call_YbSHxFlc4xoCSvf3XETGsbZJ': [{'cnt': '0'}], 'var_call_i0A9eTU3Z8NUFJnh61YAtFLo': [{'cnt': '14'}], 'var_call_PF4GYpHUIWVTox1kDbp5hWJp': [{'cnt': '3'}], 'var_call_riHOapRQsuE5OX4GsMPspBpX': [{'cnt': '1'}], 'var_call_YGinEsXSQMVtIyffZe6LxWe6': [{'cnt': '0'}], 'var_call_eVSwfdtXapdjYTJId1lmzhVU': [{'cnt': '4'}], 'var_call_6FEnOwbaLin0QziDq98b3jWS': [{'cnt': '1'}], 'var_call_aNssxzCzvctssfVtGDiGZ78s': [{'cnt': '15'}], 'var_call_TaEIxsgfrX9ZiEzEa4kUGCto': [{'cnt': '0'}], 'var_call_CeTXJaQEJA7fkZ2E9syUhCQR': [{'cnt': '12'}], 'var_call_gCy1aMkHWwSmMNfIwIcNGRBU': [{'cnt': '15'}], 'var_call_2XdOFMUTHujUHnD9PkKagrVN': [{'cnt': '0'}], 'var_call_7vFlTctqGm3JvZSEv6Yu19OQ': [{'cnt': '1'}], 'var_call_RcQ2stlxNCaCePgLaTnHTj7x': [{'cnt': '0'}], 'var_call_68Uxqo1HyEwmtgPtxXKsmuRA': [{'cnt': '8'}], 'var_call_b50jAMqXyIxXWxJ1UuoAbI5x': [{'cnt': '0'}], 'var_call_x9PD8ZZXoHenBXMM4Pj5oiA6': [{'cnt': '19'}], 'var_call_jK8ig78fhQqC3MEL9UyhFD1B': [{'cnt': '12'}], 'var_call_S9l3exeXBknqECEY3MsmeHo0': [{'cnt': '2'}], 'var_call_aFAh13BbuNaRkSRxTuVtYhbB': [{'cnt': '1'}], 'var_call_nyKMNIeXW7BRH4kbrGVdQNlu': [{'cnt': '0'}], 'var_call_Dvj3idqrkoho2aKZDbpeXSPR': [{'cnt': '3'}], 'var_call_nBXhLJl8bXg3grTlRNiseL6m': [{'cnt': '51'}], 'var_call_htZGEeY1kO8dtFa4dTOjBKER': [{'cnt': '1'}], 'var_call_0K2UxQ1NZmQblil7SEZyQgRP': [{'cnt': '32'}], 'var_call_Mj9w8yoz6ovbbuOmBGt7PPZV': [{'cnt': '11'}], 'var_call_bE99QAmKjiOFsDPqNKqOFUOp': [{'cnt': '0'}], 'var_call_m9rlyOABIfWhomsm46DCQEAD': [{'cnt': '0'}], 'var_call_E29zKgrDcS18tCYz4uSVnGBU': [{'cnt': '40'}], 'var_call_NueshWWduHBNeMcJ847TvqaX': [{'cnt': '38'}], 'var_call_wl7t8Z3JxHClo0muy1BlH6zw': [{'cnt': '1'}], 'var_call_ng77uX2dVuj07FGqoxKiGP9v': [{'cnt': '0'}], 'var_call_mScJPS5ieKVZDbQMrXMseLo7': [{'cnt': '6'}], 'var_call_HOngRNYxqxYY43uKDjowHZbU': [{'cnt': '14'}], 'var_call_gTn362NG8K9lOSjcfRIe3Bi9': [{'cnt': '0'}], 'var_call_3DiAprutAampsLNCkviuKiyo': [{'cnt': '15'}], 'var_call_nlvUTrF09EOqneBWYlyvbw4G': [{'cnt': '7'}], 'var_call_Cw4wLoXcwiFPIUuNmg7sS6tS': [{'cnt': '4'}]}

exec(code, env_args)
