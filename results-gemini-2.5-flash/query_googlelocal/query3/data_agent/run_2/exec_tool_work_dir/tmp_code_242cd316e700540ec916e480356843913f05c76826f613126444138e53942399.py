code = """import json

top_5_businesses = locals()['var_function-call-4524421853268768571']

formatted_answer = "Top 5 businesses open after 6:00 PM on at least one weekday, by average rating:\n"
for business in top_5_businesses:
    formatted_answer += "Name: " + business['name'] + "\n"
    try:
        hours_list = json.loads(business['hours'])
        hours_str_parts = []
        for day, time_range in hours_list:
            hours_str_parts.append(day + ': ' + time_range)
        hours_str = ', '.join(hours_str_parts)
    except (json.JSONDecodeError, TypeError):
        hours_str = "N/A"
    formatted_answer += "Operating Hours: " + hours_str + "\n"
    formatted_answer += "Average Rating: " + str(round(business['average_rating'], 2)) + "\n\n"

print("__RESULT__:")
print(json.dumps(formatted_answer))"""

env_args = {'var_function-call-17531646216573112097': 'file_storage/function-call-17531646216573112097.json', 'var_function-call-17887064346993606697': 'file_storage/function-call-17887064346993606697.json', 'var_function-call-7572177186537588015': 'file_storage/function-call-7572177186537588015.json', 'var_function-call-4524421853268768571': [{'name': 'IronStep', 'hours': '[["Thursday", "7AM–3:30PM"], ["Friday", "7AM–3:30PM"], ["Saturday", "Closed"], ["Sunday", "Closed"], ["Monday", "7AM–3:30PM"], ["Tuesday", "7AM–3:30PM"], ["Wednesday", "7AM–3:30PM"]]', 'average_rating': 5.0}, {'name': 'Taba Rug Gallery', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'average_rating': 5.0}, {'name': 'Beauty Divine Artistry', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]', 'average_rating': 5.0}, {'name': 'White Barn Candle Co', 'hours': '[["Thursday", "10AM–9PM"], ["Friday", "10AM–9PM"], ["Saturday", "10AM–9PM"], ["Sunday", "11AM–7PM"], ["Monday", "10AM–9PM"], ["Tuesday", "10AM–9PM"], ["Wednesday", "10AM–9PM"]]', 'average_rating': 5.0}, {'name': 'Hanford Auto Supply', 'hours': '[["Thursday", "9AM–6PM"], ["Friday", "9AM–6PM"], ["Saturday", "9AM–5PM"], ["Sunday", "Closed"], ["Monday", "9AM–6PM"], ["Tuesday", "9AM–6PM"], ["Wednesday", "9AM–6PM"]]', 'average_rating': 5.0}]}

exec(code, env_args)
