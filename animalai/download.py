from flickrapi import FlickrAPI
from urllib.request import urlretrieve
from pprint import pprint
import os, time, sys

from dotenv import load_dotenv
from os.path import join, dirname

WAIT_TIME = 1

# dotenvよりAPIキー取得
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

API_KEY= os.environ.get("FLICKR_API_KEY")
API_SECRET= os.environ.get("FLICKR_API_SECRET")

# 保存フォルダの指定
animal_name = sys.argv[1]
savedir = "./" + animal_name

flickr = FlickrAPI(API_KEY, API_SECRET, format='parsed-json')
result = flickr.photos.search(
	text = animal_name,
	per_page = 400,
	media = 'phptos',
	sort = 'relevance',
	safe_search = 1,
	extras = 'url_q, licence'
)

photos = result['photos']
pprint(photos)
