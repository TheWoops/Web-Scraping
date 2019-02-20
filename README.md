# Web Scraping kununu.com

Little project to scrape company reviews from kununu.com with the [Scrapy framework](https://docs.scrapy.org/en/latest/intro/overview.html) (based on Python).

*"Scrapy is an application framework for crawling web sites and extracting structured data <br />
which can be used for a wide range of useful applications, 
like data mining, information processing or historical archival."*


### Prerequisites

+ Scrapy installed on your machine<br />
 &nbsp; &nbsp; &nbsp; &nbsp;  → Follow this installation guide: https://docs.scrapy.org/en/latest/intro/install.html
 
### How to run this project

1. Clone this repo into your scrapy folder. *(where the default tutorial folder should exist after your installation)*
2. Your folder structure should look something like this:

         scrapy/kununu/
            README.md
            scrapy.cfg
            __init__.p
            kununu_project/
                    items.py
                    middlewares.py
                    pipelines.py
                    settings.py
                    spiders/
                       __init__.py
                       kununu.py

        scrapy/tutorial/
            scrapy.cfg
            tutorial/
                    items.py
                    ...

3. Open your python CLI (I used anaconda prompt):<br />
       3.1 Navigate into the spider folder within scrapy folder → (scrapy/kununu/kununu_project/spiders)<br />
       3.2 Execute the following command: scrapy runspider kununu.py
       
4. By default it scrapes reviews from ec4u expert consulting ag.<br />
   You can change this by adapting the links within the "kununu.py" - Spider.




    
