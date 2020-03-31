# 本ファイルの実行コマンド
# zsh ./unix-basics.sh

echo '10. 行数のカウント'
# 行数をカウントせよ．確認にはwcコマンドを用いよ．

wc -l hightemp.txt

echo '11. タブをスペースに置換'
# タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．

echo 'sed'
sed s/$'\t'/$' '/g hightemp.txt 

echo 'tr'
tr '\t' ' ' < hightemp.txt

echo 'expand'
expand -t 1 hightemp.txt

echo '12. 1列目をcol1.txtに，2列目をcol2.txtに保存'
# 各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．

cut -f 1 hightemp.txt > col1.txt
cut -f 2 hightemp.txt > col2.txt

echo '13. col1.txtとcol2.txtをマージ'
# 12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．確認にはpasteコマンドを用いよ．
paste col[1-2].txt > cols.txt

echo '14. 先頭からN行を出力'
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
echo 'Enter a head number'
read n_head
head -n $n_head hightemp.txt

echo '15. 末尾のN行を出力'
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
echo 'Enter a tail number'
read n_tail
tail -n $n_tail hightemp.txt

echo '16. ファイルをN分割する'
# 自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．

echo '17. １列目の文字列の異なり'
# 1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．

echo '18. 各行を3コラム目の数値の降順にソート'
# 各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

echo '19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる'
# 各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
