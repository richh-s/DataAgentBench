code = """import json

# top indices from previous result
rows = var_call_Oi9nfJysnYoYIOtKjy3a44ZE
indices=[r['Index'] for r in rows]

# manual mapping index->country based on well-known major indices
country_map={
 'IXIC':'United States',
 'NYA':'United States',
 'NSEI':'India',
 '000001.SS':'China',
 '399001.SZ':'China'
}

out=[]
for r in rows:
    idx=r['Index']
    out.append({
        'Index': idx,
        'Country': country_map.get(idx,'Unknown'),
        'GrowthFactor_since_2000': float(r['growth_factor'])
    })

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_idocMYDPNBzOs3BZu1QIaATA': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_call_7gYZlJs80bw859XOXlXbtOM2': [{'Date': '31 Dec 1986, 00:00'}, {'Date': 'January 02, 1987 at 12:00 AM'}, {'Date': '1987-01-05 00:00:00'}, {'Date': '06 Jan 1987, 00:00'}, {'Date': '07 Jan 1987, 00:00'}, {'Date': '1987-01-08 00:00:00'}, {'Date': '1987-01-09 00:00:00'}, {'Date': '1987-01-12 00:00:00'}, {'Date': '1987-01-13 00:00:00'}, {'Date': '1987-01-14 00:00:00'}, {'Date': 'January 15, 1987 at 12:00 AM'}, {'Date': 'January 16, 1987 at 12:00 AM'}, {'Date': 'January 19, 1987 at 12:00 AM'}, {'Date': '20 Jan 1987, 00:00'}, {'Date': 'January 21, 1987 at 12:00 AM'}, {'Date': '22 Jan 1987, 00:00'}, {'Date': 'January 23, 1987 at 12:00 AM'}, {'Date': 'January 26, 1987 at 12:00 AM'}, {'Date': '27 Jan 1987, 00:00'}, {'Date': 'January 28, 1987 at 12:00 AM'}], 'var_call_VMs9upOC3FtkUv9AeWmASaVZ': 'file_storage/call_VMs9upOC3FtkUv9AeWmASaVZ.json', 'var_call_NFdUSnvkvX4OLLflvWjUZRlC': [], 'var_call_pZxiwKZNrjlwxlB24DWTIF46': [{'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM', 'n': '104224'}], 'var_call_9mR52uPFETqIdQ1fM2klmW00': [{'Index': 'NYA', 'n': '13947', 'min_date': '01 Apr 1969, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'N225', 'n': '13874', 'min_date': '01 Apr 1971, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'IXIC', 'n': '12690', 'min_date': '01 Apr 1974, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'GSPTSE', 'n': '10526', 'min_date': '01 Apr 1981, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'HSI', 'n': '8492', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'GDAXI', 'n': '8438', 'min_date': '01 Apr 1992, 00:00', 'max_date': 'September 30, 2016 at 12:00 AM'}, {'Index': 'SSMI', 'n': '7671', 'min_date': '01 Apr 1996, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': 'TWII', 'n': '5869', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2020 at 12:00 AM'}, {'Index': '000001.SS', 'n': '5791', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': '399001.SZ', 'n': '5760', 'min_date': '01 Apr 2004, 00:00', 'max_date': 'September 30, 2015 at 12:00 AM'}, {'Index': 'N100', 'n': '5474', 'min_date': '01 Apr 2003, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}, {'Index': 'NSEI', 'n': '3346', 'min_date': '01 Apr 2014, 00:00', 'max_date': 'September 30, 2014 at 12:00 AM'}, {'Index': 'J203.JO', 'n': '2346', 'min_date': '01 Apr 2016, 00:00', 'max_date': 'September 30, 2019 at 12:00 AM'}], 'var_call_YmWYFaKdVEa2GzYWqygE66dg': 'file_storage/call_YmWYFaKdVEa2GzYWqygE66dg.json', 'var_call_cJtI1ejKD9bO8ZR3hZy8iOBj': {'parsed_non_null': 1319, 'total': 2000, 'min_parsed': '1965-12-31 00:00:00', 'max_parsed': '1974-01-16 00:00:00'}, 'var_call_UdVJs56pmmETRtC8dZtl4Vlg': 'file_storage/call_UdVJs56pmmETRtC8dZtl4Vlg.json', 'var_call_Oi9nfJysnYoYIOtKjy3a44ZE': [{'Index': '399001.SZ', 'first': 615.19519536, 'last': 2405.5648432, 'n_months': 258, 'growth_factor': 3.9102464735}, {'Index': 'IXIC', 'first': 3940.350098, 'last': 13748.74023, 'n_months': 257, 'growth_factor': 3.4892179345}, {'Index': 'NSEI', 'first': 49.405, 'last': 154.3565039, 'n_months': 165, 'growth_factor': 3.1243093594}, {'Index': 'NYA', 'first': 6574.009766, 'last': 16555.66016, 'n_months': 257, 'growth_factor': 2.5183504055}, {'Index': '000001.SS', 'first': 236.97871088, 'last': 576.12480464, 'n_months': 257, 'growth_factor': 2.4311247306}]}

exec(code, env_args)
