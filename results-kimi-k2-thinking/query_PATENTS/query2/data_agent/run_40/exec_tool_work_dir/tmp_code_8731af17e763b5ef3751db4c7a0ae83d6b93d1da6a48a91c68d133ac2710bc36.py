code = """import json
import re
from datetime import datetime

# Get the file path from storage
file_path = locals()['var_functions.query_db:8']

# Load the patent data from the file
with open(file_path, 'r') as f:
    patents_data = json.load(f)

print('Total patents with grant dates:', len(patents_data))

# Check date formats and extract year
sample_dates = []
for patent in patents_data[:5]:
    if patent['grant_date']:
        sample_dates.append(patent['grant_date'])

print('Sample grant dates:', sample_dates)

# Check for Germany-related patents
germany_count = 0
germany_info = []
for i, patent in enumerate(patents_data):
    if patent['Patents_info']:
        info = patent['Patents_info']
        if ('germany' in info.lower()) or ('de-' in info.lower()):
            germany_count += 1
            if len(germany_info) < 5:
                germany_info.append(info[:150])

print('\nTotal patents mentioning Germany:', germany_count)
for info in germany_info:
    print('  ', info)

# Check country code patterns in Patents_info
print('\nChecking country code patterns...')
countries = {}
for patent in patents_data[:2000]:
    if patent['Patents_info']:
        info = patent['Patents_info']
        # Look for patent number patterns like DE-12345678-A1 or US-201916355911-A
        id_match = re.search(r'\b([A-Z]{2})-\d{8,}-[A-Z]\d?\b', info)
        if id_match:
            country = id_match.group(1)
            countries[country] = countries.get(country, 0) + 1

print('Country codes found:', countries)"""

env_args = {'var_functions.list_db:0': ['publicationinfo'], 'var_functions.query_db:2': 'file_storage/functions.query_db:2.json', 'var_functions.query_db:5': [{'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B04B",\n  "B04C"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B04', 'synonyms': '[]', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'titlePart': '[\n  "CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B23B",\n  "B23C",\n  "B23D",\n  "B23F",\n  "B23G",\n  "B23H",\n  "B23K",\n  "B23P",\n  "B23Q"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B23', 'synonyms': '[]', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'titlePart': '[\n  "MACHINE TOOLS",\n  "METAL-WORKING NOT OTHERWISE PROVIDED FOR"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B30B"\n]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B30', 'synonyms': '[]', 'titleFull': 'PRESSES', 'titlePart': '[\n  "PRESSES"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B21B",\n  "B21C",\n  "B21D",\n  "B21F",\n  "B21G",\n  "B21H",\n  "B21J",\n  "B21K",\n  "B21L"\n]', 'dateRevised': '20190501.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B21', 'synonyms': '[]', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'titlePart': '[\n  "MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL",\n  "PUNCHING METAL"\n]'}, {'applicationReferences': '[]', 'breakdownCode': 'False', 'childGroups': '[]', 'children': '[\n  "B25B",\n  "B25C",\n  "B25D",\n  "B25F",\n  "B25G",\n  "B25H",\n  "B25J"\n]', 'dateRevised': '20130101.0', 'definition': '[]', 'glossary': '[]', 'informativeReferences': '[]', 'ipcConcordant': 'None', 'level': '4.0', 'limitingReferences': '[]', 'notAllocatable': 'True', 'parents': '[\n  "B"\n]', 'precedenceLimitingReferences': '[]', 'residualReferences': '[]', 'rules': '[]', 'scopeLimitingReferences': '[]', 'status': 'published', 'symbol': 'B25', 'synonyms': '[]', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'titlePart': '[\n  "HAND TOOLS",\n  "PORTABLE POWER-DRIVEN TOOLS",\n  "MANIPULATORS"\n]'}], 'var_functions.query_db:8': 'file_storage/functions.query_db:8.json'}

exec(code, env_args)
