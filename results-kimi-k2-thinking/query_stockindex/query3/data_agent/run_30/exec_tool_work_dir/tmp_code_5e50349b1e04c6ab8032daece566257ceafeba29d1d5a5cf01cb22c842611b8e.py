code = """import json

# Map indices to exchanges and countries based on standard financial market knowledge
index_mappings = {
    'IXIC': {'Exchange': 'NASDAQ', 'Country': 'United States'},
    '399001.SZ': {'Exchange': 'Shenzhen Stock Exchange', 'Country': 'China'},
    'NSEI': {'Exchange': 'National Stock Exchange of India', 'Country': 'India'},
    'GDAXI': {'Exchange': 'Frankfurt Stock Exchange', 'Country': 'Germany'},
    'N225': {'Exchange': 'Tokyo Stock Exchange', 'Country': 'Japan'},
    'TWII': {'Exchange': 'Taiwan Stock Exchange', 'Country': 'Taiwan'},
    'NYA': {'Exchange': 'New York Stock Exchange', 'Country': 'United States'},
    '000001.SS': {'Exchange': 'Shanghai Stock Exchange', 'Country': 'China'},
    'GSPTSE': {'Exchange': 'Toronto Stock Exchange', 'Country': 'Canada'},
    'SSMI': {'Exchange': 'SIX Swiss Exchange', 'Country': 'Switzerland'},
    'HSI': {'Exchange': 'Hong Kong Stock Exchange', 'Country': 'Hong Kong'},
    'N100': {'Exchange': 'Euronext', 'Country': 'Netherlands/Europe'},
    'J203.JO': {'Exchange': 'Johannesburg Stock Exchange', 'Country': 'South Africa'}
}

# Top 5 results from previous analysis
top_5_results = [
    {'Index': 'IXIC', 'Return_Percentage': 358.15, 'Total_Months': 251},
    {'Index': '399001.SZ', 'Return_Percentage': 127.11, 'Total_Months': 251},
    {'Index': 'NSEI', 'Return_Percentage': 115.47, 'Total_Months': 159},
    {'Index': 'GDAXI', 'Return_Percentage': 111.75, 'Total_Months': 251},
    {'Index': 'N225', 'Return_Percentage': 107.82, 'Total_Months': 251}
]

# Create final answer with country information
final_answer = []
for result in top_5_results:
    idx = result['Index']
    mapping = index_mappings.get(idx, {'Exchange': 'Unknown', 'Country': 'Unknown'})
    
    final_answer.append({
        'Rank': len(final_answer) + 1,
        'Index_Symbol': idx,
        'Index_Name': mapping['Exchange'],
        'Country': mapping['Country'],
        'Return_Percentage': result['Return_Percentage'],
        'Investment_Period_Months': result['Total_Months']
    })

print('__RESULT__:')
print(json.dumps(final_answer, indent=2))"""

