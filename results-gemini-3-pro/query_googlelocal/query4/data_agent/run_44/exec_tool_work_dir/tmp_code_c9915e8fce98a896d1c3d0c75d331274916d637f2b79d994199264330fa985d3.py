code = """import json

# Reviews count
reviews_counts = [
    {"gmap_id": "gmap_72", "cnt": 7},
    {"gmap_id": "gmap_35", "cnt": 6},
    {"gmap_id": "gmap_62", "cnt": 5}
]

# Business info
business_info = [
    {"gmap_id": "gmap_72", "name": "Zuby's Brake Tires & Wheels"},
    {"gmap_id": "gmap_35", "name": "Encino Dermatology & Laser: Alex Khadavi MD"},
    {"gmap_id": "gmap_62", "name": "Acuity Eye Group, Retina Institute & Acuity 360 Advanced Vision Center - Tustin"}
]

# Merge
result = []
for rc in reviews_counts:
    for bi in business_info:
        if rc['gmap_id'] == bi['gmap_id']:
            result.append({
                "name": bi['name'],
                "count": rc['cnt']
            })

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_function-call-12132360245582492245': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}], 'var_function-call-10376489038803128040': [{'gmap_id': 'gmap_72', 'cnt': '7'}, {'gmap_id': 'gmap_35', 'cnt': '6'}, {'gmap_id': 'gmap_62', 'cnt': '5'}], 'var_function-call-18371138828724087612': [{'gmap_id': 'gmap_72', 'name': "Zuby's Brake Tires & Wheels"}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD'}, {'gmap_id': 'gmap_62', 'name': 'Acuity Eye Group, Retina Institute & Acuity 360 Advanced Vision Center - Tustin'}]}

exec(code, env_args)
