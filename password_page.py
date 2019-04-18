'''short script to check if a shopify password page is on or offline, great to combine with your shopify monitors'''

#written in 5minutes by pxtr.ck#3068, improved by you

import requests
import datetime
import time
from discord_webhook import DiscordEmbed, DiscordWebhook

site="https://eflash.doverstreetmarket.com" #enter a random shopify site to check when password page goes down

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}


def send_notify(): #sends a notification once password page i offline

	hook="https://discordapp.com/api/webhooks/..." #Your discord webhook
	webhook = DiscordWebhook(url=hook)
	embed=DiscordEmbed(title='Shopify', description='Password page removed', color=0xadff2f)
	webhook.add_embed(embed)
	embed.add_embed_field(name='Site Link: ', value=site)
	embed.set_footer(text='Hi')
	embed.set_timestamp()
	webhook.execute()

def monitor_link():

	page=requests.get(site, headers=header)

	if "password.js" in page.text:	#checks the presence of the shopify password page JS, if it is there, it rechecks
		#print("CHECKING LINK AT: "+str(datetime.datetime.now())) #uncomment this to get a log output also for scanning and not only found requests
		time.sleep(0) #retrydelay, change like you want, add proxy support for low or no delay
		monitor_link()



	else:
		print("PASSWORD PAGE OFFLINE AT: "+str(datetime.datetime.now()))
		send_notify()
		#stops once found, obviously you can change that too, just uncomment the next 2 lines
		#time.sleep(0)
		#monitor_link()
monitor_link()
