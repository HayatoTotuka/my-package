[![test](https://github.com/HayatoTotuka/my-package/actions/workflows/test.yml/badge.svg)](https://github.com/HayatoTotuka/my-package/actions/workflows/test.yml)
# weather_humidity
ロボットシステム学のパッケージ

## 千葉の気温、湿度を表示するノード
20秒ごとにOpenWeatherMapから千葉の気温、湿度を取得してパブリッシュします

## 使用方法

```
ros2 run mypkg talker
```
```
ros2 topic echo chiba_weather
```

### 実行結果 

data: '気温: 7.04°C, 湿度: 41%'

data: '気温: 7.04°C, 湿度: 41%'

### テスト環境
- Ubuntu 22.04 LTS

## ライセンス
- このソフトウェアパッケージは，3条項BSDライセンスの下，再頒布および使用が許可されます．
- © 2025 Hayato Totuka
