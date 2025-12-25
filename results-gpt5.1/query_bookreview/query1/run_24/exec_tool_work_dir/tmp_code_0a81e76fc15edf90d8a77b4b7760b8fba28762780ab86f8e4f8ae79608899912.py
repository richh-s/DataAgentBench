code = """import json, pandas as pd

# load review data
path_reviews = var_call_84741IAQnDTggqEcb887lfDm
with open(path_reviews, 'r') as f:
    reviews = json.load(f)

# load decade per book
path_decades = var_call_9xAR0Wav3JpGzZQDRkzb5Xiu
with open(path_decades, 'r') as f:
    decades = json.load(f)

# We'll assume purchase_id pattern 'purchaseid_N' corresponds to 'bookid_N'
for r in reviews:
    pid = r['purchase_id']
    if pid.startswith('purchaseid_'):
        num = pid.split('_')[1]
        r['book_id'] = f'bookid_{num}'
    else:
        r['book_id'] = None

# make dataframes
rev_df = pd.DataFrame(reviews)
rev_df['rating'] = pd.to_numeric(rev_df['rating'], errors='coerce')

dec_df = pd.DataFrame(decades)

merged = rev_df.merge(dec_df, on='book_id', how='left')

# group by decade and book to get book-level average
book_avg = merged.dropna(subset=['decade']).groupby(['decade','book_id'])['rating'].mean().reset_index(name='book_avg_rating')

# filter decades with at least 10 distinct books
dec_counts = book_avg.groupby('decade')['book_id'].nunique().reset_index(name='book_count')
valid_decades = dec_counts[dec_counts['book_count']>=10]['decade']

valid_book_avg = book_avg[book_avg['decade'].isin(valid_decades)]

# compute decade-level average of book averages
decade_avg = valid_book_avg.groupby('decade')['book_avg_rating'].mean().reset_index(name='decade_avg_rating')

# pick best decade
best_row = decade_avg.sort_values('decade_avg_rating', ascending=False).head(1)

if best_row.empty:
    result = None
else:
    decade = int(best_row.iloc[0]['decade'])
    result = f"{decade}s"

import json as _json
out = _json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_XmGrPfgZs7xQP3tCEsxhtYxP': 'file_storage/call_XmGrPfgZs7xQP3tCEsxhtYxP.json', 'var_call_Q33oo2x09EwxgliChtHzRuEp': ['books_info'], 'var_call_3EzG2U5B7dNHHDgjq1coF5Yo': ['review'], 'var_call_84741IAQnDTggqEcb887lfDm': 'file_storage/call_84741IAQnDTggqEcb887lfDm.json', 'var_call_9xAR0Wav3JpGzZQDRkzb5Xiu': 'file_storage/call_9xAR0Wav3JpGzZQDRkzb5Xiu.json', 'var_call_lrMcPZWkndsvgUYozkU5CRDi': [{'book_id': 'bookid_1'}, {'book_id': 'bookid_2'}, {'book_id': 'bookid_3'}, {'book_id': 'bookid_4'}, {'book_id': 'bookid_5'}, {'book_id': 'bookid_6'}, {'book_id': 'bookid_7'}, {'book_id': 'bookid_8'}, {'book_id': 'bookid_9'}, {'book_id': 'bookid_10'}, {'book_id': 'bookid_11'}, {'book_id': 'bookid_12'}, {'book_id': 'bookid_13'}, {'book_id': 'bookid_14'}, {'book_id': 'bookid_15'}, {'book_id': 'bookid_16'}, {'book_id': 'bookid_17'}, {'book_id': 'bookid_18'}, {'book_id': 'bookid_19'}, {'book_id': 'bookid_20'}, {'book_id': 'bookid_21'}, {'book_id': 'bookid_22'}, {'book_id': 'bookid_23'}, {'book_id': 'bookid_24'}, {'book_id': 'bookid_25'}, {'book_id': 'bookid_32'}, {'book_id': 'bookid_26'}, {'book_id': 'bookid_27'}, {'book_id': 'bookid_28'}, {'book_id': 'bookid_29'}, {'book_id': 'bookid_30'}, {'book_id': 'bookid_31'}, {'book_id': 'bookid_33'}, {'book_id': 'bookid_34'}, {'book_id': 'bookid_35'}, {'book_id': 'bookid_36'}, {'book_id': 'bookid_37'}, {'book_id': 'bookid_38'}, {'book_id': 'bookid_56'}, {'book_id': 'bookid_39'}, {'book_id': 'bookid_40'}, {'book_id': 'bookid_41'}, {'book_id': 'bookid_42'}, {'book_id': 'bookid_43'}, {'book_id': 'bookid_62'}, {'book_id': 'bookid_44'}, {'book_id': 'bookid_45'}, {'book_id': 'bookid_46'}, {'book_id': 'bookid_47'}, {'book_id': 'bookid_48'}, {'book_id': 'bookid_49'}, {'book_id': 'bookid_50'}, {'book_id': 'bookid_51'}, {'book_id': 'bookid_52'}, {'book_id': 'bookid_53'}, {'book_id': 'bookid_54'}, {'book_id': 'bookid_55'}, {'book_id': 'bookid_57'}, {'book_id': 'bookid_58'}, {'book_id': 'bookid_59'}, {'book_id': 'bookid_60'}, {'book_id': 'bookid_61'}, {'book_id': 'bookid_63'}, {'book_id': 'bookid_64'}, {'book_id': 'bookid_65'}, {'book_id': 'bookid_66'}, {'book_id': 'bookid_67'}, {'book_id': 'bookid_68'}, {'book_id': 'bookid_69'}, {'book_id': 'bookid_70'}, {'book_id': 'bookid_71'}, {'book_id': 'bookid_72'}, {'book_id': 'bookid_73'}, {'book_id': 'bookid_74'}, {'book_id': 'bookid_75'}, {'book_id': 'bookid_81'}, {'book_id': 'bookid_76'}, {'book_id': 'bookid_77'}, {'book_id': 'bookid_78'}, {'book_id': 'bookid_79'}, {'book_id': 'bookid_80'}, {'book_id': 'bookid_82'}, {'book_id': 'bookid_83'}, {'book_id': 'bookid_84'}, {'book_id': 'bookid_85'}, {'book_id': 'bookid_86'}, {'book_id': 'bookid_87'}, {'book_id': 'bookid_88'}, {'book_id': 'bookid_89'}, {'book_id': 'bookid_90'}, {'book_id': 'bookid_91'}, {'book_id': 'bookid_92'}, {'book_id': 'bookid_93'}, {'book_id': 'bookid_94'}, {'book_id': 'bookid_95'}, {'book_id': 'bookid_96'}, {'book_id': 'bookid_97'}, {'book_id': 'bookid_98'}, {'book_id': 'bookid_99'}, {'book_id': 'bookid_100'}, {'book_id': 'bookid_101'}, {'book_id': 'bookid_102'}, {'book_id': 'bookid_103'}, {'book_id': 'bookid_104'}, {'book_id': 'bookid_105'}, {'book_id': 'bookid_106'}, {'book_id': 'bookid_107'}, {'book_id': 'bookid_108'}, {'book_id': 'bookid_164'}, {'book_id': 'bookid_109'}, {'book_id': 'bookid_110'}, {'book_id': 'bookid_111'}, {'book_id': 'bookid_112'}, {'book_id': 'bookid_113'}, {'book_id': 'bookid_114'}, {'book_id': 'bookid_115'}, {'book_id': 'bookid_116'}, {'book_id': 'bookid_117'}, {'book_id': 'bookid_118'}, {'book_id': 'bookid_119'}, {'book_id': 'bookid_120'}, {'book_id': 'bookid_127'}, {'book_id': 'bookid_184'}, {'book_id': 'bookid_121'}, {'book_id': 'bookid_122'}, {'book_id': 'bookid_123'}, {'book_id': 'bookid_124'}, {'book_id': 'bookid_125'}, {'book_id': 'bookid_126'}, {'book_id': 'bookid_128'}, {'book_id': 'bookid_129'}, {'book_id': 'bookid_130'}, {'book_id': 'bookid_131'}, {'book_id': 'bookid_132'}, {'book_id': 'bookid_133'}, {'book_id': 'bookid_134'}, {'book_id': 'bookid_135'}, {'book_id': 'bookid_136'}, {'book_id': 'bookid_137'}, {'book_id': 'bookid_138'}, {'book_id': 'bookid_139'}, {'book_id': 'bookid_140'}, {'book_id': 'bookid_141'}, {'book_id': 'bookid_142'}, {'book_id': 'bookid_143'}, {'book_id': 'bookid_144'}, {'book_id': 'bookid_145'}, {'book_id': 'bookid_156'}, {'book_id': 'bookid_146'}, {'book_id': 'bookid_147'}, {'book_id': 'bookid_148'}, {'book_id': 'bookid_149'}, {'book_id': 'bookid_150'}, {'book_id': 'bookid_157'}, {'book_id': 'bookid_151'}, {'book_id': 'bookid_152'}, {'book_id': 'bookid_153'}, {'book_id': 'bookid_154'}, {'book_id': 'bookid_155'}, {'book_id': 'bookid_158'}, {'book_id': 'bookid_159'}, {'book_id': 'bookid_160'}, {'book_id': 'bookid_161'}, {'book_id': 'bookid_162'}, {'book_id': 'bookid_163'}, {'book_id': 'bookid_165'}, {'book_id': 'bookid_166'}, {'book_id': 'bookid_167'}, {'book_id': 'bookid_168'}, {'book_id': 'bookid_169'}, {'book_id': 'bookid_170'}, {'book_id': 'bookid_171'}, {'book_id': 'bookid_172'}, {'book_id': 'bookid_173'}, {'book_id': 'bookid_174'}, {'book_id': 'bookid_175'}, {'book_id': 'bookid_176'}, {'book_id': 'bookid_177'}, {'book_id': 'bookid_178'}, {'book_id': 'bookid_179'}, {'book_id': 'bookid_180'}, {'book_id': 'bookid_181'}, {'book_id': 'bookid_182'}, {'book_id': 'bookid_183'}, {'book_id': 'bookid_185'}, {'book_id': 'bookid_186'}, {'book_id': 'bookid_187'}, {'book_id': 'bookid_188'}, {'book_id': 'bookid_189'}, {'book_id': 'bookid_190'}, {'book_id': 'bookid_191'}, {'book_id': 'bookid_192'}, {'book_id': 'bookid_193'}, {'book_id': 'bookid_194'}, {'book_id': 'bookid_195'}, {'book_id': 'bookid_196'}, {'book_id': 'bookid_197'}, {'book_id': 'bookid_198'}, {'book_id': 'bookid_199'}, {'book_id': 'bookid_200'}]}

exec(code, env_args)
