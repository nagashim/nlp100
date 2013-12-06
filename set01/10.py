# coding: utf-8
"""
(10) 各行の２コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べよ．
     ただし，(3)で作成したプログラムの出力（col2.txt）を読み込むプログラムとして
     実装せよ．
     確認にはcut, uniq, sortコマンドを用いよ．
"""

import sys

col2s = []
for line in sys.stdin:
    col2s.append(line.decode("utf-8").rstrip(u"\r\n"))

freq = {}
for col2 in col2s:
    freq[col2] = freq[col2] + 1 if col2 in freq else 1

for key, value in sorted(freq.items(), key=lambda f: f[1], reverse=True):
    print key.encode("utf-8"), value
