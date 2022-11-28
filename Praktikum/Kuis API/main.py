import requests
from embedInput import *

#webhook link
webHook = 'https://discord.com/api/webhooks/1046081056782168175/bmTZXH4zbxn8_oyzb22-3LPy3AitVsWTJLJxgq90PMCrgy_GlRQlbqCVV271LKuc0BmV'

#class embed
embed = embedClass()

#input
content = str(input('content: ')); embed.setContent(content)
authorName = str(input('author name: ')); embed.setAuthorName(authorName)
title = str(input('title: ')); embed.setTitle(title)
desc = str(input('desc: ')); embed.setDesc(desc)

#set
# embed.setContent("Hello World!")
# embed.setAuthorName("Shalahuddin Abdul Aziz")
# embed.setTitle("Kuis API Prak. PI")
# embed.setDesc("2117051083")

#embeds input
data = {
    #webhook profile picture
    'avatar' : 'https://images.pexels.com/photos/15286/pexels-photo.jpg?auto=compress&cs=tinysrgb&dpr=1&w=500',
    'username' : 'Webhook',
    'content' : embed.getContent(),
    'embeds' : [{
        'thumbnail' : {
            'url' : 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/800px-Python-logo-notext.svg.png'
        },
        'author' : {
            'name' : embed.getAuthorName()
        },
        'title' : embed.getTitle(),
        'description' : embed.getDesc()
    }]
}

#post embed ke server
disc = requests.post(webHook, json=data)

#print status response
print(disc)