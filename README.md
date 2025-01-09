[![test](https://github.com/HayatoTotuka/my-package/actions/workflows/test.yml/badge.svg)](https://github.com/HayatoTotuka/my-package/actions/workflows/test.yml)
# ROS2　千葉の天気取得パッケージ
## パッケージ概要
OpenWeatherMapのAPIを使用して、２０秒ごとに千葉県の気温、湿度を取得しパブリッシュするパッケージ

# ノード
## weather_humidity_talkerノード
- OpenWeatherMapのAPIを取得し、今の千葉の気温、湿度をパブリッシュする

## topic
公開されるtopicは` chiba_weather `で、千葉の天気を表示します。

## 使用方法

```
ros2 run mypkg weather_humidity_talker
```
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
