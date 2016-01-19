# nse-apiserver

NSE(Nmap Scripting Engine) API Server

===

# これはなに

Nmapに付属しているNSEを検索しやすくするRESTful APIサーバーです。  
curlなどで投げてあげると以下のような結果が返ってきます.

```
[
  {
    "name": "ftp-anon",
    "category": [
      "auth",
      "default",
      "safe"
    ],
    "summary": "Checks if an FTP server allows anonymous logins.\r\nIf anonymous is allowed, gets a directory listing of the root directory and highlights writeable files.",
    "summary_ja": "FTPサーバーにAnonymousログインが可能かをチェックします。\r\nAnnonymousログインが可能な場合、ルートディレクトリのディレクトリ一覧を取得し、書き込み可能なファイルを強調表示しま
す。",
    "argvs": [
      {
        "id": 3,
        "argv": "ftp-anon.maxlist",
        "argv_description": "The maximum number of files to return in the directory listing. By default it is 20, or unlimited if verbosity is enabled. Use a negative number to disable the limit
, or 0 to disable the listing entirely.",
        "argv_description_ja": "ファイルを取得する数です。デフォルトは20ですが、verboseモードの場合は無制限です。\r\n無制限に取得したい場合は負の数を, ファイルの取得を無効化するのであれば0を指定
してください。"
      }
    ],
    "example_usage": "nmap -sV -sC <target>\r\nnmap -sV --script=ftp-anon",
    "example_output": "PORT   STATE SERVICE\r\n21/tcp open  ftp\r\n| ftp-anon: Anonymous FTP login allowed (FTP code 230)\r\n| -rw-r--r--   1 1170     924            31 Mar 28  2001 .banner\r\n|
 d--x--x--x   2 root     root         1024 Jan 14  2002 bin\r\n| d--x--x--x   2 root     root         1024 Aug 10  1999 etc\r\n| drwxr-srwt   2 1170     924          2048 Jul 19 18:48 incoming [
NSE: writeable]\r\n| d--x--x--x   2 root     root         1024 Jan 14  2002 lib\r\n| drwxr-sr-x   2 1170     924          1024 Aug  5  2004 pub\r\n|_Only 6 shown. Use --script-args ftp-anon.maxl
ist=-1 to see all.",
    "author": "Eddie Bell, Rob Nicholls, Ange Gutek, David Fifield",
    "download_link": "http://nmap.org/svn/scripts/ftp-anon.nse"
  },

```

* name : スクリプト名
* category : カテゴリ名
* summary : スクリプトの説明
* summary_ja : スクリプトの説明(日本語)
* argvs : 引数の情報
* argv : 引数名
* argv_description : 引数の説明
* argv_description_ja : 引数の説明(日本語)
* example_usage : 使い方の例
* example_output : 出力例
* author : 作者
* download_link : ダウンロードリンク


===

# データ

