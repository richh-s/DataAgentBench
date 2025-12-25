code = """import json
import re
import datetime

filename = locals()['var_function-call-8428725844076895982']
with open(filename, 'r') as f:
    data = json.load(f)

print(f"Total rows: {len(data)}")

month_map = {
    'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
    'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12,
    'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'Jun': 6, 'Jul': 7, 'Aug': 8, 'Sep': 9, 'Oct': 10, 'Nov': 11, 'Dec': 12,
    'Sept': 9
}

def parse_date(date_str):
    if not date_str or date_str == "None Date":
        return None
    s = date_str.lower().replace(',', ' ').replace('dated', '').replace(' on ', ' ').replace(' of ', ' ').replace(' the ', ' ')
    year_match = re.search(r'\b(19|20)\d{2}\b', s)
    if not year_match:
        return None
    year = int(year_match.group(0))
    month = None
    for m_name, m_val in month_map.items():
        if m_name.lower() in s:
            month = m_val
            break
    if not month:
        return None
    day_match = re.search(r'\b(\d{1,2})(?:st|nd|rd|th)?\b', s)
    day = 1
    if day_match:
        d_cand = int(day_match.group(1))
        if d_cand <= 31:
            day = d_cand
    try:
        return datetime.date(year, month, day)
    except:
        return None

target_count = 0
target_cpcs = set()

for i, row in enumerate(data[:100]): # Check first 100
    g_date_str = row.get('grant_date')
    g_date = parse_date(g_date_str)
    # print(f"{i}: {g_date_str} -> {g_date}")

for row in data:
    g_date = parse_date(row.get('grant_date'))
    if g_date and g_date.year == 2019 and g_date.month >= 7:
        target_count += 1
        try:
            cpc_list = json.loads(row.get('cpc', '[]'))
            for item in cpc_list:
                code = item.get('code', '')
                if len(code) >= 3:
                    target_cpcs.add(code[:3])
        except:
            pass

print(f"Target H2 2019 patents found: {target_count}")
print(f"Target CPCs found: {len(target_cpcs)}")
print(f"Sample CPCs: {list(target_cpcs)[:5]}")

print("__RESULT__:")
print(json.dumps("DEBUG_DONE"))"""

