import json
import random
import requests
from discord_webhook import DiscordEmbed, DiscordWebhook
while True:
  ID = random.randint(1, 17400000)
  webhook = DiscordWebhook(url="YOUR_WEBHOOK_HERE")
  r = requests.get(f"https://groups.roproxy.com/v1/groups/{ID}")
  try:
    group_data = r.json()
  except json.JSONDecodeError as e:
    print(f"\x1b[31mJSONDecodeError | {e}")
    continue 
  if "owner" in r.text:
    if group_data['owner'] is None: 
      if group_data['publicEntryAllowed'] is True and "isLocked" not in r.text:
        print(f"\x1b[32mUnclaimed | https://www.roblox.com/groups/{ID} ({group_data['memberCount']})")
        embed = DiscordEmbed(title=f"Unclaimed Group | {group_data['name']}", description=group_data['description'], color=0x00ff00)
        embed.add_embed_field(name="Shout", value=f"{group_data['shout']}")
        embed.add_embed_field(name="Members", value=f"{group_data['memberCount']}")
        embed.add_embed_field(name="Entry Allowed", value=f"{group_data['publicEntryAllowed']}")
        embed.add_embed_field(name="Verified", value=f"{group_data['hasVerifiedBadge']}")
        embed.add_embed_field(name="ID", value=f"{ID}")
        embed.add_embed_field(name="Link", value=f"https://www.roblox.com/groups/{ID}")
        webhook.add_embed(embed)
        response = webhook.execute()
      else:
        print(f"\x1b[33mLocked | https://www.roblox.com/groups/{ID} ({group_data['memberCount']})")
    else:
      print(f"\x1b[31mClaimed | https://www.roblox.com/groups/{ID} ({group_data['memberCount']})")
  elif any(error.get("message") == "Too many requests" for error in group_data.get("errors", [])):
    print(f"\x1b[31mToo Many Requests | https://www.roblox.com/groups/{ID}")
  else:
    print(f"\x1b[31mInvalid | https://www.roblox.com/groups/{ID}")
