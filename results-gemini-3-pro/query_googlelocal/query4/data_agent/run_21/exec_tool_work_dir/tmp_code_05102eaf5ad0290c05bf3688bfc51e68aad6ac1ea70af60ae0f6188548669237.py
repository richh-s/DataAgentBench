code = """import pandas as pd
import json

with open(locals()['var_function-call-16858423554009881860'], 'r') as f:
    data = json.load(f)

df = pd.DataFrame(data)
df['dt'] = pd.to_datetime(df['time'], errors='coerce')
df_2019 = df[df['dt'].dt.year == 2019]
counts = df_2019.groupby('gmap_id').size().reset_index(name='review_count')
top5 = counts.sort_values('review_count', ascending=False).head(5)

print("__RESULT__:")
print(top5.to_json(orient='records'))"""

env_args = {'var_function-call-1592769850991166857': [{'name': 'Michael Rizal', 'time': 'September 03, 2020 at 04:15 PM', 'rating': '5', 'text': 'Located in the vibrant area of Los Angeles, CA 90023, this company truly stands out. "Great company. Amazing customer service and they always have what we need in stock. Sometimes, we’d ask to hold for future orders and they will! Miss Jane is very helpful and great communicator."', 'gmap_id': 'gmap_44'}, {'name': 'Faranak Rafizadeh', 'time': '2021-04-12 17:07:52', 'rating': '5', 'text': 'Los Angeles is known for its vibrant culture and friendly atmosphere. "Nice people helpful."', 'gmap_id': 'gmap_44'}, {'name': 'Javier Perez', 'time': '2018-04-23 16:24:26', 'rating': '5', 'text': 'I had a fantastic experience at this amazing spot in Los Angeles, CA 90023, where the friendly staff went above and beyond to make my visit truly enjoyable!', 'gmap_id': 'gmap_44'}, {'name': 'Luis P.', 'time': '2017-07-10 22:12:19', 'rating': '5', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the friendly staff and delicious pastries made my day truly special!', 'gmap_id': 'gmap_44'}, {'name': 'His Mama Cakez', 'time': 'May 19, 2021 at 03:55 AM', 'rating': '3', 'text': 'I had an amazing experience at this charming café in Los Angeles, where the coffee was exceptional and the atmosphere was incredibly welcoming!', 'gmap_id': 'gmap_44'}], 'var_function-call-4750361976043750993': [{'gmap_id': 'gmap_35', 'review_count': '19'}, {'gmap_id': 'gmap_53', 'review_count': '17'}, {'gmap_id': 'gmap_20', 'review_count': '14'}], 'var_function-call-4411638699898200019': [{'gmap_id': 'gmap_20', 'name': 'Aurora Massage'}, {'gmap_id': 'gmap_53', 'name': 'The Boochyard @ Local Roots'}, {'gmap_id': 'gmap_35', 'name': 'Encino Dermatology & Laser: Alex Khadavi MD'}], 'var_function-call-5189049921185773902': [{'COUNT(*)': '2000'}], 'var_function-call-16858423554009881860': 'file_storage/function-call-16858423554009881860.json', 'var_function-call-2436444936275792044': [{'gmap_id': 'gmap_35', 'review_count': 19}, {'gmap_id': 'gmap_53', 'review_count': 17}, {'gmap_id': 'gmap_20', 'review_count': 14}]}

exec(code, env_args)
