# -*- coding: utf-8 -*-
import itertools
inputlist = list(map(str, input().split()))

# permutationsをつかうと順列（全パターンの並び順）を表示できる
outputlist = list(itertools.permutations(inputlist))
print('# result as it is.')
print(outputlist)  # 単純な結果表示
print('# --------------')
print('')
print('# result as words')
print(','.join([''.join(outputlist[i])
                for i in range(len(outputlist))]))  # 文字列をつなげて単語として出力
print('# --------------')
print('')
