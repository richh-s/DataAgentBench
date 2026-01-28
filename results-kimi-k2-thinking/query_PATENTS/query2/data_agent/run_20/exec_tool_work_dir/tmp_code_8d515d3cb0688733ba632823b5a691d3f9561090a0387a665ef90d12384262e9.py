code = """import json
import re

file_path = var_functions.query_db:2
with open(file_path, 'r') as f:
    data_parsed = json.load(f)

print('Total records loaded:', len(data_parsed))

months = ['january', 'february', 'march', 'april', 'may', 'june',
          'july', 'august', 'september', 'october', 'november', 'december']

def parse_complete_date(date_str):
    if not date_str:
        return None
    date_str = date_str.lower().replace('dated', '').strip()
    date_str = re.sub(r'([0-9]{1,2})(st|nd|rd|th|,)', r'\1', date_str)
    date_str = date_str.replace('of', '').strip()
    for i, month_name in enumerate(months):
        if month_name in date_str:
            year_match = re.search(r'([0-9]{4})', date_str)
            if year_match:
                year = int(year_match.group(1))
                month_num = i + 1
                return year, month_num
    return None

def is_german_patent(patents_info):
    if not patents_info:
        return False
    info_lower = patents_info.lower()
    germany_indicators = ['germany', 'de-', 'de ', ' ep-', ' ep ']
    for indicator in germany_indicators:
        if indicator in info_lower:
            return True
    return False

print('Testing date parsing:')
for i, record in enumerate(data_parsed[:10]):
    grant_date = record.get('grant_date', '')
    parsed = parse_complete_date(grant_date)
    if parsed:
        year, month = parsed
        in_2019_h2 = (year == 2019 and month >= 7)
        print(f'Record {i}: {grant_date} -> {year}/{month} -> 2019 H2: {in_2019_h2}')

print('\nLooking for German patents:')
german_patents_2019_h2 = []
for i, record in enumerate(data_parsed[:100]):
    if is_german_patent(record.get('Patents_info', '')):
        grant_date = record.get('grant_date', '')
        parsed = parse_complete_date(grant_date)
        if parsed:
            year, month = parsed
            if year == 2019 and month >= 7:
                german_patents_2019_h2.append(record)

print(f'Found {len(german_patents_2019_h2)} German patents granted in 2019 H2 in first 100 records')

result = json.dumps({'status': 'loaded', 'count': len(data_parsed)})
print('__RESULT__:')
print(result)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json'}

exec(code, env_args)
