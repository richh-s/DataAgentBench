code = """import json

res = var_call_XyBO9DfZxyJmmYUlEioquoPU
out = []
for r in res:
    out.append({
        'Index': r['Index'],
        'Country': r['Country'],
        'Total_Return_Factor': r['Total_Return_Factor'],
        'Total_Return_%': r['Total_Return_%'],
        'Final_Value_USD': r['Final_Value_USD'],
        'Total_Contributed_USD': r['Total_Contributed_USD'],
        'Months': r['Months']
    })

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_oG7GGGtBKqLngxBBYEp8kLmU': ['index_trade'], 'var_call_1GM68aTkhLcTvW1ZJWjMz6Tm': [{'idx': 'J203.JO'}, {'idx': 'N225'}, {'idx': 'GSPTSE'}, {'idx': 'NSEI'}, {'idx': 'GDAXI'}, {'idx': 'IXIC'}, {'idx': 'NYA'}, {'idx': 'HSI'}, {'idx': '000001.SS'}, {'idx': 'SSMI'}, {'idx': 'TWII'}, {'idx': 'N100'}, {'idx': '399001.SZ'}], 'var_call_Iq339CCDNt9nvLswoOgJpgEN': 'file_storage/call_Iq339CCDNt9nvLswoOgJpgEN.json', 'var_call_XyBO9DfZxyJmmYUlEioquoPU': [{'Index': 'IXIC', 'Country': 'United States', 'Total_Return_Factor': 4.816205, 'Total_Return_%': 381.62, 'Final_Value_USD': 1237.7647, 'Total_Contributed_USD': 257.0, 'Months': 257}, {'Index': 'NSEI', 'Country': 'India', 'Total_Return_Factor': 2.356409, 'Total_Return_%': 135.64, 'Final_Value_USD': 388.8075, 'Total_Contributed_USD': 165.0, 'Months': 165}, {'Index': 'GDAXI', 'Country': 'Germany', 'Total_Return_Factor': 2.353701, 'Total_Return_%': 135.37, 'Final_Value_USD': 604.901, 'Total_Contributed_USD': 257.0, 'Months': 257}, {'Index': '399001.SZ', 'Country': 'China', 'Total_Return_Factor': 2.338381, 'Total_Return_%': 133.84, 'Final_Value_USD': 603.3023, 'Total_Contributed_USD': 258.0, 'Months': 258}, {'Index': 'TWII', 'Country': 'Taiwan', 'Total_Return_Factor': 2.244737, 'Total_Return_%': 124.47, 'Final_Value_USD': 576.8974, 'Total_Contributed_USD': 257.0, 'Months': 257}], 'var_call_LKQarw5JtfzMfo4fiECSW2Iw': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
