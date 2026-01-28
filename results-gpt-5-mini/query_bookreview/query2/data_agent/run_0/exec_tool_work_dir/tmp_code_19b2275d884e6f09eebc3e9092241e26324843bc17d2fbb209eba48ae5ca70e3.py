code = """import json, re
# load large books result from file path stored in var_call_PLO1MR3ex0cOlNNucsDcCGJP
path = var_call_PLO1MR3ex0cOlNNucsDcCGJP
with open(path, 'r', encoding='utf-8') as f:
    books = json.load(f)
reviews = var_call_NaaAh63krvjYB3TGmwxytVBG
# build set of purchase ids with avg_rating==5.0
purchase_set = {r['purchase_id']: {'avg_rating': float(r['avg_rating']), 'n_reviews': int(r['n_reviews'])} for r in reviews}

matches = []
for b in books:
    cat = (b.get('categories') or '')
    title = (b.get('title') or '')
    author = b.get('author')
    # normalize
    cat_low = cat.lower()
    title_low = title.lower()
    author_low = (author or '').lower()
    # check Literature & Fiction in categories
    if 'literature & fiction' not in cat_low:
        continue
    # check English-language: look in categories, title, author
    english = False
    if 'english' in cat_low or 'english' in title_low or 'english' in author_low:
        english = True
    # also check for patterns like 'english edition' or '(english' in title
    if not english and ('english edition' in title_low or '(english' in title_low or 'english &' in cat_low):
        english = True
    if not english:
        # also check details: sometimes categories empty but title includes 'English'
        pass
    if not english:
        continue
    # map book_id numeric suffix to purchaseid
    bid = b.get('book_id','')
    m = re.search(r"(\d+)$", bid)
    if not m:
        continue
    pid = f"purchaseid_{m.group(1)}"
    if pid not in purchase_set:
        continue
    rec = {
        'book_id': bid,
        'title': title,
        'author': author,
        'categories': cat,
        'rating_number': int(b.get('rating_number')) if b.get('rating_number') and str(b.get('rating_number')).isdigit() else b.get('rating_number'),
        'price': float(b.get('price')) if b.get('price') not in (None, '') else None,
        'avg_rating': purchase_set[pid]['avg_rating'],
        'n_reviews': purchase_set[pid]['n_reviews']
    }
    matches.append(rec)

# print result as JSON string
print("__RESULT__:")
print(json.dumps(matches))"""

env_args = {'var_call_7xdegr1cAunuSNUtaXQQHOyo': ['review'], 'var_call_NaaAh63krvjYB3TGmwxytVBG': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'n_reviews': '11'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'n_reviews': '15'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'n_reviews': '8'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'n_reviews': '14'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0', 'n_reviews': '1'}], 'var_call_C00Lagt0yhOC8PByxGQ3SqaK': ['books_info'], 'var_call_NJIff2G57hVHnp67zLFU8ByE': [], 'var_call_Cuz7fBNcYkAonui36GNggvVs': "SELECT book_id, title, author, categories, rating_number, price FROM books_info WHERE book_id LIKE '%101%' OR book_id LIKE '%105%' OR book_id LIKE '%108%' OR book_id LIKE '%110%' OR book_id LIKE '%114%' OR book_id LIKE '%116%' OR book_id LIKE '%117%' OR book_id LIKE '%118%' OR book_id LIKE '%12%' OR book_id LIKE '%121%' OR book_id LIKE '%122%' OR book_id LIKE '%123%' OR book_id LIKE '%124%' OR book_id LIKE '%126%' OR book_id LIKE '%127%' OR book_id LIKE '%128%' OR book_id LIKE '%130%' OR book_id LIKE '%132%' OR book_id LIKE '%133%' OR book_id LIKE '%134%' OR book_id LIKE '%14%' OR book_id LIKE '%143%' OR book_id LIKE '%144%' OR book_id LIKE '%146%' OR book_id LIKE '%150%' OR book_id LIKE '%151%' OR book_id LIKE '%152%' OR book_id LIKE '%153%' OR book_id LIKE '%156%' OR book_id LIKE '%16%' OR book_id LIKE '%160%' OR book_id LIKE '%163%' OR book_id LIKE '%166%' OR book_id LIKE '%168%' OR book_id LIKE '%170%' OR book_id LIKE '%171%' OR book_id LIKE '%172%' OR book_id LIKE '%174%' OR book_id LIKE '%177%' OR book_id LIKE '%180%' OR book_id LIKE '%181%' OR book_id LIKE '%182%' OR book_id LIKE '%184%' OR book_id LIKE '%192%' OR book_id LIKE '%195%' OR book_id LIKE '%197%' OR book_id LIKE '%2%' OR book_id LIKE '%21%' OR book_id LIKE '%24%' OR book_id LIKE '%26%' OR book_id LIKE '%28%' OR book_id LIKE '%29%' OR book_id LIKE '%33%' OR book_id LIKE '%34%' OR book_id LIKE '%38%' OR book_id LIKE '%39%' OR book_id LIKE '%40%' OR book_id LIKE '%41%' OR book_id LIKE '%42%' OR book_id LIKE '%47%' OR book_id LIKE '%54%' OR book_id LIKE '%56%' OR book_id LIKE '%57%' OR book_id LIKE '%59%' OR book_id LIKE '%6%' OR book_id LIKE '%60%' OR book_id LIKE '%64%' OR book_id LIKE '%7%' OR book_id LIKE '%71%' OR book_id LIKE '%73%' OR book_id LIKE '%74%' OR book_id LIKE '%75%' OR book_id LIKE '%79%' OR book_id LIKE '%80%' OR book_id LIKE '%82%' OR book_id LIKE '%83%' OR book_id LIKE '%84%' OR book_id LIKE '%88%' OR book_id LIKE '%9%' OR book_id LIKE '%90%' OR book_id LIKE '%91%' OR book_id LIKE '%97%' OR book_id LIKE '%98%';", 'var_call_PLO1MR3ex0cOlNNucsDcCGJP': 'file_storage/call_PLO1MR3ex0cOlNNucsDcCGJP.json'}

exec(code, env_args)
