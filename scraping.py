import requests
from bs4 import BeautifulSoup
def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all elements with the specified class
    elements = soup.find_all(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each element
    rich_text = [element.get_text(strip=True) for element in elements]
    rich_text_string = ' '.join(rich_text)

    link = soup.find('a', href='#technicalInformation')

    bullet_points = []
    bullet_points_string = ""
    # If the link was found, find the element it links to
    if link is not None:
        target_id = link['href'].lstrip('#')
        target_element = soup.find(id=target_id)

        # If the target element was found, get its text
        if target_element is not None:
            # Find all the list items in the target element
            list_items = target_element.find_all('li')

            # Extract the text of each list item
            bullet_points = [li.get_text(strip=True) for li in list_items]
            bullet_points_string = '\n'.join(bullet_points)

        
    text = rich_text_string +" \n "+ bullet_points_string
    return text
url_text_dict = {}
extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/")
extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/")
extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/")
extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/")
extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/")
def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all elements with the specified class
    elements = soup.find_all(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each element
    rich_text = [element.get_text(strip=True) for element in elements]
    rich_text_string = ' '.join(rich_text)

    link = soup.find('a', href='#technicalInformation')

    bullet_points = []
    bullet_points_string = ""
    # If the link was found, find the element it links to
    if link is not None:
        target_id = link['href'].lstrip('#')
        target_element = soup.find(id=target_id)

        # If the target element was found, get its text
        if target_element is not None:
            # Find all the list items in the target element
            list_items = target_element.find_all('li')

            # Extract the text of each list item
            bullet_points = [li.get_text(strip=True) for li in list_items]
            bullet_points_string = '\n'.join(bullet_points)

        
    text = rich_text_string
    return text
url_text_dict = {}
extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/")
def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all elements with the specified class
    elements = soup.find_all(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each element and stop when encountering a heading
    rich_text = []
    for element in elements:
        if element.find_next(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
            break
        rich_text.append(element.get_text(strip=True))
    rich_text_string = ' '.join(rich_text)
        
    text = rich_text_string
    return text

url_text_dict = {}
extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/")
def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find all elements with the specified class
    elements = soup.find_all(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each element
    rich_text = [element.get_text(strip=True) for element in elements]
    rich_text_string = ' '.join(rich_text)
        
    text = rich_text_string
    return text
url_text_dict = {}
extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/")
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the specified class
    div = soup.find(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each child of the div until a h2, h3 or ul tag is encountered
    text = []
    for child in div.children:
        if isinstance(child, NavigableString):
            text.append(child.strip())
        elif child.name in ['h2', 'h3', 'ul']:
            break
        else:
            text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string

print(extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/"))
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the specified class
    div = soup.find(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each child of the div until a h2, h3 or ul tag is encountered
    text = []
    for child in div.children:
        if isinstance(child, NavigableString):
            text.append(child.strip())
        elif child.name in ['ul']:
            break
        else:
            text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string

print(extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/"))
import requests
from bs4 import BeautifulSoup
import pandas as pd
df = pd.read_csv("data/tags_30_11.csv")

print(extract_text(df["url"][0]))
df = pd.read_csv("data/tags_30_11.csv")

print(extract_text(df["url"][0]))
print(df["url"][0])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the specified class
    div = soup.find(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each child of the div until a h2, h3 or ul tag is encountered
    text = []
    img_url = None
    for child in div.children:
        if isinstance(child, NavigableString):
            text.append(child.strip())
        elif child.name == 'img':
            img_url = child['src']
        elif child.name == 'ul':
            break
        else:
            text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string, img_url

text, img_url = extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/")
print(text)
print(img_url)
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the specified class
    div = soup.find(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each child of the div until a h2, h3 or ul tag is encountered
    text = []
    img_url = None
    for child in div.children:
        if isinstance(child, NavigableString):
            text.append(child.strip())
        elif child.name == 'picture':
            img_url = child['src']
        elif child.name == 'ul':
            break
        else:
            text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string, img_url

text, img_url = extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/")
print(text)
print(img_url)
df = pd.read_csv("data/tags_30_11.csv")

print(extract_text(df["url"][0]))
print(df["url"][0])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the specified class
    div = soup.find(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each child of the div until a h2, h3 or ul tag is encountered
    text = []
    img_url = None
    for child in div.children:
        if isinstance(child, NavigableString):
            text.append(child.strip())
        elif child.name == 'picture':
            img = child.find('img')
            if img:
                img_url = img['src']
        elif child.name == 'ul':
            break
        else:
            text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string, img_url

text, img_url = extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/")
print(text)
print(img_url)
df = pd.read_csv("data/tags_30_11.csv")

print(extract_text(df["url"][0]))
print(df["url"][0])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the specified class
    div = soup.find(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each child of the div until a h2, h3 or ul tag is encountered
    text = []
    img_url = None
    for child in div.children:
        if isinstance(child, NavigableString):
            text.append(child.strip())
        elif child.name == 'picture':
            img = child.find('img')
            if img:
                img_url = img['src']
        elif child.name in ['h2', 'h3', 'ul']:
            break
        else:
            text.append(child.get_text(strip=True))
            # Check for picture tag within other tags
            picture = child.find('picture')
            if picture:
                img = picture.find('img')
                if img and not img_url:  # Only set img_url if it hasn't been set yet
                    img_url = img['src']
    text_string = ' '.join(text)
        
    return text_string, img_url

text, img_url = extract_text(df["url"][0])
print(text)
print(img_url)
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the specified class
    div = soup.find(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each child of the div until a h2, h3 or ul tag is encountered
    text = []
    img_url = None
    for child in div.children:
        if isinstance(child, NavigableString):
            text.append(child.strip())
        elif child.name == 'picture':
            img = child.find('img')
            if img:
                img_url = img['src']
        elif child.name in ['h2', 'h3', 'ul']:
            break
        else:
            text.append(child.get_text(strip=True))
            # Check for picture tag within other tags
            picture = child.find('picture')
            if picture:
                img = picture.find('img')
                if img and not img_url:  # Only set img_url if it hasn't been set yet
                    img_url = img['src']
    text_string = ' '.join(text)
        
    return text_string, img_url

text, img_url = extract_text(df["url"][0])
print(text)
print(img_url)
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the specified class
    div = soup.find(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each child of the div until a h2, h3 or ul tag is encountered
    text = []
    img_url = None
    for child in div.children:
        if isinstance(child, NavigableString):
            text.append(child.strip())
        elif child.name == 'picture':
            img = child.find('img')
            if img:
                img_url = img['src']
        elif child.name in ['h2', 'h3', 'ul']:
            break
        else:
            text.append(child.get_text(strip=True))
            # Check for picture tag within other tags
            picture = child.find('picture')
            if picture:
                img = picture.find('img')
                if img and not img_url:  # Only set img_url if it hasn't been set yet
                    img_url = img['src']
    text_string = ' '.join(text)
        
    return text_string, img_url

text, img_url = extract_text(df["url"][0])
print(text)
print(img_url)
df = pd.read_csv("data/tags_30_11.csv")

print(extract_text(df["url"][0]))
print(df["url"][0])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the specified class
    div = soup.find(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each child of the div until a h2, h3 or ul tag is encountered
    text = []
    for child in div.children:
        if isinstance(child, NavigableString):
            text.append(child.strip())
        elif child.name in ['ul']:
            break
        else:
            text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string

print(extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/"))
df = pd.read_csv("data/tags_30_11.csv")

print(extract_text(df["url"][0]))
print(df["url"][0])
df = pd.read_csv("data/tags_30_11.csv")
number = 1

print(extract_text(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the specified class
    div = soup.find(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each child of the div until a ul tag is encountered
    text = []
    img_url = None
    for child in div.children:
        if isinstance(child, NavigableString):
            text.append(child.strip())
        elif child.name == 'picture':
            img = child.find('img')
            if img:
                img_url = img['src']
        elif child.name == 'ul':
            break
        else:
            text.append(str(child))  # Append the string representation of the child, including HTML tags
    text_string = ''.join(text)
        
    return text_string, img_url

text, img_url = extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/")
print(text)
print(img_url)
df = pd.read_csv("data/tags_30_11.csv")
number = 1

print(extract_text(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h3 tag is encountered
    text = []
    img_url = None
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name == 'picture':
                img = child.find('img')
                if img:
                    img_url = img['src']
            elif child.name == 'h3':
                break
            else:
                text.append(str(child))  # Append the string representation of the child, including HTML tags
    text_string = ''.join(text)
        
    return text_string, img_url

df = pd.read_csv("data/tags_30_11.csv")
number = 1

print(extract_text(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h3 tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name == 'h3':
                break
            elif child.name != 'picture':  # Exclude the picture tag
                text.append(str(child))  # Append the string representation of the child, including HTML tags
    text_string = ''.join(text)
        
    return text_string

df = pd.read_csv("data/tags_30_11.csv")
number = 1

print(extract_text(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h3 tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child):
                text.append(child.strip())
            elif child.name == 'ul':
                break
            elif child.name != 'picture':  # Exclude the picture tag
                text.append(str(child))  # Append the string representation of the child, including HTML tags
    text_string = ''.join(text)
        
    return text_string

df = pd.read_csv("data/tags_30_11.csv")
number = 1

print(extract_text(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the specified class
    div = soup.find(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each child of the div until a h2, h3 or ul tag is encountered
    text = []
    for child in div.children:
        if isinstance(child, NavigableString):
            text.append(child.strip())
        elif child.name in ['ul']:
            break
        else:
            text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string

print(extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/"))
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the specified class
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of the div until a h2, h3 or ul tag is encountered
    text = []
    for child in divs.children:
        if isinstance(child, NavigableString):
            text.append(child.strip())
        elif child.name in ['ul']:
            break
        else:
            text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string

print(extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/"))
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string

print(extract_text("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/"))
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 1

print(extract_text(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        children = list(div.children)
        for i in range(len(children)):
            child = children[i]
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            elif i < len(children) - 1 and children[i + 1].name == 'ul':
                continue  # Skip the heading before the ul tag
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string

df = pd.read_csv("data/tags_30_11.csv")
number = 1

print(extract_text(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 1

print(extract_text(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 2

print(extract_text(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 3

print(extract_text(df["url"][number]))

print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 4

print(extract_text(df["url"][number]))

print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 5

print(extract_text(df["url"][number]))

print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 6

print(extract_text(df["url"][number]))

print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 2

print(extract_text(df["url"][number]))

print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 3

print(extract_text(df["url"][number]))

print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 4

print(extract_text(df["url"][number]))

print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 5

print(extract_text(df["url"][number]))

print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 8

print(extract_text(df["url"][number]))

print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 21

print(extract_text(df["url"][number]))

print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 22

print(extract_text(df["url"][number]))

print(df["url"][number])
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_=["RichtextArea ProductPage__richtext text-wrapper", "layout--2col wrapper"])

    # Extract the text of each child of each div until a h2, h3 or ul tag is encountered
    text = []
    for div in divs:
        for child in div.children:
            if isinstance(child, NavigableString):
                text.append(child.strip())
            elif child.name in ['ul']:
                break
            else:
                text.append(child.get_text(strip=True))
    text_string = ' '.join(text)
        
    return text_string
df = pd.read_csv("data/tags_30_11.csv")
number = 23

print(extract_text(df["url"][number]))

print(df["url"][number])
from bs4 import BeautifulSoup
import requests

def find_datasheet(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the span with the specified class and text
    datasheet_span = soup.find('span', class_="Downloads__itemName", text="Datasheet")

    # If the span is found, return the parent link's href attribute
    if datasheet_span:
        datasheet_link = datasheet_span.parent.get('href')
        return datasheet_link

    # If the span is not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 1

print(find_datasheet(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests

def find_datasheet(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the span with the text "Datasheet" within this div
    if downloads_div:
        datasheet_span = downloads_div.find('span', class_="Downloads__itemName", text="Datasheet")

        # If the span is found, return the parent link's href attribute
        if datasheet_span:
            datasheet_link = datasheet_span.parent.get('href')
            return datasheet_link

    # If the div or the span is not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 1

print(find_datasheet(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests

def find_datasheet(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the span with the text "Datasheet" within this div
    if downloads_div:
        datasheet_span = downloads_div.find('span', class_="Downloads__itemName", text="Datasheet")

        # If the span is found, return the parent link's href attribute
        if datasheet_span:
            datasheet_link = datasheet_span.parent.get('href')
            return datasheet_link

    # If the div or the span is not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 2

print(find_datasheet(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find all links within this div
    if downloads_div:
        datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")

        # If the links are found, return their href attributes
        if datasheet_links:
            return [link.get('href') for link in datasheet_links]

    # If the div or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 2

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find all links within this div
    if downloads_div:
        datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")

        # If the links are found, return their href attributes
        if datasheet_links:
            return [link.get('href') for link in datasheet_links]

    # If the div or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 1

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find all links within this div
    if downloads_div:
        datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")

        # If the links are found, return their href attributes
        if datasheet_links:
            return [link.get('href') for link in datasheet_links]

    # If the div or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 3

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheets" within this div
    if downloads_div:
        datasheets_section = downloads_div.find('h3', class_="Section__subtitle", text="Data sheets").find_next_sibling()

        # If the section is found, find all links within this section
        if datasheets_section:
            datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

            # If the links are found, return their href attributes
            if datasheet_links:
                return [link.get('href') for link in datasheet_links]

    # If the div, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 3

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string="Data sheets")

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return [link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 3

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string="Data sheet")

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return [link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 3

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string="Data sheet")

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return [link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 4

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string="Data sheet")

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return [link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 5

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string="Data sheet")

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return [link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 6

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return [link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 7

print(find_datasheets(df["url"][number]))
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return [link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 5

print(find_datasheets(df["url"][number]))
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return [link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 10

print(find_datasheets(df["url"][number]))
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return [link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 11

print(find_datasheets(df["url"][number]))
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return [link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 12

print(find_datasheets(df["url"][number]))
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return [link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 13

print(find_datasheets(df["url"][number]))
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import re
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 13

print(find_datasheets(df["url"][number]))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 14

print(find_datasheets(df["url"][number]))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 15

print(find_datasheets(df["url"][number]))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return their href attributes
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 15

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 17

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 15

print(find_datasheets(df["url"][number]))
print(df["url"][number])
df = pd.read_csv("data/tags_30_11.csv")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)
df.to_csv("data/data_sheets.csv", index=False)
# only keep column url, product name and data sheets
df = df[['url', 'product_name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 15

print(find_datasheets(df["url"][number]))
print(df["url"][number])
df = pd.read_csv("data/tags_30_11.csv")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)
# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 15

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 20

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 19

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links with the name "Datasheet" within the div
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink", string="Datasheet")

            # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
            if datasheet_links:
                return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 19

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links with the name "Datasheet" within the div
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink", string="Datasheet")

            # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
            if datasheet_links:
                return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 24

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links with the name "Datasheet" within the div
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink", string="Datasheet")

            # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
            if datasheet_links:
                return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 25

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links with the name "Datasheet" within the div
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink", string="Datasheet")

            # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
            if datasheet_links:
                return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 23

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the preceding sibling has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink", string="Datasheet")

            # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
            if datasheet_links:
                return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 23

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")

            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
            if datasheet_links:
                return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 23

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")

            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
            if datasheet_links:
                return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 23

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")

            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
            if datasheet_links:
                return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 23

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, return the list of href attributes
                if datasheet_links:
                    return [link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")

            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, return the list of href attributes
            if datasheet_links:
                return [link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 23

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
            print(datasheet_links)

            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
            if datasheet_links:
                return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the div, the subtitle, the section, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 23

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")

            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, return the list of href attributes
            if datasheet_links:
                return [link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 23

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
            print(datasheet_links)
            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, return the list of href attributes
            if datasheet_links:
                return [link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 23

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            downloads_section = soup.find('h2', class_="Section__title", string="Downloads")

            # If the section is found, find the next sibling section
            if downloads_section:
                downloads_div = downloads_section.find_next_sibling()

                # If the div is found, find all links where the direct child span has the text "Datasheet"
                if downloads_div:
                    datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")

                    # Filter the links where the direct child span has the text "Datasheet"
                    datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

                    # If the links are found, return the list of href attributes
                    if datasheet_links:
                        return [link.get('href') for link in datasheet_links]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 23

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            downloads_section = soup.find('h2', class_="Section__title", string="Downloads")

            # If the section is found, find the next sibling section
            if downloads_section:
                downloads_div = downloads_section.find_next_sibling()

                # If the div is found, find all links where the direct child span has the text "Datasheet"
                if downloads_div:
                    datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
                    print(datasheet_links)

                    # Filter the links where the direct child span has the text "Datasheet"
                    datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

                    # If the links are found, return the list of href attributes
                    if datasheet_links:
                        return [link.get('href') for link in datasheet_links]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 23

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            downloads_section = soup.find('h2', class_="Section__title", string="Downloads")

    # If the section is found, find the next sibling section
    if downloads_section:
        downloads_div = downloads_section.find_next_sibling()

        # If the div is found, find all links where the direct child span has the text "Datasheet"
        if downloads_div:
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")

            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, return the list of href attributes
            if datasheet_links:
                return [link.get('href') for link in datasheet_links]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 83

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            downloads_section = soup.find('h2', class_="Section__title", string="Downloads")

    # If the section is found, find the next sibling section
    if downloads_section:
        downloads_div = downloads_section.find_next_sibling()

        # If the div is found, find all links where the direct child span has the text "Datasheet"
        if downloads_div:
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")

            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, return the list of href attributes
            if datasheet_links:
                return [link.get('href') for link in datasheet_links]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 82

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            downloads_section = soup.find('h2', class_="Section__title", string="Downloads")

    # If the section is found, find the next sibling section
    if downloads_section:
        downloads_div = downloads_section.find_next_sibling()

        # If the div is found, find all links where the direct child span has the text "Datasheet"
        if downloads_div:
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")

            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, return the list of href attributes
            if datasheet_links:
                return [link.get('href') for link in datasheet_links]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 81

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            downloads_section = soup.find('h2', class_="Section__title", string="Downloads")

    # If the section is found, find the next sibling section
    if downloads_section:
        downloads_div = downloads_section.find_next_sibling()

        # If the div is found, find all links where the direct child span has the text "Datasheet"
        if downloads_div:
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")

            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, return the list of href attributes
            if datasheet_links:
                return [link.get('href') for link in datasheet_links]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 82

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            downloads_section = soup.find('h2', class_="Section__title", string="Downloads")

    # If the section is found, find the next sibling section
    if downloads_section:
        downloads_div = downloads_section.find_next_sibling()

        # If the div is found, find all links where the direct child span has the text "Datasheet"
        if downloads_div:
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")

            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, return the list of href attributes
            if datasheet_links:
                return [link.get('href') for link in datasheet_links]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 83

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
        
            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, return the list of href attributes
            if datasheet_links:
                return [link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 84

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
        
            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, return the list of href attributes
            if datasheet_links:
                return [link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 85

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
        
            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, return the list of href attributes
            if datasheet_links:
                return [link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 83

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
        
            # Filter the links where the direct child span has the text "Datasheet"
            datasheet_links = [link for link in datasheet_links if link.find('span', class_="Downloads__itemName", string="Datasheet")]

            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 83

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 83

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return ["https://www.kongsberg.com" + href]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_csv("data/tags_30_11.csv")
number = 83

print(find_datasheets(df["url"][number]))
print(df["url"][number])
df = pd.read_csv("data/tags_30_11.csv")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)

# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return ["https://www.kongsberg.com" + href]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_excel("data/tags_12_04.xslx")
number = 83

print(find_datasheets(df["url"][number]))
print(df["url"][number])
from bs4 import BeautifulSoup
import requests
import re

def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return ["https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return ["https://www.kongsberg.com" + href]

    # If the section, the div, or the links are not found, return None
    return None

df = pd.read_excel("data/12_04/tags_12_04.xlsx")
number = 83

print(find_datasheets(df["url"][number]))
print(df["url"][number])
df = pd.read_excel("data/12_04/tags_12_04.xlsx")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)

# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
import requests
import PyPDF2
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with open('temp.pdf', 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)

        # Extract text from each page
        text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
pdf_url = 'https://example.com/sample.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import PyPDF2
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with open('temp.pdf', 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)

        # Extract text from each page
        text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
pdf_url = 'https://example.com/sample.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import PyPDF2
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with open('temp.pdf', 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)

        # Extract text from each page
        text = ''
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extract_text()

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
pdf_url = 'https://example.com/sample.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import PyPDF2
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with open('temp.pdf', 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)

        # Extract text from each page
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
pdf_url = 'https://example.com/sample.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import PyPDF2
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with open('temp.pdf', 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)

        # Extract text from each page
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return [link.get('href') if 'https://simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return [href if 'https://simrad.online' in href else "https://www.kongsberg.com" + href]

    # If the section, the div, or the links are not found, return None
    return None
df = pd.read_excel("data/12_04/tags_12_04.xlsx")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)

# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return [link.get('href') if 'https://simrad.online' or "https://www.simrad.online"  in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return [href if 'https://simrad.online' or "https://www.simrad.online" in href else "https://www.kongsberg.com" + href]

    # If the section, the div, or the links are not found, return None
    return None
df = pd.read_excel("data/12_04/tags_12_04.xlsx")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)

# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return [link.get('href') if 'https://simrad.online' or "https://www.simrad.online"  in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return [href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href]
    # If the section, the div, or the links are not found, return None
    return None
df = pd.read_excel("data/12_04/tags_12_04.xlsx")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)

# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    return [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return [href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href]
    # If the section, the div, or the links are not found, return None
    return None
df = pd.read_excel("data/12_04/tags_12_04.xlsx")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)

# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
# loop through all data sheets
df = pd.read_csv("data/data_sheets.csv")
df["text"] = ""
for i in range(len(df)):
    print(i)
    try:
        df["text"][i] = scrape_pdf_text(df["Data sheets"][i])
    except:
        print("error")
import requests
import PyPDF2
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with open('temp.pdf', 'rb') as f:
        pdf_reader = PyPDF2.PdfReader(f)

        # Extract text from each page
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            text += page.extract_text()

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            text += page.extract_text()

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical' in page_text or "TECHNICAL" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
pdf_urls = data_sheets['Data sheets'].dropna()
pdf_urls = pdf_urls.apply(eval)
pdf_urls = pdf_urls.explode()
pdf_urls = pdf_urls.unique()
pdf_urls = [url for url in pdf_urls if url.endswith('.pdf')]
print(pdf_urls)
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
pdf_urls = data_sheets['Data sheets'].dropna()
print(pdf_urls)
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    return ', '.join(links)
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
df = pd.read_excel("data/12_04/tags_12_04.xlsx")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)

# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
pdf_urls = data_sheets['Data sheets'].dropna()
print(pdf_urls)
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
pdf_urls = data_sheets['Data sheets'].dropna()
print(pdf_urls[0])
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
pdf_urls = data_sheets['Data sheets'].dropna()
print(pdf_urls["Data sheets"][0]])
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
pdf_urls = data_sheets['Data sheets'].dropna()
print(pdf_urls["Data sheets"][0])
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
pdf_urls = data_sheets['Data sheets'].dropna()
print(pdf_urls["Data sheets"][0])
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
pdf_urls = data_sheets['Data sheets'].dropna()
print(pdf_urls["Data sheets"][0])
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
pdf_urls = data_sheets['Data sheets'].dropna()
print(pdf_urls["Data sheets"])
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
print(data_sheets.columns)
pdf_urls = data_sheets['Data sheets'].dropna()

pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
print(data_sheets.columns)
pdf_urls = data_sheets['Data sheets'].dropna()

pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
# print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
print(data_sheets.columns)
pdf_urls = data_sheets['Data sheets'].dropna()
print(data_sheets.columns)

pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
# print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
print(data_sheets.columns)
pdf_urls = data_sheets['Data sheets'].dropna()
print(data_sheets["Data sheets"][0])

pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
# print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
print(data_sheets.columns)
pdf_urls = data_sheets['Data sheets'].dropna()
print(data_sheets["Data sheets"][1])

pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
# print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
print(data_sheets.columns)
pdf_urls = data_sheets['Data sheets'].dropna()
print(pdf_urls["Data sheets"][1])

pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
# print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
print(data_sheets.columns)
pdf_urls = data_sheets['Data sheets'].dropna()
print(pdf_urls.columns)
print(pdf_urls["Data sheets"][1])

pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
# print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
print(data_sheets.columns)
pdf_urls = data_sheets['Data sheets'].dropna()
print(pdf_urls.columns)
# print(pdf_urls["Data sheets"][1])

pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
# print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
print(data_sheets.columns)
data_sheets['Data sheets'].dropna()
print(data_sheets.columns)
# print(pdf_urls["Data sheets"][1])

pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
# print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
print(data_sheets.columns)
data_sheets['Data sheets'].dropna()
print(data_sheets.columns)
print(data_sheets["Data sheets"][1])

pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
# print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
print(data_sheets["Data sheets"][1])

pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
# print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
print(data_sheets["Data sheets"])

pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
# print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
print(data_sheets["Data sheets"].iloc[0])
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
# print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
print(data_sheets["Data sheets"].iloc[0])
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
# print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
print(data_sheets["Data sheets"].iloc[2])
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
# print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
print(data_sheets["Data sheets"].iloc[2])
pdf_url = 'https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Product_Name"].iloc[2]
print(data_sheets["Data sheets"].iloc[2])
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Product_Name"].iloc[2]
print(product_datasheet)
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
                # Stop adding text once "Technical Specification" is encountered
                break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
print(product_datasheet)
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            # if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
            #     # Stop adding text once "Technical Specification" is encountered
            #     break
            text += page_text

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
print(product_datasheet)
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            # if 'Technical highlights' in page_text or "TECHNICAL HIGHLIGHTS" in page_text:
            #     # Stop adding text once "Technical Specification" is encountered
            #     break
            text += page_text
    # iterate through the text and find the technical highlights and technical specification section and return the text before it
    text = text.split("\n")
    for i in range(len(text)):
        if "Technical highlights" in text[i] or "TECHNICAL HIGHLIGHTS" in text[i]:
            text = text[:i]
            break
        elif "Technical specification" in text[i] or "TECHNICAL SPECIFICATION" in text[i]:
            text = text[:i]
            break

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
print(product_datasheet)
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            text += page_text

    # Split the text into lines and find the "Technical highlights" or "Technical specification" section
    text = text.split("\n")
    for i in range(len(text)):
        if "Technical highlights" in text[i] or "TECHNICAL HIGHLIGHTS" in text[i]:
            text = text[:i]
            break
        elif "Technical specification" in text[i] or "TECHNICAL SPECIFICATION" in text[i]:
            text = text[:i]
            break

    # Join the lines with a newline character
    text = "\n".join(text)

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            page_text = page.extract_text()
            text += page_text

    # Split the text into lines and find the "Technical highlights" or "Technical specification" section
    text = text.split("\n")
    for i in range(len(text)):
        if "Technical highlights" in text[i] or "TECHNICAL HIGHLIGHTS" in text[i]:
            text = text[:i]
            break
        elif "Technical specification" in text[i] or "TECHNICAL SPECIFICATION" in text[i]:
            text = text[:i]
            break

    # Join the lines with a newline character
    text = "\n".join(text)

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            page_text = page.extract_text().split('\n')
            for line in page_text:
                if 'Features' in line:
                    in_features_section = True
                elif 'Technical Specification' in line:
                    break
                elif not line.startswith('•') and in_features_section:
                    in_features_section = False

                if not in_features_section:
                    text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            page_text = page.extract_text().split('\n')
            for line in page_text:
                if 'Features' in line:
                    in_features_section = True
                elif 'Technical Specification' in line or "TECHNICAL HIGHLIGHTS" in line or "Technical" in line or "TECHNICAL" in line or "TECHNICAL SPECIFICATIONS" in line or "Technical Specifications" in line or "Technical specification" in line or "Technical specifications" in line or "TECHNICAL SPECIFICATION" in line or "TECHNICAL SPECIFICATIONS" in line or "Technical Specification" in line or "Technical Specifications" in line or "Technical specification" in line or "Technical specifications" in line or "TECHNICAL SPECIFICATION" in line or "TECHNICAL SPECIFICATIONS" in line or "Technical Specification" in line or "Technical Specifications" in line or "Technical specification" in line or "Technical specifications" in line or "TECHNICAL SPECIFICATION" in line or "TECHNICAL SPECIFICATIONS" in line or "Technical Specification" in line or "Technical Specifications" in line or "Technical specification" in line or "Technical specifications" in line or "TECHNICAL SPECIFICATION" in line or "TECHNICAL SPECIFICATIONS" in line:
                    break
                elif not line.startswith('•') and in_features_section:
                    in_features_section = False

                if not in_features_section:
                    text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights)', line, re.IGNORECASE):
                    break
                elif not line.startswith('•') and in_features_section:
                    in_features_section = False

                if not in_features_section:
                    text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights)', line, re.IGNORECASE):
                    break
                elif not line.startswith('•') and in_features_section:
                    in_features_section = False

                if not in_features_section:
                    text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights)', line, re.IGNORECASE):
                    break
                elif not line.startswith('•') and in_features_section:
                    in_features_section = False

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights)', line, re.IGNORECASE):
                    break
                elif not line.startswith('•') and in_features_section:
                    in_features_section = False

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[3]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights)', line, re.IGNORECASE):
                    break
                elif not line.startswith('•') and in_features_section:
                    in_features_section = False

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[3]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break
                elif not line.startswith('•') and in_features_section:
                    in_features_section = False

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[3]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            # Define a crop box that excludes the margins
            # (You may need to adjust these values depending on the size of your margins)
            crop_box = (page.width * 0.1, page.height * 0.1, page.width * 0.9, page.height * 0.9)
            cropped_page = page.crop(crop_box)

            page_text = cropped_page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break
                elif not line.startswith('•') and in_features_section:
                    in_features_section = False

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            # Define a crop box that excludes the margins
            # (You may need to adjust these values depending on the size of your margins)
            crop_box = (page.width * 0.1, page.height * 0.1, page.width * 0.9, page.height * 0.9)
            cropped_page = page.crop(crop_box)

            page_text = cropped_page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break
                elif not line.startswith('•') and in_features_section:
                    in_features_section = False

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            # Define a crop box that excludes the margins
            # (You may need to adjust these values depending on the size of your margins)
            crop_box = (page.width * 0.1, page.height * 0.1, page.width * 0.9, page.height * 0.9)
            cropped_page = page.crop(crop_box)

            page_text = cropped_page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break
                elif not line.startswith('•') and in_features_section:
                    in_features_section = False

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[3]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break
                elif not line.startswith('•') and in_features_section:
                    in_features_section = False

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[3]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[3]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[4]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[5]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            # Define a crop box that excludes the margins and the last 1 cm from the bottom
            # (You may need to adjust these values depending on the size of your margins)
            crop_box = (page.width * 0.1, page.height * 0.1, page.width * 0.9, page.height - pdfplumber.utils.pdf_to_inches(1))
            cropped_page = page.crop(crop_box)

            page_text = cropped_page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            # Define a crop box that excludes the margins and the last 1 cm from the bottom
            # (You may need to adjust these values depending on the size of your margins)
            crop_box = (page.width * 0.1, page.height * 0.1, page.width * 0.9, page.height - pdfplumber.utils.pdf_to_inches(1))
            cropped_page = page.crop(crop_box)

            page_text = cropped_page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for page in pdf.pages:
            # Define a crop box that excludes the margins and the last 1 cm from the bottom
            # (You may need to adjust these values depending on the size of your margins)
            crop_box = (page.width * 0.1, page.height * 0.1, page.width * 0.9, page.height - 28.3)            
            cropped_page = page.crop(crop_box)

            page_text = cropped_page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (page.width * 0.1, page.height * 0.1, page.width * 0.9, page.height - 28.3)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 28.3)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 26.3)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 1.3)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 28.3, page.width, page.height)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 50, page.width, page.height)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 100, page.width, page.height)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 200, page.width, page.height)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                print(i)
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 200, page.width, page.height)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 200, page.width, page.height)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 400, page.width, page.height)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, 400)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, 200)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, 150)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, 100)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, 50)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, 800)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, page.height - 28)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, page.height - 100)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, page.height - 50)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, page.height - 60)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, page.height - 65)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, page.height - 69)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[6]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[5]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
import requests
import pdfplumber
import os

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        for page in pdf.pages:
            text += page.extract_text()

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
import PyPDF2
import io

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Open the PDF file
        reader = PyPDF2.PdfFileReader(f)

        # Extract text from each page
        text = ''
        for i in range(reader.getNumPages()):
            page = reader.getPage(i)
            text += page.extractText()

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
from PyPDF2 import PdfReader
import io

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Open the PDF file
        reader = PdfReader(f)

        # Extract text from each page
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
from PyPDF2 import PdfReader
import io

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Open the PDF file
        reader = PdfReader(f)

        # Extract text from each page
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url) 
print(pdf_text)
import requests
from pdfminer.high_level import extract_text
import io

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Extract text from the PDF
        text = extract_text(f)

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
from pdfminer.high_level import extract_text
import io

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Extract text from the PDF
        text = extract_text(f)

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
from PIL import Image
import pytesseract
import io
import pdf2image

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Convert PDF to images
        images = pdf2image.convert_from_bytes(f.read())

    # Extract text from each image
    text = ''
    for image in images:
        text += pytesseract.image_to_string(image)

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
from PIL import Image
import pytesseract
import io
import pdf2image

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Convert PDF to images
        images = pdf2image.convert_from_bytes(f.read())

    # Extract text from each image
    text = ''
    for image in images:
        text += pytesseract.image_to_string(image)

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
from PIL import Image
import pytesseract
import io
import pdf2image

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Convert PDF to images
        images = pdf2image.convert_from_bytes(f.read())

    # Extract text from each image
    text = ''
    for image in images:
        text += pytesseract.image_to_string(image)

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
from PIL import Image
import pytesseract
import io
import pdf2image

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Convert PDF to images
        images = pdf2image.convert_from_bytes(f.read())

    # Extract text from each image
    text = ''
    for image in images:
        text += pytesseract.image_to_string(image)

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests

def print_pdf_content(url):
    # Download the PDF file
    response = requests.get(url)
    print(response.content)

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
print_pdf_content(pdf_url)
import requests
from PyPDF2 import PdfFileReader
import io

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Open the PDF file
        reader = PdfFileReader(f)

        # Extract text from each page
        text = ''
        for i in range(reader.getNumPages()):
            page = reader.getPage(i)
            text += page.extractText()

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
from PyPDF2 import PdfFileReader
import io

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Open the PDF file
        reader = PdfReader(f)

        # Extract text from each page
        text = ''
        for i in range(reader.getNumPages()):
            page = reader.getPage(i)
            text += page.extractText()

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
from PyPDF2 import PdfReader
import io

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Open the PDF file
        reader = PdfReader(f)

        # Extract text from each page
        text = ''
        for i in range(reader.getNumPages()):
            page = reader.getPage(i)
            text += page.extractText()

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
from PyPDF2 import PdfReader
import io

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Open the PDF file
        reader = PdfReader(f)

        # Extract text from each page
        text = ''
        for i in range(len(reader.pages)):
            page = reader.getPage(i)
            text += page.extractText()

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url)
print(pdf_text)
import requests
from PyPDF2 import PdfReader
import io

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Open the PDF file
        reader = PdfReader(f)

        # Extract text from each page
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url) 
print(pdf_text)
import requests
from PyPDF2 import PdfReader
import io

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Open the PDF file
        reader = PdfReader(f)

        # Extract text from each page
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url) 
print(pdf_text)
import requests
from PyPDF2 import PdfReader
import io

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Open the PDF file
        reader = PdfReader(f)

        # Extract text from each page
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url) 
print(pdf_text)
import requests
from bs4 import BeautifulSoup
import pandas as pd 
import re
import os
import pdfplumber
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[5]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[5]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    return ', '.join(links)
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
df = pd.read_excel("data/12_04/tags_12_04.xlsx")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)

# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                print(len(pdf.pages))
                print(page.height)
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[5]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")

# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            print(i)
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[5]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")

# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")

# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[5]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")

# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features|FUNCTIONALITY', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[5]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets.head(40)

# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 6:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features|FUNCTIONALITY', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications?|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[5]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets.head(40)

# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 6:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features|FUNCTIONALITY', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[5]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets.head(40)

# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)
import streamlit as st
import pandas as pd
from openai._client import OpenAI

client = OpenAI(
    api_key=st.secrets["openai"]["api_key"],
)
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": "You are a text editor, that edits text into readable text bulks and headings. Use the same kind of language and tone and write style as the text you are editing."
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\nPlease format this text."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages,
        response_format={ "type": "json_object" }
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
import streamlit as st
import pandas as pd
from openai._client import OpenAI

client = OpenAI(
    api_key=st.secrets["openai"]["api_key"],
)
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

print(df_with_text["Scraped Text"][0])
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][0])
output_text = generate_text(input_text)

print(output_text)
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": "You are a text editor, that edits text into readable text bulks and headings. Use the same kind of language and tone and write style as the text you are editing."
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\nPlease format this text."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][0])
output_text = generate_text(input_text)

print(output_text)
print(input_text)
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": "You are a text editor, that edits text into readable text bulks and headings. Use the same kind of language and tone and write style as the text you are editing. Do not change the meaning of the text, or add any new information. Format the text as little as possible."
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\nPlease format this text."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][0])
output_text = generate_text(input_text)

print(output_text)
print(input_text)
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    return ', '.join(links)
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
number= 3
print(find_datasheets(df["url"][number]))
print(df["url"][number])
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    return ', '.join(links)
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
number= 4
print(find_datasheets(df["url"][number]))
print(df["url"][number])
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    return ', '.join(links)
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
number= 4
print("text = ",find_datasheets(df["url"][number]))
print(df["url"][number])
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 6:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features|FUNCTIONALITY', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[5]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 6:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('features|FUNCTIONALITY', line, re.IGNORECASE):
                    in_features_section = True
                elif re.search('technical (specifications|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 6:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('technical (specifications|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets.head(40)

# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
print(input_text)
assistant = client.beta.assistants.create(
    name="Kongberg content",
    instructions="""
      Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 250 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed.Write these three blocks: 
      Block 1 : [100 - 250 words. ] Provide factual information blocks to explain what value the products bring.
      minimum of one or a maximum of three.

      Block 2 : [40-100 words] Provide the key features for the product. As many as needed

      Block 3 : [10-150] Add technical specifications related to the product. expected structure is "category, parameters and parameter value" As many as needed.

      Return as Json. """,
    model="gpt-3.5-turbo-1106",
    tools=[{"type": "retrieval"}],
)
# from a pdf url create a pdf file
def create_pdf(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)
    return 'temp.pdf'

def create_file(url):
  file = client.files.create(file= create_pdf(url),purpose='assistants')
  return file
ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Tell me who is acquirer",
    file_ids=[create_file(url)]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)
      pprint(messages)
      break
    else:
      ### sleep again
      time.sleep(2)
# from a pdf url create a pdf file
def create_pdf(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)
    return 'temp.pdf'

def create_file(url):
  file = client.files.create(file= create_pdf(url),purpose='assistants')
  return file
assistant = client.beta.assistants.create(
    name="Kongberg content",
    instructions="""
      Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 250 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed.Write these three blocks: 
      Block 1 : [100 - 250 words. ] Provide factual information blocks to explain what value the products bring.
      minimum of one or a maximum of three.

      Block 2 : [40-100 words] Provide the key features for the product. As many as needed

      Block 3 : [10-150] Add technical specifications related to the product. expected structure is "category, parameters and parameter value" As many as needed.

      Return as Json. """,
    model="gpt-3.5-turbo-1106",
    tools=[{"type": "retrieval"}],
)
thread = client.beta.threads.create()
ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url)
  file = client.files.create(file=pdf_file,purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Tell me who is acquirer",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)
      pprint(messages)
      break
    else:
      ### sleep again
      time.sleep(2)
ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
# from a pdf url create a pdf file
def create_pdf(url, path):
    # Download the PDF file
    response = requests.get(url)
    with open(os.path.join(path, 'temp.pdf'), 'wb') as f:
        f.write(response.content)
    return os.path.join(path, 'temp.pdf')

def create_file(url):
  file = client.files.create(file= create_pdf(url),purpose='assistants')
  return file
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url)
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Tell me who is acquirer",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)
      pprint(messages)
      break
    else:
      ### sleep again
      time.sleep(2)
ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Tell me who is acquirer",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)
      pprint(messages)
      break
    else:
      ### sleep again
      time.sleep(2)
ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
# from a pdf url create a pdf file
def create_pdf(url, path):
    # Download the PDF file
    response = requests.get(url)
    with open(os.path.join(path, 'temp.pdf'), 'wb') as f:
        f.write(response.content)
    return os.path.join(path, 'temp.pdf')

def create_file(url):
  file = client.files.create(file= create_pdf(url),purpose='assistants')
  return file
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Tell me who is acquirer",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)
      pprint(messages)
      break
    else:
      ### sleep again
      time.sleep(2)
ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
# from a pdf url create a pdf file
def create_pdf(url, path):
    os.makedirs(path, exist_ok=True)
    # Download the PDF file
    response = requests.get(url)
    with open(os.path.join(path, 'temp.pdf'), 'wb') as f:
        f.write(response.content)
    return os.path.join(path, 'temp.pdf')

def create_file(url):
  file = client.files.create(file= create_pdf(url),purpose='assistants')
  return file
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Tell me who is acquirer",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)
      pprint(messages)
      break
    else:
      ### sleep again
      time.sleep(2)
ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Tell me who is acquirer",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      print(last_message_content)
      break
    else:
      ### sleep again
      time.sleep(2)
ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
assistant = client.beta.assistants.create(
    name="Kongberg content",
    instructions="""
      Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 250 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed.Write these three blocks: 
      Block 1 : [100 - 250 words. ] Provide factual information blocks to explain what value the products bring.
      minimum of one or a maximum of three.

      Block 2 : [40-100 words] Provide the key features for the product. As many as needed

      Block 3 : [10-150] Add technical specifications related to the product. expected structure is "category, parameters and parameter value" As many as needed.

      Return as Json. """,
    model="gpt-3.5-turbo-1106",
    tools=[{"type": "retrieval"}],
)
thread = client.beta.threads.create()
# from a pdf url create a pdf file
def create_pdf(url, path):
    os.makedirs(path, exist_ok=True)
    # Download the PDF file
    response = requests.get(url)
    with open(os.path.join(path, 'temp.pdf'), 'wb') as f:
        f.write(response.content)
    return os.path.join(path, 'temp.pdf')

def create_file(url):
  file = client.files.create(file= create_pdf(url),purpose='assistants')
  return file
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Tell me who is acquirer",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      print(last_message_content)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
print(output_text)
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="Tell me who is acquirer",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      print(last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="I have a text that I want to format into headings and text bulks. Please format this text.",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      print(last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
print(output_text)
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Use the file as context. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 250 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed.Write these three blocks: 
      Block 1 : [100 - 250 words. ] Provide factual information blocks to explain what value the products bring.
      minimum of one or a maximum of three.

      Block 2 : [40-100 words] Provide the key features for the product. As many as needed

      Block 3 : [10-150] Add technical specifications related to the product. expected structure is "category, parameters and parameter value" As many as needed.

      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      print(last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
print(output_text)
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Use the file as context. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 250 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      print(last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Use the file as context. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      print(last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
print(output_text)
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Use the file as context. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Extract the message content
      message_content = message.content[0].text
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content.value += '\n' + '\n'.join(citations)
      print(message_content.value)
      print(last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
print(output_text)
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Use the file as context. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Extract the message content
      message_content = message.content[0].text
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content.value += '\n' + '\n'.join(citations)
      print("content_annotation " , message_content.value)
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
print(output_text)
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Use the file as context. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Extract the message content
      message_content = message.content[0].text.value
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content += '\n' + '\n'.join(citations)
      print("content_annotation " , message_content.value)
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Use the file as context. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )
  message = client.beta.threads.messages.retrieve(
    thread_id=thread.id,
    message_id=message.id
  )
  # Extract the message content
  message_content = message.content[0].text
  annotations = message_content.annotations
  citations = []

  # Iterate over the annotations and add footnotes
  for index, annotation in enumerate(annotations):
      # Replace the text with a footnote
      message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

      # Gather citations based on annotation attributes
      if (file_citation := getattr(annotation, 'file_citation', None)):
          cited_file = client.files.retrieve(file_citation.file_id)
          citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
      elif (file_path := getattr(annotation, 'file_path', None)):
          cited_file = client.files.retrieve(file_path.file_id)
          citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
          # Note: File download functionality not implemented above for brevity

  # Add footnotes to the end of the message before displaying to user
  message_content.value += '\n' + '\n'.join(citations)
  print("content_annotation " , message_content.value)

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

     
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
print(output_text)
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Use the file as context. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Retrieve the message object
      message = client.beta.threads.messages.retrieve(
        thread_id=thread.id,
        message_id=message.id
      )

      # Extract the message content
      message_content = message.content[0].text
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content.value += '\n' + '\n'.join(citations)
      print("content_annotation " , message_content.value)
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
print(output_text)
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Use the file as context. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks.
      For example block: heading: "Greater endurance", text: "With spaciuous moopool and rack mount the Sounder USV System is a flexible and adaptive paltform for different applications. Te onboard power generation provides enough power to operate several payloads at once. 

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Retrieve the message object
      message = client.beta.threads.messages.retrieve(
        thread_id=thread.id,
        message_id=message.id
      )

      # Extract the message content
      message_content = message.content[0].text
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content.value += '\n' + '\n'.join(citations)
      print("content_annotation " , message_content.value)
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
print(output_text)
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks.
      For example : 
      Product Evolution
      HUGIN has been continuously evolving since development began in 1991.
      From the first commercial survey in 1997, KONGSBERG and our partners
      at the Norwegian Defense Research Establishment (FFI) have been at the
      forefront of underwater robotic technology. HUGIN continues to deliver
      World-class performance and new capabilities and features are added
      through software updates and vehicle upgrades.
      Deployability
      HUGIN can be deployed from dedicated vessels, vessels of opportunity
      or from shore. The complete HUGIN system including operator consoles,
      launch and recovery system and the AUV itself can be delivered in
      DNV-certified offshore containers. The containers allows for transport
      by sea, air and land and mobilization is easy with only an external power
      connection required. Various container sizes are available to meet the
      customer needs.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Retrieve the message object
      message = client.beta.threads.messages.retrieve(
        thread_id=thread.id,
        message_id=message.id
      )

      # Extract the message content
      message_content = message.content[0].text
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content.value += '\n' + '\n'.join(citations)
      print("content_annotation " , message_content.value)
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
assistant = client.beta.assistants.create(
    name="Kongberg content",
    instructions="""
      Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks.
      For example : 
      Product Evolution
      HUGIN has been continuously evolving since development began in 1991.
      From the first commercial survey in 1997, KONGSBERG and our partners
      at the Norwegian Defense Research Establishment (FFI) have been at the
      forefront of underwater robotic technology. HUGIN continues to deliver
      World-class performance and new capabilities and features are added
      through software updates and vehicle upgrades.
      Deployability
      HUGIN can be deployed from dedicated vessels, vessels of opportunity
      or from shore. The complete HUGIN system including operator consoles,
      launch and recovery system and the AUV itself can be delivered in
      DNV-certified offshore containers. The containers allows for transport
      by sea, air and land and mobilization is easy with only an external power
      connection required. Various container sizes are available to meet the
      customer needs.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.

     """,
    model="gpt-3.5-turbo-1106",
    tools=[{"type": "retrieval"}],
)
thread = client.beta.threads.create()
# from a pdf url create a pdf file
def create_pdf(url, path):
    os.makedirs(path, exist_ok=True)
    # Download the PDF file
    response = requests.get(url)
    with open(os.path.join(path, 'temp.pdf'), 'wb') as f:
        f.write(response.content)
    return os.path.join(path, 'temp.pdf')

def create_file(url):
  file = client.files.create(file= create_pdf(url),purpose='assistants')
  return file
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks.
      For example : 
      Product Evolution
      HUGIN has been continuously evolving since development began in 1991.
      From the first commercial survey in 1997, KONGSBERG and our partners
      at the Norwegian Defense Research Establishment (FFI) have been at the
      forefront of underwater robotic technology. HUGIN continues to deliver
      World-class performance and new capabilities and features are added
      through software updates and vehicle upgrades.
      Deployability
      HUGIN can be deployed from dedicated vessels, vessels of opportunity
      or from shore. The complete HUGIN system including operator consoles,
      launch and recovery system and the AUV itself can be delivered in
      DNV-certified offshore containers. The containers allows for transport
      by sea, air and land and mobilization is easy with only an external power
      connection required. Various container sizes are available to meet the
      customer needs.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Retrieve the message object
      message = client.beta.threads.messages.retrieve(
        thread_id=thread.id,
        message_id=message.id
      )

      # Extract the message content
      message_content = message.content[0].text
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content.value += '\n' + '\n'.join(citations)
      print("content_annotation " , message_content.value)
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks.
      For example : 
      Product Evolution
      HUGIN has been continuously evolving since development began in 1991.
      From the first commercial survey in 1997, KONGSBERG and our partners
      at the Norwegian Defense Research Establishment (FFI) have been at the
      forefront of underwater robotic technology. HUGIN continues to deliver
      World-class performance and new capabilities and features are added
      through software updates and vehicle upgrades.
      Deployability
      HUGIN can be deployed from dedicated vessels, vessels of opportunity
      or from shore. The complete HUGIN system including operator consoles,
      launch and recovery system and the AUV itself can be delivered in
      DNV-certified offshore containers. The containers allows for transport
      by sea, air and land and mobilization is easy with only an external power
      connection required. Various container sizes are available to meet the
      customer needs.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(10)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Retrieve the message object
      message = client.beta.threads.messages.retrieve(
        thread_id=thread.id,
        message_id=message.id
      )

      # Extract the message content
      message_content = message.content[0].text
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content.value += '\n' + '\n'.join(citations)
      print("content_annotation " , message_content.value)
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks.
      For example : 
      Product Evolution
      HUGIN has been continuously evolving since development began in 1991.
      From the first commercial survey in 1997, KONGSBERG and our partners
      at the Norwegian Defense Research Establishment (FFI) have been at the
      forefront of underwater robotic technology. HUGIN continues to deliver
      World-class performance and new capabilities and features are added
      through software updates and vehicle upgrades.
      Deployability
      HUGIN can be deployed from dedicated vessels, vessels of opportunity
      or from shore. The complete HUGIN system including operator consoles,
      launch and recovery system and the AUV itself can be delivered in
      DNV-certified offshore containers. The containers allows for transport
      by sea, air and land and mobilization is easy with only an external power
      connection required. Various container sizes are available to meet the
      customer needs.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(3)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Retrieve the message object
      message = client.beta.threads.messages.retrieve(
        thread_id=thread.id,
        message_id=message.id
      )

      # Extract the message content
      message_content = message.content[0].text
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content.value += '\n' + '\n'.join(citations)
      print("content_annotation " , message_content.value)
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks.
      For example : 
      Product Evolution
      HUGIN has been continuously evolving since development began in 1991.
      From the first commercial survey in 1997, KONGSBERG and our partners
      at the Norwegian Defense Research Establishment (FFI) have been at the
      forefront of underwater robotic technology. HUGIN continues to deliver
      World-class performance and new capabilities and features are added
      through software updates and vehicle upgrades.
      Deployability
      HUGIN can be deployed from dedicated vessels, vessels of opportunity
      or from shore. The complete HUGIN system including operator consoles,
      launch and recovery system and the AUV itself can be delivered in
      DNV-certified offshore containers. The containers allows for transport
      by sea, air and land and mobilization is easy with only an external power
      connection required. Various container sizes are available to meet the
      customer needs.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    print(run_status.model_dump_json(indent=4))
    time.sleep(3)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Retrieve the message object
      message = client.beta.threads.messages.retrieve(
        thread_id=thread.id,
        message_id=message.id
      )

      # Extract the message content
      message_content = message.content[0].text
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content.value += '\n' + '\n'.join(citations)
      print("content_annotation " , message_content.value)
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks.
      For example : 
      Product Evolution
      HUGIN has been continuously evolving since development began in 1991.
      From the first commercial survey in 1997, KONGSBERG and our partners
      at the Norwegian Defense Research Establishment (FFI) have been at the
      forefront of underwater robotic technology. HUGIN continues to deliver
      World-class performance and new capabilities and features are added
      through software updates and vehicle upgrades.
      Deployability
      HUGIN can be deployed from dedicated vessels, vessels of opportunity
      or from shore. The complete HUGIN system including operator consoles,
      launch and recovery system and the AUV itself can be delivered in
      DNV-certified offshore containers. The containers allows for transport
      by sea, air and land and mobilization is easy with only an external power
      connection required. Various container sizes are available to meet the
      customer needs.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    # print(run_status.model_dump_json(indent=4))
    time.sleep(3)
    print(run_status.status)
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Retrieve the message object
      message = client.beta.threads.messages.retrieve(
        thread_id=thread.id,
        message_id=message.id
      )

      # Extract the message content
      message_content = message.content[0].text
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content.value += '\n' + '\n'.join(citations)
      print("content_annotation " , message_content.value)
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
assistant = client.beta.assistants.create(
    name="Kongberg content",
    instructions="""
      Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks.
      For example : 
      Product Evolution
      HUGIN has been continuously evolving since development began in 1991.
      From the first commercial survey in 1997, KONGSBERG and our partners
      at the Norwegian Defense Research Establishment (FFI) have been at the
      forefront of underwater robotic technology. HUGIN continues to deliver
      World-class performance and new capabilities and features are added
      through software updates and vehicle upgrades.
      Deployability
      HUGIN can be deployed from dedicated vessels, vessels of opportunity
      or from shore. The complete HUGIN system including operator consoles,
      launch and recovery system and the AUV itself can be delivered in
      DNV-certified offshore containers. The containers allows for transport
      by sea, air and land and mobilization is easy with only an external power
      connection required. Various container sizes are available to meet the
      customer needs.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.

     """,
    model="gpt-3.5-turbo-1106",
    tools=[{"type": "retrieval"}],
)
thread = client.beta.threads.create()
# from a pdf url create a pdf file
def create_pdf(url, path):
    os.makedirs(path, exist_ok=True)
    # Download the PDF file
    response = requests.get(url)
    with open(os.path.join(path, 'temp.pdf'), 'wb') as f:
        f.write(response.content)
    return os.path.join(path, 'temp.pdf')

def create_file(url):
  file = client.files.create(file= create_pdf(url),purpose='assistants')
  return file
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks.
      For example : 
      Product Evolution
      HUGIN has been continuously evolving since development began in 1991.
      From the first commercial survey in 1997, KONGSBERG and our partners
      at the Norwegian Defense Research Establishment (FFI) have been at the
      forefront of underwater robotic technology. HUGIN continues to deliver
      World-class performance and new capabilities and features are added
      through software updates and vehicle upgrades.
      Deployability
      HUGIN can be deployed from dedicated vessels, vessels of opportunity
      or from shore. The complete HUGIN system including operator consoles,
      launch and recovery system and the AUV itself can be delivered in
      DNV-certified offshore containers. The containers allows for transport
      by sea, air and land and mobilization is easy with only an external power
      connection required. Various container sizes are available to meet the
      customer needs.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    # print(run_status.model_dump_json(indent=4))
    time.sleep(3)
    print(run_status.status)
    if run_status.status == 'failed':
      print("failed")
      break
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Retrieve the message object
      message = client.beta.threads.messages.retrieve(
        thread_id=thread.id,
        message_id=message.id
      )

      # Extract the message content
      message_content = message.content[0].text
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content.value += '\n' + '\n'.join(citations)
      print("content_annotation " , message_content.value)
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
print(output_text)
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": "You are a text editor, that edits text into readable text bulks and headings. Use the same kind of language and tone and write style as the text you are editing. Do not change the meaning of the text, or add any new information. Format the text as little as possible."
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\nPlease format this text."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
import streamlit as st
import pandas as pd
from openai._client import OpenAI

client = OpenAI(
    api_key=st.secrets["openai"]["api_key"],
)
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
print(input_text)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 6:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 10)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('technical (specifications|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 6:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if re.search('technical (specifications|highlights|data)', line, re.IGNORECASE):                    
                    break

                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 6:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets.head(40)

# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": "You are a text editor, that edits text into readable text bulks and headings. Use the same kind of language and tone and write style as the text you are editing. Do not change the meaning of the text, or add any new information. Format the text as little as possible."
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\nPlease format this text."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
import streamlit as st
import pandas as pd
from openai._client import OpenAI

client = OpenAI(
    api_key=st.secrets["openai"]["api_key"],
)
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": "You are a text editor, that edits text into readable text bulks and headings. Use the same kind of language and tone and write style as the text you are editing. Do not change the meaning of the text, or add any new information. Format the text as little as possible."
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\nPlease format this text."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": """ 
                Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

                Write the following three content blocks:

                Block 1 (100 - 400 words):
                Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks.
                For example : 
                Product Evolution
                HUGIN has been continuously evolving since development began in 1991.
                From the first commercial survey in 1997, KONGSBERG and our partners
                at the Norwegian Defense Research Establishment (FFI) have been at the
                forefront of underwater robotic technology. HUGIN continues to deliver
                World-class performance and new capabilities and features are added
                through software updates and vehicle upgrades.
                Deployability
                HUGIN can be deployed from dedicated vessels, vessels of opportunity
                or from shore. The complete HUGIN system including operator consoles,
                launch and recovery system and the AUV itself can be delivered in
                DNV-certified offshore containers. The containers allows for transport
                by sea, air and land and mobilization is easy with only an external power
                connection required. Various container sizes are available to meet the
                customer needs.

                Block 2 (40 - 100 words):
                List the key features of the product. Include as many as needed. Use bullet points for each feature.

                Block 3 (10 - 150 words):
                Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.

                """
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\nPlease format this text."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
assistant = client.beta.assistants.create(
    name="Kongberg content",
    instructions="""
      Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks.
      For example : 
      Product Evolution
      HUGIN has been continuously evolving since development began in 1991.
      From the first commercial survey in 1997, KONGSBERG and our partners
      at the Norwegian Defense Research Establishment (FFI) have been at the
      forefront of underwater robotic technology. HUGIN continues to deliver
      World-class performance and new capabilities and features are added
      through software updates and vehicle upgrades.
      Deployability
      HUGIN can be deployed from dedicated vessels, vessels of opportunity
      or from shore. The complete HUGIN system including operator consoles,
      launch and recovery system and the AUV itself can be delivered in
      DNV-certified offshore containers. The containers allows for transport
      by sea, air and land and mobilization is easy with only an external power
      connection required. Various container sizes are available to meet the
      customer needs.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.

     """,
    model="gpt-3.5-turbo-1106",
    tools=[{"type": "retrieval"}],
)
thread = client.beta.threads.create()
# from a pdf url create a pdf file
def create_pdf(url, path):
    os.makedirs(path, exist_ok=True)
    # Download the PDF file
    response = requests.get(url)
    with open(os.path.join(path, 'temp.pdf'), 'wb') as f:
        f.write(response.content)
    return os.path.join(path, 'temp.pdf')

def create_file(url):
  file = client.files.create(file= create_pdf(url),purpose='assistants')
  return file
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks.
      For example : 
      Product Evolution
      HUGIN has been continuously evolving since development began in 1991.
      From the first commercial survey in 1997, KONGSBERG and our partners
      at the Norwegian Defense Research Establishment (FFI) have been at the
      forefront of underwater robotic technology. HUGIN continues to deliver
      World-class performance and new capabilities and features are added
      through software updates and vehicle upgrades.
      Deployability
      HUGIN can be deployed from dedicated vessels, vessels of opportunity
      or from shore. The complete HUGIN system including operator consoles,
      launch and recovery system and the AUV itself can be delivered in
      DNV-certified offshore containers. The containers allows for transport
      by sea, air and land and mobilization is easy with only an external power
      connection required. Various container sizes are available to meet the
      customer needs.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    # print(run_status.model_dump_json(indent=4))
    time.sleep(3)
    print(run_status.status)
    if run_status.status == 'failed':
      print("failed")
      break
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Retrieve the message object
      message = client.beta.threads.messages.retrieve(
        thread_id=thread.id,
        message_id=message.id
      )

      # Extract the message content
      message_content = message.content[0].text
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content.value += '\n' + '\n'.join(citations)
      print("content_annotation " , message_content.value)
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
print(output_text)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets.head(40)

# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 6:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 60)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets.head(40)

# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": """ 
                Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

                Write the following three content blocks:

                Block 1 (100 - 400 words):
                Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks.
                For example : 
                Product Evolution
                HUGIN has been continuously evolving since development began in 1991.
                From the first commercial survey in 1997, KONGSBERG and our partners
                at the Norwegian Defense Research Establishment (FFI) have been at the
                forefront of underwater robotic technology. HUGIN continues to deliver
                World-class performance and new capabilities and features are added
                through software updates and vehicle upgrades.
                Deployability
                HUGIN can be deployed from dedicated vessels, vessels of opportunity
                or from shore. The complete HUGIN system including operator consoles,
                launch and recovery system and the AUV itself can be delivered in
                DNV-certified offshore containers. The containers allows for transport
                by sea, air and land and mobilization is easy with only an external power
                connection required. Various container sizes are available to meet the
                customer needs.

                Block 2 (40 - 100 words):
                List the key features of the product. Include as many as needed. Use bullet points for each feature.

                Block 3 (10 - 350 words):
                Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.

                """
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\n Please format this text using the same words and languange as the text. Do not change the text to much, and do not add information that is not there."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks. If the text has headings, use these headings.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    # print(run_status.model_dump_json(indent=4))
    time.sleep(3)
    print(run_status.status)
    if run_status.status == 'failed':
      print("failed")
      break
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Retrieve the message object
      message = client.beta.threads.messages.retrieve(
        thread_id=thread.id,
        message_id=message.id
      )

      # Extract the message content
      message_content = message.content[0].text
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content.value += '\n' + '\n'.join(citations)
      print("content_annotation " , message_content.value)
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
assistant = client.beta.assistants.create(
    name="Kongberg content",
    instructions="""Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks. If the text has headings, use these headings.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    model="gpt-3.5-turbo-1106",
    tools=[{"type": "retrieval"}],
)
thread = client.beta.threads.create()
# from a pdf url create a pdf file
def create_pdf(url, path):
    os.makedirs(path, exist_ok=True)
    # Download the PDF file
    response = requests.get(url)
    with open(os.path.join(path, 'temp.pdf'), 'wb') as f:
        f.write(response.content)
    return os.path.join(path, 'temp.pdf')

def create_file(url):
  file = client.files.create(file= create_pdf(url),purpose='assistants')
  return file
import os
import openai
import time
from pprint import pprint

def ask_gpt(url):
  pdf_file = create_pdf(url, "data/gpt_content")
  file = client.files.create(file=open(pdf_file, "rb"),purpose='assistants')
# Add a Message to a Thread
  message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content="""Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

      Write the following three content blocks:

      Block 1 (100 - 400 words):
      Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks. If the text has headings, use these headings.

      Block 2 (40 - 100 words):
      List the key features of the product. Include as many as needed. Use bullet points for each feature.

      Block 3 (10 - 150 words):
      Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


      Return as Json.""",
    file_ids=[file.id]  # Add the file to the message
  )

  # Run the Assistant
  run = client.beta.threads.runs.create(thread_id=thread.id,assistant_id=assistant.id,instructions="Please answer the user, just using text from the file.")
  print(run.model_dump_json(indent=4))

  # If run is 'completed', get messages and print
  while True:
    # Retrieve the run status
    run_status = client.beta.threads.runs.retrieve(thread_id=thread.id,run_id=run.id)
    # print(run_status.model_dump_json(indent=4))
    time.sleep(3)
    print(run_status.status)
    if run_status.status == 'failed':
      print("failed")
      break
    if run_status.status == 'completed':
      messages = client.beta.threads.messages.list(thread_id=thread.id)

      # Get the last message from the assistant
      last_message = messages.data[0]

      # Get the content of the last message
      last_message_content = last_message.content[0].text.value

      # Retrieve the message object
      message = client.beta.threads.messages.retrieve(
        thread_id=thread.id,
        message_id=message.id
      )

      # Extract the message content
      message_content = message.content[0].text
      annotations = message_content.annotations
      citations = []

      # Iterate over the annotations and add footnotes
      for index, annotation in enumerate(annotations):
          # Replace the text with a footnote
          message_content.value = message_content.value.replace(annotation.text, f' [{index}]')

          # Gather citations based on annotation attributes
          if (file_citation := getattr(annotation, 'file_citation', None)):
              cited_file = client.files.retrieve(file_citation.file_id)
              citations.append(f'[{index}] {file_citation.quote} from {cited_file.filename}')
          elif (file_path := getattr(annotation, 'file_path', None)):
              cited_file = client.files.retrieve(file_path.file_id)
              citations.append(f'[{index}] Click <here> to download {cited_file.filename}')
              # Note: File download functionality not implemented above for brevity

      # Add footnotes to the end of the message before displaying to user
      message_content.value += '\n' + '\n'.join(citations)
      print("content_annotation " , message_content.value)
      print("lat_message " ,last_message_content)
      print("whole message: ", message)
      return last_message_content
      break
    else:
      ### sleep again
      time.sleep(2)
print(output_text)
import streamlit as st
import pandas as pd
from openai._client import OpenAI

client = OpenAI(
    api_key=st.secrets["openai"]["api_key"],
)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets.head(40)

# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)
import streamlit as st
import pandas as pd
from openai._client import OpenAI

client = OpenAI(
    api_key=st.secrets["openai"]["api_key"],
)
import streamlit as st
import pandas as pd
from openai._client import OpenAI

client = OpenAI(
    api_key=st.secrets["openai"]["api_key"],
)
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": """Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

                Write the following three content blocks:

                Block 1 (100 - 400 words):
                Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks. If the text has headings, use these headings.

                Block 2 (40 - 100 words):
                List the key features of the product. Include as many as needed. Use bullet points for each feature.

                Block 3 (10 - 150 words):
                Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


                Return as Json."""
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\n Please format this text using the same words and languange as the text. Do not change the text to much, and do not add information that is not there."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
print(input_text)
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": """Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

                Write the following three content blocks:

                Block 1 (200 - 400 words):
                Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks. If the text has headings, use these headings. Have at elast 100 words in each block.

                Block 2 (40 - 100 words):
                List the key features of the product. Include as many as needed. Use bullet points for each feature.

                Block 3 (10 - 150 words):
                Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


                Return as Json."""
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\n Please format this text using the same words and languange as the text. Do not change the text to much, and do not add information that is not there."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": """Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

                Write the following three content blocks:

                Block 1 (200 - 400 words):
                Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks. If the text has headings, use these headings. Have at elast 100 words in each block and add a suitable heading for each block.

                Block 2 (40 - 100 words):
                List the key features of the product. Include as many as needed. Use bullet points for each feature.

                Block 3 (10 - 150 words):
                Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


                Return as Json."""
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\n Please format this text using the same words and languange as the text. Do not change the text to much, and do not add information that is not there."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
import streamlit as st
import pandas as pd
from openai._client import OpenAI

client = OpenAI(
    api_key=st.secrets["openai"]["api_key"],
)
system_prompt = """
                Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

                Write the following three content blocks:

                Block 1 (200 - 400 words):
                Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks. If the text has headings, use these headings. Have at elast 100 words in each block and add a suitable heading for each block.

                Block 2 (40 - 100 words):
                List the key features of the product. Include as many as needed. Use bullet points for each feature.

                Block 3 (10 - 150 words):
                Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


                Return as Json."""
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\n Please format this text using the same words and languange as the text. Do not change the text to much, and do not add information that is not there."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
print(input_text)
system_prompt = """
                Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

                Write the following three content blocks:

                Block 1 (200 - 400 words):
                Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks. If the text has headings, use these headings. Have at elast 100 words in each block and add a suitable heading for each block.

                Block 2 (40 - 100 words):
                List the key features or benefits of the product. Include as many as needed. Use bullet points for each feature. Use the same bullet points as the pdf.

                Block 3 (10 - 150 words):
                Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.


                Return as Json."""
assistant = client.beta.assistants.create(
    name="Kongberg content",
    instructions=system_prompt,
    model="gpt-3.5-turbo-1106",
    response_format={ "type": "json_object" },

    tools=[{"type": "retrieval"}],
)
thread = client.beta.threads.create()
assistant = client.beta.assistants.create(
    name="Kongberg content",
    instructions=system_prompt,
    model="gpt-3.5-turbo-1106",
    tools=[{"type": "retrieval"}],
)
thread = client.beta.threads.create()
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\n Please format this text using the same words and languange as the text. Do not change the text to much, and do not add information that is not there. return as json."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

print(output_text)
import json
import csv

# Parse the JSON data
data = json.loads(output_text)

# Prepare the data for the CSV
csv_data = []

# Extract data from Block 1
for item in data['Block 1']:
    csv_data.append([item['heading'], item['content'], ''])

# Extract data from Block 2
for feature in data['Block 2']['key_features']:
    csv_data.append(['', feature, ''])

# Extract data from Block 3
for spec in data['Block 3']['technical_specifications']:
    csv_data.append(['', '', spec])

# Write the data to a CSV file
with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)
# output_text = ask_gpt("https://www.kongsberg.com/contentassets/9a7a2014928540309caa9552b55e4b42/01.marine-robots-2p-03.09.21.pdf")
output_text = ask_gpt("https://www.kongsberg.com/contentassets/88df0cc7b3574a0ab3d1d0d560fae99b/datasheet_blueinsight.pdf")
import pandas as pd
import json

def add_data_to_df(df, data):
    # Extract data from Block 1
    block1_data = [{'Heading': item['heading'], 'Content': item['content']} for item in data['Block 1']]
    block1_df = pd.DataFrame(block1_data)

    # Extract data from Block 2
    block2_data = [{'Key Features': feature} for feature in data['Block 2']['key_features']]
    block2_df = pd.DataFrame(block2_data)

    # Extract data from Block 3
    block3_data = [{'Technical Specifications': spec} for spec in data['Block 3']['technical_specifications']]
    block3_df = pd.DataFrame(block3_data)

    # Concatenate the dataframes
    df = pd.concat([df, block1_df, block2_df, block3_df], axis=1)

    return df

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

input_text = (df_with_text["Scraped Text"][2])
output_text = generate_text(input_text)

# Parse the JSON data
data = json.loads(output_text)

# Add the data to the dataframe
df_with_text = add_data_to_df(df_with_text, data)

print(df_with_text)
import json
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")
index = 2
input_text = (df_with_text["Scraped Text"][index])
output_text = generate_text(input_text)
# Parse the JSON data
data = json.loads(output_text)
block1 = data['Block 1']
block2 = data['Block 2']
block3 = data['Block 3']
# Assuming df_with_text is your DataFrame and '2' is the index of the row you want to modify
df_with_text.loc[index, 'Block 1'] = str(block1)
df_with_text.loc[index, 'Block 2'] = str(block2)
df_with_text.loc[index, 'Block 3'] = str(block3)


print(output_text)
df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv",usecols=["Product_Name", "url", "Data sheets", "Scraped Text"])

for index, row in df_with_text.head(4).iterrows():
    input_text = row["Scraped Text"]
    output_text = generate_text(input_text)
    # Parse the JSON data
    data = json.loads(output_text)
    block1 = data['Block 1']
    block2 = data['Block 2']
    block3 = data['Block 3']
    # Add the blocks to the DataFrame
    df_with_text.loc[index, 'General text'] = str(block1)
    df_with_text.loc[index, 'Features'] = str(block2)
    df_with_text.loc[index, 'Technical Specifications'] = str(block3)


df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
system_prompt = """
                Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

                Write the following three content blocks:

                "General text"  (200 - 400 words):
                Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks. If the text has headings, use these headings. Have at elast 100 words in each block and add a suitable heading for each block.}

                 "Key Features": { (40 - 100 words):
                List the key features or benefits of the product. Include as many as needed. Use bullet points for each feature. Use the same bullet points as the pdf.}

                "Technical Specifications": {(10 - 150 words):
                Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.}


                Return as Json with the same formats as always."""
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\n Please format this text using the same words and languange as the text. Do not change the text to much, and do not add information that is not there. return as json."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv",usecols=["Product_Name", "url", "Data sheets", "Scraped Text"])

for index, row in df_with_text.head(4).iterrows():
    input_text = row["Scraped Text"]
    output_text = generate_text(input_text)
    # Parse the JSON data
    data = json.loads(output_text)
    block1 = data['Block 1']
    block2 = data['Block 2']
    block3 = data['Block 3']
    # Add the blocks to the DataFrame
    df_with_text.loc[index, 'General text'] = str(block1)
    df_with_text.loc[index, 'Features'] = str(block2)
    df_with_text.loc[index, 'Technical Specifications'] = str(block3)


df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv",usecols=["Product_Name", "url", "Data sheets", "Scraped Text"])

for index, row in df_with_text.head(4).iterrows():
    input_text = row["Scraped Text"]
    output_text = generate_text(input_text)
    print(output_text)
    # Parse the JSON data
    data = json.loads(output_text)
    block1 = data['General text']
    block2 = data['Key Features']
    block3 = data['Technical Specifications']
    # Add the blocks to the DataFrame
    df_with_text.loc[index, 'General text'] = str(block1)
    df_with_text.loc[index, 'Features'] = str(block2)
    df_with_text.loc[index, 'Technical Specifications'] = str(block3)


df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv",usecols=["Product_Name", "url", "Data sheets", "Scraped Text"])

for index, row in df_with_text.head(15).iterrows():
    input_text = row["Scraped Text"]
    output_text = generate_text(input_text)
    print(output_text)
    # Parse the JSON data
    data = json.loads(output_text)
    block1 = data['General text']
    block2 = data['Key Features']
    block3 = data['Technical Specifications']
    # Add the blocks to the DataFrame
    df_with_text.loc[index, 'General text'] = str(block1)
    df_with_text.loc[index, 'Features'] = str(block2)
    df_with_text.loc[index, 'Technical Specifications'] = str(block3)


df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 12:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 60)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure|data sheets|Data sheet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    return ', '.join(links)
        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
df = pd.read_excel("data/12_04/tags_12_04.xlsx")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)

# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
import requests
from PyPDF2 import PdfReader
import io

def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with io.BytesIO(response.content) as f:
        # Open the PDF file
        reader = PdfReader(f)

        # Extract text from each page
        text = ''
        for page in reader.pages:
            text += page.extract_text()

    return text

# Example usage
pdf_url = 'https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/hugin-superior.pdf'
pdf_text = scrape_pdf_text(pdf_url) 
print(pdf_text)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):

        input_text = row["Scraped Text"]
        output_text = generate_text(input_text)
        print(output_text)
        # Parse the JSON data
        data = json.loads(output_text)
        block1 = data['General text']
        block2 = data['Key Features']
        block3 = data['Technical Specifications']
        # Add the blocks to the DataFrame
        df_with_text.loc[index, 'General text'] = str(block1)
        df_with_text.loc[index, 'Features'] = str(block2)
        df_with_text.loc[index, 'Technical Specifications'] = str(block3)


df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):

        input_text = row["Scraped Text"]
        output_text = generate_text(input_text)
        print(output_text)
        # Parse the JSON data
        data = json.loads(output_text)
        block1 = data['General text']
        block2 = data['Key Features']
        block3 = data['Technical Specifications']
        # Add the blocks to the DataFrame
        df_with_text.loc[index, 'General text'] = str(block1)
        df_with_text.loc[index, 'Features'] = str(block2)
        df_with_text.loc[index, 'Technical Specifications'] = str(block3)
        df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
        df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")


# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if not pd.isnull(row["Scraped Text"]):

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            block1 = data['General text']
            block2 = data['Key Features']
            block3 = data['Technical Specifications']
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
            df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    # if pd.isnull(row["General text"]):
    if not pd.isnull(row["Scraped Text"]):

        input_text = row["Scraped Text"]
        output_text = generate_text(input_text)
        print(output_text)
        # Parse the JSON data
        data = json.loads(output_text)
        block1 = data['General text']
        block2 = data['Key Features']
        block3 = data['Technical Specifications']
        # Add the blocks to the DataFrame
        df_with_text.loc[index, 'General text'] = str(block1)
        df_with_text.loc[index, 'Features'] = str(block2)
        df_with_text.loc[index, 'Technical Specifications'] = str(block3)
        df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
        df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    # if pd.isnull(row["General text"]):
    if not pd.isnull(row["Scraped Text"]):

        input_text = row["Scraped Text"]
        output_text = generate_text(input_text)
        print(output_text)
        # Parse the JSON data
        data = json.loads(output_text)
        block1 = data['General text']
        block2 = data['Key Features']
        block3 = data['Technical Specifications']
        # Add the blocks to the DataFrame
        df_with_text.loc[index, 'General text'] = (block1)
        df_with_text.loc[index, 'Features'] = (block2)
        df_with_text.loc[index, 'Technical Specifications'] = (block3)
        df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
        df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if not pd.isnull(row["Scraped Text"]):

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            block1 = data['General text']
            block2 = data['Key Features']
            block3 = data['Technical Specifications']
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = (block1)
            df_with_text.loc[index, 'Features'] = (block2)
            df_with_text.loc[index, 'Technical Specifications'] = (block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
            df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
import pandas as pd
import json
import re

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if not pd.isnull(row["Scraped Text"]):

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            block1 = data['General text']
            block2 = data['Key Features']
            block3 = data['Technical Specifications']
            # Remove illegal characters
            block1 = re.sub(r'[\0\v\f\xa0]', '', block1)
            block2 = re.sub(r'[\0\v\f\xa0]', '', block2)
            block3 = re.sub(r'[\0\v\f\xa0]', '', block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = (block1)
            df_with_text.loc[index, 'Features'] = (block2)
            df_with_text.loc[index, 'Technical Specifications'] = (block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
            df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
import pandas as pd
import json
import re

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")
for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if not pd.isnull(row["Scraped Text"]):

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            block1 = data['General text']
            block2 = data['Key Features']
            block3 = data['Technical Specifications']
            # Remove illegal characters
            block1 = [re.sub(r'[\0\v\f\xa0]', '', item) for item in block1]
            block2 = [re.sub(r'[\0\v\f\xa0]', '', item) for item in block2]
            block3 = [re.sub(r'[\0\v\f\xa0]', '', item) for item in block3]
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = (block1)
            df_with_text.loc[index, 'Features'] = (block2)
            df_with_text.loc[index, 'Technical Specifications'] = (block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
            df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\n Please format this text using the same words and languange as the text. Do not change the text to much, and do not add information that is not there. return as json with key and value. Do not add any list or dictionary."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
system_prompt = """
                Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

                Write the following three content blocks:

                "General text":{ (200 - 400 words):
                Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks. If the text has headings, use these headings. Have at elast 100 words in each block and add a suitable heading for each block.}

                "Key Features": { (40 - 100 words):
                List the key features or benefits of the product. Include as many as needed. Use bullet points for each feature. Use the same bullet points as the pdf.}

                "Technical Specifications": {(10 - 150 words):
                Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.}



                Return as Json with the same formats as always."""
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\n Please format this text using the same words and languange as the text. Do not change the text to much, and do not add information that is not there. return as json with key and value. Do not add any list or dictionary."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
import pandas as pd
import json
import re

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")
for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if not pd.isnull(row["Scraped Text"]):

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            block1 = data['General text']
            block2 = data['Key Features']
            block3 = data['Technical Specifications']
            # Remove illegal characters
            block1 = [re.sub(r'[\0\v\f\xa0]', '', item) for item in block1]
            block2 = [re.sub(r'[\0\v\f\xa0]', '', item) for item in block2]
            block3 = [re.sub(r'[\0\v\f\xa0]', '', item) for item in block3]
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = (block1)
            df_with_text.loc[index, 'Features'] = (block2)
            df_with_text.loc[index, 'Technical Specifications'] = (block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
            df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
import pandas as pd
import json
import re

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")
for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if not pd.isnull(row["Scraped Text"]):
            print(index," product name: ", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            block1 = data['General text']
            block2 = data['Key Features']
            block3 = data['Technical Specifications']
            # Remove illegal characters
            block1 = [re.sub(r'[\0\v\f\xa0]', '', item) for item in block1]
            block2 = [re.sub(r'[\0\v\f\xa0]', '', item) for item in block2]
            block3 = [re.sub(r'[\0\v\f\xa0]', '', item) for item in block3]
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = (block1)
            df_with_text.loc[index, 'Features'] = (block2)
            df_with_text.loc[index, 'Technical Specifications'] = (block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    if not pd.isnull(row["Scraped Text"]):
        print(index,"product_name:", row["Product_Name"])

        input_text = row["Scraped Text"]
        output_text = generate_text(input_text)
        print(output_text)
        # Parse the JSON data
        data = json.loads(output_text)
        block1 = data['General text']
        block2 = data['Key Features']
        block3 = data['Technical Specifications']
        # Add the blocks to the DataFrame
        df_with_text.loc[index, 'General text'] = (block1)
        df_with_text.loc[index, 'Features'] = (block2)
        df_with_text.loc[index, 'Technical Specifications'] = (block3)
        df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
print(find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/modems/cnode-minis/"))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure|data sheets|Data sheet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    print("forund links 1")
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    return ', '.join(links)

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
print(find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/modems/cnode-minis/"))
print(find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-positioning-systems/hipap-models/HiPAP-HPR/"))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure|data sheets|Data sheet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    print("found links 1")
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    return ', '.join(links)

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data- and product sheets|Brochure|data sheets|Data sheet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    print("found links 1")
                    print(datasheet_links)
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    return ', '.join(links)

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
print(find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-positioning-systems/hipap-models/HiPAP-HPR/"))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data sheets|data- and product sheets|Brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    print("found links 1")
                    print(datasheet_links)
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    return ', '.join(links)

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
print(find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-positioning-systems/hipap-models/HiPAP-HPR/"))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data sheets|data- and product sheets|Brochure", re.I))
        print(datasheets_subtitle)
        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    print("found links 1")
                    print(datasheet_links)
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    return ', '.join(links)

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
print(find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-positioning-systems/hipap-models/HiPAP-HPR/"))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data sheets|data- and product sheets", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    return links

        # If no data sheets are found, look for brochures
        brochure_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("brochure", re.I))

        if brochure_subtitle:
            brochure_section = brochure_subtitle.find_next_sibling()

            if brochure_section:
                brochure_links = brochure_section.find_all('a', class_="Downloads__itemLink")

                if brochure_links:
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in brochure_links if link.get('href').endswith('.pdf')]
                    return links

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
print(find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-positioning-systems/hipap-models/HiPAP-HPR/"))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data sheets|data- and product sheets", re.I))
        brochure_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("brochure", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    return links

        # If no data sheets are found, look for brochures
       

        elif brochure_subtitle:
            brochure_section = brochure_subtitle.find_next_sibling()

            if brochure_section:
                brochure_links = brochure_section.find_all('a', class_="Downloads__itemLink")

                if brochure_links:
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in brochure_links if link.get('href').endswith('.pdf')]
                    return links

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
print(find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-positioning-systems/hipap-models/HiPAP-HPR/"))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data sheets|data- and product sheets", re.I))
        print(datasheets_subtitle)
        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    print("found links 1")
                    print(datasheet_links)
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    return ', '.join(links)

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
print(find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-positioning-systems/hipap-models/HiPAP-HPR/"))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data sheets|data- and product sheets", re.I))
        print(datasheets_subtitle)
        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    print("found links 1")
                    print(datasheet_links)
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    print(links)
                    return ', '.join(links)

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
print(find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-positioning-systems/hipap-models/HiPAP-HPR/"))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data sheets|data- and product sheets", re.I))
        print(datasheets_subtitle)
        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    print("found links 1")
                    print(datasheet_links)
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links if link.get('href').endswith('.pdf')]
                    print(', '.join(links))
                    return ', '.join(links)

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
print(find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-positioning-systems/hipap-models/HiPAP-HPR/"))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data sheets|data- and product sheets", re.I))
        print(datasheets_subtitle)
        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    print("found links 1")
                    print(datasheet_links)
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links]
                    print(', '.join(links))
                    return ', '.join(links)

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
print(find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-positioning-systems/hipap-models/HiPAP-HPR/"))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data sheets|data- and product sheets", re.I))
        print(datasheets_subtitle)
        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    print("found links 1")
                    print(datasheet_links)
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links]
                    links = [link.get('href') + '.pdf' if not link.get('href').endswith('.pdf') else link.get('href') for link in datasheet_links]
                    print(', '.join(links))
                    return ', '.join(links)

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
new_data = (find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-positioning-systems/hipap-models/HiPAP-HPR/"))
)
new_data = (find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-positioning-systems/hipap-models/HiPAP-HPR/"))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data sheets|data- and product sheets", re.I))
        print(datasheets_subtitle)
        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    print("found links 1")
                    print(datasheet_links)
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links]
                    print(', '.join(links))
                    return ', '.join(links)

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
    # If the section, the div, or the links are not found, return None
    return None
new_data = (find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-positioning-systems/hipap-models/HiPAP-HPR/"))
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data sheets|data- and product sheets", re.I))
        print(datasheets_subtitle)
        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links]
                    return ', '.join(links)

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                #Found a random link that was not data sheet
                href = link.get('href')
                if href.endswith('.pdf'):
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
                print(href + " is not a data sheet ", "for product: ", url)
    # If the section, the div, or the links are not found, return None

    return None
new_data = (find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-positioning-systems/hipap-models/HiPAP-HPR/"))
df = pd.read_excel("data/12_04/tags_12_04.xlsx")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)

# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data sheets|data- and product sheets", re.I))
        print(datasheets_subtitle)
        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links]
                    return ', '.join(links)

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                #Found a random link that was not data sheet
                href = link.get('href')
                if href.endswith('.pdf'):
                    print(href + " is not a data sheet ", "for product: ", url)
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
                
    # If the section, the div, or the links are not found, return None

    return None
def find_datasheets(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the div with the class "Downloads"
    downloads_div = soup.find('div', class_="Downloads")

    # If the div is found, find the section with the subtitle "Data sheet", "DATA SHEET", or "Data- and product sheets" within this div
    if downloads_div:
        datasheets_subtitle = downloads_div.find('h3', class_="Section__subtitle", string=re.compile("data sheet|data sheets|data- and product sheets|Product leaflet", re.I))

        # If the subtitle is found, find the next sibling section
        if datasheets_subtitle:
            datasheets_section = datasheets_subtitle.find_next_sibling()

            # If the section is found, find all links within this section
            if datasheets_section:
                datasheet_links = datasheets_section.find_all('a', class_="Downloads__itemLink")

                # If the links are found, prepend "https://www.kongsberg.com" to each href attribute and return the list
                if datasheet_links:
                    links = [link.get('href') if 'https://simrad.online' in link.get('href') or 'https://www.simrad.online' in link.get('href') else "https://www.kongsberg.com" + link.get('href') for link in datasheet_links]
                    print(datasheets_subtitle.get_text(strip=True) + " for product: ", url, " are: ", links)
                    return ', '.join(links)

        else:
            # If no subtitle is found, find all links where the direct child span has the text "Datasheet"
            datasheet_links = downloads_div.find_all('a', class_="Downloads__itemLink")
    
            # If the links are found, return the href attribute of the first link that ends with ".pdf"
            for link in datasheet_links:
                #Found a random link that was not data sheet
                href = link.get('href')
                if href.endswith('.pdf'):
                    print(href + " is not a data sheet ", "for product: ", url)
                    return href if 'https://simrad.online' in href or 'https://www.simrad.online' in href else "https://www.kongsberg.com" + href
                
    # If the section, the div, or the links are not found, return None

    return None
df = pd.read_excel("data/12_04/tags_12_04.xlsx")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)

# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
df = pd.read_excel("data/12_04/tags_12_04.xlsx")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)

# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
df = pd.read_excel("data/12_04/tags_12_04.xlsx")

# Add a new column "Data sheets" to the dataframe
df['Data sheets'] = df['url'].apply(find_datasheets)

# only keep column url, product name and data sheets
df = df[['url', 'Product_Name', 'Data sheets']]
df.to_csv("data/data_sheets.csv", index=False)
df.to_excel("data/data_sheets.xlsx", index=False)
new_data = (find_datasheets("https://www.kongsberg.com/maritime/products/Acoustics-Positioning-and-Communication/acoustic-control-system/ACS500/"))
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 10:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")


# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")


# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 10:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")


# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)

# Load the CSV file
data_sheets = pd.read_csv("data/data_sheets.csv")


# Filter rows with valid data sheet URLs
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]

# Scrape the text from each data sheet and save it as a new column
data_sheets['Scraped Text'] = data_sheets['Data sheets'].apply(scrape_pdf_text)

# Save the DataFrame to a new CSV file
data_sheets.to_csv("data/data_sheets_with_text.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if not pd.isnull(row["Scraped Text"]):
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            block1 = data['General text']
            block2 = data['Key Features']
            block3 = data['Technical Specifications']
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = ' '.join(block1)
            df_with_text.loc[index, 'Features'] = ' '.join(block2)
            df_with_text.loc[index, 'Technical Specifications'] = ' '.join(block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
import streamlit as st
import pandas as pd
from openai._client import OpenAI

client = OpenAI(
    api_key=st.secrets["openai"]["api_key"],
)
system_prompt = """
                Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

                Write the following three content blocks:

                "General text":{ (200 - 400 words):
                Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks. If the text has headings, use these headings. Have at elast 100 words in each block and add a suitable heading for each block.}

                "Key Features": { (40 - 100 words):
                List the key features or benefits of the product. Include as many as needed. Use bullet points for each feature. Use the same bullet points as the pdf.}

                "Technical Specifications": {(10 - 150 words):
                Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.}



                Return as Json with the same formats as always."""
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\n Please format this text using the same words and languange as the text. Do not change the text to much, and do not add information that is not there. return as json with key and value. Do not add any list or dictionary."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if not pd.isnull(row["Scraped Text"]):
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            block1 = data['General text']
            block2 = data['Key Features']
            block3 = data['Technical Specifications']
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = ' '.join(block1)
            df_with_text.loc[index, 'Features'] = ' '.join(block2)
            df_with_text.loc[index, 'Technical Specifications'] = ' '.join(block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if not pd.isnull(row["Scraped Text"]):
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            block1 = data['General text']
            block2 = data['Key Features']
            block3 = data['Technical Specifications']
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = ' '.join(block1)
            df_with_text.loc[index, 'Features'] = ' '.join(block2)
            df_with_text.loc[index, 'Technical Specifications'] = ' '.join(block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
        if not pd.isnull(row["Scraped Text"]):
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            block1 = data['General text']
            block2 = data['Key Features']
            block3 = data['Technical Specifications']
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = ' '.join(block1)
            df_with_text.loc[index, 'Features'] = ' '.join(block2)
            df_with_text.loc[index, 'Technical Specifications'] = ' '.join(block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
        if not pd.isnull(row["Scraped Text"]):
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            block1 = data['General text']
            block2 = data['Key Features']
            block3 = data['Technical Specifications']
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = ' '.join(block1)
            df_with_text.loc[index, 'Features'] = ' '.join(block2)
            df_with_text.loc[index, 'Technical Specifications'] = ' '.join(block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
        if not pd.isnull(row["Scraped Text"]):
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = ' '.join(block1)
            df_with_text.loc[index, 'Features'] = ' '.join(block2)
            df_with_text.loc[index, 'Technical Specifications'] = ' '.join(block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
        if not pd.isnull(row["Scraped Text"]):
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = ' '.join(block1)
            df_with_text.loc[index, 'Features'] = ' '.join(block2)
            df_with_text.loc[index, 'Technical Specifications'] = ' '.join(block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
        if not pd.isnull(row["Scraped Text"]):
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
print(scrape_pdf_text("https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/apos-survey---surveyors-independent-operator-station-for-hipap/"))
import requests

def save_pdf(url, filename):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Write the content to a PDF file
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"PDF saved as {filename}")
    else:
        print(f"Failed to retrieve PDF from {url}")

# Example usage
save_pdf("https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/apos-survey---surveyors-independent-operator-station-for-hipap/", "output.pdf")
print(scrape_pdf_text("https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/acs500-emergency-acoustic-bop-control-system/"))
print(save_pdf("https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/acs500-emergency-acoustic-bop-control-system/"))
print(save_pdf("https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/acs500-emergency-acoustic-bop-control-system/", "output.pdf"))
print(scrape_pdf_text("https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/acs500-emergency-acoustic-bop-control-system/"))
print(scrape_pdf_text("https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/apos-survey---surveyors-independent-operator-station-for-hipap/"))
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 10:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
print(scrape_pdf_text("https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/apos-survey---surveyors-independent-operator-station-for-hipap/"))
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 10:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file


    return text

# Example usage
print(scrape_pdf_text("https://www.kongsberg.com/globalassets/maritime/km-products/product-documents/apos-survey---surveyors-independent-operator-station-for-hipap/"))
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        print(index,"product_name:", row["Product_Name"])
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            # df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            # df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
            df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
            df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_with_text.csv", index=False)
df_with_text.to_excel("data/data_sheets_with_text.xlsx", index=False)
produkter_alle = pd.read_excel("data/styrings_data/produkter_alle.xlsx", usecols=["Product_Name","url","Product category"])
df_with_text = pd.read_csv("data/data_sheets_with_text.csv")

#Merge the two dataframes on the product name.
produkter_alle = pd.read_excel("data/styrings_data/produkter_alle.xlsx", usecols=["Product_Name","url","Product category"])
df_with_text = pd.read_csv("data/data_sheets_with_text.csv", usecols=["Product_Name","Data sheets","General text","Features","Technical Specifications"])

#Merge the two dataframes on the product name, and keep product name, url, product category from produkter_alle, the rest from df_with_text
merged = pd.merge(produkter_alle, df_with_text, on="Product_Name", how="left")
merged.to_csv("data/merged_data_test.csv", index=False)
produkter_alle = pd.read_excel("data/styrings_data/produkter_alle.xlsx", usecols=["Product_Name","url","Product category"])
df_with_text = pd.read_csv("data/data_sheets_with_text.csv", usecols=["Product_Name","Data sheets","General text","Features","Technical Specifications"])

#Merge the two dataframes on the product name, and keep product name, url, product category from produkter_alle, the rest from df_with_text
merged = pd.merge(produkter_alle, df_with_text, on="Product_Name", how="left")
merged.to_csv("data/styrings_data/ai_produkter.csv", index=False)
merged.to_excel("data/styrings_data/ai_produkter.xlsx", index=False)
data_sheets_df = pd.read_csv("data/data_sheets.csv")
# find all products that have more than one data sheet
data_sheets_df = data_sheets_df[data_sheets_df['Data sheets'].str.count(',') > 0]
data_sheets_df.to_csv("data/data_sheets_multiple.csv", index=False)
data_sheets_df = pd.read_csv("data/data_sheets.csv")
# find all products that have more than one data sheet
data_sheets_df = data_sheets_df[data_sheets_df['Data sheets'].str.count(',') > 0]
data_sheets_df.to_csv("data/data_sheets_multiple.csv", index=False)
data_sheets_df.to_excel("data/data_sheets_multiple.xlsx", index=False)
# Read the CSV file
data_sheets_df = pd.read_csv("data/data_sheets.csv")

# Find all products that have more than one data sheet
data_sheets_df = data_sheets_df[data_sheets_df['Data sheets'].str.count(',') > 0]

# Split the 'Data sheets' column into multiple columns
data_sheets_split = data_sheets_df['Data sheets'].str.split(',', expand=True)

# Rename the new columns
data_sheets_split.columns = [f'Data sheet {i+1}' for i in range(data_sheets_split.shape[1])]

# Concatenate the original DataFrame with the new DataFrame
data_sheets_df = pd.concat([data_sheets_df, data_sheets_split], axis=1)

# Drop the original 'Data sheets' column
data_sheets_df = data_sheets_df.drop(columns=['Data sheets'])

# Save the DataFrame to CSV and Excel files
data_sheets_df.to_csv("data/data_sheets_multiple.csv", index=False)
data_sheets_df.to_excel("data/data_sheets_multiple.xlsx", index=False)
merged_df = pd.read_csv("data/styrings_data/ai_produkter.csv")

# Find all products that have more no data sheets
merged_df_without_datasheet = merged_df[merged_df['Data sheets'].isna()]

# Save the DataFrame to CSV and Excel files
merged_df_without_datasheet.to_csv("data/styrings_data/ai_produkter_uten_datasheet.csv", index=False)
merged_df_without_datasheet.to_excel("data/styrings_data/ai_produkter_uten_datasheet.xlsx", index=False)
import requests

def scrape_webpage(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the HTML content of the webpage
        html_content = response.text
        return html_content
    else:
        print(f"Failed to scrape webpage. Status code: {response.status_code}")
        return None
data_sheets_df = pd.read_csv("data/data_sheets.csv")

# Find all products that have more no data sheets
df_without_datasheet = data_sheets_df[data_sheets_df['Data sheets'].isna()]

# Save the DataFrame to CSV and Excel files
df_without_datasheet.to_csv("data/styrings_data/ai_produkter_uten_datasheet.csv", index=False)
df_without_datasheet.to_excel("data/styrings_data/ai_produkter_uten_datasheet.xlsx", index=False)
df_without_datasheet = pd.read_csv("data/styrings_data/ai_produkter_uten_datasheet.csv")
# scrape the text from each product page and save it as a new column
df_without_datasheet['Scraped Text'] = df_without_datasheet['url'].apply(scrape_webpage)
df_without_datasheet.to_csv("data/styrings_data/uten_datasheet_scraped.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/styrings_data/uten_datasheet_scraped.csv")

for index, row in df_with_text.iterrows():
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_web_scraped_ai.csv", index=False)
from bs4 import BeautifulSoup

def scrape_webpage(url):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the HTML content of the webpage
        html_content = response.text

        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Extract the text from the parsed HTML content
        text_content = soup.get_text()

        return text_content
    else:
        print(f"Failed to scrape webpage. Status code: {response.status_code}")
        return None
df_without_datasheet = pd.read_csv("data/styrings_data/ai_produkter_uten_datasheet.csv")
# scrape the text from each product page and save it as a new column
df_without_datasheet['Scraped Text'] = df_without_datasheet['url'].apply(scrape_webpage)
df_without_datasheet.to_csv("data/styrings_data/uten_datasheet_scraped.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/styrings_data/uten_datasheet_scraped.csv")

for index, row in df_with_text.iterrows():
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_web_scraped_ai.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/styrings_data/data_sheets_web_scraped_ai.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_web_scraped_ai.csv", index=False)
import pandas as pd
import json

df_with_text = pd.read_csv("data/data_sheets_web_scraped_ai.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_web_scraped_ai.csv", index=False)
from bs4 import BeautifulSoup, NavigableString
import requests

def extract_text(url):
    # Get the HTML of the page
    response = requests.get(url)
    html = response.text

    # Parse the HTML with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Find the divs with the specified classes
    divs = soup.find_all(class_="RichtextArea ProductPage__richtext text-wrapper")

    # Extract the text of each div
    text_string = ''
    for div in divs:
        text_string += div.get_text() + '\n'

    return text_string

print(extract_text("https://www.kongsberg.com/maritime/products/onshore/onshore-systems/ais-network-infrastructure-shorebased/ais-service-management-system/"))
df_without_datasheet = pd.read_csv("data/styrings_data/ai_produkter_uten_datasheet.csv")
# scrape the text from each product page and save it as a new column
df_without_datasheet['Scraped Text'] = df_without_datasheet['url'].apply(extract_text)
df_without_datasheet.to_csv("data/styrings_data/uten_datasheet_scraped.csv", index=False)
import pandas as pd
import json
df_with_text = pd.read_csv("data/styrings_data/uten_datasheet_scraped.csv")

for index, row in df_with_text.iterrows():
    # if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_web_scraped_ai.csv", index=False)
import pandas as pd
import json
df_with_text = pd.read_csv("data/data_sheets_web_scraped_ai.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_web_scraped_ai.csv", index=False)
import pandas as pd
import json
df_with_text = pd.read_csv("data/data_sheets_web_scraped_ai.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_web_scraped_ai.csv", index=False)
import pandas as pd
import json
df_with_text = pd.read_csv("data/data_sheets_web_scraped_ai.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_web_scraped_ai.csv", index=False)
import pandas as pd
import json
df_with_text = pd.read_csv("data/data_sheets_web_scraped_ai.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_web_scraped_ai.csv", index=False)
system_prompt = """
                Read the whole file. Task: You are a content/format writer tasked with converting information from a PDF file into a a selected format. Only use the content found in the provided file. If there's insufficient information, insert "I don't know" in the respective block. Use the same sentences, same way of writing in the blocks if that is possible. Do not add any new information, and keep changes to a minimum, you are a formater, more than a content writer. Add where you found the information for each block.

                Write the following three content blocks:

                "General text":{ (200 - 400 words):
                Provide factual information blocks explaining the value that the products bring. Include a minimum of one and a maximum of three such blocks. If the product pdf offer more text, use three blocks. If the text has headings, use these headings. Have at elast 100 words in each block and add a suitable heading for each block.}

                "Key Features": { (40 - 100 words):
                List the key features or benefits of the product. Include as many as needed. Use bullet points for each feature. Use the same bullet points as the pdf.}

                "Technical Specifications": {(10 - 150 words):
                Add technical specifications related to the product, following the expected structure: "category, parameters, and parameter value." Include as many specifications as needed. Use bullet points for each specification.}



                Return as Json with the same formats as always. Always add General text, Key Features, Techical Specification. If you have no information say I don`t know """
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\n Please format this text using the same words and languange as the text. Do not change the text to much, and do not add information that is not there. return as json with key and value. Do not add any list or dictionary."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
def generate_text(text):
    messages = [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"I have a text that I want to format into headings and text bulks. The text is:\n\n{text}\n\n Please format this text using the same words and languange as the text. Do not change the text to much, and do not add information that is not there. return as json with key and value. Do not add any list or dictionary."
            }
        ]

    response = client.chat.completions.create(
        model="gpt-3.5-turbo-1106",
        response_format={ "type": "json_object" },
        messages=messages,
    )
    output_text = response.choices[0].message.content.strip()
    return output_text
import pandas as pd
import json
df_with_text = pd.read_csv("data/data_sheets_web_scraped_ai.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}


            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_web_scraped_ai.csv", index=False)
import pandas as pd
import json
df_with_text = pd.read_csv("data/data_sheets_web_scraped_ai.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            # print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}
            print(data)

            block1 = data['general text']
            block2 = data['key features']
            block3 = data['technical specifications']
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_web_scraped_ai.csv", index=False)
import pandas as pd
import json
df_with_text = pd.read_csv("data/data_sheets_web_scraped_ai.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            # print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}
            print(data)

            block1 = data.get('general text', '')
            block2 = data.get('key features', '')
            block3 = data.get('technical specifications', '')
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_web_scraped_ai.csv", index=False)
import pandas as pd
import json
df_with_text = pd.read_csv("data/data_sheets_web_scraped_ai.csv")

for index, row in df_with_text.iterrows():
    if pd.isnull(row["General text"]):
        if (row["Scraped Text"]) != "":
            print(index,"product_name:", row["Product_Name"])

            input_text = row["Scraped Text"]
            output_text = generate_text(input_text)
            # print(output_text)
            # Parse the JSON data
            data = json.loads(output_text)
            data = {k.lower(): v for k, v in data.items()}
            print(data)

            block1 = data.get('general text', '')
            block2 = data.get('key features', '')
            block3 = data.get('technical specifications', '')
            print(block1)
            print(block2)
            print(block3)
            # Add the blocks to the DataFrame
            df_with_text.loc[index, 'General text'] = str(block1)
            df_with_text.loc[index, 'Features'] = str(block2)
            df_with_text.loc[index, 'Technical Specifications'] = str(block3)
            df_with_text.to_csv("data/data_sheets_web_scraped_ai.csv", index=False)
df_with_text.to_excel("data/data_sheets_web_scraped_ai.xlsx", index=False)
df_without_datasheet = pd.read_csv("data/data_sheets_web_scraped_ai.csv")
df_without_datasheet = df.read_csv("data/styrings_data/ai_produkter.csv")

merged = pd.merge(df_without_datasheet, df_without_datasheet, on="Product_Name", how="left")
merged.to_csv("data/styrings_data/alle_produkter_ai.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai.xlsx", index=False)
df_without_datasheet = pd.read_csv("data/data_sheets_web_scraped_ai.csv")
df_without_datasheet = pd.read_csv("data/styrings_data/ai_produkter.csv")

merged = pd.merge(df_without_datasheet, df_without_datasheet, on="Product_Name", how="left")
merged.to_csv("data/styrings_data/alle_produkter_ai.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai.xlsx", index=False)
df_without_datasheet = pd.read_csv("data/data_sheets_web_scraped_ai.csv", usecols=["Product_Name","url","Data sheets","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/ai_produkter.csv", usecols=["Product_Name","url","General text","Features","Technical Specifications"])

merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")
merged.to_csv("data/styrings_data/alle_produkter_ai.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai.xlsx", index=False)
df_without_datasheet = pd.read_csv("data/data_sheets_web_scraped_ai.csv", usecols=["Product_Name","url","Data sheets","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/ai_produkter.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])

merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")
merged.to_csv("data/styrings_data/alle_produkter_ai.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai.xlsx", index=False)
df_without_datasheet = pd.read_csv("data/data_sheets_web_scraped_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/ai_produkter.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")
merged.to_csv("data/styrings_data/alle_produkter_ai.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai.xlsx", index=False)
df_without_datasheet = pd.read_csv("data/data_sheets_web_scraped_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/ai_produkter.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")
merged.to_csv("data/styrings_data/alle_produkter_ai.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai.xlsx", index=False)
df_without_datasheet = pd.read_csv("data/data_sheets_web_scraped_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/ai_produkter.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

merged = pd.merge(df_with_datasheet, df_without_datasheet, on=["Product_Name","General text","Features","Technical Specifications"] , how="left")
merged.to_csv("data/styrings_data/alle_produkter_ai.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai.xlsx", index=False)
df_without_datasheet = pd.read_csv("data/data_sheets_web_scraped_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/ai_produkter.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

# merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")

# Combine the DataFrames
merged = df_with_datasheet.combine_first(df_without_datasheet)

# Reset the index
merged.reset_index(inplace=True)

merged.to_csv("data/styrings_data/alle_produkter_ai.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai.xlsx", index=False)
df_without_datasheet = pd.read_csv("data/data_sheets_web_scraped_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/ai_produkter.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

# merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")

# Combine the DataFrames
merged = df_with_datasheet.combine_first(df_without_datasheet)

# Reset the index
# merged.reset_index(inplace=True)

merged.to_csv("data/styrings_data/alle_produkter_ai.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai.xlsx", index=False)
df_without_datasheet = pd.read_csv("data/data_sheets_web_scraped_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/ai_produkter.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

df_without_datasheet.set_index('Product_Name', inplace=True)
df_with_datasheet.set_index('Product_Name', inplace=True)

# merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")

# Combine the DataFrames
merged = df_with_datasheet.combine_first(df_without_datasheet)

# Reset the index
# merged.reset_index(inplace=True)

merged.to_csv("data/styrings_data/alle_produkter_ai.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai.xlsx", index=False)
df_without_datasheet = pd.read_csv("data/data_sheets_web_scraped_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/ai_produkter.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

df_without_datasheet.set_index('Product_Name', inplace=True)
df_with_datasheet.set_index('Product_Name', inplace=True)

# merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")

# Combine the DataFrames
merged = df_with_datasheet.combine_first(df_without_datasheet)

# Reset the index
merged.reset_index(inplace=True)

merged.to_csv("data/styrings_data/alle_produkter_ai.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai.xlsx", index=False)
df_data_sheet_manual = pd.read_csv("data/styrings_data/produkter_alle.xlsx")
# only keep the one with url ends with .pdf
df_data_sheet_manual = df_data_sheet_manual[df_data_sheet_manual['url'].str.endswith('.pdf')]
print(len(df_data_sheet_manual))
df_data_sheet_manual = pd.read_csv("data/styrings_data/ai_produkter.csv")
# only keep the one with url ends with .pdf
df_data_sheet_manual = df_data_sheet_manual[df_data_sheet_manual['url'].str.endswith('.pdf')]
print(len(df_data_sheet_manual))
import pandas as pd
import json

def process_text(df_with_text, output_path):
    for index, row in df_with_text.iterrows():
            if (row["Scraped Text"]) != "":
                print(index,"product_name:", row["Product_Name"])

                input_text = row["Scraped Text"]
                output_text = generate_text(input_text)
                print(output_text)
                # Parse the JSON data
                data = json.loads(output_text)
                data = {k.lower(): v for k, v in data.items()}

                block1 = data.get('general text', '')
                block2 = data.get('key features', '')
                block3 = data.get('technical specifications', '')
                print(block1)
                print(block2)
                print(block3)
                # Add the blocks to the DataFrame
                df_with_text.loc[index, 'General text'] = str(block1)
                df_with_text.loc[index, 'Features'] = str(block2)
                df_with_text.loc[index, 'Technical Specifications'] = str(block3)

    return df_with_text
df_data_sheet_manual = pd.read_csv("data/styrings_data/ai_produkter.csv")
# only keep the one with url ends with .pdf
df_data_sheet_manual = df_data_sheet_manual[df_data_sheet_manual['url'].str.endswith('.pdf')]
print(len(df_data_sheet_manual))
import pandas as pd
import json

def process_text(df_with_text):
    for index, row in df_with_text.iterrows():
            if (row["Scraped Text"]) != "":
                print(index,"product_name:", row["Product_Name"])

                input_text = row["Scraped Text"]
                output_text = generate_text(input_text)
                print(output_text)
                # Parse the JSON data
                data = json.loads(output_text)
                data = {k.lower(): v for k, v in data.items()}

                block1 = data.get('general text', '')
                block2 = data.get('key features', '')
                block3 = data.get('technical specifications', '')
                print(block1)
                print(block2)
                print(block3)
                # Add the blocks to the DataFrame
                df_with_text.loc[index, 'General text'] = str(block1)
                df_with_text.loc[index, 'Features'] = str(block2)
                df_with_text.loc[index, 'Technical Specifications'] = str(block3)

    return df_with_text
df_data_sheet_manual_ai = process_text(df_data_sheet_manual)
df_data_sheet_manual_ai.to_csv("data/styrings_data/df_data_sheet_manual_ai.csv", index=False)
def scrape_pdf_text(url):
    # Download the PDF file
    response = requests.get(url)
    with open('temp.pdf', 'wb') as f:
        f.write(response.content)

    # Open the PDF file
    with pdfplumber.open('temp.pdf') as pdf:
        # Extract text from each page
        text = ''
        in_features_section = False
        if len(pdf.pages) > 10:
            return None
        for i, page in enumerate(pdf.pages):
            # If this is the last page, define a crop box that excludes the last 1 cm from the bottom
            if i == len(pdf.pages) - 1:
                crop_box = (0, 0, page.width, page.height - 70)
                page = page.crop(crop_box)

            page_text = page.extract_text().split('\n')
                        
            for line in page_text:
                if not in_features_section:
                    line = line.replace('®', '')  # Remove ® symbol
                    if line.startswith('•'):
                        text += '\n' + line  # Add bullet point to new line
                    else:
                        text += line + '\n'

    # Remove the temporary PDF file
    os.remove('temp.pdf')

    return text

# Example usage
data_sheets = pd.read_csv("data/data_sheets.csv")
data_sheets = data_sheets[data_sheets['Data sheets'].notna()]
data_sheets = data_sheets[data_sheets['Data sheets'].str.count(',') < 1]
product_datasheet = data_sheets["Data sheets"].iloc[2]
pdf_text = scrape_pdf_text(product_datasheet)
print(pdf_text)
print(product_datasheet)
df_data_sheet_manual['Scraped Text'] = df_data_sheet_manual['url'].apply(scrape_pdf_text)
df_data_sheet_manual_ai = process_text(df_data_sheet_manual)
df_data_sheet_manual_ai.to_csv("data/styrings_data/df_data_sheet_manual_ai.csv", index=False)
df_data_sheet_manual_ai = pd.read_csv("data/styrings_data/df_data_sheet_manual_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/alle_produkter_ai.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

df_data_sheet_manual_ai.set_index('Product_Name', inplace=True)
df_with_datasheet.set_index('Product_Name', inplace=True)

# merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")

# Combine the DataFrames
merged = df_with_datasheet.combine_first(df_data_sheet_manual_ai)

# Reset the index
merged.reset_index(inplace=True)
merged.to_csv("data/styrings_data/alle_produkter_ai_test.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai_test.xlsx", index=False)
df_data_sheet_manual_ai = pd.read_csv("data/styrings_data/df_data_sheet_manual_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/alle_produkter_ai.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

df_data_sheet_manual_ai.set_index('Product_Name', inplace=True)
df_with_datasheet.set_index('Product_Name', inplace=True)

# merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")

# Combine the DataFrames
merged = df_with_datasheet.combine_first(df_data_sheet_manual_ai)

# Reset the index

merged.to_csv("data/styrings_data/alle_produkter_ai_test.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai_test.xlsx", index=False)
df_data_sheet_manual_ai = pd.read_csv("data/styrings_data/df_data_sheet_manual_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/alle_produkter_ai.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

df_data_sheet_manual_ai.set_index('Product_Name', inplace=True)
df_with_datasheet.set_index('Product_Name', inplace=True)

# merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")

# Combine the DataFrames
# merged = df_with_datasheet.combine_first(df_data_sheet_manual_ai)
df_with_datasheet.update(df_data_sheet_manual_ai)


# Reset the index

df_with_datasheet.to_csv("data/styrings_data/alle_produkter_ai_test.csv", index=False)
df_with_datasheet.to_excel("data/styrings_data/alle_produkter_ai_test.xlsx", index=False)
df_data_sheet_manual_ai = pd.read_csv("data/styrings_data/df_data_sheet_manual_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/alle_produkter_ai.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

df_data_sheet_manual_ai.set_index('Product_Name', inplace=True)
df_with_datasheet.set_index('Product_Name', inplace=True)

# merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")

# Combine the DataFrames
# merged = df_with_datasheet.combine_first(df_data_sheet_manual_ai)
df_data_sheet_manual_ai.update(df_with_datasheet)


# Reset the index

df_with_datasheet.to_csv("data/styrings_data/alle_produkter_ai_test.csv", index=False)
df_with_datasheet.to_excel("data/styrings_data/alle_produkter_ai_test.xlsx", index=False)
df_data_sheet_manual_ai = pd.read_csv("data/styrings_data/df_data_sheet_manual_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/alle_produkter_ai.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

df_data_sheet_manual_ai.set_index('Product_Name', inplace=True)
df_with_datasheet.set_index('Product_Name', inplace=True)

# merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")

# Combine the DataFrames
# merged = df_with_datasheet.combine_first(df_data_sheet_manual_ai)
df_data_sheet_manual_ai.update(df_with_datasheet)


# Reset the index

df_data_sheet_manual_ai.to_csv("data/styrings_data/alle_produkter_ai_test.csv", index=False)
df_data_sheet_manual_ai.to_excel("data/styrings_data/alle_produkter_ai_test.xlsx", index=False)
df_data_sheet_manual_ai = pd.read_csv("data/styrings_data/df_data_sheet_manual_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/alle_produkter_ai.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

df_data_sheet_manual_ai.set_index('Product_Name', inplace=True)
df_with_datasheet.set_index('Product_Name', inplace=True)

# merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")

# Combine the DataFrames
# merged = df_with_datasheet.combine_first(df_data_sheet_manual_ai)
df_with_datasheet.update(df_data_sheet_manual_ai)


# Reset the index

df_with_datasheet.to_csv("data/styrings_data/alle_produkter_ai_test.csv", index=False)
df_with_datasheet.to_excel("data/styrings_data/alle_produkter_ai_test.xlsx", index=False)
df_data_sheet_manual_ai = pd.read_csv("data/styrings_data/df_data_sheet_manual_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/alle_produkter_ai.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

df_data_sheet_manual_ai.set_index('Product_Name', inplace=True)
df_with_datasheet.set_index('Product_Name', inplace=True)

# merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")

# Combine the DataFrames
# merged = df_with_datasheet.combine_first(df_data_sheet_manual_ai)
merged = df_with_datasheet.combine_first(df_data_sheet_manual_ai)


# Reset the index

df_with_datasheet.to_csv("data/styrings_data/alle_produkter_ai_test.csv", index=False)
df_with_datasheet.to_excel("data/styrings_data/alle_produkter_ai_test.xlsx", index=False)
df_data_sheet_manual_ai = pd.read_csv("data/styrings_data/df_data_sheet_manual_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/alle_produkter_ai.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

df_data_sheet_manual_ai.set_index('Product_Name', inplace=True)
df_with_datasheet.set_index('Product_Name', inplace=True)

# merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")

# Combine the DataFrames
# merged = df_with_datasheet.combine_first(df_data_sheet_manual_ai)
merged = df_with_datasheet.combine_first(df_data_sheet_manual_ai)


# Reset the index

merged.to_csv("data/styrings_data/alle_produkter_ai_test.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai_test.xlsx", index=False)
df_data_sheet_manual_ai = pd.read_csv("data/styrings_data/df_data_sheet_manual_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/alle_produkter_ai.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

# df_data_sheet_manual_ai.set_index('Product_Name', inplace=True)
# df_with_datasheet.set_index('Product_Name', inplace=True)

# merged = pd.merge(df_with_datasheet, df_without_datasheet, on="Product_Name", how="left")

# Combine the DataFrames
# merged = df_with_datasheet.combine_first(df_data_sheet_manual_ai)
merged = df_with_datasheet.combine_first(df_data_sheet_manual_ai)


# Reset the index

merged.to_csv("data/styrings_data/alle_produkter_ai_test.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai_test.xlsx", index=False)
df_data_sheet_manual_ai = pd.read_csv("data/styrings_data/df_data_sheet_manual_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/alle_produkter_ai.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

# Merge the DataFrames
merged = pd.merge(df_with_datasheet, df_data_sheet_manual_ai, on="Product_Name", how="left")

merged.to_csv("data/styrings_data/alle_produkter_ai_test.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai_test.xlsx", index=False)
df_data_sheet_manual_ai = pd.read_csv("data/styrings_data/df_data_sheet_manual_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/alle_produkter_ai.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

# Merge the DataFrames
merged = pd.merge(df_with_datasheet, df_data_sheet_manual_ai, on="Product_Name", how="right")

merged.to_csv("data/styrings_data/alle_produkter_ai_test.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai_test.xlsx", index=False)
df_data_sheet_manual_ai = pd.read_csv("data/styrings_data/df_data_sheet_manual_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/alle_produkter_ai.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

# Merge the DataFrames
merged = pd.merge(df_with_datasheet, df_data_sheet_manual_ai, on="Product_Name", how="inner")

merged.to_csv("data/styrings_data/alle_produkter_ai_test.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai_test.xlsx", index=False)
df_data_sheet_manual_ai = pd.read_csv("data/styrings_data/df_data_sheet_manual_ai.csv", usecols=["Product_Name","General text","Features","Technical Specifications"])
df_with_datasheet = pd.read_csv("data/styrings_data/alle_produkter_ai.csv", usecols=["Product_Name","Data sheets","url","General text","Features","Technical Specifications"])

# Merge the DataFrames
merged = pd.concat([df_with_datasheet, df_data_sheet_manual_ai])

# Remove duplicates based on 'Product_Name', keeping the last occurrence
merged.drop_duplicates(subset='Product_Name', keep='last', inplace=True)

merged.to_csv("data/styrings_data/alle_produkter_ai_test.csv", index=False)
merged.to_excel("data/styrings_data/alle_produkter_ai_test.xlsx", index=False)

