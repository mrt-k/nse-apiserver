!NSE

!!defaultカテゴリのスクリプト

-sCコマンドで実行されるスクリプト

* address-info.nse
https://nmap.org/nsedoc/scripts/address-info.html

* afp-serverinfo.nse
https://nmap.org/nsedoc/scripts/afp-serverinfo.html

AFPサーバーの情報を取得する.

<<<
PORT    STATE SERVICE
548/tcp open  afp
| afp-serverinfo:
|   Server Flags:
|     Flags hex: 0x837d
|     Super Client: true
|     UUIDs: false
|     UTF8 Server Name: true
|     Open Directory: true
|     Reconnect: false
|     Server Notifications: true
|     TCP/IP: true
|     Server Signature: true
|     Server Messages: true
|     Password Saving Prohibited: true
|     Password Changing: false
|     Copy File: true
|   Server Name: foobardigital
|   Machine Type: Netatalk
|   AFP Versions: AFPVersion 1.1, AFPVersion 2.0, AFPVersion 2.1, AFP2.2, AFPX03, AFP3.1
|   UAMs: DHX2
|   Server Signature: bbeb480e00000000bbeb480e00000000
|   Network Addresses:
|     192.0.2.235
|     foobardigital.com
|_  UTF8 Server Name: foobardigital
>>>

* ajp-auth.nse
https://nmap.org/nsedoc/scripts/ajp-auth.html

認証が必要とされるAJP(Apache JServ Protocol)から認証方式やレルムを取得する.

<<<
PORT     STATE SERVICE
8009/tcp open  ajp13
| ajp-auth:
|_  Digest opaque=GPui3SvCGBoHrRMMzSsgaYBV qop=auth nonce=1336063830612:935b5b389696b0f67b9193e19f47e037 realm=example.org
>>>

* ajp-methods.nse
https://nmap.org/nsedoc/scripts/ajp-methods.html

AJP(Apache JServ Protocol)サービスにOPTIONSメソッドを送信し, 利用可能なメソッドを取得する.

<<<
PORT     STATE SERVICE
8009/tcp open  ajp13
| ajp-methods:
|   Supported methods: GET HEAD POST PUT DELETE TRACE OPTIONS
|   Potentially risky methods: PUT DELETE TRACE
|_  See https://nmap.org/nsedoc/scripts/ajp-methods.html
>>>

* amqp-info.nse
https://nmap.org/nsedoc/scripts/amqp-info.html

AMQP(advanced message queuing protocol)サーバーから情報を取得する.

amqp.versionでバージョンを指定(0-8, 0-9, 0-9-1).

<<<
5672/tcp open  amqp
| amqp-info:
|   capabilities:
|     publisher_confirms: YES
|     exchange_exchange_bindings: YES
|     basic.nack: YES
|     consumer_cancel_notify: YES
|   copyright: Copyright (C) 2007-2011 VMware, Inc.
|   information: Licensed under the MPL.  See http://www.rabbitmq.com/
|   platform: Erlang/OTP
|   product: RabbitMQ
|   version: 2.4.0
|   mechanisms: PLAIN AMQPLAIN
|_  locales: en_US
>>>

* cassandra-info.nse
https://nmap.org/nsedoc/scripts/cassandra-info.html

Cassandraサービスからクラスタ名やバージョンを取得する.

<<<
PORT     STATE SERVICE   REASON
9160/tcp open  cassandra syn-ack
| cassandra-info:
|   Cluster name: Test Cluster
|_  Version: 19.10.0
>>>

* creds-summary.nse
https://nmap.org/nsedoc/scripts/creds-summary.html

スキャン中に実施した認証情報(ブルートフォースやデフォルトパスワードをチェックするスクリプトの結果)をスキャン終了後に表示.

<<<
Post-scan script results:
| creds-summary: 
|   192.168.1.169: 
|     21/ftp: 
|_      user:user - Valid credentials
Nmap done: 1 IP address (1 host up) scanned in 9.38 seconds
>>>

* dns-nsid.nse
https://nmap.org/nsedoc/scripts/dns-nsid.html

NSID(どのDNSサーバが実際に問い合わせに応答したかを外部から判定するもの)からid.serverとbind.versionを取得する.

これは以下のコマンドと同義である.

<<<
dig CH TXT bind.version @<target>
dig +nsid CH TXT id.server @<target>
>>>

