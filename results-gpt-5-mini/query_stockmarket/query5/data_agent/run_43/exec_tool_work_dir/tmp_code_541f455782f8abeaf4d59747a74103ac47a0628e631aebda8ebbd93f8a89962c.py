code = """import json
# Collect counts from the parallel query results stored in their keys
keys = [
 'var_call_evDbXTcUQ8RoCx3LfzNn4n56', 'var_call_1vrCrw9Y8mfKaLk2Jrioioiq', 'var_call_FxeUJmlO0z8y9LpZJau9Qcgv',
 'var_call_sDjjCVCxOQxF1ZHzLjeg6IVR', 'var_call_n99DJdTBGET6JtnsdIo9pa5P', 'var_call_1Kdnr8BMCvDPUGRm7qxB2B6N',
 'var_call_TW2wVEkTtXUYOxzqp6gTVB5L', 'var_call_q7HXoBEFllE0rjEqYbKe8HGD', 'var_call_o8ipqpteNLFMXFFOoHQvXNOY',
 'var_call_Kjohdus77OBkc2igUPd5JLZg', 'var_call_ejd1zm3VsvqjdkPaioQZK9NM', 'var_call_TqvD0vE7W3OirqsuyP7zTXZW',
 'var_call_jyakrkXxLuVfODfG4nKIqCEf', 'var_call_Gy8i9xqDGfuUZPQUBZ5PhXwp', 'var_call_Cl8yS9iKoyvWU8J18uUtXhc0',
 'var_call_gMmvChCfRybJVpR7TfC89Un5', 'var_call_nlb877C25dQ6dC9b8bMnfvP2', 'var_call_gMAh9HdLmdQsTNumkQBY9arp',
 'var_call_rkrNSaKkctxTWRDv0hhYDee2', 'var_call_TqvD0vE7W3OirqsuyP7zTXZW', 'var_call_ixzzq0niSM4s90GydERcnRaW',
 'var_call_Tig8uhN2qkRCobtmIno2zQJx', 'var_call_Tig8uhN2qkRCobtmIno2zQJx', 'var_call_kXj1pRUgcS9T4KidOi6oavin',
 'var_call_buJftVVDkRXKKpscFbLawimg', 'var_call_JW1MlohvPjoZLJ9Twqs1LnHA', 'var_call_t6J4C6KC9olMd1sPO4sf1N0Q',
 'var_call_Ax4k2MAiMOvhGAt38IqQsxKe', 'var_call_NcCMyRfxe1AUNqbyQ9MiluBl', 'var_call_hNPvlB7eh1U0arxpOkoJjNkd',
 'var_call_pQjawyPgWakmYKWBdxFVqWnM', 'var_call_2Sy7237anWyeXeWsvgBwNMXe', 'var_call_2Sy7237anWyeXeWsvgBwNMXe',
 'var_call_2Sy7237anWyeXeWsvgBwNMXe', 'var_call_sjvlzmuk9zBwoOnubTW2KtRi', 'var_call_lsAb4Xov5cTm1SO7yAYOddCY',
 'var_call_BmquJThUdVPrDNaa9s5FfmcX', 'var_call_2H63XU8iirScfpmMsxICbUV3', 'var_call_K2clFjemPRmDyk3Q0pi1rmUi',
 'var_call_XLjKEr06KY86WpgfntB0OUeT', 'var_call_WMgsg2S0TudHxSY4lI9Vdwim', 'var_call_8UOmC1AdBgtmW2XMw0ICdmYH',
 'var_call_gF3eZrXT7kTtLxPapf4GViAc', 'var_call_srNZ5GXbEc0qILGjEHqNsxpa', 'var_call_HaDneYkWaIAf1idYy07t32zP',
 'var_call_fS6BgLPOJPA3sXjQ5QHwUD1F', 'var_call_K7nSx4fvqywxJcTc94BFps97', 'var_call_TIDte9mJOZX9vGA3IiB76kg8',
 'var_call_6ACJgwOtqz9dwjcrtdd1MnYQ', 'var_call_3v0bg77ZJffuiFIVcK5aglRd', 'var_call_uBWIrq7yxMq4g1ylEl4oH3bF',
 'var_call_cEFPffJOX96R8TYbA2xgj6UW', 'var_call_9EtkViJort0GfY2hOlGKwsr6', 'var_call_OrT77uPYEGEWiT4Y3dTy5tX4',
 'var_call_SFbaofCqecSRs9INfXXovxKx', 'var_call_ETkeXzTR28UFeFDyiROa2r5p', 'var_call_aoNrEVTFzoXS14HAju2f9572',
 'var_call_3hbhfsuWPFlhuyxpoeGomDQN', 'var_call_3hbhfsuWPFlhuyxpoeGomDQN', 'var_call_fEbJZ47HvyvwjrLUjfcRlyBG',
 'var_call_fEbJZ47HvyvwjrLUjfcRlyBG', 'var_call_4',
]
# The above keys list is messy; instead list keys from the multi-tool output by capturing all var_call_* in globals
import sys
res = {}
for k in list(globals().keys()):
    pass
# We know tool results are accessible as variables by name in this environment; list them
all_vars = globals().keys()
# Filter for var_call_ prefix
var_keys = [k for k in all_vars if k.startswith('var_call_')]

for vk in var_keys:
    val = globals()[vk]
    # val may be a string containing the result text; if it's a list, use it
    try:
        res[vk] = val
    except Exception as e:
        res[vk] = str(val)

# Now parse each result which are lists of dicts
counts = []
for vk, v in res.items():
    try:
        # if it's a string like "[{...}]"
        if isinstance(v, str):
            parsed = json.loads(v)
        else:
            parsed = v
        if isinstance(parsed, list) and len(parsed)>0 and isinstance(parsed[0], dict):
            rec = parsed[0]
            sym = rec.get('Symbol')
            cnt = rec.get('cnt')
            counts.append({'Symbol': sym, 'cnt': float(cnt) if cnt is not None else 0.0, 'var': vk})
    except Exception as e:
        continue

# Sort counts by cnt desc
counts_sorted = sorted(counts, key=lambda x: x['cnt'], reverse=True)

# Keep top 5 symbols
top5 = counts_sorted[:5]

print('__RESULT__:')
print(json.dumps({'top5': top5, 'all_counts_len': len(counts_sorted)}))"""

