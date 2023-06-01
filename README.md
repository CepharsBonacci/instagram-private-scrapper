# instagram-scrapper
The code shows you how to scrape photos and videos from an instagram account when the account is private
InstaPrivate Scraper
This is a Python script that utilizes the Instaloader library to scrape photos from private Instagram profiles. It provides a convenient way to access and download images from Instagram accounts that require authentication.

Installation
Clone the repository:

bash
Copy code
git clone https://github.com/CepharsBonacci/instagram-scraper.git
Install the required dependencies:

bash
Copy code
pip install instaloader
Usage
Import the instaloader library in your Python script:

python
Copy code
import instaloader
Create an instance of the Instaloader class:

python
Copy code
loader = instaloader.Instaloader()
Login to your Instagram account using your credentials:

python
Copy code
loader.login("your_username", "your_password")
Note: Logging in is optional, but necessary if you want to scrape private profiles. If you're only interested in scraping public profiles, you can skip this step.

Scrape the private profile by providing the username of the account you want to scrape:

python
Copy code
profile = instaloader.Profile.from_username(loader.context, "username_of_the_account_to_be_scraped")
Iterate over the profile's posts and download the photos:

python
Copy code
for post in profile.get_posts():
    loader.download_post(post, target=f"{profile.username}/{post.date_utc}")
This will download the photos from the profile's posts and save them in the specified target directory.

Contributing
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please open an issue or submit a pull request.

License
This project is licensed under the MIT License.
