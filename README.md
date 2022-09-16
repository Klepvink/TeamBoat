# TeamBoat
A script to automate certain Microsoft Teams functionality using the Cookies-file available to non-administrator users of the Microsoft Teams desktop application. 

Since this file is not encrypted or properly protected, an attacker could steal the MS-teams Cookies file and authenticate as the victim. This script is merely to demonstrate and automate some functionality that is available to the attacker in possession of the file. For more information, check out the following: https://www.bleepingcomputer.com/news/security/microsoft-teams-stores-auth-tokens-as-cleartext-in-windows-linux-macs/

## Usage
```python3 teamboat.py --cookies PATH_TO_COOKIES_FILE -h```

## Default paths to the cookies file
Windows: ```%AppData%\Microsoft\Teams\Cookies```

MacOS: ```~/Library/Application Support/Microsoft/Teams/Cookies```

Linux: ```~/.config/Microsoft/Microsoft Teams/Cookies```

## Contributing
If you have features that you would like to add, thats great! I am not planning on actively maintaining this tool, but feel free to fork it and let me know what additions you have made on twitter (@klepv1nk). If I like your additions or changes I might incorporate the changes in my script (and credit the author). 

If you do make changes or are planning on distributing the code, please respect the appropriate license attached/applied to this repo and it's dependencies. I would also appreciate it if you included a note explaining the tool is not for malicious purposes, because it is not meant to be.
```
        _    _
     __|_|__|_|__
   _|____________|__
  |o o o o o o o o /  Teamboat by Klepvink
~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`~'`
 Please note that using this script for illegal activities and/or with bad intentions is
 strictly prohibited (not cool), and I am not to be held responsible for any harm that is
 caused using this script. Good vibes only, please.
 ```
