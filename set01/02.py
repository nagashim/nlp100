# coding: utf-8
"""
(2) タブ１文字につきスペース１文字に置換したもの．
    確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

import sys

for line in sys.stdin:
    decoded = line.decode("utf-8")
    print decoded.rstrip("\r\n").replace(u"\t", u" ").encode("utf-8")
