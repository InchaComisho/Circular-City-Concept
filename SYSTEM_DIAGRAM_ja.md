# 循環都市構想 システム図
## 水・熱・エネルギー・有機物・食料・AI管理の循環フロー

---

## この文書の目的

この文書は、READMEで説明した循環都市構想を、水、熱、エネルギー、有機物、食料、AI管理の関係として図解する。図は実装済みシステムを示すものではなく、検証と段階導入のための構造整理である。

---

## 1. 全体循環フロー

```mermaid
flowchart TD
    Rain[雨水] --> Storage[雨水貯留]
    Storage --> Toilet[トイレ洗浄]
    Storage --> Green[緑化・散水]
    Storage --> Mist[超音波ミスト冷却]
    Wastewater[下水・排水] --> Treatment[下水処理・高度処理]
    Treatment --> Reclaimed[再生水]
    Reclaimed --> Cooling[冷却・清掃・修景用水]
    Organic[生ごみ・落ち葉・剪定枝] --> Compost[堆肥化・腐葉土化]
    Compost --> Soil[都市土壌再生]
    Soil --> Green
    Solar[ペロブスカイト太陽電池 / BIPV] --> Battery[分散蓄電]
    Wind[垂直軸風力] --> Battery
    Hydro[小型圧力水力] --> Battery
    Battery --> Sensors[AI・センサー管理]
    Sensors --> OS[循環都市OS]
    OS --> Storage
    OS --> Treatment
    OS --> Mist
    OS --> Green
```

---

## 2. 水循環図

```mermaid
flowchart TD
    Potable[上水] --> Drinking[飲用・調理・入浴]
    Rain[雨水] --> FirstFlush[初期雨水分離]
    FirstFlush --> RainTank[雨水タンク]
    RainTank --> NonPotable[非飲用用途]
    Grey[グレーウォーター] --> GreyTreatment[建物内処理]
    GreyTreatment --> NonPotable
    Wastewater[下水] --> WWTP[下水処理]
    WWTP --> Treated[下水処理水]
    Treated --> Advanced[高度処理]
    Advanced --> Reclaimed[再生水]
    Reclaimed --> NonPotable
    RainTank --> Emergency[非常用水]
    NonPotable --> Toilet[トイレ洗浄]
    NonPotable --> Irrigation[散水・緑化]
    NonPotable --> Cleaning[清掃]
    NonPotable --> Cooling[冷却]
```

---

## 3. エネルギー循環図

```mermaid
flowchart TD
    BIPV[BIPV・ペロブスカイト] --> DC[直流回路]
    Wind[垂直軸風力] --> DC
    Hydro[小型圧力水力] --> DC
    DC --> Battery[蓄電池]
    Battery --> Sensors[センサー]
    Battery --> Pumps[ポンプ]
    Battery --> Mist[ミスト冷却]
    Battery --> EmergencyPower[非常用電源]
    WasteHeat[排水熱・下水熱] --> HeatPump[ヒートポンプ]
    HeatPump --> BuildingUse[給湯・空調・温室]
    Sensors --> Control[発電・蓄電制御]
    Control --> Battery
```

---

## 4. 有機物・土壌循環図

```mermaid
flowchart TD
    FoodWaste[生ごみ] --> Separation[分別]
    Leaves[落ち葉] --> Separation
    Pruning[剪定枝] --> Separation
    Separation --> ContamCheck[異物・汚染確認]
    ContamCheck --> Compost[堆肥化]
    Compost --> Humus[腐植・腐葉土]
    Humus --> UrbanSoil[都市土壌]
    UrbanSoil --> Greening[緑化]
    UrbanSoil --> UrbanAgri[都市農業]
    UrbanAgri --> Food[食料・教育・防災]
    Greening --> Leaves
```

---

## 5. AI制御レイヤー図

```mermaid
flowchart TD
    Sensors[センサー群] --> Data[都市循環データ]
    Weather[気象予測] --> Data
    Tank[タンク水位] --> Data
    WaterQuality[水質] --> Data
    Generation[発電量] --> Data
    HeatRisk[暑熱リスク] --> Data
    Data --> AI[AI支援判断]
    AI --> Maintenance[保守予測]
    AI --> Normal[平常運用]
    AI --> Emergency[災害時モード]
    Normal --> PumpControl[ポンプ制御]
    Normal --> MistControl[ミスト制御]
    Normal --> Irrigation[散水制御]
    Emergency --> Priority[水・電力の優先配分]
```

---

## ノードの説明

| ノード | 役割 |
| --- | --- |
| 雨水貯留 | 屋根・外壁の雨水を非飲用用途に使う入口 |
| 下水処理・高度処理 | 公衆衛生を守りながら再生水・熱・資源回収へ接続する拠点 |
| 分散蓄電 | 太陽光、風力、小型水力の変動を吸収する |
| 都市土壌再生 | 有機物循環と緑化・都市農業をつなぐ |
| AI・センサー管理 | 監視、異常検知、保守予測、災害時切替を支援する |

---

## 故障点と安全制御点

| 領域 | 故障点 | 安全制御点 |
| --- | --- | --- |
| 水 | 誤接続、滞留、細菌増殖、フィルター詰まり | 表示、逆流防止、水質監視、定期洗浄 |
| ミスト | レジオネラ、ノズル汚染、滑り | 殺菌、停止条件、清掃記録 |
| エネルギー | 蓄電池劣化、過熱、発電不安定 | 認証機器、温度監視、遮断装置 |
| 有機物 | 悪臭、害虫、重金属、マイクロプラスチック | 分別、検査、完熟確認、搬入制限 |
| AI | センサー故障、誤判断、ブラックボックス化 | 人間の最終判断、ログ、手動切替 |

---

## READMEとの関係

READMEは循環都市構想の本文、技術要素、ロードマップを説明する。本書はその構想を図として再配置し、各要素がどの循環に属し、どこで検証・保守・安全制御が必要になるかを示す補足資料である。
