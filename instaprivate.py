
import instaloader

# Create an instance of Instaloader
loader = instaloader.Instaloader()

# Login to Instagram
loader.login("your_username", "your password")

# Scrape the private profile
profile = instaloader.Profile.from_username(loader.context, "username of account to be scrapped")

# Iterate over the profile's posts and download the photos
for post in profile.get_posts():
    loader.download_post(post, target=f"{profile.username}/{post.date_utc}")
