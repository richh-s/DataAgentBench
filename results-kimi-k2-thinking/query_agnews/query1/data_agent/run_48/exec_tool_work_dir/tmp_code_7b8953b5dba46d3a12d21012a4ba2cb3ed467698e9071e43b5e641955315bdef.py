code = """import json
articles_file = locals()['var_functions.query_db:6']

# Read all articles data
with open(articles_file, 'r') as f:
    all_articles = json.load(f)

# Define very specific sports indicators
strong_sports_keywords = [
    # Professional sports leagues
    'nfl', 'nba', 'mlb', 'nhl', 'ncaa', 'major league', 'premier league',
    'world cup', 'super bowl', 'madden nfl', 'espn',
    
    # Specific sports with context
    'football game', 'basketball game', 'baseball game', 'soccer match',
    'tennis match', 'golf tournament',
    
    # Sports positions and roles
    'quarterback', 'pitcher', 'goalkeeper', 'coach', 'linebacker',
    'point guard', 'shortstop', 'forward', 
    
    # Sports events
    'championship', 'playoffs', 'finals', 'tournament', 'season',
    'game', 'match', 'race'
]

# Sports category words
sports_categories = ['football', 'basketball', 'baseball', 'soccer', 'hockey', 
                    'tennis', 'golf', 'cricket', 'rugby', 'boxing', 'wrestling',
                    'olympic', 'olympics']

def is_sports_article(title, description):
    """Strict check for sports articles"""
    title_lower = title.lower()
    desc_lower = description.lower()
    full_text = title_lower + ' ' + desc_lower
    
    # Count sports category mentions
    category_count = sum(1 for sport in sports_categories if sport in full_text)
    
    # Check for strong sports indicators
    strong_indicators = sum(1 for indicator in strong_sports_keywords if indicator in full_text)
    
    # Check if title contains sports-specific context
    sports_context = False
    sports_phrases = ['win', 'defeat', 'victory', 'champion', 'score', 'season', 'game', 'match',
                     'playoff', 'finals', 'coach', 'quarterback', 'pitcher', 'team', 'player']
    
    if any(phrase in title_lower for phrase in sports_phrases):
        sports_context = True
    
    # Must have at least 1 strong indicator OR (1 category and sports context)
    return strong_indicators >= 1 or (category_count >= 1 and sports_context)

sports_articles = []

for article in all_articles:
    title = article.get('title', '')
    description = article.get('description', '')
    
    if is_sports_article(title, description):
        sports_articles.append({
            'article_id': article.get('article_id', 'N/A'),
            'title': title,
            'description': description,
            'description_length': len(description)
        })

# Find the article with longest description
if sports_articles:
    longest_article = max(sports_articles, key=lambda x: x['description_length'])
    
    # Get top 15 for verification
    top_15 = sorted(sports_articles, key=lambda x: x['description_length'], reverse=True)[:15]
    
    print("__RESULT__:")
    print(json.dumps({
        'longest_sports_article': longest_article,
        'top_15_candidates': top_15,
        'total_sports_articles': len(sports_articles)
    }, ensure_ascii=False, indent=2))
else:
    print("__RESULT__:")
    print(json.dumps({'error': 'No sports articles found'}, ensure_ascii=False))"""