env_args = {'var_functions.query_db:0': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}], 'var_functions.query_db:2': [{'Index': '000001.SS'}, {'Index': '399001.SZ'}, {'Index': 'GDAXI'}, {'Index': 'GSPTSE'}, {'Index': 'HSI'}, {'Index': 'IXIC'}, {'Index': 'J203.JO'}, {'Index': 'N100'}, {'Index': 'N225'}, {'Index': 'NSEI'}, {'Index': 'NYA'}, {'Index': 'SSMI'}, {'Index': 'TWII'}], 'var_functions.list_db:4': ['index_trade'], 'var_functions.query_db:6': [{'Index': '000001.SS', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '5791'}, {'Index': '399001.SZ', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '5760'}, {'Index': 'GDAXI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_days': '8438'}, {'Index': 'GSPTSE', 'first_date': '01 Apr 1981, 00:00', 'last_date': 'September 30, 2016 at 12:00 AM', 'total_days': '10526'}, {'Index': 'HSI', 'first_date': '01 Apr 1992, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '8492'}, {'Index': 'IXIC', 'first_date': '01 Apr 1974, 00:00', 'last_date': 'September 30, 2015 at 12:00 AM', 'total_days': '12690'}, {'Index': 'J203.JO', 'first_date': '01 Apr 2016, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '2346'}, {'Index': 'N100', 'first_date': '01 Apr 2003, 00:00', 'last_date': 'September 30, 2019 at 12:00 AM', 'total_days': '5474'}, {'Index': 'N225', 'first_date': '01 Apr 1971, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '13874'}, {'Index': 'NSEI', 'first_date': '01 Apr 2014, 00:00', 'last_date': 'September 30, 2014 at 12:00 AM', 'total_days': '3346'}, {'Index': 'NYA', 'first_date': '01 Apr 1969, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '13947'}, {'Index': 'SSMI', 'first_date': '01 Apr 1996, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '7671'}, {'Index': 'TWII', 'first_date': '01 Apr 2004, 00:00', 'last_date': 'September 30, 2020 at 12:00 AM', 'total_days': '5869'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json', 'var_functions.query_db:10': 'file_storage/functions.query_db:10.json', 'var_functions.query_db:12': 'file_storage/functions.query_db:12.json', 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json', 'var_functions.execute_python:20': {'total_indices_analyzed': 13, 'top_5_indices': [{'Index': 'IXIC', 'First_Date': '2000-01-06', 'Last_Date': '2020-12-29', 'Total_Months': 251, 'First_Price': 3727.13, 'Last_Price': 12850.22, 'Total_Invested': 25200, 'Final_Value': 115452.57, 'Total_Return': 90252.57, 'Return_Percentage': 358.15}, {'Index': '399001.SZ', 'First_Date': '2000-01-05', 'Last_Date': '2020-12-30', 'Total_Months': 251, 'First_Price': 557.81, 'Last_Price': 2272.25, 'Total_Invested': 25200, 'Final_Value': 57230.69, 'Total_Return': 32030.69, 'Return_Percentage': 127.11}, {'Index': 'NSEI', 'First_Date': '2007-09-25', 'Last_Date': '2020-12-30', 'Total_Months': 159, 'First_Price': 49.39, 'Last_Price': 139.82, 'Total_Invested': 16000, 'Final_Value': 34475.41, 'Total_Return': 18475.41, 'Return_Percentage': 115.47}, {'Index': 'GDAXI', 'First_Date': '2000-01-05', 'Last_Date': '2020-12-29', 'Total_Months': 251, 'First_Price': 7932.53, 'Last_Price': 16788.88, 'Total_Invested': 25200, 'Final_Value': 53360.14, 'Total_Return': 28160.14, 'Return_Percentage': 111.75}, {'Index': 'N225', 'First_Date': '2000-01-04', 'Last_Date': '2020-12-30', 'Total_Months': 251, 'First_Price': 190.03, 'Last_Price': 274.44, 'Total_Invested': 25200, 'Final_Value': 52370.75, 'Total_Return': 27170.75, 'Return_Percentage': 107.82}], 'all_indices': [{'Index': 'IXIC', 'Return_Percentage': 358.15, 'Total_Months': 251}, {'Index': '399001.SZ', 'Return_Percentage': 127.11, 'Total_Months': 251}, {'Index': 'NSEI', 'Return_Percentage': 115.47, 'Total_Months': 159}, {'Index': 'GDAXI', 'Return_Percentage': 111.75, 'Total_Months': 251}, {'Index': 'N225', 'Return_Percentage': 107.82, 'Total_Months': 251}, {'Index': 'TWII', 'Return_Percentage': 94.72, 'Total_Months': 251}, {'Index': 'NYA', 'Return_Percentage': 77.18, 'Total_Months': 251}, {'Index': '000001.SS', 'Return_Percentage': 56.17, 'Total_Months': 251}, {'Index': 'GSPTSE', 'Return_Percentage': 54.8, 'Total_Months': 251}, {'Index': 'SSMI', 'Return_Percentage': 49.7, 'Total_Months': 251}, {'Index': 'HSI', 'Return_Percentage': 47.21, 'Total_Months': 251}, {'Index': 'N100', 'Return_Percentage': 43.33, 'Total_Months': 251}, {'Index': 'J203.JO', 'Return_Percentage': 22.22, 'Total_Months': 106}]}, 'var_functions.query_db:22': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}]}

exec(code, env_args)
