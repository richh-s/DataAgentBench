code = """import json, re
import pandas as pd

# load publication records
pub_src = var_call_NbILj6o04k4SsIOviSOloErz
if isinstance(pub_src, str):
    with open(pub_src, 'r', encoding='utf-8') as f:
        pubs = json.load(f)
else:
    pubs = pub_src

def parse_year(s):
    if not s:
        return None
    m = re.search(r'(19|20)\\d{2}', s)
    return int(m.group(0)) if m else None

def in_h2_2019(s):
    if not s or '2019' not in s:
        return False
    s_l = s.lower()
    months = ['jul', 'aug', 'sep', 'oct', 'nov', 'dec']
    return any(m in s_l for m in months)

def extract_level4(code):
    if not code or not isinstance(code, str):
        return None
    c = code.strip()
    m = re.match(r'^([A-HY]\\d{2}[A-Z])', c)
    return m.group(1) if m else None

rows = []
for r in pubs:
    gd = r.get('grant_date')
    if not in_h2_2019(gd):
        continue
    fy = parse_year(r.get('filing_date'))
    if fy is None:
        continue
    cpc_raw = r.get('cpc')
    try:
        cpcs = json.loads(cpc_raw) if isinstance(cpc_raw, str) else (cpc_raw or [])
    except Exception:
        cpcs = []
    codes = []
    for it in cpcs:
        code = it.get('code') if isinstance(it, dict) else None
        l4 = extract_level4(code)
        if l4:
            codes.append(l4)
    # deduplicate per patent record
    for l4 in sorted(set(codes)):
        rows.append({'cpc_l4': l4, 'filing_year': fy})

df = pd.DataFrame(rows)
if df.empty:
    out = []
else:
    counts = df.groupby(['cpc_l4','filing_year']).size().reset_index(name='n')

    # compute EMA per cpc_l4 across years
    alpha = 0.1
    results = []
    for cpc, g in counts.groupby('cpc_l4'):
        g2 = g.sort_values('filing_year').copy()
        ema = None
        for _, rr in g2.iterrows():
            x = float(rr['n'])
            ema = x if ema is None else (alpha*x + (1-alpha)*ema)
            results.append({'cpc_l4': cpc, 'filing_year': int(rr['filing_year']), 'ema': float(ema), 'n': int(rr['n'])})
    ema_df = pd.DataFrame(results)
    # best year per cpc (max ema, tie -> latest year)
    best = (ema_df.sort_values(['cpc_l4','ema','filing_year'], ascending=[True,False,False])
                 .groupby('cpc_l4', as_index=False).head(1))

    # join titles from CPC definition level 4
    # query result might be empty due to status filter; use status='published'
    # We'll fetch needed titles via python by querying db? not allowed; use existing small query? none. We'll do a new query outside python.
    out = best.to_dict('records')

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_leUQxF7YFeUc8QKXBKuHUIpM': [], 'var_call_RLAZYDi7LLtwpXSykhBuJq0o': [], 'var_call_v84r07Y1h81Ek8JRojUYJdjh': [{'grant_date': '14th Mar 2019', 'Patents_info': 'Patent application (no. DE-102013211266-A) from DE, assigned to IBM, with publication number DE-102013211266-B4.'}, {'grant_date': 'Mar 19th, 2019', 'Patents_info': 'In RU, the patent filing (app. number RU-2017142236-A) is held by Sletov Aleksandr Anatolevich and has publication no. RU-2682615-C1.'}, {'grant_date': 'Mar 12th, 2019', 'Patents_info': 'The RU patent application (number RU-2018105657-A) is held by OBSHCHESTVO S OGRANICHENNOJ OTVETSTVENNOSTYU VORMKHOLS VNEDRENIE and has publication no. RU-2681783-C1.'}, {'grant_date': '2019 on Jul 12th', 'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.'}, {'grant_date': 'on March 14th, 2019', 'Patents_info': 'Patent application (number RU-2016134259-A) from RU, owned by KVINETIK LTD, with publication number RU-2681957-C2.'}, {'grant_date': 'July 8th, 2019', 'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.'}, {'grant_date': '8th April 2019', 'Patents_info': 'The DK patent filing (application number DK-14835716-T) is owned by UNIV OSLO HF and has pub. number DK-3069138-T3.'}, {'grant_date': '2019, May 30th', 'Patents_info': 'The RU patent application (ID RU-2018146701-U) is held by [] and has publication no. RU-189707-U1.'}, {'grant_date': '22nd May 2019', 'Patents_info': 'The ES patent application (ID ES-11727548-T) is assigned to LOHR IND and has pub. number ES-2713511-T3.'}, {'grant_date': '2019 on Nov 14th', 'Patents_info': 'In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193787-U1.'}, {'grant_date': 'May 2nd, 2019', 'Patents_info': 'Application (no. KR-20170000057-U) from KR, assigned to [], with pub. number KR-200489109-Y1.'}, {'grant_date': 'on September 3rd, 2019', 'Patents_info': 'In KR, the application (ID KR-20170006144-U) is belonging to [] and has pub. number KR-200489330-Y1.'}, {'grant_date': '23rd of July, 2019', 'Patents_info': '[] holds the KR application (ID KR-20180005063-U), with pub. number KR-200489690-Y1.'}, {'grant_date': '24th January 2019', 'Patents_info': 'Patent application (number AU-2018102026-A) from AU, belonging to ROCHEWAY PTY LTD, with publication number AU-2018102026-A4.'}, {'grant_date': 'October 25th, 2019', 'Patents_info': 'The FR patent application (number FR-1550824-A) is owned by OBERTHUR TECHNOLOGIES and has pub. number FR-3032292-B1.'}, {'grant_date': 'May 17th, 2019', 'Patents_info': 'Patent filing (app. number FR-1656473-A) from FR, assigned to ALSTOM TRANSP TECH, with publication number FR-3053744-B1.'}, {'grant_date': '2nd January 2019', 'Patents_info': 'In EP, the application (no. EP-10762743-A) is owned by TOTAL SA and has publication no. EP-2471103-B1.'}, {'grant_date': 'January 9th, 2019', 'Patents_info': 'In EP, the patent application (number EP-11747102-A) is assigned to SONY CORP and has pub. number EP-2541988-B1.'}, {'grant_date': 'on April 10th, 2019', 'Patents_info': 'Application (ID EP-12806859-A) from EP, owned by 3M INNOVATIVE PROPERTIES CO, with pub. number EP-2798076-B1.'}, {'grant_date': '28th of August, 2019', 'Patents_info': 'Application (ID EP-13874810-A) from EP, held by HONG KONG R&D CENTRE FOR LOGISTICS AND SUPPLY CHAIN MANAGEMENT ENABLING TECH LIMITED, with publication number EP-2954502-B1.'}, {'grant_date': 'Aug 7th, 2019', 'Patents_info': 'AI ALPINE US BIDCO INC holds the EP patent filing (application number EP-14189312-A), with pub. number EP-2865859-B1.'}, {'grant_date': 'on December 11th, 2019', 'Patents_info': 'The EP application (ID EP-15715423-A) is assigned to PEPTITECH S R L and has publication no. EP-3125917-B1.'}, {'grant_date': '19th June 2019', 'Patents_info': 'Application (no. EP-16020282-A) from EP, owned by SINTECO IMPIANTI S R L, with publication no. EP-3124882-B1.'}, {'grant_date': '2019, November 27th', 'Patents_info': 'BERNSTEIN AG holds the EP patent filing (application no. EP-16782246-A), with pub. number EP-3365735-B1.'}, {'grant_date': 'dated 30th January 2019', 'Patents_info': 'The BE patent application (no. BE-201805053-A) is assigned to EMBALEX S L and has publication number BE-1025367-B1.'}, {'grant_date': '25th Dec 2019', 'Patents_info': 'The JP patent application (ID JP-2019531845-A) is belonging to [] and has pub. number JP-6625286-B1.'}, {'grant_date': 'Mar 22nd, 2019', 'Patents_info': '[] holds the KR patent filing (app. number KR-20110125091-A), with publication number KR-101961486-B1.'}, {'grant_date': '26th Jun 2019', 'Patents_info': 'In KR, the application (number KR-20160081916-A) is held by [] and has publication number KR-101993463-B1.'}, {'grant_date': '6th of March, 2019', 'Patents_info': 'The KR patent application (ID KR-20170004388-A) is owned by [] and has publication number KR-101954771-B1.'}, {'grant_date': '3rd May 2019', 'Patents_info': '[] holds the KR patent filing (application number KR-20170019837-A), with publication no. KR-101974833-B1.'}, {'grant_date': '2019, May 10th', 'Patents_info': 'In KR, the application (number KR-20170037907-A) is owned by [] and has publication no. KR-101976918-B1.'}, {'grant_date': 'June 25th, 2019', 'Patents_info': 'Patent application (ID KR-20170100317-A) from KR, held by [], with publication number KR-101992230-B1.'}, {'grant_date': 'February the 28th, 2019', 'Patents_info': 'Patent filing (application number KR-20170100446-A) from KR, held by [], with publication no. KR-101953297-B1.'}, {'grant_date': 'Jun 18th, 2019', 'Patents_info': 'In KR, the application (ID KR-20170103602-A) is held by [] and has publication number KR-101990586-B1.'}, {'grant_date': '5th of November, 2019', 'Patents_info': '[] holds the KR patent filing (application number KR-20170136376-A), with publication number KR-102040577-B1.'}, {'grant_date': '6th of August, 2019', 'Patents_info': '[] holds the KR application (no. KR-20170137256-A), with publication no. KR-102007693-B1.'}, {'grant_date': '25th September 2019', 'Patents_info': 'The KR patent filing (application no. KR-20170158871-A) is belonging to [] and has pub. number KR-102025248-B1.'}, {'grant_date': '2019 on Nov 26th', 'Patents_info': 'The KR patent application (number KR-20170166876-A) is owned by [] and has pub. number KR-102037072-B1.'}, {'grant_date': 'dated 4th November 2019', 'Patents_info': 'The KR patent filing (application no. KR-20170170141-A) is assigned to [] and has publication no. KR-102026805-B1.'}, {'grant_date': '2019 on Oct 2nd', 'Patents_info': 'Patent filing (application no. KR-20170174743-A) from KR, assigned to [], with publication number KR-102027768-B1.'}, {'grant_date': 'dated 26th August 2019', 'Patents_info': 'The KR application (no. KR-20170178007-A) is belonging to [] and has pub. number KR-102014352-B1.'}, {'grant_date': 'Jan 11th, 2019', 'Patents_info': 'Patent filing (application number KR-20177023520-A) from KR, held by [], with publication no. KR-101937904-B1.'}, {'grant_date': 'on March 8th, 2019', 'Patents_info': 'Patent application (no. KR-20180068234-A) from KR, assigned to KANG EUI HYEOC, with pub. number KR-101956504-B1.'}, {'grant_date': '2019, July 15th', 'Patents_info': 'The KR patent application (ID KR-20180082930-A) is assigned to [] and has pub. number KR-102000399-B1.'}, {'grant_date': 'May 2nd, 2019', 'Patents_info': 'UNIV DONGGUK IND ACAD COOP holds the KR patent filing (application no. KR-20180155867-A), with publication no. KR-101974345-B1.'}, {'grant_date': 'February the 5th, 2019', 'Patents_info': 'The US application (no. US-201615217223-A) is owned by GOOGLE INC and has publication no. US-10198045-B1.'}, {'grant_date': 'February the 12th, 2019', 'Patents_info': 'In US, the patent application (no. US-201715436848-A) is belonging to RAPP LUKE EDWARD and has publication number US-10201626-B1.'}, {'grant_date': '22nd Oct 2019', 'Patents_info': 'In US, the patent filing (application no. US-201715591352-A) is belonging to AMBARELLA INC and has pub. number US-10452449-B1.'}, {'grant_date': '14th May 2019', 'Patents_info': 'Patent application (number US-201815950282-A) from US, assigned to DONG GUAN BRIGHT YINHUEY LIGHTING CO LTD, with pub. number US-10290193-B1.'}, {'grant_date': '23rd Apr 2019', 'Patents_info': 'The US patent application (number US-201816009329-A) is owned by GLOBALFOUNDRIES INC and has pub. number US-10269735-B1.'}], 'var_call_E0blvTT54BGW3wfNOqs87sl4': [{'n': '260808', 'min_level': '2.0', 'max_level': '19.0'}], 'var_call_c59A6Vm8BPuWr9u0InCimDRY': [{'symbol': 'B04', 'titleFull': 'CENTRIFUGAL APPARATUS OR MACHINES FOR CARRYING-OUT PHYSICAL OR CHEMICAL PROCESSES', 'level': '4.0', 'status': 'published'}, {'symbol': 'B23', 'titleFull': 'MACHINE TOOLS; METAL-WORKING NOT OTHERWISE PROVIDED FOR', 'level': '4.0', 'status': 'published'}, {'symbol': 'B30', 'titleFull': 'PRESSES', 'level': '4.0', 'status': 'published'}, {'symbol': 'B21', 'titleFull': 'MECHANICAL METAL-WORKING WITHOUT ESSENTIALLY REMOVING MATERIAL; PUNCHING METAL', 'level': '4.0', 'status': 'published'}, {'symbol': 'B25', 'titleFull': 'HAND TOOLS; PORTABLE POWER-DRIVEN TOOLS; MANIPULATORS', 'level': '4.0', 'status': 'published'}], 'var_call_NbILj6o04k4SsIOviSOloErz': 'file_storage/call_NbILj6o04k4SsIOviSOloErz.json'}

exec(code, env_args)
