from bs4 import BeautifulSoup
import re
import requests

url = "https://www.parlimen.gov.my/bills-dewan-rakyat.html?uweb=dr&lang=en"
headers = {'user-agent': 'my-agent/1.0.1'}

soup = BeautifulSoup(requests.get(url, headers=headers).text)

table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="ruulist")
rows = table.findAll(lambda tag: tag.name=='tr')
href = table.findAll(lambda tag: tag.name=='a')

#define patterns
re_pattern = r'\bBill\b'
remove_the = "The"
remove_after_pdf = "\',\'"

#remove unwanted items
del href[1::2]
clean_rows = []
for row in rows:
    if re.search(re_pattern, str(row)):
        x = row.text.strip().replace('\n', '').replace('\t', " ").replace('First', " First").replace("        ","   ").split(remove_the, 1)[0]
        clean_rows.append(x)

#turn results into a new text file
word = ""
for row, link in zip(clean_rows,href):
    if re.search(re_pattern, str(row)):
        y = str(link).replace("<a href=\"#\" onclick=\"loadResult(\'", "https://www.parlimen.gov.my").split(remove_after_pdf, 1)[0].replace(" ", "%20")
        word += row + "\n"
        word += y + "\n\n"

with open('new.txt','w') as a:
    a.write(word)

#Compare new results against old
def scraper():
    with open('new.txt', 'r') as current, open('old.txt', 'r') as old:
        old_txt = old.readlines()
        current_txt = current.readlines()

        if old_txt == current_txt:  # compare the two files
            print("No change")

        else:  # return
            x = ""
            for line in current_txt:
                if line not in old_txt:
                    x += line

            with open('old.txt', 'w') as data:
                data.write(word)

            return x




