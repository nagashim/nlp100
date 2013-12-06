# coding: utf-8
"""
(5) 自然数Nをコマンドライン引数にとり，入力のうち先頭のN行だけ．
    確認にはheadコマンドを用いよ．
"""

import sys

n = int(sys.argv[1])
lines = sys.stdin.readlines()
for line in lines[:n]:
    print line.rstrip()
