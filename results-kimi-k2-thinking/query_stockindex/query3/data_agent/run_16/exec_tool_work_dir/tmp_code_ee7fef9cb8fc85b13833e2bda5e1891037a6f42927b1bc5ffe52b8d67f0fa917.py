code = """import json
import re

# Get the file path from storage
file_path = var_functions.query_db:16
print('File path:', file_path)

# Load the data from the file
with open(file_path, 'r') as f:
    trade_data = json.load(f)

print('Total records:', len(trade_data))
print('First few records:')
for i, rec in enumerate(trade_data[:3]):
    print('  ', rec)

# Extract year from date strings
year_pattern = re.compile(r'(\d{4})')

def extract_year(date_str):
    match = year_pattern.search(date_str)
    return int(match.group(1)) if match else None

# Filter records from 2000 onwards
records_2000_plus = []
for rec in trade_data:
    year = extract_year(rec['Date'])
    if year and year >= 2000:
        records_2000_plus.append({
            'Index': rec['Index'],
            'Date': rec['Date'],
            'Year': year,
            'CloseUSD': float(rec['CloseUSD'])
        })

print('\nRecords from 2000 onwards:', len(records_2000_plus))

unique_indices = sorted(set(r['Index'] for r in records_2000_plus))
print('Unique indices:', unique_indices)
print('Count:', len(unique_indices))"""