env_args = {'var_functions.query_db:0': 'file_storage/functions.query_db:0.json', 'var_functions.query_db:5': [{'_id': '696981f543fc64c07afdc7ac', 'article_id': '0', 'title': 'Wall St. Bears Claw Back Into the Black (Reuters)', 'description': "Reuters - Short-sellers, Wall Street's dwindling\\band of ultra-cynics, are seeing green again."}, {'_id': '696981f543fc64c07afdc7ad', 'article_id': '1', 'title': 'Carlyle Looks Toward Commercial Aerospace (Reuters)', 'description': 'Reuters - Private investment firm Carlyle Group,\\which has a reputation for making well-timed and occasionally\\controversial plays in the defense industry, has quietly placed\\its bets on another part of the market.'}, {'_id': '696981f543fc64c07afdc7ae', 'article_id': '2', 'title': "Oil and Economy Cloud Stocks' Outlook (Reuters)", 'description': 'Reuters - Soaring crude prices plus worries\\about the economy and the outlook for earnings are expected to\\hang over the stock market next week during the depth of the\\summer doldrums.'}, {'_id': '696981f543fc64c07afdc7af', 'article_id': '3', 'title': 'Iraq Halts Oil Exports from Main Southern Pipeline (Reuters)', 'description': 'Reuters - Authorities have halted oil export\\flows from the main pipeline in southern Iraq after\\intelligence showed a rebel militia could strike\\infrastructure, an oil official said on Saturday.'}, {'_id': '696981f543fc64c07afdc7b0', 'article_id': '4', 'title': 'Oil prices soar to all-time record, posing new menace to US economy (AFP)', 'description': 'AFP - Tearaway world oil prices, toppling records and straining wallets, present a new economic menace barely three months before the US presidential elections.'}], 'var_functions.query_db:6': 'file_storage/functions.query_db:6.json', 'var_functions.execute_python:8': 'file_storage/functions.execute_python:8.json', 'var_functions.execute_python:10': {'title': '2004 US Senate Outlook', 'article_id': '69024', 'description_length': 944, 'total_sports_articles_found': 16719}, 'var_functions.execute_python:12': 'file_storage/functions.execute_python:12.json', 'var_functions.execute_python:14': {'longest_article': {'article_id': '69024', 'title': '2004 US Senate Outlook', 'description': "With all the hoopla over Bush and Kerry, some of you may not have been paying close attention to the other races going on in this loaded US political season. I've read a good dozen or so Senate outlooks, and my blurry eyes and spinning brain kept getting lost in all the numbers and losing track of who, ultimately, was likely to control the Senate on November third. So I made my very own Senate outlook to figure it out (or add further confusion, depending on what you think of my predictions). The bad news is, we probably won't know who controls the Senate on November third. The good news, if you're a Democrat (or a person who loves one), is that my best guess at this point is that when the dust settles, Democrats will probably be in control by the very slimmest possible margin. Shock! But everyone knows the Dems have no chance of taking either house of Congress. I think everyone hasn't been paying attention. Read on for my rundown.", 'description_length': 944, 'sports_score': 3, 'indicators': ['track']}, 'top_10_candidates': [{'article_id': '69024', 'title': '2004 US Senate Outlook', 'description': "With all the hoopla over Bush and Kerry, some of you may not have been paying close attention to the other races going on in this loaded US political season. I've read a good dozen or so Senate outlooks, and my blurry eyes and spinning brain kept getting lost in all the numbers and losing track of who, ultimately, was likely to control the Senate on November third. So I made my very own Senate outlook to figure it out (or add further confusion, depending on what you think of my predictions). The bad news is, we probably won't know who controls the Senate on November third. The good news, if you're a Democrat (or a person who loves one), is that my best guess at this point is that when the dust settles, Democrats will probably be in control by the very slimmest possible margin. Shock! But everyone knows the Dems have no chance of taking either house of Congress. I think everyone hasn't been paying attention. Read on for my rundown.", 'description_length': 944, 'sports_score': 3, 'indicators': ['track']}, {'article_id': '31510', 'title': 'Cavaliers, Hokies Play Host', 'description': "Akron at No. 12 Virginia &lt;br&gt;   Where:  Scott Stadium, Charlottesville&lt;br&gt;   When:  3 p.m.    Radio:  WTNT-570    Tickets:  Sold out &lt;br&gt;   Another Top QB:  Like North Carolina's Darian Durant last week, Akron quarterback Charlie Frye is the key to his team's slim chances of upsetting the Cavaliers. The 6-foot-4 senior, likened by Virginia Coach Al Groh to recent ACC stars Matt Schaub and Philip Rivers, ranks fourth among active NCAA quarterbacks with 9,048 career passing yards. In losses the past two weeks to Penn State and Middle Tennessee, Frye completed 60 of 80 passes for 622 yards. Weather permitting, he will present a challenge for an inexperienced Virginia secondary that made a few too many errors in deep coverage in its first two games.", 'description_length': 773, 'sports_score': 10, 'indicators': ['ncaa', 'coach', 'quarterback', 'coach']}, {'article_id': '31509', 'title': 'Area College Football Capsules', 'description': 'Navy at Tulsa &lt;br&gt;   Where:  Skelly Stadium    When:  7 p.m. &lt;br&gt;   Shooting for 3-0:  Navy is off to its first 2-0 start since 1996. The Midshipmen haven\'t started 3-0 since 1979, when they won their first six games and finished 7-4. Navy has started 3-0 only twice in the past 40 years -- the 1978 team won its first seven games. Tulsa, which improved from 1-11 in 2002 to 8-5 last season, the best turnaround in college football, has lost its first two games, 21-3 at Kansas and 38-21 at Oklahoma State. Going 3-0 "would be a great start, and it would be a great beginning to achieve the goals that they\'ve set for themselves," Navy Coach Paul Johnson said. "It\'s not going to make the season if we win, and it\'s not going to kill it if we lose."', 'description_length': 761, 'sports_score': 11, 'indicators': ['football', 'season', 'coach', 'team', 'coach']}, {'article_id': '72244', 'title': "What Colorado's Amendment 36 means for America...", 'description': 'During the nineties, our state saw an increase in population, due to "The Californians" (who we like to bitch about) migrating to our low tax/low smog state.  Though most of us natives like to bitch about their supposedly shallow, urban sprawl, rude soccer mom, cell phone, and shopping mall ways, they have done something useful and actually turned us backwards hillbilly, gun toting, Republican loving rednecks into a swing state. Now we have to deal with traffic on I-25 being snarled for hours whenever Dick Cheney decides to send his motorcade through rush hour.  The most important issue on the ballot in our state is Amendment 36, which would change our electoral voting from "winner takes all" to a proportional voting system.  ', 'description_length': 736, 'sports_score': 6, 'indicators': ['soccer', 'soccer']}, {'article_id': '46531', 'title': 'Ex-Astronaut Casts Doubt on Space Tourism', 'description': 'PRAGUE, Czech Republic -- Eugene Cernan, the last man to walk on the moon during the final Apollo landing, said Thursday he doesn\'t expect space tourism to become reality in the near future, despite a strong demand.   Cernan, now 70, who was commander of NASA\'s Apollo 17 mission and set foot on the lunar surface in December 1972 during his third space flight, acknowledged that "there are many people interested in space tourism."     But the former astronaut said he believed "we are a long way away from the day when we can send a bus of tourists to the moon." He spoke to reporters before being awarded a medal by the Czech Academy of Sciences for his contribution to science...', 'description_length': 683, 'sports_score': 3, 'indicators': ['medal']}, {'article_id': '89533', 'title': 'Tressel Trailed by Allegations', 'description': "Oh, if only the biggest problems in Columbus, Ohio, were how the Buckeyes might get their running game going and beat Purdue today. Not so. In a pair of stories -- one in ESPN the Magazine, the other on ESPN.com -- Ohio State Coach    Jim Tressel  was first accused by former star running back Maurice Clarett of helping him gain access to free cars and of hooking him up with boosters for cash payments. The second story traced such scams back to Tressel's days as the coach at Youngstown State, in Clarett's home town. Ohio State's response to Clarett: He's a liar, and he's lying. Suddenly, though, the Boilermakers aren't Tressel's most daunting opponent.", 'description_length': 659, 'sports_score': 5, 'indicators': ['coach', 'game', 'coach']}, {'article_id': '6968', 'title': 'THECHAT', 'description': '&lt;em&gt; Dean Cain has spent much of his life in a uniform. He\'s done time as an all-American safety at Princeton (where he established a since-broken single-season Division I-AA record for interceptions), an undrafted free agent with the Buffalo Bills (before a preseason knee injury ended his football career), a sportsman of the future (in the aptly named movie "Futuresport") and an iconic superhero (in television\'s "Lois and Clark: The New Adventures of Superman"). Next up is a set of pinstripes -- Cain plays star third baseman Conrad Dean in the CBS drama "Clubhouse," which is scheduled to debut next month. &lt;/em&gt;', 'description_length': 631, 'sports_score': 3, 'indicators': ['football']}, {'article_id': '89534', 'title': 'Croissants, Coffee and a Kickoff', 'description': 'When the alarm goes off today for the players at Boise State and San Jose State, they\'ll yawn, stretch and mutter something like, "It must be noon somewhere." Think television is an innocent bystander in college sports? If so, hit the snooze button. The Broncos and Spartans will kick off their Western Athletic Conference tilt at 9:02 a.m. Pacific Time, for the benefit of ESPN2. To adjust, Boise State Coach Dan Hawkins has had the team up at 5 a.m. all week. "We\'re used to having to play whenever ESPN wants to cover it," Boise State\'s    Daryn Colledge  told the Idaho Statesman. Ah, the purity of college athletics.', 'description_length': 621, 'sports_score': 5, 'indicators': ['coach', 'team', 'coach']}, {'article_id': '31513', 'title': 'The Rundown', 'description': '5 LSU at 14 Auburn  3:30 p.m., WUSA-9, WJZ-13 &lt;br&gt;Don\'t expect a resolution to LSU\'s quarterback controversy, which pits freshman JaMarcus Russell against senior Marcus Randall. "My view is that both quarterbacks can be weapons for our team," LSU Coach Nick Saban said. No such controversy in Auburn\'s backfield, where Carnell Williams and Ronnie Brown are both averaging more than 100 rushing yards per game. Hurricane Ivan, of course, is raging in the South. But so is Auburn, which remembers the 31-7 thrashing at the hands of LSU last season. The winner of this game will be the favorite in the SEC West.', 'description_length': 614, 'sports_score': 8, 'indicators': ['coach', 'quarterback', 'game', 'coach']}, {'article_id': '9003', 'title': 'Online Music Goes Back to School (washingtonpost.com)', 'description': "washingtonpost.com - In this era of high-speed Internet access, the back-to-school season features college students streaming back into their broadband-wired dormitory rooms, booting up their computers and letting gigabytes of digital tunes flow like a waterfall -- and for many students, the question of whether the downloading violates copyright laws plays second fiddle. However, a legal, affordable alternative has a chance to thrive in this potentially huge market, or at least that's what the digital music business and the universities are hoping.", 'description_length': 554, 'sports_score': 3, 'indicators': ['season']}], 'total_sports_articles': 12424}}

exec(code, env_args)
