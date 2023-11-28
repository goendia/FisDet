# -*- coding: utf-8 -*-
"""
Created on Tue Feb 03 01:05:43 2015

@author: Manuel
"""

import sqlite3 as lite
import sys

def sqlEditor(debPath, sql):
    
    con = lite.connect(debPath)
    with con:
        
        cur = con.cursor()    
        cur.execute(sql)
        #cur.execute("SELECT sql FROM sqlite_master WHERE tbl_name = 'fische' AND type = 'table'")
       # cur.execute("SELECT * FROM fische ORDER BY Sub.ID ASC")
    
       # print(table_info(table_name)
        while True:
          
            row = cur.fetchone()
            
            if row:
                print row[0], row[1], row[2], row[3], row[4]
            else: 
                break
sqlEditor('C:\CStuff\home.db', "SELECT * FROM fische ORDER BY sub_id DESC LIMIT 256")