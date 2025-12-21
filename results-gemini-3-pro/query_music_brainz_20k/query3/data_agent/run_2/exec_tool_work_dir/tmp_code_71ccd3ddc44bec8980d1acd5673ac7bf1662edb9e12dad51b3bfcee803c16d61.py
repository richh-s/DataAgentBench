code = """import json
import re

# Load data
with open(locals()['var_function-call-10663605738424963180'], 'r') as f:
    sales_data = json.load(f)
with open(locals()['var_function-call-10663605738424965213'], 'r') as f:
    tracks_data = json.load(f)

sales_map = {}
for s in sales_data:
    tid = str(s['track_id'])
    rev = float(s['total_revenue']) if s['total_revenue'] else 0.0
    sales_map[tid] = rev

target_normalized_titles = ['lifework', 'groovey', 'na']

debug_info = {k: [] for k in target_normalized_titles}

def normalize_text(text):
    if not text or text.lower() in ['none', 'unknown', '[unknown]']:
        return ""
    text = text.lower()
    text = re.sub(r'\([^)]*\)', '', text)
    text = re.sub(r'\[[^]]*\]', '', text)
    text = re.sub(r'[^\w\s]', '', text, flags=re.UNICODE)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

for t in tracks_data:
    tid = str(s['track_id']) # Wait, loop variable is t
    tid = str(t['track_id'])
    
    raw_title = t['title']
    raw_artist = t['artist']
    
    # Same splitting logic for consistency
    if (not raw_artist or str(raw_artist).lower() in ['none', 'unknown', '[unknown]']):
        if raw_title and ' - ' in raw_title:
            parts = raw_title.split(' - ', 1)
            p0 = parts[0].strip()
            p1 = parts[1].strip()
            if re.match(r'^\d+$', p0):
                raw_title = p1
            else:
                raw_artist = p0
                raw_title = p1
        elif raw_title and re.match(r'^\d+-\s*', raw_title):
             cleaned = re.sub(r'^\d+-\s*', '', raw_title)
             raw_title = cleaned

    n_title = normalize_text(raw_title)
    
    if n_title in target_normalized_titles:
        debug_info[n_title].append({
            "raw_title": t['title'],
            "raw_artist": t['artist'],
            "computed_raw_title": raw_title,
            "computed_raw_artist": raw_artist,
            "revenue": sales_map.get(tid, 0.0)
        })

print("__RESULT__:")
print(json.dumps(debug_info))"""

