## Airflow

from datetime import timedelta

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
# These args will get passed on to each operator
# You can override them on a per-task basis during operator initialization

### JUPYTER ###

# import the libraries
#
## WebScrapping Libraries
from bs4 import BeautifulSoup
import requests
import urllib.request

## NLP and ML Libraries
import nltk
from newspaper import Article
nltk.download('floresta') # "Portuguese Treebank" divides the text into a list of sentences using ML algorithm
from nltk.corpus import stopwords
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

## Data Frame manipulation and Analytics Libraries
import pandas as pd
import time
import matplotlib.pyplot as py
import plotly_express as px
import plotly as plt
import datetime


search = 'energia'
page = 2

def _define_scrapper_cnn_website(search, page):


# """ 
# Scrapes the CNN Website based on a theme and a page number.
# """

    page_theme = search
    page_number = str(page)

    url = 'https://www.cnnbrasil.com.br/tudo-sobre/' + page_theme + '/' + 'pagina' + page_number +'/' 
    webpage = requests.get(url)
    soup = BeautifulSoup(webpage.text, 'html.parser')

    # Get the location of the information
    article_date = soup.find_all('span', attrs= {'class': 'home__title__date'}) # location of data information
    article_title = soup.find_all('h2', attrs= {'class': 'news-item-header__title'} ) # location of title information
    article_tag = soup.find_all('span', attrs= {'class': 'latest__news__category'} ) # location of the tag
    article_theme = soup.find_all('h1', attrs= {'class': 'tags__topics__title'} ) # location of the theme
    article_links = soup.find_all('a',attrs={'class': 'home__list__tag'} )# location of the links

    # Loop through the article_date
    for i in article_date:
        temp=0
        temp = i.text.strip()
        date = temp[0:10]
        time = temp[14:19]
        date_time = date +'-'+ time

        date_time = pd.to_datetime(date_time,format= '%d/%m/%Y-%H:%M').strftime('%d/%m/%Y - %H:%M')
        dates.append(date_time)

    # Loop through the article_titles and set the theme
    for i in article_title:
        temp = 0
        temp = i.text.strip()
        title.append(temp)
        theme.append(article_theme[0].text.strip().split()[2])

    # Loop through the article_tags
    for i in article_tag:
        temp = 0
        temp = i.text.strip()
        tag.append(temp)

    # Loop through the article_links
    for i in article_links:
        href = i.get('href')
        links.append(href)

        # NLP Process: Scrapes the article, download the information and parse a nlp into a interable object
        article = Article(href) # Scrapes the Article
        article.download()
        article.parse()
        article.nlp()

        # Interact with the articles
        site_name = article.meta_data['og']['site_name']
        text = article.text
        summary = article.summary
        texts.append(text)
        summarys.append(summary)
        authors.append(site_name)

def _scrape_and_generate_csv_cnn_website(search, page):
        # Create lists to store the scraped data
    theme = []
    tag = []
    title = []
    authors = []
    dates = []  
    links = []
    texts = []
    summarys = []

    # performs the scrapping with the chosen search on the given pages
    for i in range(1 , page+1):

        #applies the function
        _define_scrapper_cnn_website(search, i )

        # checks how many lines are created for each page
        print(i,        # page
        len(authors),  
        len(links), 
        len(theme), 
        len(tag), 
        len(title),
        len(dates), 
        len(texts), 
        len(summarys)
        )
        # creates a dataframe based on the stored lists

    df = pd.DataFrame( columns= ['dates','theme','authors','tag','title','summarys','texts','links' ] )
    df.dates = dates
    df.dates = pd.to_datetime(df.dates,format= '%d/%m/%Y - %H:%M')
    df.theme = theme
    df.authors = authors
    df.tag = tag
    df.title = title
    df.summarys = summarys
    df.texts = texts
    df.links = links

    # check the analyzed dates
    date_min = str(df.dates.dt.date.min().strftime('%d/%m/%Y'))+' at '+ str(df.dates.dt.time.min())
    date_max = str(df.dates.dt.date.max().strftime('%d/%m/%Y'))+' at '+ str(df.dates.dt.time.max())
    df_date_range = 'DF Date Rage: from ['+ date_min + '] to [' + date_max + ']'
    print(df_date_range)

    # checks if the dataframe has null values
    print(df.isnull().sum()) 
    return df



default_args = {
    'owner': 'vinicius_guerra ',
    'depends_on_past': False    ,   
    'start_date': days_ago(2),
    'email': ['viniciusgribas@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}
dag = DAG(
    'CNN_news_Raspagem_e_Relatorio',
    default_args=default_args,
    description='A simple tutorial DAG',
)

with dag:

    raspar =  PythonOperator(
        task_id = 'Raspar_Dados',
        python_callable = _scrape_and_generate_csv_cnn_website,
        provide_context = True,
        params = {"raspagem" : "2022-06-18"}
    )

    # gerar_df = PythonOperator(
    #     task_id = 'Gerar_DataFrame',
    #     python_callable = _generate_dataframe
    # )

    # exportar_relatorios = PythonOperator(
    #     task_id = "Exportar_Relatórios",
    #     python_callable = _reports_export
    # )

    raspar 