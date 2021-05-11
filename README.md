# Yahoo-finance-scraping

## Description of the script

This script scraps historical finance data from [yahoo finance website](https://finance.yahoo.com/), based on company name, starting and ending period and frequency interval, then represents the data using RESTful services, in this case flask was used.

## Languages and tools

<img align="left" alt="Python" width="70px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" />
<img align="left" alt="Beautifulsoup" width="120px" src="https://sixfeetup.com/blog/an-introduction-to-beautifulsoup/@@images/27e8bf2a-5469-407e-b84d-5cf53b1b0bb6.png" />
<img align="left" alt="Flask" width="120px" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/flask/flask.png" />
<img align="left" alt="Pandas" width="120px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png" />
<img align="left" alt="SQLite3" width="120px" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/SQLite370.svg/1200px-SQLite370.svg.png" /> </br> </br> </br> </br>
 


### Requirements

#### Install `requirements.txt` using following command

```shell
pip install -r requirements.txt
```

### Quick guide

#### To run the code type `python api.py`

#### After running, you can fetch the data from the server by sending GET request to

```shell
http://127.0.0.1:5000/api/v7/finances/historical/all
```
