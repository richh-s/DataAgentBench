code = """import json, re
from collections import defaultdict

pub_path = var_call_93nbrQx7BQWZpY6lcR3aUu1W
with open(pub_path, 'r', encoding='utf-8') as f:
    pubs = json.load(f)

cpc_path = var_call_m1Hpssfn6VXXHXhXmjgyXmHg
with open(cpc_path, 'r', encoding='utf-8') as f:
    cpc_defs = json.load(f)

# build level4 map
level4_map = {row['symbol']: row.get('titleFull','') for row in cpc_defs}
level4_set = set(level4_map.keys())

# robust year extraction
year_re = re.compile(r"(19|20)\d{2}")

def extract_year(text):
    if not text:
        return None
    m = year_re.findall(text)
    if m:
        # find last match
        all_matches = year_re.findall(text)
        # actually find all full matches
        all_full = re.findall(r"(?:19|20)\d{2}", text)
        if all_full:
            return int(all_full[-1])
    return None

# Build counts: unique patents per group per year
counts = defaultdict(lambda: defaultdict(int))
years_set = set()

for rec in pubs:
    filing = rec.get('filing_date','') or ''
    grant = rec.get('grant_date','') or ''
    year = extract_year(filing)
    if not year:
        year = extract_year(grant)
    if not year:
        continue
    years_set.add(year)
    cpc_field = rec.get('cpc')
    if not cpc_field:
        continue
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    # collect unique groups for this patent
    groups = set()
    for entry in cpcs:
        code = entry.get('code')
        if not code:
            continue
        code_norm = code.replace(' ', '')
        group = code_norm[:3]
        if group in level4_set:
            groups.add(group)
    for g in groups:
        counts[g][year] += 1

if not years_set:
    results = []
else:
    years = list(range(min(years_set), max(years_set)+1))
    alpha = 0.1
    results = []
    for group, yc in counts.items():
        # create series
        series = [yc.get(y,0) for y in years]
        if not any(series):
            continue
        ema = series[0]
        ema_vals = [ema]
        for x in series[1:]:
            ema = alpha * x + (1 - alpha) * ema
            ema_vals.append(ema)
        # find max ema and its year
        max_idx = max(range(len(ema_vals)), key=lambda i: ema_vals[i])
        best_year = years[max_idx]
        results.append({'symbol': group, 'titleFull': level4_map.get(group,''), 'best_year': best_year, 'max_ema': round(ema_vals[max_idx],3)})
    # sort by max_ema desc
    results = sorted(results, key=lambda r: -r['max_ema'])

# Limit to top 10 maybe all
output = {'num_records': len(pubs), 'years_covered': sorted(list(years_set)), 'top_groups': results}

print('__RESULT__:')
print(json.dumps(output))"""

