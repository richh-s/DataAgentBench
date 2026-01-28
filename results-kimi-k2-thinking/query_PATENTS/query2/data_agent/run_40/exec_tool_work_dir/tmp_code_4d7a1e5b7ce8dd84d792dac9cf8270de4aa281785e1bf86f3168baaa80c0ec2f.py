code = """import json
import re
from datetime import datetime

# Load the patent data from the file
with open(var_functions.query_db:8, 'r') as f:
    patents_data = json.load(f)

print(f"Total patents with grant dates: {len(patents_data)}")
print(f"First few records:")
for i, patent in enumerate(patents_data[:3]):
    print(f"\nPatent {i+1}:")
    print(f"Patents_info: {patent['Patents_info'][:200]}...")
    print(f"Grant date: {patent['grant_date']}")
    print(f"CPC codes: {patent['cpc'][:150]}...")

# Check date formats
print("\n\nSample grant dates:")
for patent in patents_data[:10]:
    if patent['grant_date']:
        print(f"  '{patent['grant_date']}'")

# Check for Germany-related patents
print("\n\nSample patents that mention Germany:")
germany_count = 0
for patent in patents_data[:1000]:
    if patent['Patents_info'] and 'germany' in patent['Patents_info'].lower():
        if germany_count < 5:
            print(f"  {patent['Patents_info'][:150]}")
        germany_count += 1

print(f"\nPatents mentioning Germany in first 1000: {germany_count}")

# Check country codes in Patents_info
print("\n\nExtracting country codes from Patents_info:")
country_codes = {}
for patent in patents_data[:2000]:
    if patent['Patents_info']:
        # Look for patterns like "DE-" or "Germany" or "german"
        info = patent['Patents_info'].upper()
        if 'DE-' in info or 'DE/' in info:
            parts = info.split('DE-')
            if len(parts) > 1:
                code = 'DE'
                country_codes[code] = country_codes.get(code, 0) + 1
        elif 'GERMANY' in info:
            country_codes['GERMANY'] = country_codes.get('GERMANY', 0) + 1
        elif 'GERMAN' in info:
            country_codes['GERMAN'] = country_codes.get('GERMAN', 0) + 1

print(f"Country occurrences: {country_codes}")"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B04B",\n  "B04C"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B04', 'synonyms': '[]', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'titlePart': '[\n  "CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B23B",\n  "B23C",\n  "B23D",\n  "B23F",\n  "B23G",\n  "B23H",\n  "B23K",\n  "B23P",\n  "B23Q"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B23', 'synonyms': '[]', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'titlePart': '[\n  "MACHINE TOOLS",\n  "METAL-WORKING NOT OTHERWISE PROVIDED FOR"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B30B"\n]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B30', 'synonyms': '[]', 'titleFull': 'PRESSES', 'titlePart': '[\n  "PRESSES"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B21B",\n  "B21C",\n  "B21D",\n  "B21F",\n  "B21G",\n  "B21H",\n  "B21J",\n  "B21K",\n  "B21L"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B21', 'synonyms': '[]', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'titlePart': '[\n  "MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL",\n  "PUNCHING METAL"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B25B",\n  "B25C",\n  "B25D",\n  "B25F",\n  "B25G",\n  "B25H",\n  "B25J"\n]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B25', 'synonyms': '[]', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'titlePart': '[\n  "HAND TOOLS",\n  "PORTABLE POWER-DRIVEN TOOLS",\n  "MANIPULATORS"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