<<<
53/udp open  domain  udp-response
| dns-nsid:
|   NSID dns.example.com (646E732E6578616D706C652E636F6D)
|   id.server: dns.example.com
|_  bind.version: 9.7.3-P3
>>>

* dns-recursion.nse
https://nmap.org/nsedoc/scripts/dns-recursion.html

DNSサーバーが外部のアドレスに対して名前解決を行っているか

<<<
PORT   STATE SERVICE REASON
53/udp open  domain  udp-response
|_dns-recursion: Recursion appears to be enabled
>>>

* dns-service-discovery.nse
https://nmap.org/nsedoc/scripts/dns-service-discovery.html

zeroconfのようなDNS Service Discovery protocolを利用して情報を取得.

<<<
PORT     STATE SERVICE  REASON
5353/udp open  zeroconf udp-response
| dns-service-discovery:
|   548/tcp afpovertcp
|     model=MacBook5,1
|     Address=192.168.0.2 fe80:0:0:0:223:6cff:1234:5678
|   3689/tcp daap
|     txtvers=1
|     iTSh Version=196609
|     MID=0xFB5338C04123456
|     Database ID=6FA9761FE123456
|     dmv=131078
|     Version=196616
|     OSsi=0x1F6
|     Machine Name=Patrik Karlsson\xE2\x80\x99s Library
|     Media Kinds Shared=1
|     Machine ID=8945A7123456
|     Password=0
|_    Address=192.168.0.2 fe80:0:0:0:223:6cff:1234:5678
>>>

* epmd-info.nse
https://nmap.org/nsedoc/scripts/epmd-info.html

EPMD(Erlang Port Mapper Daemon)に接続し, ノードのポート番号を取得する.

<<<
PORT     STATE SERVICE
4369/tcp open  epmd
| epmd-info.nse:
|   epmd_port: 4369
|   nodes:
|     rabbit: 36804
|_    ejabberd: 46540
>>>


* finger.nse
https://nmap.org/nsedoc/scripts/finger.html

fingerサービスからユーザー名を取得する.

<<<
PORT   STATE SERVICE
79/tcp open  finger
| finger:
| Welcome to Linux version 2.6.31.12-0.2-default at linux-pb94.site !
|  01:14am  up  18:54,  4 users,  load average: 0.14, 0.08, 0.01
|
| Login      Name                  Tty      Idle  Login Time   Where
| Gutek      Ange Gutek           *:0          -     Wed 06:19 console
| Gutek      Ange Gutek            pts/1   18:54     Wed 06:20
| Gutek      Ange Gutek           *pts/0       -     Thu 00:41
|_Gutek      Ange Gutek           *pts/4       3     Thu 01:06
>>>

* flume-master-info.nse
https://nmap.org/nsedoc/scripts/flume-master-info.html

FlumeのマスターページからFlumeやJavaのバージョンや設定などを取得する.

-vオプションを使用した場合, 詳細な情報を得られる.

<<<
PORT      STATE SERVICE         REASON
35871/tcp open  flume-master syn-ack
| flume-master-info:
|   Version:  0.9.4-cdh3u3
|   ServerID: 0
|   Flume nodes:
|     node1.example.com
|     node2.example.com
|     node5.example.com
|     node6.example.com
|     node3.example.com
|     node4.example.com
|   Zookeeper Master:
|     master1.example.com
|   Hbase Master Master:
|     hdfs://master1.example.com:8020/hbase
|   Enviroment:
|     java.runtime.name: Java(TM) SE Runtime Environment
|     java.runtime.version: 1.6.0_36-a01
|     java.version: 1.6.0_36
|     java.vm.name: Java HotSpot(TM) 64-Bit Server VM
|     java.vm.vendor: Sun Microsystems Inc.
|     java.vm.version: 14.0-b12
|     os.arch: amd64
|     os.name: Linux
|     os.version: 2.6.32-220.4.2.el6.x86_64
|     user.country: US
|     user.name: flume
|   Config:
|     dfs.datanode.address: 0.0.0.0:50010
|     dfs.datanode.http.address: 0.0.0.0:50075
|     dfs.datanode.https.address: 0.0.0.0:50475
|     dfs.datanode.ipc.address: 0.0.0.0:50020
|     dfs.http.address: master1.example.com:50070
|     dfs.https.address: 0.0.0.0:50470
|     dfs.secondary.http.address: 0.0.0.0:50090
|     flume.collector.dfs.dir: hdfs://master1.example.com/user/flume/collected
|     flume.collector.event.host: node1.example.com
|     flume.master.servers: master1.example.com
|     fs.default.name: hdfs://master1.example.com:8020
|     mapred.job.tracker: master1.example.com:9001
|     mapred.job.tracker.handler.count: 10
|     mapred.job.tracker.http.address: 0.0.0.0:50030
|     mapred.job.tracker.http.address: 0.0.0.0:50030
|     mapred.job.tracker.jobhistory.lru.cache.size: 5
|     mapred.job.tracker.persist.jobstatus.active: false
|     mapred.job.tracker.persist.jobstatus.dir: /jobtracker/jobsInfo
|     mapred.job.tracker.persist.jobstatus.hours: 0
|     mapred.job.tracker.retiredjobs.cache.size: 1000
|     mapred.task.tracker.http.address: 0.0.0.0:50060
|_    mapred.task.tracker.report.address: 127.0.0.1:0
>>>


