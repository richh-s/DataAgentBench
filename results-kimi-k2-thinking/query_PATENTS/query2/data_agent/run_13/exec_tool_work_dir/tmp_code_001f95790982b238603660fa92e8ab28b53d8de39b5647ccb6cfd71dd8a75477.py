code = """import json
import re

# Load the data from H2 2019 file
file_path = locals()['var_functions.query_db:11']

# Read the data
with open(file_path, 'r') as f:
    data = json.load(f)

print(f"Total H2 2019 patents: {len(data)}")

# Let's look for German patents using pattern matching
suspicious_entries = []
german_entries = []

for idx, record in enumerate(data[:100]):  # Check first 100
    patent_info = record.get('Patents_info', '')
    
    # Look for country codes
    country_patterns = [
        r'\b([A-Z]{2})\b[-\s]',
        r'\(([A-Z]{2})\b',
        r'from\s+([A-Z]{2})\b',
        r'\b([A-Z]{2})\d{2}\b',  # e.g., DE20, EP14
    ]
    
    found_countries = []
    for pattern in country_patterns:
        matches = re.findall(pattern, patent_info)
        found_countries.extend(matches)
    
    if found_countries:
        suspicious_entries.append({
            'info': patent_info[:150],
            'countries': list(set(found_countries)),
            'full': patent_info
        })
        
    if 'DE' in str(found_countries) or 'Germany' in patent_info:
        german_entries.append({
            'info': patent_info,
            'countries': found_countries
        })

print(f"Found {len(suspicious_entries)} entries with country codes")
print(f"\nFirst 10 entries with potential country codes:")
for i, entry in enumerate(suspicious_entries[:10]):
    print(f"{i+1}. Countries: {entry['countries']}")
    print(f"   Info: {entry['info']}")
    print()

print(f"\nGerman candidates: {len(german_entries)}")
for i, entry in enumerate(german_entries[:5]):
    print(f"{i+1}. {entry['info'][:150]}")

print('__RESULT__:')
print(json.dumps({
    'h2_2019_total': len(data),
    'entries_with_country_codes': len(suspicious_entries),
    'german_candidates': len(german_entries)
}))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.execute_python:2': ['publicationinfo'], 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json', 'var_functions.query_db:6': [{'grant_date': '10th Apr 1883'}, {'grant_date': '10th Apr 1888'}, {'grant_date': '10th Apr 1923'}, {'grant_date': '10th Apr 1945'}, {'grant_date': '10th Apr 1952'}, {'grant_date': '10th Apr 1969'}, {'grant_date': '10th Apr 1974'}, {'grant_date': '10th Apr 1979'}, {'grant_date': '10th Apr 1980'}, {'grant_date': '10th Apr 1984'}, {'grant_date': '10th Apr 1990'}, {'grant_date': '10th Apr 2001'}, {'grant_date': '10th Apr 2006'}, {'grant_date': '10th Apr 2008'}, {'grant_date': '10th Apr 2018'}, {'grant_date': '10th Apr 2019'}, {'grant_date': '10th Apr 2020'}, {'grant_date': '10th Apr 2023'}, {'grant_date': '10th Apr 2024'}, {'grant_date': '10th April 1956'}, {'grant_date': '10th April 1962'}, {'grant_date': '10th April 1964'}, {'grant_date': '10th April 1973'}, {'grant_date': '10th April 1979'}, {'grant_date': '10th April 1990'}, {'grant_date': '10th April 2000'}, {'grant_date': '10th April 2001'}, {'grant_date': '10th April 2002'}, {'grant_date': '10th April 2005'}, {'grant_date': '10th April 2007'}, {'grant_date': '10th April 2012'}, {'grant_date': '10th April 2013'}, {'grant_date': '10th April 2014'}, {'grant_date': '10th April 2018'}, {'grant_date': '10th April 2020'}, {'grant_date': '10th April 2023'}, {'grant_date': '10th Aug 1948'}, {'grant_date': '10th Aug 1954'}, {'grant_date': '10th Aug 1959'}, {'grant_date': '10th Aug 1970'}, {'grant_date': '10th Aug 1973'}, {'grant_date': '10th Aug 1974'}, {'grant_date': '10th Aug 1976'}, {'grant_date': '10th Aug 1993'}, {'grant_date': '10th Aug 2004'}, {'grant_date': '10th Aug 2006'}, {'grant_date': '10th Aug 2011'}, {'grant_date': '10th Aug 2014'}, {'grant_date': '10th Aug 2016'}, {'grant_date': '10th Aug 2018'}], 'var_functions.query_db:11': 'file_storage/functions.query_db:11.json', 'var_functions.execute_python:10': 'Loaded 1929 records', 'var_functions.execute_python:12': {'total_german_patents_h2_2019': 0, 'sample_patents': []}, 'var_functions.query_db:16': 'file_storage/functions.query_db:16.json'}

exec(code, env_args)
