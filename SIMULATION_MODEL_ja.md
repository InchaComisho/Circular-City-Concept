# 循環都市構想 — シミュレーションモデル説明書

## 目的

このシミュレーションは**概念比較ツール**である。
特定の都市に対する予測モデルではない。

このシミュレーションの目的は、透明で単純な計算式と正規化された値を使い、レトロフィット（改修）段階ごとに循環型インフラ介入が持続可能性と災害レジリエンスをどのように改善しうるかを可視化することである。

このシミュレーションが主張しないこと：
- 実際の都市において特定の数値改善が発生すること
- いずれかのレトロフィット段階を特定の期間内に完了できること
- 結果が実際の測定値により検証されていること

このシミュレーションが主張すること：
- 段階間の構造的な差異を比較することが、方向性の理解に有用であること
- 示された相対的な改善が、前提に照らして概念的に合理的であること

---

## 前提条件

1. すべての変数値は**0.0から1.0**に正規化されている。
2. Level 0は、循環型インフラがほぼ存在しない典型的な線形都市を表す。
3. 各レベルは、互いを補強する一貫したインフラセットを追加する。
4. レベルごとの変数値は**概念的な推定値**であり、特定の都市の測定データではない。
5. 計算式には単純な加重平均を使用する。重みは循環都市構想フレームワークに基づく相対的重要度を反映する。
6. 水自立日数には概念的な最大スケールとして**30日**を使用する。これは30日が達成可能または十分であることを意味しない。
7. ガバナンス品質と住民受容度は、他のすべての変数に間接的に影響するイネーブラー（実現促進要因）として扱う。
8. このモデルは、各レベルのインフラが完全に稼働し、適切に維持されていることを前提とする。

---

## 変数一覧

特に注記がない限り、すべての変数は0.0から1.0に正規化されている。

### 水の変数

| 変数 | 説明 |
|---|---|
| `rainwater_storage` | 雨水収集システムの容量と普及範囲 |
| `reclaimed_water_capacity` | 非飲用再利用向けの再生水（処理済み下水）の利用可能性 |
| `greywater_reuse` | 風呂・洗濯・洗面からのグレーウォーターの再利用率 |
| `potable_water_dependency` | 外部上水道への依存度（高いほど自律性が低い；ほとんどの指標で**反転**して使用） |

### エネルギーの変数

| 変数 | 説明 |
|---|---|
| `distributed_energy` | 分散型エネルギー発電の総合的な能力 |
| `battery_storage` | 地域の蓄電容量 |
| `solar_bipv` | 建材一体型太陽光発電（ペロブスカイト・従来型PV、屋根・外壁設置） |
| `vertical_axis_wind` | 都市型垂直軸風力タービンの貢献度 |
| `small_hydropower` | 水インフラの小型圧力回収水力発電 |

### 緑のインフラ変数

| 変数 | 説明 |
|---|---|
| `urban_greening` | 屋上緑化・壁面緑化・雨庭・都市の樹木被覆の範囲 |
| `mist_cooling` | 超音波ミスト冷却ネットワークの普及範囲 |
| `permeable_surface` | 透水性のある都市表面の割合（雨庭・透水性舗装） |

### 有機物・食料の変数

| 変数 | 説明 |
|---|---|
| `organic_matter_recycling` | 都市有機物のうち堆肥化または土壌循環へ戻される割合 |
| `local_food_capacity` | 都市内食料生産能力の程度（非常時食料レジリエンス） |

### ガバナンス・運用の変数

| 変数 | 説明 |
|---|---|
| `ai_sensor_control` | AIとセンサーによる都市循環管理の普及範囲 |
| `maintenance_capacity` | 分散型インフラの維持管理のための制度的・人的能力 |
| `governance_quality` | 循環型インフラを支えるガバナンス構造の質 |
| `public_acceptance` | 循環システムに対する住民の理解と受容度 |

---

## シナリオ定義

| レベル | 名称 | 説明 |
|---|---|---|
| Level 0 | 現在の線形都市 | 循環型インフラがない標準的な都市。資源が流入し、消費され、排出される。 |
| Level 1 | 住宅レベルの循環 | 個々の家庭が雨水タンク、小型太陽光パネル、家庭内堆肥化、基本的な断熱を導入する。 |
| Level 2 | 建物レベルの循環 | 建物が屋上貯留、グレーウォーターシステム、BIPV、屋上緑化、建物単位の蓄電池、排水熱回収を導入する。 |
| Level 3 | 街区レベルの循環インフラ | 街区が共用再生水配管、雨庭、透水性舗装、ミスト冷却ネットワーク、都市農園、街区蓄電池を設置する。 |
| Level 4 | 自治体レベルの循環インフラ | 自治体が下水処理水の高度利用、公共施設の発電面化、下水熱利用、非常用水ネットワーク、都市規模のAI管理を展開する。 |
| Level 5 | 循環都市OS | 都市全体が統合された循環代謝として機能する。水・エネルギー・熱・有機物・食料のすべての流れが、都市規模のAIとセンサーネットワークによって相互接続されたシステムとして管理される。 |