* freelancer-info.nse
https://nmap.org/nsedoc/scripts/freelancer-info.html

Freelancerというゲームのサービス(FLServer.exe)を検知する.

-sVオプションを使用した場合, サーバ名, 現在のプレイヤー数, プレイヤーの最大人数, パスワードは設定されているかなどを表示する.

-sCオプションでの実行ではなく, 明示的に --script=freelancer-info と指定して実行した場合, プレイヤーに害を与えることができるか, 新規ユーザーを追加できるかなどについても表示する.

<<<
PORT     STATE SERVICE    REASON       VERSION
2302/udp open  freelancer udp-response Freelancer (name: Discovery Freelancer RP 24/7; players: 152/225; password: no)
| freelancer-info:
|   server name: Discovery Freelancer RP 24/7
|   server description: This is the official discovery freelancer RP server. To know more about the server, please visit www.discoverygc.com
|   players: 152
|   max. players: 225
|   password: no
|   allow players to harm other players: yes
|_  allow new players: yes
>>>

* ftp-anon
https://nmap.org/nsedoc/scripts/ftp-anon.html

FTPのanonymous(匿名)ログインできるかを確認する.

ログインできる場合, ルートディレクトリのファイル一覧を取得し書き込み可能なファイルに関しては強調表示(writeableと)される.

引数にはftp-anon.maxlistがあり, 指定した数字の数だけファイル一覧を取得する. 0の場合はファイル一覧は取得しない.

<<<
PORT   STATE SERVICE
21/tcp open  ftp
| ftp-anon: Anonymous FTP login allowed (FTP code 230)
| -rw-r--r--   1 1170     924            31 Mar 28  2001 .banner
| d--x--x--x   2 root     root         1024 Jan 14  2002 bin
| d--x--x--x   2 root     root         1024 Aug 10  1999 etc
| drwxr-srwt   2 1170     924          2048 Jul 19 18:48 incoming [NSE: writeable]
| d--x--x--x   2 root     root         1024 Jan 14  2002 lib
| drwxr-sr-x   2 1170     924          1024 Aug  5  2004 pub
|_Only 6 shown. Use --script-args ftp-anon.maxlist=-1 to see all.
>>>

* ftp-bounce.nse
https://nmap.org/nsedoc/scripts/ftp-bounce.html

FTP Bounce Attackが可能か調査する.

引数はftp-bounce.usernameとftp-bounce.passwordがあり, デフォルトではanonymous, IEUser@となっている

<<<
PORT   STATE SERVICE
21/tcp open  ftp
|_ftp-bounce: bounce working!

PORT   STATE SERVICE
21/tcp open  ftp
|_ftp-bounce: server forbids bouncing to low ports <1025

PORT   STATE SERVICE
21/tcp open  ftp
|_ftp-bounce: no banner
>>>

* ganglia-info.nse
https://nmap.org/nsedoc/scripts/ganglia-info.html

GangliaからOS, ディスク, メモリ, CPUなどの情報を取得する.

引数はganglia-info.bytes, ganglia-info.timeout, slaxml.debugがあり, それぞれ, 取得する情報のバイト数(デフォルトで1000000), タイムアウトする時間(デフォルトで30s), デバッグレベル(デフォルトで3)となっている.

