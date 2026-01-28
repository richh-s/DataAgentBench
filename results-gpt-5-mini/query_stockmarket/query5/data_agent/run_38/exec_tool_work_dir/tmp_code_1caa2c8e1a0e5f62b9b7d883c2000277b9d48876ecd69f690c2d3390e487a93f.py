code = """import json
# Load Market Category S records (file path stored in var_call_I0eYLDdGovELtoxJKKig6MRB)
with open(var_call_I0eYLDdGovELtoxJKKig6MRB, 'r') as f:
    recs = json.load(f)
symbols_all = [r['Symbol'] for r in recs]

# Keys from the parallel query results (in the same order queries were issued)
keys = [
'var_call_jqiqOMXi3FXE2ZbUSWFOlC0i','var_call_ShewDKuvvOhZnsQt63HXG4RY','var_call_cDPmtcpyWz9sxsOygYgUwtFB',
'var_call_1jtMUS91XnSOLDcGqov3cCen','var_call_05lyD2XdGKpc8Qyata79EqNw','var_call_jwP7J80JVpWFRwWNg2CRP1A2',
'var_call_QfqDjSbEGMNcevRyA15qX3Qr','var_call_jipD6xtZbOSn20CQqa15QVVK','var_call_r2km1K7RIACLPMZu9DbPySa1',
'var_call_K9VJOdxhHqs3Z0yaEgr8S8GG','var_call_VUUlI0DxTAx8Kb0EpHQ5kYGC','var_call_uhXOI21EhU8GV08RrQWDzKu2',
'var_call_mcdlnthDgkzHFwACQkkPqCMF','var_call_9VdZCZLirXXp7v95tn5Zj4zn','var_call_5FIYBm2Xd6B7DOxj65M86XMk',
'var_call_o1yhAUySS81gn0EX2UFSDOFr','var_call_jJ0FSa2Unm1vOKbwvQgRKC4I','var_call_YC9kHURFgaLTtc7NGL4SC97S',
'var_call_yj85YUMUNguZ6o2B2YSeJVB3','var_call_Ldz8NgtxWtbFin5s3PbNfXZY','var_call_1Bi9CzfF8ULq6cLQs9951odr',
'var_call_BNZMwl2zTpMDFBYj2KGgsHTI','var_call_zORe86rQtDYstlMxawMXyJWT','var_call_KMX5rvnq1N7FeKrExDzLrTXc',
'var_call_CD9aI6sJjFoxldhGbn62QFkl','var_call_ioIJKJkls0C9hNyMnkV5oWEK','var_call_PbTjPugs3YG9O3Vqtvn9FD6J',
'var_call_QqZzu8nV7SgZgaUPCS5Ynvt9','var_call_I4QtSqKwnyuxafplGQ7Yvo0A','var_call_l8DzPPOZXmWlOm6xWKzwr5bY',
'var_call_SgdjnWjXFFyzHknYncypyeeb','var_call_1suYVln8NrizZf4WHFL0Myfr','var_call_YS7DlHyEPAlplERunYnmf2Dr',
'var_call_JZnZ3phqBpOpgPqZ9TwMhF1m','var_call_ckohbmRz7hIpeBxuCAwTEMRK','var_call_ei6fZvxWKcSAYBZNzOsnjvpN',
'var_call_EEefNAus5kYm58zEe7zD9hj4','var_call_IbR3Qz1LWcvjvElFgUov8R2U','var_call_b2cZQuZfH6IKH45U0efaeiIJ',
'var_call_cGqpKrNp4g5eeBLan7qROnq1','var_call_YxHS7qN9LH7gorllW3TxJ7cE','var_call_RSCj6W9YEYED6lNF71gzrhBU',
'var_call_1vOybSrZVLoWMy187kPalyB0','var_call_PXTZQ361oQ7i0OqH4gIEhUMV','var_call_L2RDMd8skuIDDRUyDgot7q36',
'var_call_FPuI35BurOepSNS9a7h2ZP9u','var_call_ih9xbVzckyWAEZvj9xKzT7Nw','var_call_ehrao2edVmNsPChKm9klpRHn',
'var_call_bNjgZGoFVTIigR37SYU8M9BO','var_call_QUnkDLjuz17UayvYvlNYSAI8'
]

# Determine symbols considered (same order as queries were issued)
symbols = symbols_all[:len(keys)]

results = []
for key, sym in zip(keys, symbols):
    # access the variable by name
    data = globals().get(key)
    if data is None:
        # maybe large results are stored as file path; try to open
        try:
            with open(key, 'r') as f:
                data = json.load(f)
        except Exception:
            data = []
    # data expected to be a list like [{"cnt": "13"}]
    cnt = 0
    if isinstance(data, list) and len(data)>0 and 'cnt' in data[0]:
        try:
            cnt = int(data[0]['cnt'])
        except:
            try:
                cnt = int(float(data[0]['cnt']))
            except:
                cnt = 0
    results.append({'symbol': sym, 'count': cnt})

# Sort and take top 5
results_sorted = sorted(results, key=lambda x: x['count'], reverse=True)
top5 = results_sorted[:5]

# Map symbols to company descriptions
sym_to_desc = {r['Symbol']: r['Company Description'] for r in recs}
output = [sym_to_desc.get(item['symbol'], item['symbol']) for item in top5]

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_7VImgvlgFEaHlFsiKpCoAckB': 'file_storage/call_7VImgvlgFEaHlFsiKpCoAckB.json', 'var_call_lbLogyRQLAZG0TxA1yH5r3aq': 'file_storage/call_lbLogyRQLAZG0TxA1yH5r3aq.json', 'var_call_I0eYLDdGovELtoxJKKig6MRB': 'file_storage/call_I0eYLDdGovELtoxJKKig6MRB.json', 'var_call_elBfmAEkw9Rwad3H5cvMHPtR': {'count': 86, 'symbols_sample': ['AGMH', 'ALACU', 'AMHC', 'ANDA', 'APEX', 'BCLI', 'BHAT', 'BIOC', 'BKYI', 'BLFS', 'BOSC', 'BOTJ', 'BWEN', 'CBAT', 'CCCL', 'CDMOP', 'CEMI', 'CFBK', 'CFFA', 'CLRB', 'CORV', 'CPAAU', 'CPAH', 'CUBA', 'CVV', 'DZSI', 'ELSE', 'EXPC', 'EYEG', 'FAMI', 'FNCB', 'FSBW', 'FTFT', 'GDYN', 'GLG', 'GRNVU', 'GTEC', 'HCCOU', 'HNNA', 'HQI', 'HRTX', 'IDEX', 'IGIC', 'IOTS', 'ISNS', 'ITI', 'LACQ', 'MBCN', 'MBNKP', 'MCEP']}, 'var_call_jqiqOMXi3FXE2ZbUSWFOlC0i': [{'cnt': '13'}], 'var_call_ShewDKuvvOhZnsQt63HXG4RY': [{'cnt': '0'}], 'var_call_cDPmtcpyWz9sxsOygYgUwtFB': [{'cnt': '0'}], 'var_call_1jtMUS91XnSOLDcGqov3cCen': [{'cnt': '0'}], 'var_call_05lyD2XdGKpc8Qyata79EqNw': [{'cnt': '15'}], 'var_call_jwP7J80JVpWFRwWNg2CRP1A2': [{'cnt': '0'}], 'var_call_QfqDjSbEGMNcevRyA15qX3Qr': [{'cnt': '10'}], 'var_call_jipD6xtZbOSn20CQqa15QVVK': [{'cnt': '21'}], 'var_call_r2km1K7RIACLPMZu9DbPySa1': [{'cnt': '16'}], 'var_call_K9VJOdxhHqs3Z0yaEgr8S8GG': [{'cnt': '0'}], 'var_call_VUUlI0DxTAx8Kb0EpHQ5kYGC': [{'cnt': '3'}], 'var_call_uhXOI21EhU8GV08RrQWDzKu2': [{'cnt': '0'}], 'var_call_mcdlnthDgkzHFwACQkkPqCMF': [{'cnt': '5'}], 'var_call_9VdZCZLirXXp7v95tn5Zj4zn': [{'cnt': '23'}], 'var_call_5FIYBm2Xd6B7DOxj65M86XMk': [{'cnt': '13'}], 'var_call_o1yhAUySS81gn0EX2UFSDOFr': [{'cnt': '0'}], 'var_call_jJ0FSa2Unm1vOKbwvQgRKC4I': [{'cnt': '3'}], 'var_call_YC9kHURFgaLTtc7NGL4SC97S': [{'cnt': '0'}], 'var_call_yj85YUMUNguZ6o2B2YSeJVB3': [{'cnt': '0'}], 'var_call_Ldz8NgtxWtbFin5s3PbNfXZY': [{'cnt': '14'}], 'var_call_1Bi9CzfF8ULq6cLQs9951odr': [{'cnt': '10'}], 'var_call_BNZMwl2zTpMDFBYj2KGgsHTI': [{'cnt': '0'}], 'var_call_zORe86rQtDYstlMxawMXyJWT': [{'cnt': '16'}], 'var_call_KMX5rvnq1N7FeKrExDzLrTXc': [{'cnt': '0'}], 'var_call_CD9aI6sJjFoxldhGbn62QFkl': [{'cnt': '0'}], 'var_call_ioIJKJkls0C9hNyMnkV5oWEK': [{'cnt': '1'}], 'var_call_PbTjPugs3YG9O3Vqtvn9FD6J': [{'cnt': '0'}], 'var_call_QqZzu8nV7SgZgaUPCS5Ynvt9': [{'cnt': '0'}], 'var_call_I4QtSqKwnyuxafplGQ7Yvo0A': [{'cnt': '18'}], 'var_call_l8DzPPOZXmWlOm6xWKzwr5bY': [{'cnt': '23'}], 'var_call_SgdjnWjXFFyzHknYncypyeeb': [{'cnt': '1'}], 'var_call_1suYVln8NrizZf4WHFL0Myfr': [{'cnt': '0'}], 'var_call_YS7DlHyEPAlplERunYnmf2Dr': [{'cnt': '21'}], 'var_call_JZnZ3phqBpOpgPqZ9TwMhF1m': [{'cnt': '0'}], 'var_call_ckohbmRz7hIpeBxuCAwTEMRK': [{'cnt': '42'}], 'var_call_ei6fZvxWKcSAYBZNzOsnjvpN': [{'cnt': '0'}], 'var_call_EEefNAus5kYm58zEe7zD9hj4': [{'cnt': '0'}], 'var_call_IbR3Qz1LWcvjvElFgUov8R2U': [{'cnt': '0'}], 'var_call_b2cZQuZfH6IKH45U0efaeiIJ': [{'cnt': '0'}], 'var_call_cGqpKrNp4g5eeBLan7qROnq1': [{'cnt': '2'}], 'var_call_YxHS7qN9LH7gorllW3TxJ7cE': [{'cnt': '1'}], 'var_call_RSCj6W9YEYED6lNF71gzrhBU': [{'cnt': '15'}], 'var_call_1vOybSrZVLoWMy187kPalyB0': [{'cnt': '0'}], 'var_call_PXTZQ361oQ7i0OqH4gIEhUMV': [{'cnt': '1'}], 'var_call_L2RDMd8skuIDDRUyDgot7q36': [{'cnt': '0'}], 'var_call_FPuI35BurOepSNS9a7h2ZP9u': [{'cnt': '0'}], 'var_call_ih9xbVzckyWAEZvj9xKzT7Nw': [{'cnt': '0'}], 'var_call_ehrao2edVmNsPChKm9klpRHn': [{'cnt': '0'}], 'var_call_bNjgZGoFVTIigR37SYU8M9BO': [{'cnt': '0'}], 'var_call_QUnkDLjuz17UayvYvlNYSAI8': [{'cnt': '14'}]}

exec(code, env_args)
