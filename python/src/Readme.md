## Scrapper module
A scrapper module developed and compaitble in Python3.

# Dependecies for this module:
- sys
- urllib
- re
- queue
- threading
- datetime

# You can use this module using the following steps:

Just download the `scrappermaster.py` file in your desktop and copy the file in `site_packages` directory in your installed python3 folder if it is windows otherwise copy it to the `/usr/lib/python3.x/` folder, so that you can import this.

Then simply load it in your python file by adding the following steps:
```
import scrappermaster
endpoint='https://example-endpoing.html'
scrappermaster.invokeScrapping(endpoint)
```

> If you provide a null string to this module then the scrapper will run for default url [Medium Website](https://medium.com)
