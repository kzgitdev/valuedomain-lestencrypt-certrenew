## 概要
value-domain のAPIを使って、Letsencrypt のTXTレコード情報を追加・更新・削除するスクリプトです。

## 用途
LetsencryptのDNS-01チャレンジを活用して、3ヶ月ごとにrenewを実行するときに活用できます。


## 使用環境・開発環境

Ubuntu:20.04 docker image
docker コンテナでpython実行環境を構築

必要なパッケージ
Python、dnsutils
詳細はsetup.shをご覧ください。


## 使い方

0. API KEYの発行・再発行

Value-domainのAPIサーバーを使用するためのAPI KEYを取得します。

https://www.value-domain.com/vdapi/

1. apikey.txtにAPI KEYを記述する
```
$ vi apikey.txt
rjXryrRhtqBcy1bsdZp5swvjO7eftiLDF6Gu1Pu5WCW4b1teJo4ULZb5WwvX2U3kFci5jSE8fMBGSMqwKpX0awDF0aTiqeMXSoxU
```
2. cert.pyを実行します。
```
$ ptyhon
>>> import cert
>>> cert = cert.Certificate('example.com')
```

3.関数について

3-1.
現在のDNS/URL情報を取得できます。

cert.records

3-2.
DNS/URL情報の追加
```
$ cert.addRecords(['txt _acme-challenge L31X44xN2NMC65AQsqxfdSW6unlvSb2dKrHHQiVk6A2JWcMDk9d0I8J4GsdGKyEhsSpNxUgLOm9I9STlOLS5Kg0JAJ1WKrMIfTU'])
*value domain のレコードの記述に従っています。
```
3-2
DNS/URL情報の更新
cert.putRequest()

3-3
DNS/URL情報の削除
削除したいレコードを記述し、DNS/URL情報を更新します
```
$ cert.removeRecords(['txt _acme-challenge txt L31X44xN2NMC65AQsqxfdSW6unlvSb2dKrHHQiVk6A2JWcMDk9d0I8J4GsdGKyEhsSpNxUgLOm9I9STlOLS5Kg0JAJ1WKrMIfTU'])
$ cert.putRequest()
```
3-4
digコマンドでDNS/URL情報を確認する
```
$ cert.commandDig(['-t txt _acme-challenge.example.com'])
; <<>> DiG 9.16.1-Ubuntu <<>> @ns1.value-domain.com -t txt _acme-challenge.example.com
; (3 servers found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 498
;; flags: qr aa rd; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1680
;; QUESTION SECTION:
;_acme-challenge.example.com.  IN      TXT

;; ANSWER SECTION:
_acme-challenge.example.com. 60 IN     TXT     "L31X44xN2NMC65AQsqxfdSW6unlvSb2dKrHHQiVk6A2JWcMDk9d0I8J4GsdGKyEhsSpNxUgLOm9I9STlOLS5Kg0JAJ1WKrMIfTU"
_acme-challenge.example.com. 60 IN     TXT     "r4yhBYWHLmHx60h7NJj57P5M1XP5AwaS3CVCGZNg3YPucdBxoCn71Uta8kg0IhXwoZzSokqc3FJzNgz27FASTrwH3m5Q6pEfCWu"

;; Query time: 28 msec
;; SERVER: 54.65.150.1#53(54.65.150.1)
;; WHEN: Wed Dec 16 05:41:40 UTC 2020
;; MSG SIZE  rcvd: 285

```
