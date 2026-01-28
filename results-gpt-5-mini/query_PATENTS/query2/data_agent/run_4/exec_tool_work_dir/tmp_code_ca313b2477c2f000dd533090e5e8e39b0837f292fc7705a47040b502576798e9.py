code = """import json, re

path = var_call_93nbrQx7BQWZpY6lcR3aUu1W
with open(path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

year_re = re.compile(r"\b(19|20)\d{2}\b")

def extract_year(text):
    if not text:
        return None
    m = year_re.search(text)
    if m:
        return int(m.group(0))
    return None

out = []
for rec in pubs:
    info = rec.get('Patents_info')
    filing = rec.get('filing_date')
    grant = rec.get('grant_date')
    filing_y = extract_year(filing or '')
    grant_y = extract_year(grant or '')
    # sample cpc codes
    cpcs = []
    try:
        if rec.get('cpc'):
            cpcs_json = json.loads(rec.get('cpc'))
            for e in cpcs_json[:5]:
                cpcs.append(e.get('code'))
    except Exception:
        cpcs = [rec.get('cpc')]
    out.append({'info': info, 'filing_date': filing, 'filing_year': filing_y, 'grant_date': grant, 'grant_year': grant_y, 'cpcs_sample': cpcs})

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_T6EVN0wa6vXygggLELsEzSqf': 'file_storage/call_T6EVN0wa6vXygggLELsEzSqf.json', 'var_call_m1Hpssfn6VXXHXhXmjgyXmHg': 'file_storage/call_m1Hpssfn6VXXHXhXmjgyXmHg.json', 'var_call_iCbx0nyULprDUxHZEIFTb9kJ': [], 'var_call_ABeRRIOm5CmvsmZQcYRzkK9j': {'num_records_sampled': 74, 'parsed_with_year_and_cpc': 0, 'years_found_sample': [], 'num_level4_symbols': 137, 'top_groups_sample': []}, 'var_call_AaU6OyCxPJeTVcXNDrAcJQ7c': {'total_records_sampled': 74, 'found_examples': {'DE': ['GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.'], '/DE': [], 'Germany': [], 'country_code': [], 'DE-': ['In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.']}, 'word_counts_sample': {}}, 'var_call_9zQ9GwG4xZVECv3m35cXtlly': {'matched_records': 21, 'years_covered': [], 'results': []}, 'var_call_93nbrQx7BQWZpY6lcR3aUu1W': 'file_storage/call_93nbrQx7BQWZpY6lcR3aUu1W.json', 'var_call_RGNdh0k5QDb5TGcLr7vy3pV1': {'num_records': 23, 'years_covered': [], 'results': []}}

exec(code, env_args)