env_args = {'var_function-call-1888771270792040030': ['publicationinfo'], 'var_function-call-6434570943978445363': 'file_storage/function-call-6434570943978445363.json', 'var_function-call-15179652926461999085': [{'symbol': 'B04', 'level': '4.0', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES'}, {'symbol': 'B23', 'level': '4.0', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR'}, {'symbol': 'B30', 'level': '4.0', 'titleFull': 'PRESSES'}, {'symbol': 'B21', 'level': '4.0', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL'}, {'symbol': 'B25', 'level': '4.0', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS'}], 'var_function-call-10764568967162063911': [{'symbol': 'A', 'level': '2.0'}, {'symbol': 'A01', 'level': '4.0'}, {'symbol': 'A01B', 'level': '5.0'}, {'symbol': 'A01B1/00', 'level': '7.0'}], 'var_function-call-8139530506660812023': [{'Patents_info': 'In AT, the patent filing (application no. AT-52022-U) is assigned to ST Extruded Products Germany GmbH and has publication no. AT-17758-U1.', 'grant_date': 'None Date'}, {'Patents_info': 'Application (no. AU-2006246481-A) from AU, belonging to KAO GERMANY GMBH, with pub. number AU-2006246481-B2.', 'grant_date': 'September the 6th, 2012'}, {'Patents_info': 'TRELLEBORG AUTOMOTIVE GERMANY holds the PL patent application (number PL-07728345-T), with publication no. PL-2010798-T3.', 'grant_date': 'None Date'}, {'Patents_info': 'The DE application (number DE-102008034343-A) is assigned to CONTINENTAL MECH COMPONENTS GERMANY GMBH and has pub. number DE-102008034343-B4.', 'grant_date': '16th Mar 2017'}, {'Patents_info': 'In EP, the application (ID EP-18829350-A) is belonging to MEYER BURGER GERMANY GMBH and has pub. number EP-3729486-C0.', 'grant_date': 'None Date'}], 'var_function-call-4097148127731783155': [{'symbol': 'H04', 'level': '4.0'}], 'var_function-call-1604636425446054396': [{'COUNT(*)': '277813'}], 'var_function-call-8428725844076895982': 'file_storage/function-call-8428725844076895982.json', 'var_function-call-941338243621651918': [], 'var_function-call-2651097392656680875': [{'count(*)': '68'}], 'var_function-call-1262798950123470256': [{'grant_date': '14th Mar 2019'}, {'grant_date': 'dated 21st November 2019'}, {'grant_date': 'Mar 21st, 2019'}, {'grant_date': '5th of December, 2019'}, {'grant_date': '22nd of August, 2019'}, {'grant_date': 'September the 19th, 2019'}, {'grant_date': 'on March 14th, 2019'}, {'grant_date': '28th Feb 2019'}, {'grant_date': '17th of October, 2019'}, {'grant_date': 'on March 21st, 2019'}, {'grant_date': '7th March 2019'}, {'grant_date': 'February 28th, 2019'}, {'grant_date': 'August the 29th, 2019'}, {'grant_date': 'dated 4th July 2019'}, {'grant_date': '28th March 2019'}, {'grant_date': '2019 on Mar 28th'}, {'grant_date': '26th September 2019'}, {'grant_date': '2019, December 24th'}, {'grant_date': '21st of February, 2019'}, {'grant_date': '2nd Oct 2019'}, {'grant_date': 'December 24th, 2019'}, {'grant_date': 'August the 14th, 2019'}, {'grant_date': 'dated 9th May 2019'}, {'grant_date': 'Aug 29th, 2019'}, {'grant_date': '2019 on Mar 14th'}, {'grant_date': 'Apr 25th, 2019'}, {'grant_date': '2019 on Nov 7th'}, {'grant_date': 'December 19th, 2019'}, {'grant_date': '2019, July 18th'}, {'grant_date': '2019 on Jul 4th'}, {'grant_date': '4th of April, 2019'}, {'grant_date': 'January the 24th, 2019'}, {'grant_date': '7th of March, 2019'}, {'grant_date': 'October 10th, 2019'}, {'grant_date': '24th December 2019'}, {'grant_date': '22nd August 2019'}, {'grant_date': 'Aug 14th, 2019'}, {'grant_date': '2019, April 4th'}, {'grant_date': '2019 on Oct 17th'}, {'grant_date': 'Oct 24th, 2019'}, {'grant_date': '2019 on Jan 17th'}, {'grant_date': 'June 13th, 2019'}, {'grant_date': '19th of June, 2019'}, {'grant_date': 'on July 4th, 2019'}, {'grant_date': 'July the 18th, 2019'}, {'grant_date': 'April the 25th, 2019'}, {'grant_date': 'June the 13th, 2019'}, {'grant_date': '2019 on Oct 10th'}, {'grant_date': '2019, June 19th'}, {'grant_date': '2019, May 23rd'}, {'grant_date': '2019, May 29th'}, {'grant_date': '28th Nov 2019'}, {'grant_date': 'October the 10th, 2019'}, {'grant_date': '2019 on Aug 8th'}, {'grant_date': 'dated 21st March 2019'}, {'grant_date': '14th Aug 2019'}, {'grant_date': 'Jan 3rd, 2019'}, {'grant_date': '2019 on Mar 7th'}, {'grant_date': '31st January 2019'}, {'grant_date': '2019 on Oct 24th'}, {'grant_date': '23rd May 2019'}, {'grant_date': 'dated 9th May 2019'}, {'grant_date': '2019 on Oct 24th'}, {'grant_date': '6th Jun 2019'}, {'grant_date': 'dated 10th October 2019'}, {'grant_date': 'May 9th, 2019'}, {'grant_date': '2019, October 2nd'}, {'grant_date': '6th of June, 2019'}]}

exec(code, env_args)
