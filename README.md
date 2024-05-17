# clip_stitch
An application to download and stitch together the most popular twitch clips for a specified streamer and time frame.

## Getting Started
```bash
  git clone https://github.com/scurran080/clip_stitch.git
```
```bash
cd clip-stitch
```

```bash
pip install -r requirements.txt
```
**If using PyCharm the IDE will notice the requirements.txt file and offer to create a virtual environment with the needed libraries.**

A twitch account and application registered on the developer console is required. Don't have a token? [Go Here](https://dev.twitch.tv/console).
Create a .env file and place the following in the file with the placeholders swapped for your twitch id and token.
```
CLIENT_ID=ID_PLACEHOLDER
CLIENT_SECRET=SECRET_PLACEHOLDER
```

## Example Usage
```bash
python3 main.py -username=STREAMERSNAME -limit=10 -begin=04/01/2024 -end=05/01/2024
```

Individual clips will be stored in the tmp file. I may get around to adding automatic cleanup.

![image](https://github.com/scurran080/clip_stitch/assets/56182216/e5d4162a-8dc3-413d-a9e2-e32e9204892d)
