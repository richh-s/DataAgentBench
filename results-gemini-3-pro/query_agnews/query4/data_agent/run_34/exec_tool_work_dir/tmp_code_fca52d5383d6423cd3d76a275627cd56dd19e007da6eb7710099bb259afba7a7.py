code = """import json
import random

# Load metadata for 2015
with open(locals()['var_function-call-16836183799483844241'], 'r') as f:
    metadata = json.load(f)
    # metadata is a list of dicts: {"article_id": "13", "region": "Europe"}

# Load articles
with open(locals()['var_function-call-17656108898543788620'], 'r') as f:
    articles = json.load(f)
    # articles is a list of dicts: {"article_id": "13", "title": "...", "description": "..."}

# Create a dict for articles for fast lookup
# Normalize article_id to string
articles_map = {str(a['article_id']): a for a in articles}

# Join
joined = []
for m in metadata:
    aid = str(m['article_id'])
    if aid in articles_map:
        art = articles_map[aid]
        joined.append({
            "region": m['region'],
            "title": art.get('title', ''),
            "description": art.get('description', '')
        })

# Print sample
sample = random.sample(joined, 20) if len(joined) > 20 else joined
print("__RESULT__:")
print(json.dumps(sample))"""

env_args = {'var_function-call-4087601676422552917': ['authors', 'article_metadata'], 'var_function-call-4087601676422553258': ['articles'], 'var_function-call-16836183799483844241': 'file_storage/function-call-16836183799483844241.json', 'var_function-call-11996756743093828097': 'file_storage/function-call-11996756743093828097.json', 'var_function-call-8460452426655104065': {'min': 13, 'max': 127570, 'count': 6696}, 'var_function-call-17656108898543788620': [{'article_id': '13', 'title': 'Google IPO Auction Off to Rocky Start', 'description': " WASHINGTON/NEW YORK (Reuters) - The auction for Google  Inc.'s highly anticipated initial public offering got off to a  rocky start on Friday after the Web search company sidestepped  a bullet from U.S. securities regulators."}, {'article_id': '14', 'title': 'Dollar Falls Broadly on Record Trade Gap', 'description': " NEW YORK (Reuters) - The dollar tumbled broadly on Friday  after data showing a record U.S. trade deficit in June cast  fresh doubts on the economy's recovery and its ability to draw  foreign capital to fund the growing gap."}, {'article_id': '15', 'title': 'Rescuing an Old Saver', 'description': "If you think you may need to help your elderly relatives with their finances, don't be shy about having the money talk -- soon."}, {'article_id': '16', 'title': 'Kids Rule for Back-to-School', 'description': 'The purchasing power of kids is a big part of why the back-to-school season has become such a huge marketing phenomenon.'}, {'article_id': '17', 'title': 'In a Down Market, Head Toward Value Funds', 'description': "There is little cause for celebration in the stock market these days, but investors in value-focused mutual funds have reason to feel a bit smug -- if only because they've lost less than the folks who stuck with growth."}]}

exec(code, env_args)
