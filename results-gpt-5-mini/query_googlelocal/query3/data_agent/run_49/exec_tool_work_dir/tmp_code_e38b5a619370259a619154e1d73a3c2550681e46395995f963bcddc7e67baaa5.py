code = """import json, os

d = var_call_QvNrckj2avgoUbMN3CSOQXZN
# d may be a Python list, a JSON string, or a file path
if isinstance(d, list):
    data = d
elif isinstance(d, str):
    try:
        data = json.loads(d)
    except Exception:
        try:
            with open(d, 'r') as f:
                data = json.load(f)
        except Exception:
            data = []
else:
    data = []

lines = []
for item in data:
    name = item.get('name','')
    hours = item.get('hours','')
    avg = item.get('average_rating', None)
    lines.append("Name: " + name)
    lines.append("Hours: " + hours)
    lines.append("Average Rating: " + (str(avg) if avg is not None else 'N/A'))
    lines.append("")

answer_text = "\n".join(lines).strip()

print("__RESULT__:")
print(json.dumps(answer_text))"""

env_args = {'var_call_3lnKVJvdm1DbPWa3S61ySIUT': 'file_storage/call_3lnKVJvdm1DbPWa3S61ySIUT.json', 'var_call_hX3jqNAGPgfeV8NWzJw1qApd': 'file_storage/call_hX3jqNAGPgfeV8NWzJw1qApd.json', 'var_call_QvNrckj2avgoUbMN3CSOQXZN': [{'name': 'Beauty Divine Artistry', 'hours': '[["Thursday", "9AM–8PM"], ["Friday", "9AM–8PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "9AM–8PM"], ["Tuesday", "9AM–8PM"], ["Wednesday", "9AM–8PM"]]', 'average_rating': 5.0}, {'name': 'TACOS LA CABANA', 'hours': '[["Thursday", "Closed"], ["Friday", "5–11PM"], ["Saturday", "5–11PM"], ["Sunday", "5–11PM"], ["Monday", "5–11PM"], ["Tuesday", "Closed"], ["Wednesday", "Closed"]]', 'average_rating': 5.0}, {'name': 'Taba Rug Gallery', 'hours': '[["Thursday", "10AM–7PM"], ["Friday", "10AM–7PM"], ["Saturday", "10AM–7PM"], ["Sunday", "11AM–6PM"], ["Monday", "10AM–7PM"], ["Tuesday", "10AM–7PM"], ["Wednesday", "10AM–7PM"]]', 'average_rating': 5.0}, {'name': 'White Barn Candle Co', 'hours': '[["Thursday", "10AM–9PM"], ["Friday", "10AM–9PM"], ["Saturday", "10AM–9PM"], ["Sunday", "11AM–7PM"], ["Monday", "10AM–9PM"], ["Tuesday", "10AM–9PM"], ["Wednesday", "10AM–9PM"]]', 'average_rating': 5.0}, {'name': 'Paradise tattoo', 'hours': '[["Thursday", "12–10PM"], ["Friday", "12PM–12AM"], ["Saturday", "12PM–12AM"], ["Sunday", "12–10PM"], ["Monday", "12–10PM"], ["Tuesday", "12–10PM"], ["Wednesday", "12–10PM"]]', 'average_rating': 4.96}]}

exec(code, env_args)