env_args = {'var_functions.list_db:0': ['index_info'], 'var_functions.query_db:2': [{'Exchange': 'New York Stock Exchange', 'Currency': 'USD'}, {'Exchange': 'NASDAQ', 'Currency': 'USD'}, {'Exchange': 'Hong Kong Stock Exchange', 'Currency': 'HKD'}, {'Exchange': 'Shanghai Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Tokyo Stock Exchange', 'Currency': 'JPY'}, {'Exchange': 'Euronext', 'Currency': 'EUR'}, {'Exchange': 'Shenzhen Stock Exchange', 'Currency': 'CNY'}, {'Exchange': 'Toronto Stock Exchange', 'Currency': 'CAD'}, {'Exchange': 'National Stock Exchange of India', 'Currency': 'INR'}, {'Exchange': 'Frankfurt Stock Exchange', 'Currency': 'EUR'}, {'Exchange': 'Korea Exchange', 'Currency': 'KRW'}, {'Exchange': 'SIX Swiss Exchange', 'Currency': 'CHF'}, {'Exchange': 'Taiwan Stock Exchange', 'Currency': 'TWD'}, {'Exchange': 'Johannesburg Stock Exchange', 'Currency': 'ZAR'}], 'var_functions.list_db:5': ['index_trade'], 'var_functions.query_db:6': [{'Index': 'J203.JO'}, {'Index': 'N225'}, {'Index': 'GSPTSE'}, {'Index': 'NSEI'}, {'Index': 'GDAXI'}, {'Index': 'IXIC'}, {'Index': 'HSI'}, {'Index': 'NYA'}, {'Index': '000001.SS'}, {'Index': 'SSMI'}, {'Index': 'TWII'}, {'Index': 'N100'}, {'Index': '399001.SZ'}], 'var_functions.query_db:8': [{'Index': 'N225', 'Date': '01 Apr 1971, 00:00', 'Open': '2414.040039', 'High': '2414.040039', 'Low': '2414.040039', 'Close': '2414.040039', 'Adj Close': '2414.040039', 'CloseUSD': '24.14040039'}, {'Index': 'N225', 'Date': '01 Apr 1976, 00:00', 'Open': '4581.819824', 'High': '4581.819824', 'Low': '4581.819824', 'Close': '4581.819824', 'Adj Close': '4581.819824', 'CloseUSD': '45.81819824'}, {'Index': 'N225', 'Date': '01 Apr 1977, 00:00', 'Open': '5008.379883', 'High': '5008.379883', 'Low': '5008.379883', 'Close': '5008.379883', 'Adj Close': '5008.379883', 'CloseUSD': '50.08379883'}, {'Index': 'N225', 'Date': '01 Apr 1980, 00:00', 'Open': '6502.799805', 'High': '6502.799805', 'Low': '6502.799805', 'Close': '6502.799805', 'Adj Close': '6502.799805', 'CloseUSD': '65.02799805'}, {'Index': 'N225', 'Date': '01 Apr 1981, 00:00', 'Open': '7389.990234', 'High': '7389.990234', 'Low': '7389.990234', 'Close': '7389.990234', 'Adj Close': '7389.990234', 'CloseUSD': '73.89990234'}], 'var_functions.query_db:12': [{'Index': 'HSI', 'Date': '03 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': 'January 04, 2000 at 12:00 AM'}, {'Index': 'HSI', 'Date': '05 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': 'January 06, 2000 at 12:00 AM'}, {'Index': 'HSI', 'Date': 'January 07, 2000 at 12:00 AM'}, {'Index': 'HSI', 'Date': '10 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': 'January 11, 2000 at 12:00 AM'}, {'Index': 'HSI', 'Date': 'January 12, 2000 at 12:00 AM'}, {'Index': 'HSI', 'Date': '13 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': '2000-01-14 00:00:00'}, {'Index': 'HSI', 'Date': 'January 17, 2000 at 12:00 AM'}, {'Index': 'HSI', 'Date': '18 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': '19 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': '20 Jan 2000, 00:00'}, {'Index': 'HSI', 'Date': '2000-01-21 00:00:00'}], 'var_functions.query_db:14': [{'date_prefix': '2000-01-24 00:00:00'}, {'date_prefix': '2000-03-01 00:00:00'}, {'date_prefix': '06 Mar 2000, 00:00'}, {'date_prefix': 'March 31, 2000 at 12'}, {'date_prefix': '04 Jul 2000, 00:00'}, {'date_prefix': 'July 06, 2000 at 12:'}, {'date_prefix': '10 Jul 2000, 00:00'}, {'date_prefix': '2000-08-25 00:00:00'}, {'date_prefix': '12 Oct 2000, 00:00'}, {'date_prefix': '2000-11-01 00:00:00'}, {'date_prefix': 'November 29, 2000 at'}, {'date_prefix': '2000-02-23 00:00:00'}, {'date_prefix': 'April 26, 2000 at 12'}, {'date_prefix': '02 May 2000, 00:00'}, {'date_prefix': '2000-05-05 00:00:00'}, {'date_prefix': '17 May 2000, 00:00'}, {'date_prefix': 'May 26, 2000 at 12:0'}, {'date_prefix': '2000-10-02 00:00:00'}, {'date_prefix': '2000-11-17 00:00:00'}, {'date_prefix': 'March 10, 2000 at 12'}, {'date_prefix': 'August 01, 2000 at 1'}, {'date_prefix': 'February 22, 2000 at'}, {'date_prefix': '2000-04-19 00:00:00'}, {'date_prefix': '07 Jul 2000, 00:00'}, {'date_prefix': '17 Jul 2000, 00:00'}, {'date_prefix': '2000-08-04 00:00:00'}, {'date_prefix': '25 Oct 2000, 00:00'}, {'date_prefix': 'November 06, 2000 at'}, {'date_prefix': 'December 01, 2000 at'}, {'date_prefix': '07 Feb 2000, 00:00'}, {'date_prefix': '21 Apr 2000, 00:00'}, {'date_prefix': 'November 21, 2000 at'}, {'date_prefix': 'March 20, 2000 at 12'}, {'date_prefix': '2000-11-09 00:00:00'}, {'date_prefix': '25 Dec 2000, 00:00'}, {'date_prefix': '2000-05-10 00:00:00'}, {'date_prefix': '05 Jan 2000, 00:00'}, {'date_prefix': 'January 06, 2000 at '}, {'date_prefix': '10 Jan 2000, 00:00'}, {'date_prefix': '19 Jan 2000, 00:00'}, {'date_prefix': '2000-02-02 00:00:00'}, {'date_prefix': 'April 19, 2000 at 12'}, {'date_prefix': 'May 08, 2000 at 12:0'}, {'date_prefix': 'May 12, 2000 at 12:0'}, {'date_prefix': 'June 28, 2000 at 12:'}, {'date_prefix': '01 Aug 2000, 00:00'}, {'date_prefix': '2000-08-09 00:00:00'}, {'date_prefix': '21 Aug 2000, 00:00'}, {'date_prefix': '2000-08-22 00:00:00'}, {'date_prefix': 'September 01, 2000 a'}, {'date_prefix': '2000-09-08 00:00:00'}, {'date_prefix': '29 Sep 2000, 00:00'}, {'date_prefix': '2000-10-03 00:00:00'}, {'date_prefix': 'November 23, 2000 at'}, {'date_prefix': '04 Jan 2000, 00:00'}, {'date_prefix': '2000-02-01 00:00:00'}, {'date_prefix': '2000-03-09 00:00:00'}, {'date_prefix': '17 Mar 2000, 00:00'}, {'date_prefix': '17 Apr 2000, 00:00'}, {'date_prefix': '2000-05-12 00:00:00'}, {'date_prefix': 'June 19, 2000 at 12:'}, {'date_prefix': 'June 21, 2000 at 12:'}, {'date_prefix': 'November 09, 2000 at'}, {'date_prefix': 'February 25, 2000 at'}, {'date_prefix': '14 Mar 2000, 00:00'}, {'date_prefix': '2000-04-14 00:00:00'}, {'date_prefix': '2000-07-25 00:00:00'}, {'date_prefix': '2000-07-26 00:00:00'}, {'date_prefix': '09 Oct 2000, 00:00'}, {'date_prefix': 'January 26, 2000 at '}, {'date_prefix': '24 Mar 2000, 00:00'}, {'date_prefix': 'May 15, 2000 at 12:0'}, {'date_prefix': 'May 24, 2000 at 12:0'}, {'date_prefix': 'August 28, 2000 at 1'}, {'date_prefix': '2000-10-24 00:00:00'}, {'date_prefix': 'October 30, 2000 at '}, {'date_prefix': 'November 30, 2000 at'}, {'date_prefix': 'May 01, 2000 at 12:0'}, {'date_prefix': '2000-10-18 00:00:00'}, {'date_prefix': 'April 21, 2000 at 12'}, {'date_prefix': '2000-09-28 00:00:00'}, {'date_prefix': 'October 24, 2000 at '}, {'date_prefix': 'March 06, 2000 at 12'}, {'date_prefix': 'July 04, 2000 at 12:'}, {'date_prefix': '04 Dec 2000, 00:00'}, {'date_prefix': '23 Nov 2000, 00:00'}, {'date_prefix': '11 Oct 2000, 00:00'}, {'date_prefix': '03 Jan 2000, 00:00'}, {'date_prefix': '28 Jan 2000, 00:00'}, {'date_prefix': '27 Mar 2000, 00:00'}, {'date_prefix': 'March 29, 2000 at 12'}, {'date_prefix': '04 May 2000, 00:00'}, {'date_prefix': '2000-06-05 00:00:00'}, {'date_prefix': '2000-07-21 00:00:00'}, {'date_prefix': '15 Sep 2000, 00:00'}, {'date_prefix': '22 Sep 2000, 00:00'}, {'date_prefix': '2000-12-18 00:00:00'}, {'date_prefix': '2000-01-13 00:00:00'}, {'date_prefix': 'January 21, 2000 at '}, {'date_prefix': '2000-01-27 00:00:00'}], 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
