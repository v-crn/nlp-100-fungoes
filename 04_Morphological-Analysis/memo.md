# 第4章　形態素解析

## パッケージのインストール

[MeCabとCaboChaをMacに導入してPythonから使ってみる - Qiita](https://qiita.com/musaprg/items/9a572ad5c4e28f79d2ae)

### KNP

[ku-nlp/pyknp: A Python Module for JUMAN++/KNP](https://github.com/ku-nlp/pyknp)

次節で示すように、cabocha の導入ができなかったので代わりにこちらの係り受け解析器 "KNP" を使用する。

### cabocha (cabocha-python の導入ができなかったので不採用)

[Mac(Catalina)にcabocha-pythonがインストールできないときの対処法 - Qiita](https://qiita.com/minetta30/items/06929b7eca48cc5b10fb)

```zsh
./configure --with-mecab-config=`which mecab-config` --with-charset=UTF8
make
```

Terminal に `cabocha` と打ち込んで適当な日本語の文章を入力すると係り受け解析結果を返してくれるようになればOK。

#### Python バンディング

cabocha-python のインストールでエラーが発生してしまう。

```
❯ pyflow install cabocha-python
Found lockfile
⬇ Installing cabocha_python 0.69.1 ...
thread 'main' panicked at 'Problem running setup.py bdist_wheel: Os { code: 2, kind: NotFound, message: "No such file or directory" }', /Users/USERNAME/.cargo/registry/src/github.com-1ecc6299db9ec823/pyflow-0.2.5/src/install.rs:344:13
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
```

試したこと

- `set RUST_BACKTRACE=1`
- make を使ってインストール

結局解決できなかった。

## 形態素解析済みデータの用意

```sh
curl -O http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt
mecab < neko.txt > neko.txt.mecab
```

mecab < ./data/neko.txt > ./data/neko.txt.mecab
