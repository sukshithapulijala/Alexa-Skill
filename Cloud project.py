import requests
from bs4 import BeautifulSoup
from datetime import datetime


page = requests.get("https://www.imdb.com/calendar/?ref_=nv_mv_cal")
soup = BeautifulSoup(page.content, 'html.parser')

div_main = soup.find_all(id="main")
month_elem = div_main[0].find_all('h4')
ul_elem = div_main[0].find_all('ul')

print(div_main)
print(month_elem)
print(ul_elem)

movies = {}

today = datetime.today().date()

def week_number_of_month(date_value):
    return (date_value.isocalendar()[1] - date_value.replace(day=1).isocalendar()[1] + 1)

today_num = week_number_of_month(today)

week_wanted = '2020-05'

for i in range(0,len(month_elem)):
    day = month_elem[i].text
    if 'W' in week_wanted:
        y, w, _ = datetime.strptime(day, "%d %B %Y").isocalendar()

        # print("%dW%02d" % (y, w))

        movie_week = str(y) + 'W' + str(w)

        speak_output = 'The movies releasing in that week are '
    else:
        month = datetime.strptime(day, '%d %B %Y').month
        ndate = datetime.strptime(day, '%d %B %Y').day
        year = datetime.strptime(day, '%d %B %Y').year

        dt_stamp = datetime(year, month, ndate)
        movie_week = dt_stamp.strftime('%Y-%m')
        speak_output = 'The movies releasing in that month are '

    m = ul_elem[i].find_all('a')
    a = []

    for i in m:
        text = i.text
        a.append(text)

    if movie_week in movies.keys():
        movies[movie_week] = movies[movie_week] + a
    else:
        movies[movie_week] = a
    # print(movies)
    if week_wanted in movies:

        speak_output = speak_output + str(movies[week_wanted]).strip('[]')
        # for movie in movies[week_wanted]:
        #
        #     speak_output = speak_output + ", " + movie
    else:
        speak_output = "There are no movie releases."

# print(speak_output)
# print(movies[week_wanted])



