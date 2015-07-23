#-*- coding: utf-8 -*-
import shelve
from contextlib import closing

class save_data():
    def __init__(self):     
        print "deal the data"
    def creat_shelf(self,key,value):
        with closing(shelve.open('test_shelf.db')) as s:
            s[key]=value
    def print_shelf(self,key):
        with closing(shelve.open('test_shelf.db')) as s:
            existing = s[key]
            print existing
    def del_shelf_key(self,key):
        with closing(shelve.open('test_shelf.db')) as s:
            del s[key]
    def get_all_val(self):
        with closing(shelve.open('test_shelf.db')) as s:
            print s
            data_dic = s.items()
            
            #print [a.decode('utf8') for a in s]
            return data_dic
            #return [a for a in s]
        
if __name__ == '__main__':
    key='\\bjfile02\BJShare\Public\TS\Field_Captured_TS\中星9码流\20131108\file_ABS_20131108_11880MHz.ts\ABS_20131108_11880MHz.ts'
    value={'int':12,'float':9.5,'string':'sample data'}
    data = save_data()
    #data.creat_shelf(key,value)     
    #data.del_shelf_key(key)
    #data.print_shelf(key)
    data.get_all_val()