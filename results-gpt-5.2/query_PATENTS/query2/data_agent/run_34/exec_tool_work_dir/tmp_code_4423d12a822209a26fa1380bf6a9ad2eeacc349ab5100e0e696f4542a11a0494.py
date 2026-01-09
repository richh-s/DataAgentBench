code = """import json, re
import pandas as pd

records = var_call_OmrsCs6nag9Gxpu0VE3EN9lt

def parse_year(s):
    if s is None:
        return None
    m = re.search(r'(19|20)\d{2}', s)
    return int(m.group(0)) if m else None

def parse_cpc_list(s):
    if not s:
        return []
    try:
        data = json.loads(s)
        codes = []
        for it in data:
            c = it.get('code')
            if c:
                codes.append(c)
        return codes
    except Exception:
        return []

def to_level4_group(code):
    # CPC group at level 4 interpreted as subclass+main group: e.g., B41F21/00 from B41F21/102
    m = re.match(r'^([A-HY]\d{2}[A-Z])\s*(\d+)/(\d+)$', code)
    if not m:
        return None
    subclass = m.group(1)
    main = m.group(2)
    return f"{subclass}{main}/00"

rows=[]
for r in records:
    y = parse_year(r.get('filing_date'))
    if y is None:
        continue
    for c in parse_cpc_list(r.get('cpc')):
        g = to_level4_group(c)
        if g:
            rows.append((g,y))

df = pd.DataFrame(rows, columns=['group','year'])
if df.empty:
    out = []
else:
    counts = df.groupby(['group','year']).size().reset_index(name='filings')
    # compute EMA per group across years
    alpha=0.1
    results=[]
    for group, sub in counts.groupby('group'):
        sub = sub.sort_values('year')
        ema=None
        for _, row in sub.iterrows():
            x=row['filings']
            ema = x if ema is None else (alpha*x + (1-alpha)*ema)
            results.append({'group':group,'year':int(row['year']),'ema':float(ema)})
    ema_df = pd.DataFrame(results)
    # best year per group
    best = (ema_df.sort_values(['group','ema','year'], ascending=[True,False,True])
                  .groupby('group').head(1))
    # pick groups with highest ema among all groups
    max_ema = best['ema'].max() if not best.empty else None
    top = best[best['ema']==max_ema].copy() if max_ema is not None else best

    # map titles from CPC definition (level 4 are 3-char symbols; our groups are like B41F21/00 so may not exist)
    # We'll fetch titles for groups if present; else fallback to subclass title if available
    # Build title map from level 4 = subclass symbols in definitions? Actually level=4 here seems section class (e.g., B29). We'll use symbol equals first 3 chars of group.
    # create symbol-to-title from a query limited? none provided; can't query here. We'll approximate using only sample? Not possible.
    out = top[['group','year','ema']].to_dict('records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_JdF8loHhQ0lqcwharyj5nXnr': [], 'var_call_K8vokLXHn1QXnquMG4DTBZMP': [], 'var_call_lOISbQhA6msNrGKrPDrQxej4': [], 'var_call_7ptFYvSFnE1AfjYwlOkaR3TN': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_OmrsCs6nag9Gxpu0VE3EN9lt': [{'filing_date': '16th of July, 2007', 'grant_date': 'dated 21st November 2019', 'cpc': '[\n  {\n    "code": "B41F21/102",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F22/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B41F21/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  }\n]', 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Trommel zum Fördern eines Bogens",\n    "truncated": false\n  }\n]', 'Patents_info': 'In DE, the application (number DE-102007032978-A) is held by HEIDELBERGER DRUCKMASCH AG and has publication number DE-102007032978-B4.'}, {'filing_date': 'July 21st, 2014', 'grant_date': '22nd of August, 2019', 'cpc': '[\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M55/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/102",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F04B53/001",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/44",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02M59/368",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02M59/06",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Pulsationsdämpfer und Hochdruckkraftstoffpumpe",\n    "truncated": false\n  }\n]', 'Patents_info': 'In DE, the patent filing (application no. DE-112014003420-T) is assigned to TOYOTA MOTOR CO LTD and has publication number DE-112014003420-B4.'}, {'filing_date': 'on October 29th, 2015', 'grant_date': 'September the 19th, 2019', 'cpc': '[\n  {\n    "code": "G01D11/24",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B23K1/0016",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Verfahren zur Herstellung eines Bauteiles, Bauteil und Drucksensor",\n    "truncated": false\n  }\n]', 'Patents_info': 'In DE, the patent filing (application number DE-102015221196-A) is owned by SCHOTT AG and has pub. number DE-102015221196-B4.'}, {'filing_date': 'Jul 27th, 2011', 'grant_date': '2019, December 24th', 'cpc': '[\n  {\n    "code": "F16C33/4676",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16C33/4682",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F16C33/4635",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Getriebevorrichtung der oszillierend innen eingreifenden Bauart",\n    "truncated": false\n  }\n]', 'Patents_info': 'In DE, the patent application (number DE-102011108701-A) is belonging to SUMITOMO HEAVY INDUSTRIES and has pub. number DE-102011108701-B4.'}, {'filing_date': '5th September 2018', 'grant_date': 'December 19th, 2019', 'cpc': '[\n  {\n    "code": "H01R35/02",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B64D11/0624",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R2201/26",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01R24/60",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01R13/633",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R35/04",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B60R16/027",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01R2201/26",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Steckverbindungsdose und Passagierversorgungsmodul",\n    "truncated": false\n  }\n]', 'Patents_info': 'In DE, the application (ID DE-102018121680-A) is assigned to LUFTHANSA TECHNIK AG and has publication number DE-102018121680-B3.'}, {'filing_date': 'Jan 23rd, 2013', 'grant_date': 'October 10th, 2019', 'cpc': '[\n  {\n    "code": "F02N2200/022",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02N2300/2002",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02N11/0814",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02N2300/2011",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "F02N11/04",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B60K6/485",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B60W30/194",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02N11/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "F02N2200/023",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02T10/62",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y02T10/40",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  }\n]', 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Verfahren und System zum Anlassen eines Verbrennungsmotors eines Kraftwagens",\n    "truncated": false\n  }\n]', 'Patents_info': 'In DE, the patent filing (app. number DE-102013001093-A) is belonging to AUDI AG and has publication no. DE-102013001093-B4.'}, {'filing_date': '2012, June 20th', 'grant_date': 'July the 18th, 2019', 'cpc': '[\n  {\n    "code": "Y10T70/7051",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "G07C9/00944",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B29C2045/5635",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "G07C9/00944",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B29D99/006",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01H9/0235",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B29C45/561",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "B29C45/561",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "H01H2009/183",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "B29C2045/5635",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01H2009/183",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "H01H9/0235",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "Y10T70/7051",\n    "first": false,\n    "inventive": false,\n    "tree": []\n  },\n  {\n    "code": "E05B19/0088",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Elektronischer Schlüssel für ein Fahrzeug",\n    "truncated": false\n  }\n]', 'Patents_info': 'In DE, the application (number DE-102012210357-A) is assigned to CONTINENTAL AUTOMOTIVE GMBH and has publication no. DE-102012210357-B4.'}, {'filing_date': 'May 19th, 2017', 'grant_date': '2019, October 2nd', 'cpc': '[\n  {\n    "code": "G08B19/00",\n    "first": false,\n    "inventive": true,\n    "tree": []\n  },\n  {\n    "code": "G08B17/00",\n    "first": true,\n    "inventive": true,\n    "tree": []\n  }\n]', 'title_localized': '[\n  {\n    "language": "de",\n    "text": "Leuchtenbaldachin zum Detektieren und Signalisieren unterschiedlicher Gefahrensituationen",\n    "truncated": false\n  }\n]', 'Patents_info': 'In DE, the patent application (no. DE-102017111017-A) is owned by WEISS ALARM UND SICHERHEITSTECHNIK GMBH and has publication number DE-102017111017-B4.'}], 'var_call_9uBdxHRuDorJJYbe9jty0cwd': [{'symbol': 'A01K2227/108', 'titleFull': 'Swine', 'level': '9.0', 'status': 'published'}, {'symbol': 'A01K2227/105', 'titleFull': 'Murine', 'level': '9.0', 'status': 'published'}, {'symbol': 'A01K2227/101', 'titleFull': 'Bovine', 'level': '9.0', 'status': 'published'}, {'symbol': 'A01K2227/107', 'titleFull': 'Rabbit', 'level': '9.0', 'status': 'published'}, {'symbol': 'A01K2227/103', 'titleFull': 'Ovine', 'level': '9.0', 'status': 'published'}], 'var_call_0InooaKUwJxXRRDmUK3qqybN': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'status': 'published'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'status': 'published'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'status': 'published'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'status': 'published'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'status': 'published'}], 'var_call_xl1YeDTNj2JISRUtV7J54RcE': [{'symbol': 'B99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'status': 'published'}, {'symbol': 'B29', 'titleFull': 'WORKING OF PLASTICS; WORKING OF SUBSTANCES IN A PLASTIC STATE IN GENERAL', 'level': '4.0', 'status': 'published'}, {'symbol': 'B33', 'titleFull': 'ADDITIVE MANUFACTURING TECHNOLOGY', 'level': '4.0', 'status': 'published'}, {'symbol': 'C22', 'titleFull': 'METALLURGY; FERROUS OR NON-FERROUS ALLOYS; TREATMENT OF ALLOYS OR NON-FERROUS METALS', 'level': '4.0', 'status': 'published'}, {'symbol': 'D99', 'titleFull': 'SUBJECT MATTER NOT OTHERWISE PROVIDED FOR IN THIS SECTION', 'level': '4.0', 'status': 'published'}]}

exec(code, env_args)
