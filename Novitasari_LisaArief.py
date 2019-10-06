import instaloader
import pandas as pd

username = "cobaakudong"
L = instaloader.Instaloader(max_connection_attempts=0)
L.login("alcanderanshar", "nagasakure")

profile = instaloader.Profile.from_username(L.context, username)

usernamelist = []
captionlist = []
hashtaglist = []
likeslist = []
commentlist = []
followerlist = []

count = 1
for post in profile.get_posts():
        print("mengambil data dari akun " + username + " postingan ke " + str(count) + " dari " + str(profile.mediacount))
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
        print("Profile Instagram dengan username " + username_follower + " tidak bisa diakses karena kuota habis")
    count = 1
    for post in profile_follower.get_posts():
        print("mengambil data dari " + username_follower + " postingan ke " + str(count) + " dari " + str(profile_follower.mediacount) + ", follower ke " + str(count_account) + " dari " + str(profile.followers))
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
nama_file = "Data_" + username + ".csv"
data.to_csv(nama_file)
