#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  speedtester.py
#
#  Copyright 2019 Ian Searle <ian.searle@rmit.edu.au>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import speedtest
import mysql.connector

HOSTNAME='inte2043.its.rmit.edu.au'
USERNAME='inte2043'
PASSWD='Business_IT'
DBNAME='inte2043'
TABLENAME='speedtest'

DB_WRITE=True

def _set_query (download, upload, url, isp):
        download = str(download)
        upload = str(upload)
        return ("INSERT INTO " + TABLENAME + "(download_speed, upload_speed, url, isp) VALUES ("+download+","+upload+",'"+url+"','"+isp+"');")

def _sql_write(sql_query):
    db=mysql.connector.connect(host=HOSTNAME,user=USERNAME,passwd=PASSWD,db=DBNAME)
    curs = db.cursor()
    curs.execute(sql_query)
    db.commit()
    curs.close()
    db.close()
    return (0)

def sql_write(download, upload, url, isp):
    if DB_WRITE:
        sql_query=_set_query (download, upload, url, isp)
#        print(sql_query)
#        quit ()
        _sql_write(sql_query)

def print_data (download, upload, url, isp):
    print('Download:', download, 'Mb')
    print('Upload:',upload, 'Mb')
    print('URL:',url)
    print('ISP:',isp)
    return(0)

def speedtester():
    print ("Wait for Speed Test ...")
    servers = []
# If you want to test against a specific server
# servers = [1234]

    s = speedtest.Speedtest()
    s.get_servers(servers)
    s.get_best_server()
    s.download()
    s.upload()
    s.results.share()

    results_dict = s.results.dict()
    return(results_dict)

def main(args):
    results=speedtester()
    download=round(results['download']/1048576,2)
    upload=round(results['upload']/1048576,2)
    url=results['server']['url']
    isp=results['client']['isp']
    print_data (download, upload, url, isp)
    sql_write(download, upload, url, isp)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
