import json
import random
import requests
from discord_webhook import DiscordEmbed, DiscordWebhook
while True:
  ID = random.randint(9450000, 10000000)
  webhook = DiscordWebhook(url="YOUR_WEBHOOK_HERE")
  r = requests.get(f'https://groups.roproxy.com/v1/groups/{ID}')
  try:
    group_data = r.json()
  except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")
    continue 
  if "owner" in r.text:
    if group_data['owner'] is None: 
      if group_data['publicEntryAllowed'] is True and 'isLocked' not in r.text:
        print(f"\x1b[42mUnclaimed > https://www.roblox.com/groups/{ID} ({group_data['memberCount']})")
        embed = DiscordEmbed(title='Unclaimed Group Found!', color=000000)
        embed.add_embed_field(name='ID', value=f"{ID}")
        embed.add_embed_field(name='Description', value=f"{group_data['description']}")
        embed.add_embed_field(name='Members', value=f"{group_data['memberCount']}")
        embed.add_embed_field(name='Link', value=f'https://www.roblox.com/groups/{ID}')
        webhook.add_embed(embed)
        response = webhook.execute()
      else:
        print(f"\x1b[31mLocked > https://www.roblox.com/groups/{ID} ({group_data['memberCount']})")
    else:
      print(f"\x1b[31mClaimed > https://www.roblox.com/groups/{ID} ({group_data['memberCount']})")
  elif any(error.get('message') == "Too many requests" for error in group_data.get('errors', [])):
    print(f"\x1b[31mToo Many Requests > https://www.roblox.com/groups/{ID}")
  else:
    print(f"\x1b[31mInvalid > https://www.roblox.com/groups/{ID}")