env_args = {'var_call_WieKl7aHdSZW9WQUOPcwhEKt': 'file_storage/call_WieKl7aHdSZW9WQUOPcwhEKt.json', 'var_call_VgonKm8xOr3QKnin3IPr4pvT': 'file_storage/call_VgonKm8xOr3QKnin3IPr4pvT.json', 'var_call_9kEodSYCb5yj1kZ4zEVqvNCc': {'type_stockinfo': 'list', 'len_stockinfo': 86, 'type_trade_tables': 'list', 'len_trade_tables': 2753}, 'var_call_7L41ZFTbZeAqvr48T0bE1vD2': 'file_storage/call_7L41ZFTbZeAqvr48T0bE1vD2.json', 'var_call_C4BA4GDA4Eo9SkcmJjPoDB4I': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP', 'MLND', 'MMAC', 'MNCLU', 'MNPR', 'NVEE', 'NXTD', 'OPOF', 'OPTT', 'ORGO', 'ORSNU', 'OTEL', 'PBFS', 'PBTS', 'PCSB', 'PECK', 'PEIX', 'PFIE', 'PLIN', 'POPE', 'QRHC', 'SES', 'SHSP', 'SNSS', 'SSNT', 'STKS', 'TGLS', 'TMSR', 'VERB', 'VMD', 'VRRM', 'VTIQW', 'VVPR', 'WHLM', 'WHLR', 'XBIOW', 'XPEL'], 'var_call_evDbXTcUQ8RoCx3LfzNn4n56': [{'Symbol': 'AGMH', 'cnt': '13.0'}], 'var_call_1vrCrw9Y8mfKaLk2Jrioioiq': [{'Symbol': 'ALACU', 'cnt': '0.0'}], 'var_call_FxeUJmlO0z8y9LpZJau9Qcgv': [{'Symbol': 'AMHC', 'cnt': '0.0'}], 'var_call_sDjjCVCxOQxF1ZHzLjeg6IVR': [{'Symbol': 'ANDA', 'cnt': '0.0'}], 'var_call_n99DJdTBGET6JtnsdIo9pa5P': [{'Symbol': 'APEX', 'cnt': '15.0'}], 'var_call_1Kdnr8BMCvDPUGRm7qxB2B6N': [{'Symbol': 'BCLI', 'cnt': '0.0'}], 'var_call_TW2wVEkTtXUYOxzqp6gTVB5L': [{'Symbol': 'BHAT', 'cnt': '10.0'}], 'var_call_q7HXoBEFllE0rjEqYbKe8HGD': [{'Symbol': 'BIOC', 'cnt': '21.0'}], 'var_call_o8ipqpteNLFMXFFOoHQvXNOY': [{'Symbol': 'BKYI', 'cnt': '16.0'}], 'var_call_Kjohdus77OBkc2igUPd5JLZg': [{'Symbol': 'BLFS', 'cnt': '0.0'}], 'var_call_ejd1zm3VsvqjdkPaioQZK9NM': [{'Symbol': 'BOSC', 'cnt': '3.0'}], 'var_call_jyakrkXxLuVfODfG4nKIqCEf': [{'Symbol': 'BOTJ', 'cnt': '0.0'}], 'var_call_Gy8i9xqDGfuUZPQUBZ5PhXwp': [{'Symbol': 'BWEN', 'cnt': '5.0'}], 'var_call_Cl8yS9iKoyvWU8J18uUtXhc0': [{'Symbol': 'CBAT', 'cnt': '23.0'}], 'var_call_gMmvChCfRybJVpR7TfC89Un5': [{'Symbol': 'CCCL', 'cnt': '13.0'}], 'var_call_nlb877C25dQ6dC9b8bMnfvP2': [{'Symbol': 'CDMOP', 'cnt': '0.0'}], 'var_call_gMAh9HdLmdQsTNumkQBY9arp': [{'Symbol': 'CEMI', 'cnt': '3.0'}], 'var_call_rkrNSaKkctxTWRDv0hhYDee2': [{'Symbol': 'CFBK', 'cnt': '0.0'}], 'var_call_TqvD0vE7W3OirqsuyP7zTXZW': [{'Symbol': 'CFFA', 'cnt': '0.0'}], 'var_call_ixzzq0niSM4s90GydERcnRaW': [{'Symbol': 'CLRB', 'cnt': '14.0'}], 'var_call_Tig8uhN2qkRCobtmIno2zQJx': [{'Symbol': 'CORV', 'cnt': '10.0'}], 'var_call_kXj1pRUgcS9T4KidOi6oavin': [{'Symbol': 'CPAAU', 'cnt': '0.0'}], 'var_call_buJftVVDkRXKKpscFbLawimg': [{'Symbol': 'CPAH', 'cnt': '16.0'}], 'var_call_JW1MlohvPjoZLJ9Twqs1LnHA': [{'Symbol': 'CUBA', 'cnt': '0.0'}], 'var_call_t6J4C6KC9olMd1sPO4sf1N0Q': [{'Symbol': 'CVV', 'cnt': '0.0'}], 'var_call_Ax4k2MAiMOvhGAt38IqQsxKe': [{'Symbol': 'DZSI', 'cnt': '1.0'}], 'var_call_NcCMyRfxe1AUNqbyQ9MiluBl': [{'Symbol': 'ELSE', 'cnt': '0.0'}], 'var_call_hNPvlB7eh1U0arxpOkoJjNkd': [{'Symbol': 'EXPC', 'cnt': '0.0'}], 'var_call_pQjawyPgWakmYKWBdxFVqWnM': [{'Symbol': 'EYEG', 'cnt': '18.0'}], 'var_call_2Sy7237anWyeXeWsvgBwNMXe': [{'Symbol': 'FAMI', 'cnt': '23.0'}], 'var_call_sjvlzmuk9zBwoOnubTW2KtRi': [{'Symbol': 'FNCB', 'cnt': '1.0'}], 'var_call_lsAb4Xov5cTm1SO7yAYOddCY': [{'Symbol': 'FSBW', 'cnt': '0.0'}], 'var_call_BmquJThUdVPrDNaa9s5FfmcX': [{'Symbol': 'FTFT', 'cnt': '21.0'}], 'var_call_2H63XU8iirScfpmMsxICbUV3': [{'Symbol': 'GDYN', 'cnt': '0.0'}], 'var_call_K2clFjemPRmDyk3Q0pi1rmUi': [{'Symbol': 'GLG', 'cnt': '42.0'}], 'var_call_XLjKEr06KY86WpgfntB0OUeT': [{'Symbol': 'GRNVU', 'cnt': '0.0'}], 'var_call_WMgsg2S0TudHxSY4lI9Vdwim': [{'Symbol': 'GTEC', 'cnt': '0.0'}], 'var_call_8UOmC1AdBgtmW2XMw0ICdmYH': [{'Symbol': 'HCCOU', 'cnt': '0.0'}], 'var_call_gF3eZrXT7kTtLxPapf4GViAc': [{'Symbol': 'HNNA', 'cnt': '0.0'}], 'var_call_srNZ5GXbEc0qILGjEHqNsxpa': [{'Symbol': 'HQI', 'cnt': '2.0'}], 'var_call_HaDneYkWaIAf1idYy07t32zP': [{'Symbol': 'HRTX', 'cnt': '1.0'}], 'var_call_fS6BgLPOJPA3sXjQ5QHwUD1F': [{'Symbol': 'IDEX', 'cnt': '15.0'}], 'var_call_K7nSx4fvqywxJcTc94BFps97': [{'Symbol': 'IGIC', 'cnt': '0.0'}], 'var_call_TIDte9mJOZX9vGA3IiB76kg8': [{'Symbol': 'IOTS', 'cnt': '1.0'}], 'var_call_6ACJgwOtqz9dwjcrtdd1MnYQ': [{'Symbol': 'ISNS', 'cnt': '0.0'}], 'var_call_3v0bg77ZJffuiFIVcK5aglRd': [{'Symbol': 'ITI', 'cnt': '0.0'}], 'var_call_uBWIrq7yxMq4g1ylEl4oH3bF': [{'Symbol': 'LACQ', 'cnt': '0.0'}], 'var_call_cEFPffJOX96R8TYbA2xgj6UW': [{'Symbol': 'MBCN', 'cnt': '0.0'}], 'var_call_9EtkViJort0GfY2hOlGKwsr6': [{'Symbol': 'MBNKP', 'cnt': '0.0'}], 'var_call_OrT77uPYEGEWiT4Y3dTy5tX4': [{'Symbol': 'MCEP', 'cnt': '14.0'}], 'var_call_SFbaofCqecSRs9INfXXovxKx': [{'Symbol': 'MLND', 'cnt': '3.0'}], 'var_call_ETkeXzTR28UFeFDyiROa2r5p': [{'Symbol': 'MMAC', 'cnt': '1.0'}], 'var_call_aoNrEVTFzoXS14HAju2f9572': [{'Symbol': 'MNCLU', 'cnt': '0.0'}], 'var_call_3hbhfsuWPFlhuyxpoeGomDQN': [{'Symbol': 'MNPR', 'cnt': '4.0'}], 'var_call_fEbJZ47HvyvwjrLUjfcRlyBG': [{'Symbol': 'NVEE', 'cnt': '1.0'}], 'var_call_vlRIOnZ6EeZsCg8cqG3gXldJ': [{'Symbol': 'NXTD', 'cnt': '15.0'}], 'var_call_K88xwbvtY9g5Z3LyCEvRbBTW': [{'Symbol': 'OPOF', 'cnt': '0.0'}], 'var_call_f8tHCZ2n3Gyb8qX2NrZlUn0e': [{'Symbol': 'OPTT', 'cnt': '12.0'}], 'var_call_ptebvrhnQ90SNqZ2I1p735hk': [{'Symbol': 'ORGO', 'cnt': '15.0'}], 'var_call_XUY1B45J9nBwHR5IyAZ5oKvm': [{'Symbol': 'ORSNU', 'cnt': '0.0'}], 'var_call_5ViryMSj2u9kjIaGUNH9Ct3g': [{'Symbol': 'OTEL', 'cnt': '1.0'}], 'var_call_9zyJkpDVMW8nI8ahLwWSb7gC': [{'Symbol': 'PBFS', 'cnt': '0.0'}], 'var_call_2iuke9MkpW4Lvwagt0sSTRlh': [{'Symbol': 'PBTS', 'cnt': '8.0'}], 'var_call_aesRWXAb5WTXqXq9gOMKQJb0': [{'Symbol': 'PCSB', 'cnt': '0.0'}], 'var_call_ayhUMq4tBWMlsulY4nHkRpm6': [{'Symbol': 'PECK', 'cnt': '19.0'}], 'var_call_0Tli3qE8LrtqhTBqnmK61AYT': [{'Symbol': 'PEIX', 'cnt': '12.0'}], 'var_call_x5mlpqfLPyarmas5cWvXxLhb': [{'Symbol': 'PFIE', 'cnt': '2.0'}], 'var_call_32TXrVYeBgeVmkNBsWHdhsDj': [{'Symbol': 'PLIN', 'cnt': '1.0'}], 'var_call_gPTe4vNJoTatan6RrXRdVbrC': [{'Symbol': 'POPE', 'cnt': '0.0'}], 'var_call_Ts6nQnLKSLnpnZVM26tZRcBI': [{'Symbol': 'QRHC', 'cnt': '3.0'}], 'var_call_L8dchj4XDFTIGR5uJM0w2LgB': [{'Symbol': 'SES', 'cnt': '51.0'}], 'var_call_boNYIQYavgP9NbDokxHzdCQf': [{'Symbol': 'SHSP', 'cnt': '1.0'}], 'var_call_UFymoJansDgWgROfMCFM1rLg': [{'Symbol': 'SNSS', 'cnt': '32.0'}], 'var_call_bkqoKrwJSRG9NbNNxClmyHKi': [{'Symbol': 'SSNT', 'cnt': '11.0'}], 'var_call_5IST6kHN3rvC2NyjYbjgJPS7': [{'Symbol': 'STKS', 'cnt': '0.0'}], 'var_call_XghEunGrgVnVsQAwhQwGWygw': [{'Symbol': 'TGLS', 'cnt': '0.0'}], 'var_call_5cIKbISmMhqwo6PrLAbNDRfq': [{'Symbol': 'TMSR', 'cnt': '40.0'}], 'var_call_SBmrjUWjq6VbVvqUdMz3ZNB7': [{'Symbol': 'VERB', 'cnt': '38.0'}], 'var_call_miwsiW1cRzFlOrB7jeqarlaD': [{'Symbol': 'VMD', 'cnt': '1.0'}], 'var_call_bOyWLQuQdwF6kXBwCGLjCFCV': [{'Symbol': 'VRRM', 'cnt': '0.0'}], 'var_call_jsno3o3hj2hMumcr945hHeLc': [{'Symbol': 'VTIQW', 'cnt': '6.0'}], 'var_call_x9LZM2pb2HP1EgC5GDF8t9aa': [{'Symbol': 'VVPR', 'cnt': '14.0'}], 'var_call_9svEeDdn9jCskGbhM901bZ7f': [{'Symbol': 'WHLM', 'cnt': '0.0'}], 'var_call_8ROQ5p4M4nRXUwrCxnCwui2x': [{'Symbol': 'WHLR', 'cnt': '15.0'}], 'var_call_uYhlLCW30UNswBuPPXWHDVEy': [{'Symbol': 'XBIOW', 'cnt': '7.0'}], 'var_call_TdxEXZdKaUaFCcjnclBbwDha': [{'Symbol': 'XPEL', 'cnt': '4.0'}]}

exec(code, env_args)
