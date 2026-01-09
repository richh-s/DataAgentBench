code = """import json, re
import pandas as pd

path = var_call_NETCgiRx70xDGMqzp64VWVxg
with open(path,'r',encoding='utf-8') as f:
    rows = json.load(f)

# Build map from UC publication_number -> list of primary CPC subclass codes (e.g., F25B21/00 => F25B)
uc_pub_to_primary_subclass=set()
uc_pubs=set()
for r in rows:
    pi=r.get('Patents_info','')
    if 'UNIV CALIFORNIA' in pi:
        m=re.search(r'pub\.? number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', pi)
        if not m:
            m=re.search(r'publication number\s+([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', pi)
        pub=m.group(1) if m else None
        if pub:
            uc_pubs.add(pub)
            # parse cpc json
            cpc_str=r.get('cpc')
            primary=set()
            if cpc_str:
                try:
                    cpcs=json.loads(cpc_str)
                    for entry in cpcs:
                        if entry.get('first'):
                            code=entry.get('code','')
                            # subclass is first 4 chars letters+digits up to length 4
                            sc=code.replace(' ','')
                            sc=sc[:4]
                            primary.add(sc)
                except Exception:
                    pass
            if not primary and cpc_str:
                # fallback regex extract codes and take first
                codes=re.findall(r'"code"\s*:\s*"([A-Z0-9]+)\s*/', cpc_str)
                primary.update([c[:4] for c in codes[:1]])
            for sc in primary:
                uc_pub_to_primary_subclass.add(sc)

res={'uc_publications_count':len(uc_pubs),'primary_subclasses':sorted(list(uc_pub_to_primary_subclass))}
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_YJidZmBvU5MTPVYW57hU6WF7': ['publicationinfo'], 'var_call_LRepTdXnPvuewKZleMJeYEt0': ['cpc_definition'], 'var_call_89qb0KndyOtUX3EZVb5EyOw1': [], 'var_call_EpTAmg0Qd8RR0QwpJzsoYOy4': [], 'var_call_orSJcL9REVmx7crexoGaa75w': [{'Patents_info': 'PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.'}, {'Patents_info': 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.'}, {'Patents_info': 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.'}, {'Patents_info': 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.'}, {'Patents_info': 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'}], 'var_call_u13kdrbYze9McgMf77J8ZfqV': ['PANASONIC IP MAN CO LTD holds the US patent application (ID US-201916293577-A), with publication number US-11081687-B2.', 'GLASSNER RUDOLF holds the US patent filing (application no. US-201916355911-A), with publication number US-10794458-B2.', 'In US, the application (ID US-201916369247-A) is owned by COVESTRO LLC and has publication no. US-11124615-B2.', 'In US, the patent filing (app. number US-201916369879-A) is assigned to HOMOLOGY MEDICINES INC and has pub. number US-10610606-B2.', 'In US, the patent application (no. US-201916373467-A) is owned by APPLETON GRP LLC and has publication number US-10957507-B2.'], 'var_call_NETCgiRx70xDGMqzp64VWVxg': 'file_storage/call_NETCgiRx70xDGMqzp64VWVxg.json'}

exec(code, env_args)
