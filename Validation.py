#validate, regex

import re

print("Hello this program will be used to validate user input.\n"
      "There are 2 parts, first it willl check your email format. \n"
      "Second it will return the unique id number of a single youtube video of your choice.")
print()

email = input("Whats your email for any domain ending in .co.uk: ").strip()

if re.search(r"^[^@]+@+[^@]+\.co.uk$", email, re.IGNORECASE):
    print(f"Valid format {email}")
else:
    print("Invalid format")

Youtube_URL_ID = input("Please enter the youtube URL: ").strip() 

if matches:= re.search(r"^https?://(?:www\.)?youtube\.com/watch[?]v=([^/]+)$", Youtube_URL_ID, re.IGNORECASE):
    print("The unique ID of your youtube video is:", matches.group(1))
else:
    print("Invalid URL or ID contains '/'")



