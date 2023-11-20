import json
import random
import requests
while True:
  ID = random.randint(9450000, 10000000)
  r = requests.get(f"https://groups.roproxy.com/v1/groups/{ID}")
  try:
    group_data = r.json()
  except json.JSONDecodeError as e:
    print(f"JSONDecodeError: {e}")
    continue 
  if "owner" in r.text:
    if group_data['owner'] is None: 
      if group_data['publicEntryAllowed'] is True and "isLocked" not in r.text:
        print(f"\x1b[32mUnclaimed | https://www.roblox.com/groups/{ID} ({group_data['memberCount']})")
      else:
        print(f"\x1b[33mLocked | https://www.roblox.com/groups/{ID} ({group_data['memberCount']})")
    else:
      print(f"\x1b[31mClaimed | https://www.roblox.com/groups/{ID} ({group_data['0memberCount']})")
  elif any(error.get("message") == "Too many requests" for error in group_data.get("errors", [])):
    print(f"\x1b[31mToo Many Requests | https://www.roblox.com/groups/{ID}")
  else:
    print(f"\x1b[31mInvalid | https://www.roblox.com/groups/{ID}")
