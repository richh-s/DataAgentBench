code = """import json, re
# Load variables from storage
books_file = var_call_UU1AWfEZMBJtrCVmaPoVyEc5
reviews = var_call_2wlsMthvCIKzPfotz3LJJAU6

# Read full books data from file path
with open(books_file, 'r') as f:
    books = json.load(f)

# Build review map by numeric id
rev_map = {}
for r in reviews:
    pid = r.get('purchase_id','')
    m = re.search(r"(\d+)$", pid)
    if m:
        num = m.group(1)
        rev_map[num] = {'purchase_id': pid, 'avg_rating': float(r.get('avg_rating',0)), 'n_reviews': int(r.get('n_reviews',0))}

matches = []
for b in books:
    bid = b.get('book_id','')
    m = re.search(r"(\d+)$", bid)
    if not m:
        continue
    num = m.group(1)
    if num not in rev_map:
        continue
    # check english language in details or description
    details = (b.get('details') or '')
    description = ''
    try:
        desc = b.get('description')
        if isinstance(desc, list):
            description = ' '.join(desc)
        else:
            description = str(desc)
    except Exception:
        description = str(b.get('description',''))
    text = (details + ' ' + description).lower()
    if 'english' in text:
        # parse author
        author_raw = b.get('author')
        author_name = None
        if isinstance(author_raw, str):
            try:
                parsed = json.loads(author_raw)
                if isinstance(parsed, dict):
                    author_name = parsed.get('name')
                else:
                    author_name = author_raw
            except Exception:
                author_name = author_raw
        else:
            author_name = author_raw
        try:
            rating_number = int(b.get('rating_number'))
        except Exception:
            rating_number = b.get('rating_number')
        try:
            price = float(b.get('price'))
        except Exception:
            price = b.get('price')
        matches.append({
            'book_id': bid,
            'title': b.get('title'),
            'author': author_name,
            'rating_number': rating_number,
            'price': price,
            'avg_rating': rev_map[num]['avg_rating'],
            'n_reviews': rev_map[num]['n_reviews'],
            'categories': b.get('categories'),
            'details': b.get('details')
        })

print('__RESULT__:')
print(json.dumps(matches))"""

