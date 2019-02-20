# -*- coding:utf-8 -*-
import redis
import os
import json

r = redis.Redis(host='184.170.214.178', port=6379, db=0)

uid_list = os.listdir('./author_list')
for user_file in uid_list:
    uid = user_file.split('.')[0]
    r.sadd("uid_set", uid)

with open('author_idx.txt', 'r') as fp:
    idx = int(fp.read()) - 1
fp.close()

with open('author_list.json', 'r') as fp:
    # authors_dirs = ['https://scholar.google.com.hk/citations?user=HmyM5B8AAAAJ&hl=zh-CN&oi=sra']
    authors_dirs = json.loads(fp.read())
fp.close()

count = 0
# while idx < len(authors_dirs):
while idx < 500:
    uid = authors_dirs[idx].split('user=')[1].split('&')[0]
    count += 1
    idx += 1
    r.sadd("uid_set", uid)
print (count)

with open('author_idx.txt', 'r') as fp:
    idx = int(fp.read()) - 1
fp.close()

# while idx < len(authors_dirs):
while idx < 500:
    r.rpush("author_url_list", authors_dirs[idx])
    idx += 1



