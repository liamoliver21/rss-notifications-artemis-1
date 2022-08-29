# python -m pip install plyer
from plyer import notification
from bs4 import BeautifulSoup
import requests
import time


def get_updates():
    # Reading the data inside the xml
    # file to a variable under the name
    # data
    data = str(requests.get("https://blogs.nasa.gov/artemis/tag/artemis-i3/feed/").text)
    Bs_data = BeautifulSoup(data)
    b_unique = Bs_data.find_all('title')
    return b_unique
 
def remove_tags(html):
  
    # parse html content
    soup = BeautifulSoup(html, "html.parser")
  
    for data in soup(['style', 'script']):
        # Remove tags
        data.decompose()
  
    # return data by retrieving the tag content
    return ' '.join(soup.stripped_strings)

b_unique = get_updates()
previous = str(b_unique[1])

while True:
    b_unique = get_updates()
    if(previous != str(b_unique[1])):
        previous = str(b_unique[1])
        notification.notify(
            title='Artemis I update',
            message=remove_tags(str(b_unique[1])),
            app_icon='C:/Users/Administrator/Desktop/code/artimis1/icon.ico',  # e.g. 'C:\\icon_32x32.ico'
            timeout=10,  # seconds
        )
    time.sleep(2400)