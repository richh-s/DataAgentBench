code = """import json
from pathlib import Path

fund = json.loads(Path(var_call_SroaF07HpSeBDUZSoLhd6zNu).read_text())
proj_list = var_call_olh0o0lon6HvgVDvXEfo94yx['projects']
fund_map = {r['Project_Name']: int(r['total_amount']) for r in fund}

total = sum(fund_map.get(p, 0) for p in proj_list)
missing = [p for p in proj_list if p not in fund_map]
print('__RESULT__:')
print(json.dumps({'projects': proj_list, 'project_count': len(proj_list), 'total_funding': total, 'missing_funding_projects': missing}))"""

env_args = {'var_call_TpPn0yAmA3vLsADt1sJwRJSb': ['Funding'], 'var_call_357DOrmSTlhzjregOEGXC2P6': ['civic_docs'], 'var_call_DQLKJrtf3yYi1VEkTJZXOohY': 'file_storage/call_DQLKJrtf3yYi1VEkTJZXOohY.json', 'var_call_Iw0tspcMNdI7eyL6QtP7EKU2': {'spring22_projects': ['(cid:131) Advertise: Spring 2022', '(cid:131) Complete Design: February 2022', '(cid:131) Complete Design: January 2022', '(cid:131) Complete Design: March 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Complete Design: Winter 2021', '(cid:131) Complete Design: Winter 2021/2022'], 'count': 7}, 'var_call_Xiaqyh7c6Gike1PzxA4xLEez': 'file_storage/call_Xiaqyh7c6Gike1PzxA4xLEez.json', 'var_call_KEyBGkmNBAjxvcnWF5GshHD6': {'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'count': 14}, 'var_call_olh0o0lon6HvgVDvXEfo94yx': {'projects': ['Marie Canyon Green Streets'], 'count': 1}, 'var_call_SroaF07HpSeBDUZSoLhd6zNu': 'file_storage/call_SroaF07HpSeBDUZSoLhd6zNu.json'}

exec(code, env_args)
