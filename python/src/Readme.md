This a scrapper module build in Python3.8

Dependecies:
sys
urllib
re
queue
threading
datetime

To use the package use the simple script below:
Just download the .py file in your desktop and copy the file in site_packages directory in your installed python folder.

Then add the below lines to execute the scrapper module:

import scrappermaster

and to use this for a particular website use the syntax below:

endpoint='https://example-endpoing.html'
scrappermaster.invokeScrapping(endpoint)