env_args = {'var_function-call-10663605738424963180': 'file_storage/function-call-10663605738424963180.json', 'var_function-call-10663605738424965213': 'file_storage/function-call-10663605738424965213.json', 'var_function-call-10167274036622288126': {'title': '003-', 'artist': 'None', 'revenue_usd': 8582.15, 'normalized_key': ['003', '']}, 'var_function-call-18198350123033394744': [{'key': ['003', ''], 'revenue': 8582.15, 'sample_titles': ['003-', '003-', '003-', '003-,  ', '003-'], 'sample_artists': ['None', ' ', 'None', 'None', 'None'], 'count': 9}, {'key': ['001', ''], 'revenue': 7467.97, 'sample_titles': ['00-1', '00-1', '001-', '001-', '001-'], 'sample_artists': ['None', '[unknown]', 'None', 'None', 'None'], 'count': 7}, {'key': ['004', ''], 'revenue': 7271.32, 'sample_titles': ['004-/', '004-"" (, , , )', '004- ', '004-', '004-'], 'sample_artists': ['None', ' ', ' ', '    ""', 'None'], 'count': 8}, {'key': ['005', ''], 'revenue': 6155.29, 'sample_titles': ['005', '005-', '005- ', '005-    ', '005- '], 'sample_artists': ['None', 'None', ' ', ' ', ' '], 'count': 8}, {'key': ['groovey', 'rich matteson'], 'revenue': 5417.34, 'sample_titles': ['Groovey', 'Groovey', 'Groovey', 'Groovey'], 'sample_artists': ['Rich Matteson', 'Rich Matteson', 'Rich Matteson', 'Rich Matteson'], 'count': 4}, {'key': ['zo gaat het leven aan je voor', 'syb van der ploeg'], 'revenue': 5256.43, 'sample_titles': ['Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'Zo gaat het leven aan je voor', 'Zo gaat het leven aan je voor'], 'sample_artists': ['Syb van der Ploeg', 'Syb van der Ploeg', 'Syb van der Ploeg'], 'count': 3}, {'key': ['009', ''], 'revenue': 5045.7, 'sample_titles': ['009-  ', '009-   ', '009-', '009- '], 'sample_artists': [' ', 'None', 'None', ' '], 'count': 4}, {'key': ['002', ''], 'revenue': 5013.4400000000005, 'sample_titles': ['002-', '002', '002-', '002-'], 'sample_artists': ['None', 'None', ' ', 'None'], 'count': 4}, {'key': ['vagga', 'ske'], 'revenue': 4981.380000000001, 'sample_titles': ['Vagga', 'Vagga', 'Vagga (Feelings Are Great)'], 'sample_artists': ['Ske', 'Ske', 'Ske'], 'count': 3}, {'key': ['ki meil pahanu', ''], 'revenue': 4916.11, 'sample_titles': ['Kiä meil pahanu?', 'Kiä meil pahanu? (Mina lätsi Siidile)', 'Kiä meil pahanu'], 'sample_artists': ['[tiidmäldä]', '[tiidmäldä]', '[tiidmäldä]'], 'count': 3}], 'var_function-call-612826103142165320': [{'key': ['lifework', ''], 'revenue': 5504.94, 'sample_titles': ['Lifework', 'Lifework (HERO -Original Sound Track)', 'Lifework', 'Lifework'], 'sample_artists': ['None', '服部隆之', '服部隆之', '服部隆之'], 'count': 4}, {'key': ['groovey', 'rich matteson'], 'revenue': 5417.34, 'sample_titles': ['Groovey', 'Groovey', 'Groovey', 'Groovey'], 'sample_artists': ['Rich Matteson', 'Rich Matteson', 'Rich Matteson', 'Rich Matteson'], 'count': 4}, {'key': ['zo gaat het leven aan je voor', 'syb van der ploeg'], 'revenue': 5256.43, 'sample_titles': ['Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'Zo gaat het leven aan je voor', 'Zo gaat het leven aan je voor'], 'sample_artists': ['Syb van der Ploeg', 'Syb van der Ploeg', 'Syb van der Ploeg'], 'count': 3}, {'key': ['vagga', 'ske'], 'revenue': 4981.380000000001, 'sample_titles': ['Vagga', 'Vagga', 'Vagga (Feelings Are Great)'], 'sample_artists': ['Ske', 'Ske', 'Ske'], 'count': 3}, {'key': ['ki meil pahanu', ''], 'revenue': 4916.11, 'sample_titles': ['Kiä meil pahanu?', 'Kiä meil pahanu? (Mina lätsi Siidile)', 'Kiä meil pahanu'], 'sample_artists': ['[tiidmäldä]', '[tiidmäldä]', '[tiidmäldä]'], 'count': 3}, {'key': ['emerge', 'fischerspooner'], 'revenue': 4896.24, 'sample_titles': ['Emerge (Dexter remix)', 'Emerge (Dexter remix) (#1)', 'Emerge (Dave Clarke remix)', 'Emerge (Dexter remix)'], 'sample_artists': ['Fischerspooner', 'Fischerspooner', 'Fischerspooner', 'Fischerspooner'], 'count': 4}, {'key': ['best friends', 'hans zimmer'], 'revenue': 4806.24, 'sample_titles': ['Best Friends', 'Best Friends (Madagascar / Robots)', 'Best Friends'], 'sample_artists': ['Hans Zimmer', 'Hans Zimmer', 'Hans Zimmer'], 'count': 3}, {'key': ['letters a short essay', 'echolyn'], 'revenue': 4694.76, 'sample_titles': ['Letters A Short Essay (As the World)', 'Letters: A Short Essay', 'Letters: A Short Essay'], 'sample_artists': ['echolyn', 'echolyn', 'echolyn'], 'count': 3}, {'key': ['ne veruj', 'vrisak generacije'], 'revenue': 4693.259999999999, 'sample_titles': ['Ne veruj (Beer Drinkers Revenge)', 'Ne veruj', 'Ne veruj'], 'sample_artists': ['Vrisak generacije', 'Vrisak generacije', 'Vrisak generacije'], 'count': 3}, {'key': ['travel', 'guts pie earshot'], 'revenue': 4595.34, 'sample_titles': ['Travel (live) (amparo fugaz)', 'Travel (live)', 'Travel (live)'], 'sample_artists': ['Guts Pie Earshot', 'Guts Pie Earshot', 'Guts Pie Earshot'], 'count': 3}], 'var_function-call-7702281503212453936': [{'key': ['lifework', '服部隆之'], 'revenue': 5504.9400000000005}, {'key': ['groovey', 'rich matteson'], 'revenue': 5417.34}, {'key': ['zo gaat het leven aan je voor', 'syb van der ploeg'], 'revenue': 5256.43}, {'key': ['na', 'ludwig van beethoven'], 'revenue': 5042.32}, {'key': ['vagga', 'ske'], 'revenue': 4981.38}, {'key': ['kiä meil pahanu', ''], 'revenue': 4916.110000000001}, {'key': ['emerge', 'fischerspooner'], 'revenue': 4896.240000000001}, {'key': ['best friends', 'hans zimmer'], 'revenue': 4806.24}, {'key': ['intro', 'earl zinger'], 'revenue': 4771.3}, {'key': ['letters a short essay', 'echolyn'], 'revenue': 4694.76}]}

exec(code, env_args)