env_args = {'var_call_sO3Tmm0I7H4FDuQjVCjyHrNf': ['review'], 'var_call_fI6gok46YruWoC4Co6kZSr21': 'file_storage/call_fI6gok46YruWoC4Co6kZSr21.json', 'var_call_wsqlXjJaM2D50pADObUecib8': ['books_info'], 'var_call_HmeQqjiITeWXgSfmV1K5hCe9': [{'book_id': 'bookid_179', 'title': 'A Cherry Cola Christmas (A Cherry Cola Book Club Novel)', 'author': '{"avatar": "https://m.media-amazon.com/images/I/21xw6GAunVL._SY600_.jpg", "name": "Ashton Lee", "about": ["Discover more of the author’s books, see similar authors, read author blogs and more"]}', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '64', 'price': '5.64', 'description': '["Review", "“The challenges of keeping any library anywhere open and effectively serving its patrons is a problem facing most communities. Lee brings these salient topics to light in an unpredictably entertaining series.”--", "Booklist", "“If\xa0Fannie\xa0Flagg\xa0and\xa0Jan\xa0Karon’s\xa0Mitford\xa0were\xa0to\xa0come\xa0together,\xa0the\xa0end\xa0result\xa0might\xa0very\xa0well be\xa0Cherico,\xa0Mississippi.\\"--Michael\xa0Morris,\xa0author\xa0of", "Man\xa0in\xa0the\xa0Blue\xa0Moon", "About the Author", "Ashton Lee", "was born in historic Natchez, Mississippi, into a large, extended Southern family which gave him much fodder for his fiction later in life.\xa0His father, who wrote under the pen name of R. Keene Lee right after WWII, was an editor and writer in New York of what is now called pulp fiction. As a result, Ashton inherited a love of\xa0reading and writing early on and did all the things aspiring authors are supposed to do, including majoring in English when he attended The University of the South, affectionately known as Sewanee.\xa0While there, he studied Creative Writing under Andrew Lytle, then editor of the", "Sewanee Review", ", and a member of the Southern Agrarians in the 1920s.Ashton lives in Oxford, MS", ",", "enjoying the amenities of a university town that many writers have called hom", "e.", "Readers can like Ashton Lee at: facebook.com/ashtonlee.net."]'}, {'book_id': 'bookid_188', 'title': "The Vampyre and Other Tales of the Macabre (Oxford World's Classics)", 'author': '{"avatar": "https://m.media-amazon.com/images/I/A14eOK33ILL._SY600_.jpg", "name": "Robert Morrison", "about": ["Robert Morrison studied at the University of Lethbridge; the University of Oxford; and the University of Edinburgh. Currently he is British Academy Global Professor at Bath Spa University and Queen\'s National Scholar at Queen\'s University in Kingston, Ontario. He specializes in nineteenth-century British literature and culture.", "His most recent book, The Regency Years, During Which Jane Austen Writes, Napoleon Fights, Byron Makes Love and Britain Becomes Modern (2019), was longlisted for the RBC Taylor Prize, and named by The Economist as a Book of the Year. His biography of Thomas De Quincey, The English Opium-Eater (2009), was shortlisted for the James Tait Black Prize. Morrison published Thomas De Quincey: Selected Writings in the 21st-Century Oxford Authors series (2019). His annotated edition of Jane Austen\'s Persuasion was published by Harvard University Press (2011). With Daniel Sanjiv Roberts, he edited Romanticism and Blackwood\'s Magazine: \\"An Unprecedented Phenomenon\\" (2013) and Thomas De Quincey: New Theoretical and Critical Directions (2008). With Chris Baldick, he edited The Vampyre and Other Tales of the Macabre (1997) and Tales of Terror from Blackwood’s Magazine (1995) for Oxford World\'s Classics."]}', 'categories': '["Books", "Literature & Fiction", "Genre Fiction"]', 'rating_number': '162', 'price': '9.95', 'description': '["Review", "`Moving effortlessly from folklore to melodrama, the Introduction assesses the position that Polidori\'s story . . . We may not be ableto recover the experience of the origianl readers, but we can be grateful to the editors for bringing back to life tales that are not only of academic interest but which still exert their own nightmarish fascination\' Studies in Hogg and his World", "About the Author", "Chris Baldick is Head of English at Goldsmith\'s College, University of London. Robert Morrison is Associate Professor of English at Acadia University, Canada."]'}], 'var_call_2wlsMthvCIKzPfotz3LJJAU6': [{'purchase_id': 'purchaseid_101', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_105', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_108', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_110', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_114', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_116', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_117', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_118', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_12', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_121', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_122', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_123', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_124', 'avg_rating': '5.0', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_126', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_127', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_128', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_130', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_132', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_133', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_134', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_14', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_143', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_144', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_146', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_150', 'avg_rating': '5.0', 'n_reviews': '11'}, {'purchase_id': 'purchaseid_151', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_152', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_153', 'avg_rating': '5.0', 'n_reviews': '15'}, {'purchase_id': 'purchaseid_156', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_16', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_160', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_163', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_166', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_168', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_170', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_171', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_172', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_174', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_177', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_180', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_181', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_182', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_184', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_192', 'avg_rating': '5.0', 'n_reviews': '6'}, {'purchase_id': 'purchaseid_195', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_197', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_2', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_21', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_24', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_26', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_28', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_29', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_33', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_34', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_38', 'avg_rating': '5.0', 'n_reviews': '4'}, {'purchase_id': 'purchaseid_39', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_40', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_41', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_42', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_47', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_54', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_56', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_57', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_59', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_6', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_60', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_64', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_7', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_71', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_73', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_74', 'avg_rating': '5.0', 'n_reviews': '8'}, {'purchase_id': 'purchaseid_75', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_79', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_80', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_82', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_83', 'avg_rating': '5.0', 'n_reviews': '14'}, {'purchase_id': 'purchaseid_84', 'avg_rating': '5.0', 'n_reviews': '2'}, {'purchase_id': 'purchaseid_88', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_9', 'avg_rating': '5.0', 'n_reviews': '3'}, {'purchase_id': 'purchaseid_90', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_91', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_97', 'avg_rating': '5.0', 'n_reviews': '1'}, {'purchase_id': 'purchaseid_98', 'avg_rating': '5.0', 'n_reviews': '1'}], 'var_call_OjhxvgPCMIrQTYavSIgF5CAI': [], 'var_call_hfsSBxA2uwpyDFeugySy2HRF': ['2', '6', '7', '9', '12', '14', '16', '21', '24', '26', '28', '29', '33', '34', '38', '39', '40', '41', '42', '47', '54', '56', '57', '59', '60', '64', '71', '73', '74', '75', '79', '80', '82', '83', '84', '88', '90', '91', '97', '98', '101', '105', '108', '110', '114', '116', '117', '118', '121', '122', '123', '124', '126', '127', '128', '130', '132', '133', '134', '143', '144', '146', '150', '151', '152', '153', '156', '160', '163', '166', '168', '170', '171', '172', '174', '177', '180', '181', '182', '184', '192', '195', '197'], 'var_call_UU1AWfEZMBJtrCVmaPoVyEc5': 'file_storage/call_UU1AWfEZMBJtrCVmaPoVyEc5.json'}

exec(code, env_args)
