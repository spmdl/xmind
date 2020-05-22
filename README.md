# XMind

向兩位大神專案致敬

[coolcode/tomato-clock](https://github.com/coolcode/tomato-clock)

[zhuifengshen/xmind](https://github.com/zhuifengshen/xmind)

這邊修改了 create_xmind.py 的部分（引入 tomato-clock）

* [想了解更多詳細過程可以參考我的筆記](https://medium.com/@cbb104002/side-project-tomato-clock-xmind-d5c2ddf14e9b?source=friends_link&sk=107d0970b1a8f8748983d0cd50a2bbc1)

## Table of Contents

- [Background](#background)
- [Install](#install)
- [Usage](#usage)
- [執行環境](#執行環境)

### Background

使用番茄工作法以及 Ｍindmap 紀錄進度，在透過批判性思維來檢視

問題：
常常太鑽牛角尖在一些小問題，一但方向想錯了沒有去檢視，往往就會額外花很多時間去解決。

解決：
1. 避免浪費一大堆時間在一個小問題上：番茄工作法（tomato-clock）
2. 檢視：mindmap 做筆記統整（xmind）
3. 檢討：檢視 mindmap 找出改進的地方（批判性思維 ）

## Install

```
[coolcode/tomato-clock](https://github.com/coolcode/tomato-clock)

[zhuifengshen/xmind](https://github.com/zhuifengshen/xmind)

請先學習 run 起上方兩個大神的專案（喜歡的可以給個 Star👍）
```

## Usage

```bash
$ git clone https://github.com/spmdl/xmind.git
```

```bash
$ cd example
$ python create_xmind.py
```

執行過程
```bash
create root node:
flask Hello Wrold
t:tree | c:create child_node | e:end
input: c
child_node_name：MVC
w:web | k:keep | ed:edic web | e:end
 當前 web
 請輸入選擇： w
web_name：架構圖
web_src：https://gitmind.com/app/flowchart/33b171656
create node | end
 at 架構圖->[]
input node：基礎架構圖
create node | end
 at 架構圖->['基礎架構圖']
input node：end
w:web | k:keep | ed:edic web | e:end
 當前 架構圖->['基礎架構圖']
 請輸入選擇： end
```

### Demo

這邊 gif 放上來都失敗，想看的可以移駕 [想了解更多詳細過程可以參考我的筆記](https://medium.com/@cbb104002/side-project-tomato-clock-xmind-d5c2ddf14e9b?source=friends_link&sk=107d0970b1a8f8748983d0cd50a2bbc1)
最下方有 
這邊 gif 放上來都失敗，想看的可以移駕 D

![xmind](https://imgur.com/ZMfGDNA.png)

## 執行環境

* Python 3.7.6
* macOS Mojave


