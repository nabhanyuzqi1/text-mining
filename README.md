
# Text Mining
Text Mining using Python Libraries "Tweepy" and Twitter API v2
## Twitter Developer Account
You have to make an twitter account then sign up as developer on this site https://developer.twitter.com
make sure you apply for Elevated Usage on Project API.

![image](https://user-images.githubusercontent.com/30825747/175817987-b4b41209-6b1f-4ab5-b5f5-a204edd38dd6.png)
# Tweepy

Tweepy is an open source Python package that gives you a very convenient way to access the Twitter API with Python. Tweepy includes a set of classes and methods that represent Twitter's models and API endpoints, and it transparently handles various implementation details, such as: Data encoding and decoding.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install tweepy.

```bash
pip install tweepy
```
![image](https://user-images.githubusercontent.com/30825747/175818156-fb3b8e99-a4aa-4dd7-af4d-7c77a14e033d.png)

## Usage

```python
#import module
import tweepy

#your api key from twitter developer page
api_key = ''
api_key_secret = ''
access_token = ''
access_token_secret = ''

#aunthenticate
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
```
## Tweepy Official Documentation
You can read the full documentation from this site https://docs.tweepy.org/en/stable/

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
