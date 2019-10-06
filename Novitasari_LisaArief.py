# ILMU KOMPUTER 2018 UNJ
# ASSIGNMENT 3
# NOVITASARI (1313618033)
# LISA ARIEF (1313618033)

import instaloader
import pandas as pd
import time

username = "budi_subagja17"
L = instaloader.Instaloader(max_connection_attempts=0)
L.login("ghost.toon", "nagasakure")

profile = instaloader.Profile.from_username(L.context, username)

usernamelist = []
captionlist = []
hashtaglist = []
likeslist = []
commentlist = []
followerlist = []

count = 1
for post in profile.get_posts():
        print("Data dari " + username + ", postingan ke " + str(count) + " dari " + str(profile.mediacount) + ".")
        caption = post.caption
        if caption is None:
            caption = ""
        if caption is not None:
            caption = caption.encode('ascii', 'ignore').decode('ascii')
        hashtag = post.caption_hashtags
        likes = post.likes
        
        comments = []
        for comment in post.get_comments() :
            comments.append(comment.text.encode('ascii', 'ignore').decode('ascii'))

        usernamelist.append(username)
        captionlist.append(caption)
        hashtaglist.append(hashtag)
        likeslist.append(likes)
        commentlist.append(comments)
        count = count+1

followers = []
count_account = 1
for follower in profile.get_followers():
    username_follower = follower.username
    profile_follower = instaloader.Profile.from_username(L.context, username_follower)
    if profile_follower.is_private == True:
        print(username_follower + " tidak bisa diakses karena akun di Private.")
    count = 1
    for post in profile_follower.get_posts():
        print("Data dari " + username_follower + ", postingan ke " + str(count) + " dari " + str(profile_follower.mediacount) + ", follower ke " + str(count_account) + " dari " + str(profile.followers) + ".")
        caption = post.caption
        if caption is None:
            caption = ""
        if caption is not None:
            caption = caption.encode('ascii', 'ignore').decode('ascii')
        
        hashtag = post.caption_hashtags
        likes = post.likes
        
        comments = []
        for comment in post.get_comments() :
            comments.append(comment.text.encode('ascii', 'ignore').decode('ascii'))

        usernamelist.append(username_follower)
        captionlist.append(caption)
        hashtaglist.append(hashtag)
        likeslist.append(likes)
        commentlist.append(comments)
        count = count+1
    count_account = count_account + 1

data = pd.DataFrame({"Account":usernamelist, "Post":captionlist, "Tag":hashtaglist, "Likes":likeslist, "Comments":commentlist})
timestring = time.strftime("%Y%m%d_%H%M%S")
nama_file = "Dataset_" + username + "_" + timestring + ".csv"
data.to_csv(nama_file)
