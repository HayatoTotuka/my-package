[![test](https://github.com/HayatoTotuka/my-package/actions/workflows/test.yml/badge.svg)](https://github.com/HayatoTotuka/my-package/actions/workflows/test.yml)
# ROS2　千葉の天気取得パッケージ
このパッケージは、OpenWeatherMap API を利用して、20秒ごとに千葉県の気温と湿度を取得し、それをROS2のトピックとして公開する機能を提供します。

## パッケージ概要
- 千葉県の気温と湿度を定期的に取得し、ROS2トピックで配信します
- データ取得間隔：20秒

## ノード
 ` weather_humidity_talker `
  -  ` weather_humidity_talker ` ノードは、OpenWeatherMap APIを使用して千葉県の現在の気温と湿度を取得します。
  -  取得した情報をトピック ` chiba_weather ` にパブリッシュします
     

## トピック
` chiba_weather `
- 内容
  - 千葉県の気温と湿度を文字列形式で配信します。
  - 例: ` data: '気温: ~~.~~°C, 湿度: ~~%' `

## 使用方法
ノードの実行
```
ros2 run mypkg weather_humidity_talker
```
トピックの確認
```
ros2 topic echo chiba_weather
```


### 実行結果 
```
data: '気温: 7.04°C, 湿度: 41%'
---
data: '気温: 7.04°C, 湿度: 41%'
---
```


### テスト環境
- Ubuntu 22.04 LTS



## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Hayato Totuka