<<<
8649/tcp open   unknown syn-ack
| ganglia-info:
|   Ganglia Version: 3.1.7
|   Cluster 1:
|     Name: unspecified
|     Owner: unspecified
|     Host 1:
|       Name: sled9735.sd.dreamhost.com
|       IP: 10.208.42.221
|       load_one: 0.53
|       mem_total: 24685564KB
|       os_release: 3.1.9-vs2.3.2.5
|       proc_run: 0
|       load_five: 0.52
|       gexec: OFF
|       disk_free: 305.765GB
|       mem_cached: 18857264KB
|       pkts_in: 821.73packets/sec
|       bytes_in: 72686.10bytes/sec
|       bytes_out: 5612221.50bytes/sec
|       swap_total: 1998844KB
|       mem_free: 187964KB
|       load_fifteen: 0.57
|       os_name: Linux
|       boottime: 1429708366s
|       cpu_idle: 96.3%
|       cpu_user: 2.7%
|       cpu_nice: 0.0%
|       cpu_aidle: 94.7%
|       mem_buffers: 169588KB
|       cpu_system: 0.8%
|       part_max_used: 31.5%
|       disk_total: 435.962GB
|       mem_shared: 0KB
|       cpu_wio: 0.2%
|       machine_type: x86_64
|       proc_total: 1027
|       cpu_num: 8CPUs
|       cpu_speed: 2400MHz
|       pkts_out: 3977.13packets/sec
|       swap_free: 1393392KB
>>>

* giop-info.nse
https://nmap.org/nsedoc/scripts/giop-info.html

CORBAから情報を取得する.

<<<
PORT     STATE SERVICE              REASON
1050/tcp open  java-or-OTGfileshare syn-ack
| giop-info:
|   Object: Hello
|   Context: Test
|_  Object: GoodBye
>>>

* gopher-ls.nse
https://nmap.org/nsedoc/scripts/gopher-ls.html

gopherサービスからディレクトリ一覧を取得する. goを書く人とは関係ない.

引数gopher-ls.maxfilesで取得するファイル数を指定可能. lessもしくは0で全てのファイルを取得. デフォルトは10.

<<<
70/tcp open  gopher
| gopher-ls:
| [txt] /gresearch.txt "Gopher, the next big thing?"
| [dir] /taxf "Tax Forms"
|_Only 2 shown. Use --script-args gopher-ls.maxfiles=-1 to see all.
>>>

* hadoop-datanode-info.nse
https://nmap.org/nsedoc/scripts/hadoop-datanode-info.html

Hadoopデータノードからログディレクトリなどの情報を取得する.

<<<
PORT      STATE SERVICE         REASON
50075/tcp open  hadoop-datanode syn-ack
| hadoop-datanode-info:
|_  Logs: /logs/
>>>

* hadoop-jobtracker-info.nse
https://nmap.org/nsedoc/scripts/hadoop-jobtracker-info.html

HadoopのJobTrackerからJobTrackerの状態やHadoopのバージョンなどを取得する.

<<<
50030/tcp open  hadoop-jobtracker
| hadoop-jobtracker-info:
|   State: RUNNING
|   Started: Wed May 11 22:33:44 PDT 2011, bob
|   Version: 0.20.2 (f415ef415ef415ef415ef415ef415ef415ef415e)
|   Compiled: Wed May 11 22:33:44 PDT 2011 by bob from unknown
|   Identifier: 201111031342
|   Log Files: logs/
|   Tasktrackers:
|     tracker1.example.com:50060
|     tracker2.example.com:50060
|   Userhistory:
|     User: bob (Wed Sep 07 12:14:33 CEST 2011)
|_    User: bob (Wed Sep 07 12:14:33 CEST 2011)
>>>

* hadoop-namenode-info.nse
https://nmap.org/nsedoc/scripts/hadoop-namenode-info.html

HadoopのNameNodeからHadoopのバージョンやサービスの開始時間などを取得する

<<<
PORT      STATE SERVICE         REASON
50070/tcp open  hadoop-namenode syn-ack
| hadoop-namenode-info:
|   Started:  Wed May 11 22:33:44 PDT 2011
|   Version:  0.20.2-cdh3u1, f415ef415ef415ef415ef415ef415ef415ef415e
|   Compiled:  Wed May 11 22:33:44 PDT 2011 by bob from unknown
|   Upgrades:  There are no upgrades in progress.
|   Filesystem: /nn_browsedfscontent.jsp
|   Logs: /logs/
|   Storage:
|     Total   Used (DFS)  Used (Non DFS)  Remaining
|     100 TB  85 TB       500 GB          14.5 TB
|   Datanodes (Live):
|     datanode1.example.com:50075
|_    datanode2.example.com:50075
>>>

* hadoop-secondary-namenode-info.nse
https://nmap.org/nsedoc/scripts/hadoop-secondary-namenode-info.html

