code = """import json, re

path = var_call_vVVmQ2VpsYjPkYThYNl2X0H7
with open(path,'r',encoding='utf-8') as f:
    all_recs=json.load(f)
uc_path = var_call_D8KOFXg6SsoYmdwmDXj91rd5
with open(uc_path,'r',encoding='utf-8') as f:
    uc_recs=json.load(f)

uc_pub=set()
for r in uc_recs:
    pi=r.get('Patents_info','')
    m=re.search(r'publication number\s+([A-Z]{2}-[0-9]+[A-Z0-9-]*?)\.', pi)
    if m:
        uc_pub.add(m.group(1))

def extract_assignee(pi:str):
    m=re.search(r'^(.+?)\s+holds\s+the', pi, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m=re.search(r'is\s+(?:owned by|assigned to)\s+(.+?)\s+and\s+has', pi, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    return None

pairs=set()
for r in all_recs:
    cit=r.get('citation')
    if not cit or cit=='[]':
        continue
    try:
        cit_list=json.loads(cit)
    except Exception:
        continue
    if not any((c.get('publication_number') in uc_pub) for c in cit_list if isinstance(c, dict)):
        continue
    ass=extract_assignee(r.get('Patents_info','') or '')
    if not ass:
        continue
    up=ass.upper()
    if ('UNIV CALIFORNIA' in up) or ('UNIVERSITY OF CALIFORNIA' in up) or ('REGENTS OF THE UNIVERSITY OF CALIFORNIA' in up):
        continue
    cpc=r.get('cpc')
    subclasses=set()
    if cpc:
        try:
            cpc_list=json.loads(cpc)
            for e in cpc_list:
                if isinstance(e, dict) and e.get('first') is True:
                    code=e.get('code')
                    if code:
                        subclasses.add(code.split('/')[0] + '/00')
        except Exception:
            pass
    for sc in subclasses:
        pairs.add((ass, sc))

cpc_titles={r['symbol']: r['titleFull'] for r in var_call_khodqaEDGHolrYGa7q4Hf9o6}
rows=[{'citing_assignee': ass, 'cpc_subclass_title': cpc_titles.get(sc,'')} for ass, sc in sorted(pairs)]

print('__RESULT__:')
print(json.dumps({'rows': rows}))"""

env_args = {'var_call_6r9kRKlWpAnxGL0RQggEq1u2': ['publicationinfo'], 'var_call_E96U2H3Ln095YkOv6QIGX04g': ['cpc_definition'], 'var_call_tPdPyr8N8C3FwSeXzne8Nu8v': [], 'var_call_d2oOELDTbDWpa9VNRi39QqwN': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_D8KOFXg6SsoYmdwmDXj91rd5': 'file_storage/call_D8KOFXg6SsoYmdwmDXj91rd5.json', 'var_call_8KqE4sLa73ab8P4tWMqgU4h7': {'uc_pub_count': 58}, 'var_call_vVVmQ2VpsYjPkYThYNl2X0H7': 'file_storage/call_vVVmQ2VpsYjPkYThYNl2X0H7.json', 'var_call_V2dELoNPRXWkvTbTKg3JC1bc': {'pair_count': 4, 'subclass_count': 4, 'pairs_preview': [['CALIFORNIA INST OF TECHN', 'G01V1'], ['CRYSTAL IS INC', 'C30B11'], ['CRYSTAL IS INC', 'C30B25'], ['SCHOWALTER LEO J', 'H01L21']], 'subclasses': ['C30B11', 'C30B25', 'G01V1', 'H01L21']}, 'var_call_9k4W5Z1wQN7usgZ5aBafcgRl': [], 'var_call_kDN362lOJym2nP39fJxSv5Rq': [{'symbol': 'G01V1/06', 'titleFull': 'Ignition devices'}, {'symbol': 'G01V1/09', 'titleFull': 'Transporting arrangements, e.g. on vehicles'}, {'symbol': 'G01V1/047', 'titleFull': 'Arrangements for coupling the generator to the ground'}, {'symbol': 'G01V1/189', 'titleFull': 'Combinations of different types of receiving elements'}, {'symbol': 'G01V1/186', 'titleFull': 'Hydrophones'}, {'symbol': 'G01V1/181', 'titleFull': 'Geophones'}, {'symbol': 'G01V1/201', 'titleFull': 'Constructional details of seismic cables, e.g. streamers'}, {'symbol': 'G01V1/306', 'titleFull': 'Analysis for determining physical properties of the subsurface, e.g. impedance, porosity or attenuation profiles'}, {'symbol': 'G01V1/307', 'titleFull': 'Analysis for determining seismic attributes, e.g. amplitude, instantaneous phase or frequency, reflection strength or polarity'}, {'symbol': 'G01V1/301', 'titleFull': 'Analysis for determining seismic cross-sections or geostructures'}, {'symbol': 'G01V1/303', 'titleFull': 'Analysis for determining velocity profiles or travel times'}, {'symbol': 'G01V1/308', 'titleFull': 'Time lapse or 4D effects, e.g. production related effects to the formation'}, {'symbol': 'G01V1/325', 'titleFull': 'Transforming one representation into another'}, {'symbol': 'G01V1/345', 'titleFull': 'Visualisation of seismic data or attributes, e.g. in 3D cubes'}, {'symbol': 'G01V1/37', 'titleFull': 'Effecting static or dynamic corrections on records, e.g. correcting spread; Correlating seismic signals; Eliminating effects of unwanted energy specially adapted for seismic systems using continuous agitation of the ground, e.g. using pulse compression of frequency swept signals for enhancement of received signals'}, {'symbol': 'G01V1/364', 'titleFull': 'Seismic filtering'}, {'symbol': 'G01V1/362', 'titleFull': 'Effecting static or dynamic corrections; Stacking'}, {'symbol': 'G01V1/48', 'titleFull': 'Processing data'}, {'symbol': 'G01V1/46', 'titleFull': 'Data acquisition'}, {'symbol': 'G01V1/523', 'titleFull': 'Damping devices'}], 'var_call_khodqaEDGHolrYGa7q4Hf9o6': [{'symbol': 'H01L21/00', 'titleFull': 'Processes or apparatus adapted for the manufacture or treatment of semiconductor or solid state devices or of parts thereof'}, {'symbol': 'C30B25/00', 'titleFull': 'Single-crystal growth by chemical reaction of reactive gases, e.g. chemical vapour-deposition growth'}, {'symbol': 'C30B11/00', 'titleFull': 'Single-crystal growth by normal freezing or freezing under temperature gradient, e.g. Bridgman-Stockbarger method'}, {'symbol': 'G01V1/00', 'titleFull': 'Seismology; Seismic or acoustic prospecting or detecting'}]}

exec(code, env_args)
