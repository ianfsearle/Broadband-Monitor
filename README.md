# Broadband Speed Test
This activity measures the upload and download speed of an Internet connection and logs the data to a MySQL database.  
## Equipment
* Raspberry Pi Kit including keyboard screen and mouse.
* Network connection - wired or wireless

Set up the equipment as instructed in the Week 10 notes.
## Software libraries
The instructions are on the public repository, *Github*.  Here is the URL: 
[https://github.com/sivel/speedtest-cli](https://github.com/sivel/speedtest-cli)

**Note**: Install the software for Python 3.  The instructions in the repository are for Python 2.  The command to install is:

~~~
pip3 install speedtest-cli
~~~
Follow the *Usage* examples for the command line utility. Note the difference in output when the **-- csv** parameter is used.  
## Recording data to a spreadsheet
We will now change the parameters to the speedtest program so that we get the data in a form that can be included in a spreadsheet.

Firstly we get the column headers and put them into the spreadsheet file.

~~~
speedtest --csv-header > speedtest.csv
~~~

Then we will get the first row of data:

~~~
speedtest --csv >> speedtest.csv
~~~
Repeat the last command a few times:

~~~
speedtest --csv >> speedtest.csv
~~~
Open the speedtest.csv with LibreOffice Calc and see the spreadsheet of speed test results.
## Setting up the database
### Install MySQL libraries

~~~
pip3 install mysql-connector-python
~~~
### Create the database
Use whatever tool you are comfortable with to connect to the database server on *inte2043.ite.rmit.edu.au*.  You will be able to see the authentication details you need. 


**Note**: change the table name to something unique for your group
~~~
CREATE TABLE speedtest
  (id bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  download_speed FLOAT NOT NULL,
  upload_speed FLOAT NOT NULL,
  url VARCHAR (200),
  isp VARCHAR (50),
  time_date timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `time_date_inx` (`time_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
~~~
Test your database with an INSERT command modeled on this one but change to ber compatible with the table you created.

~~~
INSERT INTO speedtest (download_speed, upload_speed, url, isp) VALUES (1, 2, 'example.com', 'MyISP');
~~~
And test again with  

~~~
SELECT * FROM speedtest;
~~~
# Run the Python Program
Load the **speedtester.py** Python program into an editor (Geany is a suitable editor).  
Look for the lines:
~~~
HOSTNAME='inte2043.its.rmit.edu.au'
USERNAME='inte2043'
PASSWD='Business_IT'
DBNAME='inte2043'
TABLENAME='speedtest'
~~~
Change the TABLENAME to suit the one you set up in the database.

Run the Python program with either:

~~~
python3 speedtester.py
~~~
or
~~~
./speedtester.py
~~~
Query the database to see if the data has been recorded.
# Evidence
Show your tutor the data in the spreadsheet and in the database.