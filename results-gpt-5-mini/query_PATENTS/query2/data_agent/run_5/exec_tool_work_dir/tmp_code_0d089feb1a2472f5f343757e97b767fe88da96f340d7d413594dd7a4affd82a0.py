code = """import json, re
from collections import defaultdict

with open(var_call_FwfTz2at0Mr84i7lnCuDNtwv, 'r') as f:
    records = json.load(f)

months_h2 = ['jul','july','aug','august','sep','sept','september','oct','october','nov','november','dec','december']

# Filter for Germany
def is_germany(pi):
    if not pi:
        return False
    s = pi.lower()
    if ' de ' in s or 'de,' in s or 'de.' in s or ' from de' in s or 'germany' in s or 'deutsch' in s or ' deutschland' in s:
        return True
    # look for country codes like (no. DE- or DE,
    if re.search(r'\bDE\b', pi):
        return True
    return False

# Build group-year-family set
group_year_fams = defaultdict(lambda: defaultdict(set))

for r in records:
    gd = (r.get('grant_date') or '').lower()
    if '2019' not in gd:
        continue
    if not any(m in gd for m in months_h2):
        continue
    if not is_germany(r.get('Patents_info','')):
        continue
    fam = r.get('family_id')
    filing = (r.get('filing_date') or '')
    m = re.search(r'(19|20)\d{2}', filing)
    if not m:
        continue
    year = int(m.group(0))
    cpc_field = r.get('cpc') or ''
    try:
        cpcs = json.loads(cpc_field)
    except Exception:
        try:
            cpcs = json.loads(cpc_field.replace("'", '"'))
        except Exception:
            continue
    for e in cpcs:
        if isinstance(e, dict):
            code = e.get('code')
        else:
            code = None
        if not code:
            continue
        # extract level-4 group: letters+digits until 4 chars
        # standard: first 4 chars
        group = code.replace('\\n','').strip()
        # remove leading/trailing quotes
        if '/' in group:
            grp = group.split('/')[0]
        else:
            grp = group
        grp4 = grp[:4]
        if len(grp4) < 4:
            continue
        group_year_fams[grp4][year].add(fam)

# Compute EMA
alpha = 0.1
results = []
for group, years_map in group_year_fams.items():
    years = sorted(years_map.keys())
    counts = [len(years_map[y]) for y in years]
    if not counts:
        continue
    ema = []
    ema_prev = counts[0]
    ema.append(ema_prev)
    for x in counts[1:]:
        ema_curr = alpha * x + (1-alpha) * ema_prev
        ema.append(ema_curr)
        ema_prev = ema_curr
    # find best year (year with max EMA)
    best_idx = max(range(len(years)), key=lambda i: ema[i])
    results.append({
        'group_code': group,
        'years': years,
        'counts': counts,
        'ema': [round(v,6) for v in ema],
        'best_year': years[best_idx],
        'best_ema': round(ema[best_idx],6)
    })

# sort results by best_ema desc
results_sorted = sorted(results, key=lambda x: x['best_ema'], reverse=True)

out = {'results': results_sorted}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_2KWjt8JKvALQF3B1Xrp7spAo': 'file_storage/call_2KWjt8JKvALQF3B1Xrp7spAo.json', 'var_call_DoMQ2XCAoGqwJKBJyG5u70sk': {'groups': [], 'group_codes': []}, 'var_call_bHiWZui9dvxOvyz8cCTNyOSW': {'country_counts': {'RU': 9, 'EP': 16, 'KR': 62, 'AU': 12, 'US': 91, 'JP': 48, 'DE': 10, 'GB': 1, 'CN': 327, 'CA': 19, 'TW': 4, 'FR': 3, 'ES': 1, 'DK': 1}, 'samples': [{'grant_date': '2019 on Jul 12th', 'Patents_info': 'Application (no. RU-2018119076-A) from RU, assigned to FEDERALNOE GOSUDARSTVENNOE KAZENNOE VOENNOE OBRAZOVATELNOE UCHREZHDENIE VYSSHEGO OBRAZOVANIYA VOENNA, with publication no. RU-2694421-C1.'}, {'grant_date': 'July 8th, 2019', 'Patents_info': 'The DK patent application (number DK-14719221-T) is held by JASKE WOLFGANG and has publication number DK-2965013-T3.'}, {'grant_date': '2019 on Nov 14th', 'Patents_info': 'In RU, the patent filing (application no. RU-2019124341-U) is owned by [] and has pub. number RU-193787-U1.'}, {'grant_date': 'on September 3rd, 2019', 'Patents_info': 'In KR, the application (ID KR-20170006144-U) is belonging to [] and has pub. number KR-200489330-Y1.'}, {'grant_date': '23rd of July, 2019', 'Patents_info': '[] holds the KR application (ID KR-20180005063-U), with pub. number KR-200489690-Y1.'}, {'grant_date': 'October 25th, 2019', 'Patents_info': 'The FR patent application (number FR-1550824-A) is owned by OBERTHUR TECHNOLOGIES and has pub. number FR-3032292-B1.'}, {'grant_date': '28th of August, 2019', 'Patents_info': 'Application (ID EP-13874810-A) from EP, held by HONG KONG R&D CENTRE FOR LOGISTICS AND SUPPLY CHAIN MANAGEMENT ENABLING TECH LIMITED, with publication number EP-2954502-B1.'}, {'grant_date': 'Aug 7th, 2019', 'Patents_info': 'AI ALPINE US BIDCO INC holds the EP patent filing (application number EP-14189312-A), with pub. number EP-2865859-B1.'}, {'grant_date': 'on December 11th, 2019', 'Patents_info': 'The EP application (ID EP-15715423-A) is assigned to PEPTITECH S R L and has publication no. EP-3125917-B1.'}, {'grant_date': '2019, November 27th', 'Patents_info': 'BERNSTEIN AG holds the EP patent filing (application no. EP-16782246-A), with pub. number EP-3365735-B1.'}, {'grant_date': '25th Dec 2019', 'Patents_info': 'The JP patent application (ID JP-2019531845-A) is belonging to [] and has pub. number JP-6625286-B1.'}, {'grant_date': '5th of November, 2019', 'Patents_info': '[] holds the KR patent filing (application number KR-20170136376-A), with publication number KR-102040577-B1.'}, {'grant_date': '6th of August, 2019', 'Patents_info': '[] holds the KR application (no. KR-20170137256-A), with publication no. KR-102007693-B1.'}, {'grant_date': '25th September 2019', 'Patents_info': 'The KR patent filing (application no. KR-20170158871-A) is belonging to [] and has pub. number KR-102025248-B1.'}, {'grant_date': '2019 on Nov 26th', 'Patents_info': 'The KR patent application (number KR-20170166876-A) is owned by [] and has pub. number KR-102037072-B1.'}, {'grant_date': 'dated 4th November 2019', 'Patents_info': 'The KR patent filing (application no. KR-20170170141-A) is assigned to [] and has publication no. KR-102026805-B1.'}, {'grant_date': '2019 on Oct 2nd', 'Patents_info': 'Patent filing (application no. KR-20170174743-A) from KR, assigned to [], with publication number KR-102027768-B1.'}, {'grant_date': 'dated 26th August 2019', 'Patents_info': 'The KR application (no. KR-20170178007-A) is belonging to [] and has pub. number KR-102014352-B1.'}, {'grant_date': '2019, July 15th', 'Patents_info': 'The KR patent application (ID KR-20180082930-A) is assigned to [] and has pub. number KR-102000399-B1.'}, {'grant_date': '22nd Oct 2019', 'Patents_info': 'In US, the patent filing (application no. US-201715591352-A) is belonging to AMBARELLA INC and has pub. number US-10452449-B1.'}, {'grant_date': 'on November 7th, 2019', 'Patents_info': 'Patent application (ID AU-2017235116-A) from AU, owned by UNIV YAMAGUCHI, with publication no. AU-2017235116-B2.'}, {'grant_date': 'on October 31st, 2019', 'Patents_info': 'GRIFOLS WORLDWIDE OPERATIONS LTD holds the AU patent filing (application no. AU-2015201496-A), with publication number AU-2015201496-B2.'}, {'grant_date': '30th Jul 2019', 'Patents_info': 'The KR patent filing (application number KR-20140159020-A) is owned by [] and has pub. number KR-102005472-B1.'}, {'grant_date': '2019, September 2nd', 'Patents_info': '[] holds the KR application (ID KR-20147021741-A), with publication number KR-102017360-B1.'}, {'grant_date': '29th Aug 2019', 'Patents_info': '[] holds the KR patent filing (application number KR-20160125594-A), with publication number KR-102016204-B1.'}, {'grant_date': '26th Nov 2019', 'Patents_info': 'In KR, the application (number KR-20170124936-A) is belonging to [] and has publication number KR-102039148-B1.'}, {'grant_date': '2019 on Sep 30th', 'Patents_info': 'In KR, the patent filing (app. number KR-20170151189-A) is held by [] and has pub. number KR-101990545-B1.'}, {'grant_date': 'October the 15th, 2019', 'Patents_info': 'In KR, the application (ID KR-20170163559-A) is belonging to [] and has publication number KR-102032620-B1.'}, {'grant_date': '12th of August, 2019', 'Patents_info': '[] holds the KR patent application (number KR-20177011077-A), with publication number KR-102009685-B1.'}, {'grant_date': 'August 26th, 2019', 'Patents_info': 'In KR, the patent application (ID KR-20177035487-A) is owned by [] and has publication no. KR-102014631-B1.'}, {'grant_date': 'Sep 9th, 2019', 'Patents_info': 'SEOYON INTECH CO LTD holds the KR patent filing (application number KR-20180028161-A), with publication no. KR-102019811-B1.'}, {'grant_date': '2019 on Jul 18th', 'Patents_info': 'The KR application (number KR-20180073594-A) is held by YOUNG IL CHEMICAL CO LTD and has pub. number KR-102001639-B1.'}, {'grant_date': 'July 3rd, 2019', 'Patents_info': 'Application (ID KR-20180103221-A) from KR, owned by [], with publication no. KR-101995717-B1.'}, {'grant_date': '8th of November, 2019', 'Patents_info': 'WINTEC KOREA INC holds the KR patent filing (application no. KR-20180135455-A), with pub. number KR-102042076-B1.'}, {'grant_date': 'September 20th, 2019', 'Patents_info': 'In KR, the patent application (no. KR-20180151499-A) is belonging to ENV ENERGY O&M INC and has publication no. KR-102023639-B1.'}, {'grant_date': '25th Nov 2019', 'Patents_info': 'KIM BANG SUB holds the KR patent filing (app. number KR-20190126520-A), with publication number KR-102048571-B1.'}, {'grant_date': 'August the 20th, 2019', 'Patents_info': 'The US patent application (ID US-201314065664-A) is belonging to EATON CORP and has publication no. US-10389553-B2.'}, {'grant_date': 'July 30th, 2019', 'Patents_info': 'The US patent filing (application number US-201214357078-A) is owned by ORGANOX LTD and has publication no. US-10362780-B2.'}, {'grant_date': '2019 on Nov 12th', 'Patents_info': 'Patent filing (application number US-201314374314-A) from US, owned by REMENDIUM LABS LLC, with publication no. US-10470862-B2.'}, {'grant_date': '1st October 2019', 'Patents_info': 'The US application (no. US-201414494246-A) is owned by INTEL CORP and has publication number US-10429803-B2.'}, {'grant_date': 'on November 5th, 2019', 'Patents_info': 'In US, the patent application (no. US-201314655932-A) is held by SERINPET LTDA REPRESENTACIONES Y SERVICIOS DE PETROLEOS and has pub. number US-10465517-B2.'}, {'grant_date': '31st December 2019', 'Patents_info': 'Application (no. US-201414901588-A) from US, owned by COPAN ITALIA SPA, with publication number US-10517575-B2.'}, {'grant_date': '23rd July 2019', 'Patents_info': 'ASENSEI INC holds the US application (no. US-201614987995-A), with pub. number US-10360811-B2.'}, {'grant_date': 'Oct 1st, 2019', 'Patents_info': 'UNIV KING ABDULAZIZ holds the US application (no. US-201615197115-A), with publication number US-10427382-B2.'}, {'grant_date': '6th August 2019', 'Patents_info': 'Application (number US-201615207944-A) from US, belonging to INFOVISION OPTOELECT KUNSHAN, with pub. number US-10371971-B2.'}, {'grant_date': 'November the 26th, 2019', 'Patents_info': 'Patent filing (application number US-201715461919-A) from US, assigned to WIPRO LTD, with pub. number US-10489440-B2.'}, {'grant_date': 'August the 20th, 2019', 'Patents_info': 'TAKATA CORP holds the US patent filing (application number US-201615559561-A), with publication number US-10384637-B2.'}, {'grant_date': 'dated 8th October 2019', 'Patents_info': 'The US patent application (ID US-201615761951-A) is held by HEWLETT PACKARD DEVELOPMENT CO and has publication no. US-10436614-B2.'}, {'grant_date': 'July the 9th, 2019', 'Patents_info': 'The US application (number US-201715791853-A) is owned by DENSO INT AMERICA INC and has pub. number US-10348153-B2.'}, {'grant_date': 'Dec 10th, 2019', 'Patents_info': 'In US, the application (no. US-201815912356-A) is assigned to THE FLOWR CANNABIS ULC and has publication no. US-10499731-B2.'}]}, 'var_call_FwfTz2at0Mr84i7lnCuDNtwv': 'file_storage/call_FwfTz2at0Mr84i7lnCuDNtwv.json'}

exec(code, env_args)