NSEのデータはまだ未完成です。  
[NSE Doc](https://nmap.org/nsedoc/index.html)からデータを地道に投入していくつもりです。  
データはdb.jsonとして保存してあるので, データを追加してプルリクしていただけると助かります。

===

# Install

```
git clone https://github.com/mrt-k/nse-apiserver
cd nse-apiserver
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py loaddata db.json
```

===

# Usage

```
./manage.py runserver
```

###### 全て取得

```
$ curl http://localhost:8000/api/nse/ | jq
[
  {
    "name": "ftp-anon",
    "category": [
      "auth",
      "default",
      "safe"
    ],
    "summary": "Checks if an FTP server allows anonymous logins.\r\nIf anonymous is allowed, gets a directory listing of the root directory and highlights writeable files.",
    "summary_ja": "FTPサーバーにAnonymousログインが可能かをチェックします。\r\nAnnonymousログインが可能な場合、ルートディレクトリのディレクトリ一覧を取得し、書き込み可能なファイルを強調表示しま
す。",
    "argvs": [
      {
        "id": 3,
        "argv": "ftp-anon.maxlist",
        "argv_description": "The maximum number of files to return in the directory listing. By default it is 20, or unlimited if verbosity is enabled. Use a negative number to disable the limit
, or 0 to disable the listing entirely.",
        "argv_description_ja": "ファイルを取得する数です。デフォルトは20ですが、verboseモードの場合は無制限です。\r\n無制限に取得したい場合は負の数を, ファイルの取得を無効化するのであれば0を指定
してください。"
      }
    ],
    "example_usage": "nmap -sV -sC <target>\r\nnmap -sV --script=ftp-anon",
    "example_output": "PORT   STATE SERVICE\r\n21/tcp open  ftp\r\n| ftp-anon: Anonymous FTP login allowed (FTP code 230)\r\n| -rw-r--r--   1 1170     924            31 Mar 28  2001 .banner\r\n|
 d--x--x--x   2 root     root         1024 Jan 14  2002 bin\r\n| d--x--x--x   2 root     root         1024 Aug 10  1999 etc\r\n| drwxr-srwt   2 1170     924          2048 Jul 19 18:48 incoming [
NSE: writeable]\r\n| d--x--x--x   2 root     root         1024 Jan 14  2002 lib\r\n| drwxr-sr-x   2 1170     924          1024 Aug  5  2004 pub\r\n|_Only 6 shown. Use --script-args ftp-anon.maxl
ist=-1 to see all.",
    "author": "Eddie Bell, Rob Nicholls, Ange Gutek, David Fifield",
    "download_link": "http://nmap.org/svn/scripts/ftp-anon.nse"
  },

```

###### フィルタ

以下のパラメータでフィルタしてあります

* name : スクリプト名
* category : カテゴリ名
* author : 作者名

Ex) authカテゴリに属するNSEにフィルタ

```
$ curl http://localhost:8000/api/nse/\?category\=auth | jq
[
  {
    "name": "ftp-anon",
    "category": [
      "auth",
      "default",
      "safe"
    ],
    "summary": "Checks if an FTP server allows anonymous logins.\r\nIf anonymous is allowed, gets a directory listing of the root directory and highlights writeable files.",
    "summary_ja": "FTPサーバーにAnonymousログインが可能かをチェックします。\r\nAnnonymousログインが可能な場合、ルートディレクトリのディレクトリ一覧を取得し、書き込み可能なファイルを強調表示しま
す。",
    "argvs": [
      {
        "id": 3,
        "argv": "ftp-anon.maxlist",
        "argv_description": "The maximum number of files to return in the directory listing. By default it is 20, or unlimited if verbosity is enabled. Use a negative number to disable the limit
, or 0 to disable the listing entirely.",
        "argv_description_ja": "ファイルを取得する数です。デフォルトは20ですが、verboseモードの場合は無制限です。\r\n無制限に取得したい場合は負の数を, ファイルの取得を無効化するのであれば0を指定
してください。"
      }
    ],
    "example_usage": "nmap -sV -sC <target>\r\nnmap -sV --script=ftp-anon",
    "example_output": "PORT   STATE SERVICE\r\n21/tcp open  ftp\r\n| ftp-anon: Anonymous FTP login allowed (FTP code 230)\r\n| -rw-r--r--   1 1170     924            31 Mar 28  2001 .banner\r\n|
 d--x--x--x   2 root     root         1024 Jan 14  2002 bin\r\n| d--x--x--x   2 root     root         1024 Aug 10  1999 etc\r\n| drwxr-srwt   2 1170     924          2048 Jul 19 18:48 incoming [
NSE: writeable]\r\n| d--x--x--x   2 root     root         1024 Jan 14  2002 lib\r\n| drwxr-sr-x   2 1170     924          1024 Aug  5  2004 pub\r\n|_Only 6 shown. Use --script-args ftp-anon.maxl
ist=-1 to see all.",
    "author": "Eddie Bell, Rob Nicholls, Ange Gutek, David Fifield",
    "download_link": "http://nmap.org/svn/scripts/ftp-anon.nse"
  },
  {
    "name": "ajp-auth",
    "category": [
      "auth",
      "default",
      "safe"
```


###### 検索

以下の要素から検索結果が返ってきます。

* name : スクリプト名
* category : カテゴリ名
* author : 作者名

```
$ curl http://localhost:8000/api/nse/\?search\=auth | jq
```

# TODO

* めっちゃある

