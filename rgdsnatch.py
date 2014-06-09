#!/usr/local/bin/python

# <markdowncell>

# rgdsnatch: Reddit script to get posts and data from RedditGetsDrawn and post to artcontroldrawsyou

# <codecell>

import os
import random
import requests
import re
import json
import praw

# <codecell>

os.chdir('/home/wcmckee/rgd')

# <codecell>

r = praw.Reddit(user_agent='rgdsnatch')

# <codecell>

r.login('artcontrol', 'test123')

# <codecell>

rd = r.get_subreddit('redditgetsdrawn')

# <codecell>

rdnewz = rd.get_new()

# <codecell>

rdnew = []

# <codecell>

for uz in rdnewz:
    #print uz
    rdnew.append(uz)

# <codecell>

rd.get_top

# <codecell>

linkdict = {}

# <codecell>

for newa in rdnew:
    #rint newa.url
    #print newa.author
    linkdict.update({str(newa.author): str(newa.url)})

# <codecell>

import json

# <codecell>

newzjson = json.dumps(linkdict)

# <codecell>

newzjson

# <codecell>


# <codecell>

newposts = open('userurl.json', 'a')
newposts.write(newzjson)
print 'file userurl.json updated'
newposts.close()

# <codecell>