---

## 指標の計算式

### 持続可能性指数（Sustainability Index）

都市が線形消費ではなく資源を循環させる完全性を反映する。

```
水スコア   = (rainwater_storage + reclaimed_water_capacity
              + greywater_reuse + (1 - potable_water_dependency)) / 4

エネルギースコア = (distributed_energy + solar_bipv + battery_storage) / 3

緑スコア   = (urban_greening + permeable_surface) / 2

有機物スコア = (organic_matter_recycling + local_food_capacity) / 2

持続可能性指数 = 0.35 × 水スコア
               + 0.25 × エネルギースコア
               + 0.20 × 緑スコア
               + 0.20 × 有機物スコア
```

### 災害レジリエンス指数（Disaster Resilience Index）

災害発生中および発生後、都市機能がどの程度維持されるかを測定する。

```
水レジリエンス   = (rainwater_storage + reclaimed_water_capacity
                    + (1 - potable_water_dependency)) / 3

エネルギーレジリエンス = (battery_storage + distributed_energy) / 2

食料レジリエンス = local_food_capacity

ガバナンスレジリエンス = (maintenance_capacity + governance_quality
                          + ai_sensor_control) / 3

洪水レジリエンス = (permeable_surface + urban_greening) / 2

災害レジリエンス指数 = 0.25 × 水レジリエンス
                      + 0.25 × エネルギーレジリエンス
                      + 0.15 × 食料レジリエンス
                      + 0.20 × ガバナンスレジリエンス
                      + 0.15 × 洪水レジリエンス
```

### 水自立日数（Water Autonomy Days）

外部上水道なしで貯留水と再循環水のみで都市機能を維持できる日数の概念的推定値。最大スケール：30日（概念的のみ）。

```
自律スコア = rainwater_storage × 0.35
            + reclaimed_water_capacity × 0.30
            + greywater_reuse × 0.20
            + (1 - potable_water_dependency) × 0.15

水自立日数 = 30 × 自律スコア
```

### エネルギー自律スコア（Energy Autonomy Score）

分散型発電と地域蓄電の統合スコア。

```
エネルギー自律スコア = distributed_energy × 0.25
                      + battery_storage × 0.30
                      + solar_bipv × 0.25
                      + vertical_axis_wind × 0.10
                      + small_hydropower × 0.10
```

### 熱緩和スコア（Heat Mitigation Score）

都市熱を低減し、猛暑時に住民を守る能力。

```
熱緩和スコア = urban_greening × 0.35
              + mist_cooling × 0.35
              + permeable_surface × 0.20
              + (1 - potable_water_dependency) × 0.10
```

### 洪水緩和スコア（Flood Mitigation Score）

大雨・都市洪水を吸収・管理する能力。

```
洪水緩和スコア = permeable_surface × 0.40
               + urban_greening × 0.30
               + rainwater_storage × 0.20
               + ai_sensor_control × 0.10
```

### 循環スコア（Circularity Score）

都市システム内で資源がどれだけ完全に循環されているか。

```
循環スコア = (1 - potable_water_dependency) × 0.20
            + rainwater_storage × 0.15
            + reclaimed_water_capacity × 0.15
            + greywater_reuse × 0.15
            + organic_matter_recycling × 0.20
            + local_food_capacity × 0.15
```

### 復旧能力スコア（Recovery Capacity Score）

災害後の都市機能回復の速度と完全性。

```
復旧能力スコア = battery_storage × 0.15
               + distributed_energy × 0.15
               + rainwater_storage × 0.15
               + local_food_capacity × 0.10
               + maintenance_capacity × 0.15
               + governance_quality × 0.15
               + ai_sensor_control × 0.15
```

---

## 災害イベントの計算式

各災害イベントは、その災害シナリオにおいて維持される都市機能の割合（0.0〜1.0）を計算する。

### 停電（Power Outage）
```
= battery_storage × 0.40
+ distributed_energy × 0.40
+ ai_sensor_control × 0.20
```

### 断水（Water Outage）
```
= rainwater_storage × 0.35
+ reclaimed_water_capacity × 0.30
+ greywater_reuse × 0.20
+ (1 - potable_water_dependency) × 0.15
```

### 猛暑（Extreme Heat）
```
= mist_cooling × 0.35
+ urban_greening × 0.35
+ permeable_surface × 0.15
+ ai_sensor_control × 0.15
```

### 豪雨・都市洪水（Heavy Rainfall / Urban Flooding）
```
= permeable_surface × 0.40
+ urban_greening × 0.25
+ rainwater_storage × 0.20
+ ai_sensor_control × 0.15
```

### 物流停止（Logistics Disruption）
```
= local_food_capacity × 0.35
+ organic_matter_recycling × 0.20
+ rainwater_storage × 0.20
+ battery_storage × 0.15
+ distributed_energy × 0.10
```

---

## 実行方法

**必要条件：** Python 3.8以上、matplotlib、numpy

依存関係のインストール：
```bash
pip install -r requirements.txt
```

シミュレーションの実行：
```bash
python circular_city_resilience_simulation.py
```

