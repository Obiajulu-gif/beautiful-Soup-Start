from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")

# this will get the website html page
yc_webpage = response.text

# getting the web page and parsing it
soup = BeautifulSoup(yc_webpage, "html.parser")

# this line of code tends to get all the element in a tag that contain the below specification
article = soup.find_all(name ="a", class_="titlelink")

# this line of code houses all the  links and text with similar tag properties
article_texts = []
article_links = []

# this line of code loops through the list of article and get the text & link in it
for article_tag in article:
    # getting the text
    text = article_tag.getText()
    article_texts.append(text)

    # getting the attribute from the selected element
    link = article_tag.get("href")
    article_links.append(link)

article_score = [int(score.getText().split()[0]) for score in soup.find_all(name= "span", class_="score")]

print(article_texts)
print(article_links)
print(article_score)

# this line of codes tends to get the highest upvote and give us the text and link related to it
maximum_score = max(article_score)
index_of_max = article_score.index(maximum_score)
maximum_score_text = article_texts[index_of_max]
maximum_score_link = article_links[index_of_max]
print(maximum_score)
print(maximum_score_text)
print(maximum_score_link)


# # we can also use lxml as our html.parser because some site dont accept html.parser
# # import lxml
#
# # we added encoding="utf8" so as to avoid error  been throw to us
# with open(file="website.html", encoding="utf8") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # this will also give us the tag of title
# print(soup.title)
#
# # this will only give us only the content inside the title tag
# print(soup.title.string)
#
# # this will print the entire content in the web page
# print(soup)
#
# # this will indent all the content in the web page properly
# print(soup.prettify())
#
# # this will give us the first anchor tag in the web page
# # or first of an element in the web page
# print(soup.a)
#
# # it find all of the similar tag in the web page and give us a list of them
# all_tags = soup.find_all(name='a')
# print(all_tags)
#
# # to get the text inside the anchor tag
# for tag in all_tags:
#     # print(tag.getText())
#     # to get only the link inside the anchor tag
#     print(tag.get("href"))
#
# # to get an attribute together with it's tag
# heading =  soup.find(name="h1", id="name")
# print(heading.string)
#
# # to get an class together with it's tag we use (class_) for class
# section_heading = soup.find(name="h3",class_="heading")
# # to get the text in it
# print(section_heading.get_text())
# # to get the value or name of the specific class
# print(section_heading.get("class"))
#
# # to get a specfic element in the web page
# # we explictly state the group of element in which it sit in
# company_url = soup.select_one(selector="p em strong a ")
# print(company_url)
#
# # to get the id in a web page
# name = soup.select_one(selector="#name")
# print(name)
#
# # to get all class that bear a similar class name and it will be in form of a list
# heading = soup.select(".heading")
# print(heading)
