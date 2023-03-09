# LinkedIn connections scraper - Effortlessly Scrape LinkedIn Connections with this Python Command Line Tool

This command line LinkedIn connections scraper is a powerful tool that enables you to easily scrape information from your LinkedIn connections and store it in an Excel file. With just a few simple commands, the tool can extract key information such as first name, last name, gender, and LinkedIn URL, helping you to better manage your professional network. Whether you're looking to build new connections, stay in touch with existing ones, or simply keep track of your LinkedIn activity, the LinkedIn connections scraper is a must-have tool for any professional looking to get ahead.

# Prerequisites

1. You must own a LinkedIn account.
2. You must have access to the target person's connections. This will usually happen when you are connected to them. If you are unsure about them try to go first manually on their profile manually and check if you can see their connections data.
3. You must have Python installed on your machine. Plese refer to [their official page](https://www.python.org/downloads/) for instructions in case you do not.

# Command line arguments:

```
  -h, --help            show this help message and exit
  --start START         The index of the first page to scrape
  --end END             The index of the last page to scrape
  --target_url TARGET_URL The url of the profile you want to scrape the connection from
```

# Instructions

1. Clone this repository 

```
$ git clone https://github.com/aao056/linkedin-connection-scraper.git
```
2. Install the dependencies
```
$ pip install -r requirements.txt
```
3. Create in the same directory an .env file containing your credentials:
```
EMAIL=<YOUR-LINKEDIN-EMAIL>
PASSWORD=<YOUR-LINKEDIN-PASSWORD>
```
4. You should be able to run it now like this:
```
$ python scraper.py --start 1 --end 10 --target_url=https://www.linkedin.com/in/john-doe/
```
5. Now you should have a .xlsx file called data.xlsx in the current project directory.

# Bonus section

When dealing with targets with a many connections (above 20 pages), for best results, it is ideal to run the script multiple times in order to cover the range and not attempt to retrieve all the information from one run. For example, let us take a profile with 900+ connections ( about 99 pages ):

```
$ python scraper.py --start 1 --end 20 --target_url=https://www.linkedin.com/in/john-doe/
$ python scraper.py --start 20 --end 40 --target_url=https://www.linkedin.com/in/john-doe/
$ python scraper.py --start 40 --end 60 --target_url=https://www.linkedin.com/in/john-doe/
$ python scraper.py --start 60 --end 80 --target_url=https://www.linkedin.com/in/john-doe/
$ python scraper.py --start 80 --end 100 --target_url=https://www.linkedin.com/in/john-doe/
```