env_args = {'var_call_T6EVN0wa6vXygggLELsEzSqf': 'file_storage/call_T6EVN0wa6vXygggLELsEzSqf.json', 'var_call_m1Hpssfn6VXXHXhXmjgyXmHg': 'file_storage/call_m1Hpssfn6VXXHXhXmjgyXmHg.json', 'var_call_iCbx0nyULprDUxHZEIFTb9kJ': [], 'var_call_ABeRRIOm5CmvsmZQcYRzkK9j': {'num_records_sampled': 74, 'parsed_with_year_and_cpc': 0, 'years_found_sample': [], 'num_level4_symbols': 137, 'top_groups_sample': []}, 'var_call_AaU6OyCxPJeTVcXNDrAcJQ7c': {'total_records_sampled': 74, 'found_examples': {'DE': ['GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.', 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.', 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.', 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.', 'In US, the patent filing (application number US-201616068918-A) is owned by DENSO CORP and has publication no. US-10369965-B2.'], '/DE': [], 'Germany': [], 'country_code': [], 'DE-': ['In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.']}, 'word_counts_sample': {}}, 'var_call_9zQ9GwG4xZVECv3m35cXtlly': {'matched_records': 21, 'years_covered': [], 'results': []}, 'var_call_93nbrQx7BQWZpY6lcR3aUu1W': 'file_storage/call_93nbrQx7BQWZpY6lcR3aUu1W.json', 'var_call_RGNdh0k5QDb5TGcLr7vy3pV1': {'num_records': 23, 'years_covered': [], 'results': []}, 'var_call_xX74RHwlq6mRafTkCdKrrQEg': [{'info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.', 'filing_date': '16th of July, 2007', 'filing_year': None, 'grant_date': 'dated 21st November 2019', 'grant_year': None, 'cpcs_sample': ['B41F21/102', 'B41F22/00', 'B41F21/00']}, {'info': 'The DE patent application (no. DE-102010042467-A) is owned by CONTINENTAL AUTOMOTIVE GMBH and has pub. number DE-102010042467-B4.', 'filing_date': 'dated 14th October 2010', 'filing_year': None, 'grant_date': '5th of December, 2019', 'grant_year': None, 'cpcs_sample': ['F02D41/3005', 'F02D41/20', 'F02M65/005', 'F02D41/00', 'F02D41/20']}, {'info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.', 'filing_date': 'July 21st, 2014', 'filing_year': None, 'grant_date': '22nd of August, 2019', 'grant_year': None, 'cpcs_sample': ['F02M59/102', 'F02M55/04', 'F02M55/04', 'F02M59/102', 'F02M59/44']}, {'info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.', 'filing_date': 'on October 29th, 2015', 'filing_year': None, 'grant_date': 'September the 19th, 2019', 'grant_year': None, 'cpcs_sample': ['G01D11/24', 'B23K1/0016']}, {'info': 'The DE application (number DE-102014111322-A) is owned by LEMKE SEBASTIAN and has publication no. DE-102014111322-B4.', 'filing_date': 'on August 8th, 2014', 'filing_year': None, 'grant_date': '17th of October, 2019', 'grant_year': None, 'cpcs_sample': ['B63B21/50']}, {'info': 'Application (no. DE-112015005888-T) from DE, belonging to APPLE INC, with publication number DE-112015005888-B4.', 'filing_date': 'on December 15th, 2015', 'filing_year': None, 'grant_date': 'August the 29th, 2019', 'grant_year': None, 'cpcs_sample': ['H04W72/21', 'H04W72/56', 'H04W72/21', 'H04W72/56', 'H04W72/56']}, {'info': 'The DE application (ID DE-102016102746-A) is belonging to HAWE Altenstadt Holding GmbH and has pub. number DE-102016102746-B4.', 'filing_date': 'on February 17th, 2016', 'filing_year': None, 'grant_date': 'dated 4th July 2019', 'grant_year': None, 'cpcs_sample': ['B66C23/80', 'E02F9/085', 'B60S9/10']}, {'info': 'The DE patent filing (application no. DE-102018213557-A) is assigned to BAYERISCHE MOTOREN WERKE AG and has publication number DE-102018213557-B3.', 'filing_date': 'dated 10th August 2018', 'filing_year': None, 'grant_date': '26th September 2019', 'grant_year': None, 'cpcs_sample': ['F02D41/0087', 'F02D15/00', 'F02D13/06', 'Y02T10/12']}, {'info': 'In DE, the patent application (number DE-102011108701-A) is belonging to SUMITOMO HEAVY INDUSTRIES and has pub. number DE-102011108701-B4.', 'filing_date': 'Jul 27th, 2011', 'filing_year': None, 'grant_date': '2019, December 24th', 'grant_year': None, 'cpcs_sample': ['F16C33/4676', 'F16C33/4682', 'F16C33/4635']}, {'info': 'Patent filing (app. number DE-102016108055-A) from DE, owned by OTTOBOCK SE & CO KGAA, with publication no. DE-102016108055-B4.', 'filing_date': 'April 29th, 2016', 'filing_year': None, 'grant_date': 'December 24th, 2019', 'grant_year': None, 'cpcs_sample': ['A61F5/14', 'A61F5/0127', 'A61F5/0111', 'A43B17/00', 'A43B7/20']}, {'info': 'The DE patent filing (app. number DE-102018120196-A) is owned by OSTERMANN FRANK and has publication number DE-102018120196-B3.', 'filing_date': '20th Aug 2018', 'filing_year': None, 'grant_date': 'August the 14th, 2019', 'grant_year': None, 'cpcs_sample': ['F24B5/023', 'F23L15/04', 'F23L1/00', 'F24B5/023', 'F23L15/04']}, {'info': 'In DE, the application (ID DE-102018121680-A) is assigned to LUFTHANSA TECHNIK AG and has publication number DE-102018121680-B3.', 'filing_date': '5th September 2018', 'filing_year': None, 'grant_date': 'December 19th, 2019', 'grant_year': None, 'cpcs_sample': ['H01R35/02', 'B64D11/0624', 'H01R2201/26', 'H01R24/60', 'H01R13/633']}, {'info': 'The DE application (number DE-102008034068-A) is belonging to SEMIKRON ELEKTRONIK GMBH & CO KG and has pub. number DE-102008034068-B4.', 'filing_date': '2008, July 22nd', 'filing_year': None, 'grant_date': '2019, July 18th', 'grant_year': None, 'cpcs_sample': ['H01L23/48', 'H01L23/02', 'H01L2924/01079', 'H01L23/34', 'H01L25/072']}, {'info': 'In DE, the patent filing (app. number DE-102013001093-A) is belonging to AUDI AG and has publication no. DE-102013001093-B4.', 'filing_date': 'Jan 23rd, 2013', 'filing_year': None, 'grant_date': 'October 10th, 2019', 'grant_year': None, 'cpcs_sample': ['F02N2200/022', 'F02N2300/2002', 'F02N11/0814', 'F02N2300/2011', 'F02N11/04']}, {'info': 'The DE application (ID DE-102015215505-A) is belonging to NUCTECH CO LTD and has publication number DE-102015215505-B8.', 'filing_date': 'on August 13th, 2015', 'filing_year': None, 'grant_date': '24th December 2019', 'grant_year': None, 'cpcs_sample': ['C04B2235/9653', 'C04B2235/77', 'C04B2235/72', 'C04B2235/666', 'C04B2235/662']}, {'info': 'The DE patent filing (application number DE-102007032434-A) is held by KRONES AG and has pub. number DE-102007032434-B4.', 'filing_date': 'on July 10th, 2007', 'filing_year': None, 'grant_date': '22nd August 2019', 'grant_year': None, 'cpcs_sample': ['B29C49/42087', 'B29C2049/5868', 'B29C2049/5817', 'B29C2049/4294', 'B29C49/06']}, {'info': 'The DE patent filing (app. number DE-112016000121-T) is assigned to HOYA CORP and has publication no. DE-112016000121-B4.', 'filing_date': '29th of August, 2016', 'filing_year': None, 'grant_date': 'on July 4th, 2019', 'grant_year': None, 'cpcs_sample': ['G02B15/167', 'A61B1/00188', 'G02B15/15', 'G02B13/02', 'G02B23/24']}, {'info': 'In DE, the application (number DE-102012210357-A) is assigned to CONTINENTAL AUTOMOTIVE GMBH and has publication no. DE-102012210357-B4.', 'filing_date': '2012, June 20th', 'filing_year': None, 'grant_date': 'July the 18th, 2019', 'grant_year': None, 'cpcs_sample': ['Y10T70/7051', 'G07C9/00944', 'B29C2045/5635', 'G07C9/00944', 'B29D99/006']}, {'info': 'The DE patent filing (app. number DE-102009024240-A) is held by PORSCHE AG and has publication number DE-102009024240-B4.', 'filing_date': 'May the 29th, 2009', 'filing_year': None, 'grant_date': 'October the 10th, 2019', 'grant_year': None, 'cpcs_sample': ['F16H37/042', 'F16H37/046', 'F16H2200/0065', 'F16H3/006', 'F16H2200/0056']}, {'info': 'In CA, the application (ID CA-2977497-A) is owned by TE CONNECTIVITY GERMANY GMBH and has publication number CA-2977497-C.', 'filing_date': '23rd of February, 2016', 'filing_year': None, 'grant_date': '2019, September 24th', 'grant_year': None, 'cpcs_sample': ['H01R43/048', 'H01R4/188', 'H01R4/184', 'H01R43/058', 'H01R4/188']}, {'info': 'The US patent application (no. US-201815935082-A) is held by JOHNSON MATTHEY CATALYSTS GERMANY GMBH and has publication number US-10500575-B2.', 'filing_date': '26th of March, 2018', 'filing_year': None, 'grant_date': '10th of December, 2019', 'grant_year': None, 'cpcs_sample': ['B01J29/48', 'B01J29/46', 'B01D2255/911', 'B01D2255/20738', 'Y02C20/10']}, {'info': 'Application (ID DE-102012107580-A) from DE, held by KRAUSS MAFFEI WEGMANN GMBH & CO KG, with publication number DE-102012107580-C5.', 'filing_date': '2012 on Aug 17th', 'filing_year': None, 'grant_date': 'dated 10th October 2019', 'grant_year': None, 'cpcs_sample': ['E02F3/7631', 'E02F9/006', 'E02F3/96', 'F42B3/006', 'F41H11/16']}, {'info': 'In DE, the patent application (no. DE-102017111017-A) is owned by WEISS ALARM UND SICHERHEITSTECHNIK GMBH and has publication number DE-102017111017-B4.', 'filing_date': 'May 19th, 2017', 'filing_year': None, 'grant_date': '2019, October 2nd', 'grant_year': None, 'cpcs_sample': ['G08B19/00', 'G08B17/00']}]}

exec(code, env_args)
