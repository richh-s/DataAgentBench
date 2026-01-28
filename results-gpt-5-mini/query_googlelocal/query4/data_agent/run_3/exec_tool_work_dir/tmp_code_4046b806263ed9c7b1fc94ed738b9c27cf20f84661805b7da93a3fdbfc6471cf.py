code = """import json
rev = var_call_WCNvW4WaLrFNoSfvCcN5yI1o
bus = var_call_RPbgs6NS700EcuTRGRMz1f4F
map_name = {b['gmap_id']: b['name'] for b in bus}
rows = []
for r in rev:
    gid = r['gmap_id']
    cnt = int(r['high_reviews'])
    name = map_name.get(gid, None)
    rows.append({'gmap_id': gid, 'name': name, 'high_reviews': cnt})
rows_sorted = sorted(rows, key=lambda x: x['high_reviews'], reverse=True)
top3 = rows_sorted[:3]
print("__RESULT__:")
print(json.dumps(top3))"""

env_args = {'var_call_WCNvW4WaLrFNoSfvCcN5yI1o': [{'gmap_id': 'gmap_20', 'high_reviews': '8'}, {'gmap_id': 'gmap_53', 'high_reviews': '7'}, {'gmap_id': 'gmap_40', 'high_reviews': '6'}, {'gmap_id': 'gmap_35', 'high_reviews': '6'}, {'gmap_id': 'gmap_72', 'high_reviews': '5'}, {'gmap_id': 'gmap_62', 'high_reviews': '5'}, {'gmap_id': 'gmap_46', 'high_reviews': '5'}, {'gmap_id': 'gmap_17', 'high_reviews': '4'}, {'gmap_id': 'gmap_69', 'high_reviews': '3'}, {'gmap_id': 'gmap_56', 'high_reviews': '3'}], 'var_call_RPbgs6NS700EcuTRGRMz1f4F': [{'gmap_id': 'gmap_17', 'name': 'Black Tie Ski Rental Delivery of Mammoth', 'description': ' Offering a wide selection of winter sports equipment for hire, this service in Mammoth Lakes, CA 93546 ensures you’re fully equipped for an unforgettable day on the slopes.'}, {'gmap_id': 'gmap_20', 'name': 'Aurora Massage', 'description': ' Located in Sacramento, CA 95821, this wellness center offers expert bodywork services designed to relax and rejuvenate your mind and body.'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots', 'description': ' This vibrant establishment in Vista, CA 92081 specializes in crafting a diverse selection of artisanal beers, offering a cozy atmosphere for tasting and enjoying unique local brews.'}, {'gmap_id': 'gmap_72', 'name': "Zuby's Brake Tires & Wheels", 'description': ' This auto service center in Garden Grove, CA 92843 specializes in providing high-quality wheels and tire-related services to ensure your vehicle runs smoothly and safely.'}, {'gmap_id': 'gmap_56', 'name': 'J & T Plumbing Pros', 'description': ' Serving Riverside, CA 92503, this skilled provider specializes in comprehensive plumbing solutions, ensuring efficient repairs and installations for residential and commercial needs.'}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD', 'description': ' Offering comprehensive medical care and personalized health solutions in Encino, CA 91436, this clinic specializes in diagnosing and treating a wide range of health conditions.'}, {'gmap_id': 'gmap_62', 'name': 'Acuity Eye Group, Retina Institute & Acuity 360 Advanced Vision Center - Tustin', 'description': ' Located in Tustin, CA 92780, this eye care clinic offers expert vision assessments and advanced treatments for a wide range of eye conditions.'}, {'gmap_id': 'gmap_46', 'name': 'B2Sign, Inc.', 'description': ' This Pomona-based establishment specializes in high-quality printing services, offering a range of products from business cards to custom banners, conveniently located in Pomona, CA 91766.'}, {'gmap_id': 'gmap_69', 'name': 'Taitz Orly DDS', 'description': ' Providing comprehensive oral care and specialized treatments, this dental practice in Rancho Santa Margarita, CA 92688, is dedicated to ensuring your smile stays healthy and bright.'}, {'gmap_id': 'gmap_40', 'name': 'Widows Peak Salon', 'description': ' This trendy grooming studio in Los Angeles, CA 90012 offers expert styling, cutting-edge color treatments, and personalized consultations to enhance your unique look.'}]}

exec(code, env_args)