HadoopのSecondary NameNodeからHadoopのバージョンやサービスの開始時間などを取得する

<<<
PORT      STATE  SERVICE REASON
50090/tcp open   unknown syn-ack
| hadoop-secondary-namenode-info:
|   Start: Wed May 11 22:33:44 PDT 2011
|   Version: 0.20.2, f415ef415ef415ef415ef415ef415ef415ef415e
|   Compiled: Wed May 11 22:33:44 PDT 2011 by bob from unknown
|   Log: /logs/
|   namenode: namenode1.example.com/192.0.1.1:8020
|   Last Checkpoint: Wed May 11 22:33:44 PDT 2011
|   Checkpoint Period: 3600 seconds
|_  Checkpoint Size: 12345678 MB
>>>

* hadoop-tasktracker-info.nse
https://nmap.org/nsedoc/scripts/hadoop-tasktracker-info.html

HadoopのTaskTrackerからHadoopのバージョンやコンパイル日時などを取得

<<<
PORT      STATE SERVICE            REASON
50060/tcp open  hadoop-tasktracker syn-ack
| hadoop-tasktracker-info:
|   Version: 0.20.1 (f415ef415ef415ef415ef415ef415ef415ef415e)
|   Compiled: Wed May 11 22:33:44 PDT 2011 by bob from unknown
|_  Logs: /logs/
>>>

* hbase-master-info.nse
https://nmap.org/nsedoc/scripts/hbase-master-info.html

HBaseからHBaseのバージョンやRegionサーバーなどの情報を取得する.

<<<
| hbase-master-info:
|   Hbase Version: 0.90.1
|   Hbase Compiled: Wed May 11 22:33:44 PDT 2011, bob
|   HBase Root Directory: hdfs://master.example.com:8020/hbase
|   Hadoop Version: 0.20  f415ef415ef415ef415ef415ef415ef415ef415e
|   Hadoop Compiled: Wed May 11 22:33:44 PDT 2011, bob
|   Average Load: 0.12
|   Zookeeper Quorum: zookeeper.example.com:2181
|   Region Servers:
|     region1.example.com:60030
|_    region2.example.com:60030
>>>

* hbase-region-info.nse
https://nmap.org/nsedoc/scripts/hbase-region-info.html

HBaseのRegionサーバーの情報を取得する.

<<<
PORT      STATE SERVICE      REASON
60030/tcp open  hbase-region syn-ack
| hbase-region-info:
|   Hbase Version: 0.90.1
|   Hbase Compiled: Wed May 11 22:33:44 PDT 2011, bob
|   Metrics requests=0, regions=0, stores=0, storefiles=0, storefileIndexSize=0, memstoreSize=0,
|   compactionQueueSize=0, flushQueueSize=0, usedHeap=0, maxHeap=0, blockCacheSize=0,
|   blockCacheFree=0, blockCacheCount=0, blockCacheHitCount=0, blockCacheMissCount=0,
|   blockCacheEvictedCount=0, blockCacheHitRatio=0, blockCacheHitCachingRatio=0
|_  Zookeeper Quorum: zookeeper.example.com:2181
>>>

* hddtemp-info.nse
https://nmap.org/nsedoc/scripts/hddtemp-info.html

hddtempからHDDの情報を取得する.

<<<
7634/tcp open  hddtemp
| hddtemp-info:
|_  /dev/sda: WDC WD2500JS-60MHB1: 38 C
>>>

* hnap-info.nse
https://nmap.org/nsedoc/scripts/hnap-info.html

HNAPを利用している機器の情報を取得する. カメラやルーター, NASなどのベンダー名やファームウェアバージョンなどの情報を取得可能.

<<<
PORT     STATE SERVICE    REASON
8080/tcp open  http-proxy syn-ack
| hnap-info: 
|   Type: GatewayWithWiFi
|   Device: Ingraham
|   Vendor: Linksys
|   Description: Linksys E1200
|   Model: E1200
|   Firmware: 1.0.00 build 11
|   Presentation URL: http://192.168.1.1/
|   SOAPACTIONS: 
|     http://purenetworks.com/HNAP1/IsDeviceReady
|     http://purenetworks.com/HNAP1/GetDeviceSettings
|     http://purenetworks.com/HNAP1/SetDeviceSettings
|     http://purenetworks.com/HNAP1/GetDeviceSettings2
|     http://purenetworks.com/HNAP1/SetDeviceSettings2
>>>