スクリプトは以下を実行する：
1. 端末にサマリーテーブルを出力する
2. 同じディレクトリにPNGチャートファイルを保存する

---

## 出力チャートの説明

| ファイル名 | 内容 |
|---|---|
| `circular_city_sustainability_index.png` | 全レトロフィット段階の持続可能性指数 |
| `circular_city_disaster_resilience_index.png` | 全レトロフィット段階の災害レジリエンス指数 |
| `water_autonomy_days.png` | 各段階の概念的な水自立日数 |
| `energy_autonomy_score.png` | 各段階のエネルギー自律スコア |
| `heat_mitigation_score.png` | 各段階の熱緩和スコア |
| `retrofit_level_comparison.png` | 全段階・全指標の横断比較 |
| `disaster_scenario_comparison.png` | 各段階・各災害タイプで維持される都市機能 |

### 各チャートの読み方

- **棒の高さ**はその指標における相対的なパフォーマンスを表す。`potable_water_dependency`（外部上水依存度）は全計算式で反転されているため、高いほど良い。
- **色の変化**は赤（Level 0）から紫（Level 5）へと循環度の増加を示す。
- **1.0の破線**は理論上の最大値である。目標値や基準値ではない。
- **水自立日数**は30日を概念的な最大スケールとして使用する。日数の値は相対的な改善を示すものであり、絶対的な生存可能期間を示すものではない。
- **災害シナリオチャート**は各イベント発生中に維持される都市機能の割合を示す。復旧時間を示すものではない。

> 注記：Water Autonomy Days（水自立日数）は日数単位の指標である。  
> そのため、正規化された複合指標比較グラフには含めず、個別グラフとして表示している。

---

## 限界と留意点

このモデルには以下の限界がある。結論を導く前に認識しておく必要がある。

1. **キャリブレーションなし。** 変数値は実際の測定値から導かれたものではない。著者が割り当てた概念的な推定値である。
2. **場所依存性なし。** 気候帯、降雨パターン、人口密度、既存インフラは考慮されていない。
3. **線形集約。** 実際のインフラシステムには、このモデルが表現できない非線形な相互作用、フィードバックループ、連鎖的な障害が存在する。
4. **コストモデリングなし。** 経済的なコスト、投資要件、投資対効果は含まれていない。
5. **時間軸なし。** モデルは静的な状態を比較するものであり、移行のタイムラインをシミュレートするものではない。
6. **障害モデリングなし。** モデルはすべての設置済みシステムが完全に機能していることを前提とする。実際のシステムは故障し、維持管理を必要とし、劣化する。
7. **ガバナンスの一定性前提。** ガバナンス品質と住民受容度は動的にモデル化されておらず、静的な値として設定されている。

---

## なぜ「概念的」であり「予測的」ではないのか

このシミュレーションの目的は、改善の方向性についての**概念的な推論を支援する**ことであり、工学的・政策的分析に代わるものではない。

実際の都市インフラの意思決定には以下が必要である：
- 現地調査とデータ収集
- 工学的フィージビリティ調査
- 法規制の審査
- ステークホルダーとの協議
- パイロットプロジェクトとモニタリング

このモデルは**思考ツール**である。循環都市構想の構造的な論理を可視化し、各レトロフィット段階の相対的な利点を透明で再現可能な方法で比較するために設計されている。

このシミュレーションの数値を特定の都市やプロジェクトへの予測として引用してはならない。

---

## 生成されるグラフ

- `circular_city_sustainability_index.png`
- `circular_city_disaster_resilience_index.png`
- `water_autonomy_days.png`
- `energy_autonomy_score.png`
- `heat_mitigation_score.png`
- `retrofit_level_comparison.png`
- `disaster_scenario_comparison.png`

---

*ドキュメントバージョン：2026年6月*

---

## 著者

マスター / inchacomusho / InchaComisho

日本の独立構想者、観測者、提案者、AI調律者、人工叡智の定義者。  
自然補完科学の学問体系の構築・提唱者。  
クーリングクレジット・フレームワークの定義者、自然冷却価値評価プロトコルの創設者・原著作者。  
温暖化因果構造と完全解決策の定義者・体系化者。

マスターは、地球温暖化を単なるCO₂濃度の問題ではなく、森林喪失、土壌劣化、水循環断絶、水の相転移の弱体化、大気循環・海洋循環・食の循環／有機物循環の弱体化、蒸散・雲形成・降雨循環の弱体化、自然冷却フィードバックの停止として統合的に捉え、その解決策を排出削減、炭素固定源回復、物理的冷却、自然冷却機能の再起動、MRV、クーリングクレジット、文明OSへ接続する公開フレームワークとして提示している。

自然法則思想、地球循環再生、AIとの共創を中心に、NOTE・GitHub・各種公開媒体を通じて公開活動を行う。

## ライセンス

CC BY 4.0

本記事は、Creative Commons Attribution 4.0 International License（CC BY 4.0）で公開する。  
著者表示を行う限り、共有、転載、翻訳、改変、再利用を許可する。