code = """import json, os

# Load the user data
users_2016 = var_functions.query_db:2

# Extract user IDs
user_ids_2016 = [user['user_id'] for user in users_2016]

print('__RESULT__:')
print(json.dumps({'user_count': len(user_ids_2016), 'sample_users': user_ids_2016[:5]}))"""

env_args = {'var_functions.list_db:0': ['checkin', 'business'], 'var_functions.query_db:2': [{'user_id': 'userid_746', 'name': 'Rita', 'review_count': '179', 'yelping_since': '2016-06-23 01:59:28', 'useful': '205', 'funny': '27', 'cool': '55', 'elite': '2017,2018,2019,20,20,2021'}, {'user_id': 'userid_1109', 'name': 'Bruce', 'review_count': '23', 'yelping_since': '2016-10-16 18:32:25', 'useful': '14', 'funny': '11', 'cool': '1', 'elite': ''}, {'user_id': 'userid_1950', 'name': 'Samantha', 'review_count': '120', 'yelping_since': '2016-04-16 03:42:28', 'useful': '90', 'funny': '25', 'cool': '40', 'elite': '2018,2019,20,20,2021'}, {'user_id': 'userid_1316', 'name': 'Kathleen', 'review_count': '289', 'yelping_since': '2016-12-29 21:32:44', 'useful': '379', 'funny': '82', 'cool': '232', 'elite': '2018,2019,20,20,2021'}, {'user_id': 'userid_1182', 'name': 'Caroline', 'review_count': '33', 'yelping_since': '2016-03-20 18:41:14', 'useful': '59', 'funny': '7', 'cool': '29', 'elite': ''}, {'user_id': 'userid_151', 'name': 'Dawn', 'review_count': '3', 'yelping_since': '2016-11-07 18:40:10', 'useful': '3', 'funny': '1', 'cool': '1', 'elite': ''}, {'user_id': 'userid_1158', 'name': 'Wendel', 'review_count': '90', 'yelping_since': '2016-01-31 16:25:04', 'useful': '83', 'funny': '12', 'cool': '11', 'elite': ''}, {'user_id': 'userid_508', 'name': 'Jim', 'review_count': '41', 'yelping_since': '2016-07-08 22:37:42', 'useful': '35', 'funny': '6', 'cool': '9', 'elite': ''}, {'user_id': 'userid_435', 'name': 'Danielle', 'review_count': '13', 'yelping_since': '2016-10-31 09:46:54', 'useful': '7', 'funny': '1', 'cool': '3', 'elite': ''}, {'user_id': 'userid_958', 'name': 'Deanna', 'review_count': '47', 'yelping_since': '2016-03-23 20:55:45', 'useful': '42', 'funny': '11', 'cool': '25', 'elite': '2017,2018'}]}

exec(code, env_args)
