code = """import json

with open(locals()['var_function-call-13827168507574417079'], 'r') as f:
    tracks_data = json.load(f)

keyword1 = "groove"
keyword2 = "matteson"

matches = []
for t in tracks_data:
    s = str(t).lower()
    if keyword1 in s or keyword2 in s:
        matches.append(t)

print("__RESULT__:")
print(json.dumps(matches[:20])) # Limit to 20"""

env_args = {'var_function-call-15720467439112676785': 'file_storage/function-call-15720467439112676785.json', 'var_function-call-13827168507574417079': 'file_storage/function-call-13827168507574417079.json', 'var_function-call-4873491316950649724': [{'rank': 1, 'key': ['none', ''], 'display': 'None by 幡谷尚史', 'revenue': 17150.55}, {'rank': 2, 'key': ['003', ''], 'display': '003-', 'revenue': 8582.15}, {'rank': 3, 'key': ['001', ''], 'display': '00-1', 'revenue': 7467.97}, {'rank': 4, 'key': ['004', ''], 'display': '004-/', 'revenue': 7271.32}, {'rank': 5, 'key': ['005', ''], 'display': '005', 'revenue': 6155.29}], 'var_function-call-391238844812898672': [{'rank': 1, 'key': ['003', ''], 'revenue': 8582.15, 'sample_title': '003-', 'sample_artist': ' ', 'num_tracks': 9}, {'rank': 2, 'key': ['001', ''], 'revenue': 7467.97, 'sample_title': '00-1', 'sample_artist': '[unknown]', 'num_tracks': 7}, {'rank': 3, 'key': ['004', ''], 'revenue': 7271.32, 'sample_title': '004-"" (, , , )', 'sample_artist': ' ', 'num_tracks': 8}, {'rank': 4, 'key': ['005', ''], 'revenue': 6155.29, 'sample_title': '005- ', 'sample_artist': ' ', 'num_tracks': 8}, {'rank': 5, 'key': ['groovey', 'rich matteson'], 'revenue': 5417.34, 'sample_title': 'Groovey', 'sample_artist': 'Rich Matteson', 'num_tracks': 4}, {'rank': 6, 'key': ['zo gaat het leven aan je voor', 'syb van der ploeg'], 'revenue': 5256.43, 'sample_title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'sample_artist': 'Syb van der Ploeg', 'num_tracks': 3}, {'rank': 7, 'key': ['009', ''], 'revenue': 5045.7, 'sample_title': '009-  ', 'sample_artist': ' ', 'num_tracks': 4}, {'rank': 8, 'key': ['002', ''], 'revenue': 5013.4400000000005, 'sample_title': '002-', 'sample_artist': ' ', 'num_tracks': 4}, {'rank': 9, 'key': ['vagga', 'ske'], 'revenue': 4981.380000000001, 'sample_title': 'Vagga', 'sample_artist': 'Ske', 'num_tracks': 3}, {'rank': 10, 'key': ['ki meil pahanu', ''], 'revenue': 4916.11, 'sample_title': 'Kiä meil pahanu? (Mina lätsi Siidile)', 'sample_artist': '[tiidmäldä]', 'num_tracks': 3}], 'var_function-call-7366206927427081119': [{'rank': 1, 'key': ['groovey', 'rich matteson'], 'revenue': 5417.34, 'title': 'Rich Matteson - Groovey', 'artist': 'None'}, {'rank': 2, 'key': ['zo gaat het leven aan je voor', 'syb van der ploeg'], 'revenue': 5256.43, 'title': 'Zo gaat het leven aan je voor (Hillich fjoer | Heilig vuur)', 'artist': 'Syb van der Ploeg'}, {'rank': 3, 'key': ['vagga', 'ske'], 'revenue': 4981.380000000001, 'title': 'Vagga (Feelings Are Great)', 'artist': 'Ske'}, {'rank': 4, 'key': ['emerge', 'fischerspooner'], 'revenue': 4896.24, 'title': 'Fischerspooner - Emerge (Dexter remix)', 'artist': 'None'}, {'rank': 5, 'key': ['best friends', 'hans zimmer'], 'revenue': 4806.24, 'title': 'Best Friends (Madagascar / Robots)', 'artist': 'Hans Zimmer'}]}

exec(code, env_args)
