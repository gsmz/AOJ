# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        AOJUserSolvedList.py
# Purpose:     AOJのAPIを使った簡単な解いた問題一覧取得スクリプト
#
# Author:      gsmz
#
# Created:     22/03/2013
# Copyright:   (c) gsmz 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from xml.dom import minidom
from urllib import urlopen
def main():
    # 取得したい人のUserIDを追加していく
    # 例) useridlist = ["gsmz", "piyo", "hoge"]
    #
    useridlist = []
    for userid in useridlist:
        src = (urlopen("http://judge.u-aizu.ac.jp/onlinejudge/webservice/user?id="+userid).read())
        elements = minidom.parseString(src).getElementsByTagName("id")
        solved_elements = minidom.parseString(src).getElementsByTagName("solved")
        for i, element in enumerate(elements) :
            if i == 0:
                print "user id[", element.childNodes[0].data, "]"
                print "solved : ", solved_elements[0].childNodes[0].data
                print "---solved list:"
            else:
                prob_id = element.childNodes[0].data
                #prob_src = (urlopen("http://judge.u-aizu.ac.jp/onlinejudge/webservice/problem?id="+prob_id).read())
                #prob_elements = minidom.parseString(prob_src).getElementsByTagName("name")
                print "  |-[%3d] : %5s " % (i,prob_id) #, prob_elements[0].childNodes[0].data.replace('\n', ''))
        print "------------------------------"
        print "\n"
if __name__ == '__main__':
    main()
