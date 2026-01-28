code = """import json
import re
from datetime import datetime

# First, let's load the German patents data from the previous query
with open(var_functions.query_db:5, 'r') as f:
    german_patents = json.load(f)

# Let's analyze the data to understand its structure
print(f"Total German patents found: {len(german_patents)}")
print("\nSample of data structure:")
for i, patent in enumerate(german_patents[:3]):
    print(f"\nPatent {i+1}:")
    print(f"  Patents_info: {patent['Patents_info'][:200]}...")
    print(f"  grant_date: {patent['grant_date']}")
    print(f"  cpc: {patent['cpc'][:100]}...")

# Let's try to extract grant dates and filter for 2019
date_patterns = [
    r'\b(\d{1,2})[\w\s]*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)\s*,?\s*(\d{4})\b',
    r'\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})\b',
    r'\b(\d{4})\s*,?\s*(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2})\b',
    r'\b(\d{4})\b'
]

months = {
    'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
    'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12,
    'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6,
    'july': 7, 'august': 8, 'september': 9, 'october': 10, 'november': 11, 'december': 12
}

def parse_date(date_str):
    """Parse natural language date strings"""
    if not date_str or date_str == 'null':
        return None
    
    date_str_lower = date_str.lower()
    
    # Try regex patterns
    for pattern in date_patterns:
        match = re.search(pattern, date_str_lower, re.IGNORECASE)
        if match:
            groups = match.groups()
            try:
                # Try different patterns
                if len(groups) == 3:
                    if groups[0].isdigit() and groups[1].isalpha():
                        # DD Month YYYY or YYYY Month DD
                        day = int(groups[0])
                        month = months.get(groups[1][:3])
                        year = int(groups[2])
                        return datetime(year, month, day)
                    elif groups[1].isdigit() and groups[2].isdigit():
                        # Month DD YYYY or similar
                        month = months.get(groups[0][:3])
                        day = int(groups[1])
                        year = int(groups[2])
                        return datetime(year, month, day)
                elif len(groups) == 1 and groups[0].isdigit():
                    # Just year
                    year = int(groups[0])
                    return datetime(year, 1, 1)
            except:
                continue
    
    return None

# Parse grant dates and filter for 2019 second half
patents_2019 = []
for patent in german_patents:
    grant_date = parse_date(patent['grant_date'])
    if grant_date and grant_date.year == 2019 and grant_date.month >= 7:
        patents_2019.append({
            'patent_info': patent['Patents_info'],
            'grant_date': patent['grant_date'],
            'filing_date': patent.get('filing_date', ''),
            'cpc': patent['cpc'],
            'parsed_grant_date': grant_date
        })

print(f"\n\nGerman patents granted in second half of 2019: {len(patents_2019)}")
if patents_2019:
    print("\nSample patents from 2019:")
    for i, patent in enumerate(patents_2019[:5]):
        print(f"  {i+1}. {patent['patent_info'][:150]}...")
        print(f"     Grant: {patent['grant_date']}")

# Extract CPC codes
all_cpc_codes = []
cpc_patent_counts = {}

for patent in patents_2019:
    try:
        cpc_data = json.loads(patent['cpc'])
        if isinstance(cpc_data, list):
            for cpc_item in cpc_data:
                code = cpc_item.get('code', '')
                if code:
                    all_cpc_codes.append(code)
                    cpc_patent_counts[code] = cpc_patent_counts.get(code, 0) + 1
    except:
        # Try regex extraction as fallback
        cpc_matches = re.findall(r'"code":\s*"([^"]+)"', patent['cpc'])
        for code in cpc_matches:
            all_cpc_codes.append(code)
            cpc_patent_counts[code] = cpc_patent_counts.get(code, 0) + 1

print(f"\nTotal unique CPC codes found: {len(set(all_cpc_codes))}")
print(f"Total CPC code occurrences: {len(all_cpc_codes)}")
print(f"\nTop 10 CPC codes:")
for code, count in sorted(cpc_patent_counts.items(), key=lambda x: x[1], reverse=True)[:10]:
    print(f"  {code}: {count}")

# Output results for next step
result = {
    'total_patents_2019': len(patents_2019),
    'patents': patents_2019,
    'cpc_codes': list(set(all_cpc_codes)),
    'cpc_patent_counts': cpc_patent_counts
}

print("\n__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': 'file_storage/functions.query_db:5.json'}

exec(code, env_args)
