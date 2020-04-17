import os
import urllib.parse
google = os.popen('zenity --entry --text="Enter your Google search: " --title="Search"').read()
google = urllib.parse.quote(google)
os.system('chromium-browser http://www.google.com/search?q=%s' % (google))
                                                         
