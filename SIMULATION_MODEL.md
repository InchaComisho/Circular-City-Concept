# Circular City Concept — Simulation Model Documentation

## Purpose

This simulation is a **conceptual comparison tool**.
It is not a prediction model for any real city.

Its purpose is to illustrate how circular infrastructure interventions at different retrofit levels may improve sustainability and disaster resilience, using transparent, simple equations and normalized values.

The simulation does not claim:
- That specific numeric improvements will occur in real cities
- That any retrofit level can be completed in a given timeframe
- That results are validated against real-world measurements

It claims only:
- That comparing structural differences across levels is useful for understanding direction
- That the relative improvements shown are conceptually reasonable given the underlying assumptions

---

## Assumptions

1. All variable values are normalized between **0.0 and 1.0**.
2. Level 0 represents a typical linear city with minimal circular infrastructure.
3. Each level adds coherent sets of infrastructure that reinforce each other.
4. Variables per level are **conceptual estimates**, not measured data from any specific city.
5. Equations use simple weighted averages. Weights reflect relative importance based on the Circular City Concept framework.
6. Water Autonomy Days uses a conceptual maximum scale of **30 days**. This does not imply that 30 days is achievable or sufficient.
7. Governance quality and public acceptance are treated as enablers that affect all other variables indirectly; they are included in recovery capacity.
8. This model assumes that each level's infrastructure is fully operational and properly maintained.

---

## Variables

All variables are normalized from 0.0 to 1.0 unless noted otherwise.

### Water Variables

| Variable | Description |
|---|---|
| `rainwater_storage` | Capacity and coverage of rainwater harvesting systems |
| `reclaimed_water_capacity` | Availability of reclaimed / treated wastewater for non-potable reuse |
| `greywater_reuse` | Proportion of greywater from baths, laundry, and basins being reused |
| `potable_water_dependency` | Dependence on external mains supply (higher = less autonomous; **inverted** in most indexes) |

### Energy Variables

| Variable | Description |
|---|---|
| `distributed_energy` | Overall distributed energy generation capacity |
| `battery_storage` | Local battery storage capacity |
| `solar_bipv` | Building-integrated solar (perovskite / conventional PV on roofs and walls) |
| `vertical_axis_wind` | Urban vertical-axis wind turbine contribution |
| `small_hydropower` | Small pressure-recovery hydropower from water infrastructure |

### Green Infrastructure Variables

| Variable | Description |
|---|---|
| `urban_greening` | Extent of rooftop greening, green walls, rain gardens, and urban canopy |
| `mist_cooling` | Coverage of ultrasonic mist cooling networks |
| `permeable_surface` | Proportion of urban surface that is permeable (rain gardens, permeable pavement) |

### Organic Matter and Food Variables

| Variable | Description |
|---|---|
| `organic_matter_recycling` | Proportion of urban organic matter composted or returned to the soil cycle |
| `local_food_capacity` | Degree of urban food production capacity (emergency food resilience) |

### Governance and Operations Variables

| Variable | Description |
|---|---|
| `ai_sensor_control` | Coverage of AI and sensor-based urban circulation management |
| `maintenance_capacity` | Institutional and human capacity for maintaining distributed infrastructure |
| `governance_quality` | Quality of governance structures supporting circular infrastructure |
| `public_acceptance` | Degree of public understanding and acceptance of circular systems |

---

## Scenario Definitions

| Level | Name | Description |
|---|---|---|
| Level 0 | Current Linear City | Standard city with no circular infrastructure. Resources enter, are consumed, and are discharged. |
| Level 1 | Household-Level Circularity | Individual households install rainwater tanks, small solar panels, home composting, and basic insulation. |
| Level 2 | Building-Level Circulation | Buildings adopt rooftop storage, greywater systems, BIPV, green roofs, building-scale batteries, and drainage heat recovery. |
| Level 3 | District-Level Circular Infrastructure | Districts install shared reclaimed water pipes, rain gardens, permeable surfaces, mist cooling networks, urban farms, and district batteries. |
| Level 4 | Municipal Circular Infrastructure | Municipality deploys advanced wastewater reuse, public facility solar conversion, wastewater heat recovery, emergency water networks, and city-wide AI management. |
| Level 5 | Circular City OS | The entire city functions as an integrated circular metabolism. All flows — water, energy, heat, organic matter, food — are managed as interconnected systems by a city-scale AI and sensor network. |

---

## Index Equations

### Sustainability Index

Reflects how completely the city circulates resources rather than consuming linearly.

```
water_score  = (rainwater_storage + reclaimed_water_capacity
                + greywater_reuse + (1 - potable_water_dependency)) / 4

energy_score = (distributed_energy + solar_bipv + battery_storage) / 3

green_score  = (urban_greening + permeable_surface) / 2

organic_score = (organic_matter_recycling + local_food_capacity) / 2

Sustainability Index = 0.35 × water_score
                     + 0.25 × energy_score
                     + 0.20 × green_score
                     + 0.20 × organic_score
```

### Disaster Resilience Index

Measures how functional the city remains during and after disaster events.

```
water_res  = (rainwater_storage + reclaimed_water_capacity
              + (1 - potable_water_dependency)) / 3

energy_res = (battery_storage + distributed_energy) / 2

food_res   = local_food_capacity

gov_res    = (maintenance_capacity + governance_quality
              + ai_sensor_control) / 3

flood_res  = (permeable_surface + urban_greening) / 2

Disaster Resilience Index = 0.25 × water_res
                           + 0.25 × energy_res
                           + 0.15 × food_res
                           + 0.20 × gov_res
                           + 0.15 × flood_res
```

### Water Autonomy Days

Conceptual estimate of how many days urban functions could be maintained using stored and recirculated water without external mains supply. Maximum scale: 30 days (conceptual only).

```
autonomy_score = rainwater_storage × 0.35
               + reclaimed_water_capacity × 0.30
               + greywater_reuse × 0.20
               + (1 - potable_water_dependency) × 0.15

Water Autonomy Days = 30 × autonomy_score
```

### Energy Autonomy Score

Combined distributed generation and local storage score.

```
Energy Autonomy Score = distributed_energy × 0.25
                       + battery_storage × 0.30
                       + solar_bipv × 0.25
                       + vertical_axis_wind × 0.10
                       + small_hydropower × 0.10
```

### Heat Mitigation Score

Capacity to reduce urban heat and protect residents during extreme heat events.

```
Heat Mitigation Score = urban_greening × 0.35
                       + mist_cooling × 0.35
                       + permeable_surface × 0.20
                       + (1 - potable_water_dependency) × 0.10
```

### Flood Mitigation Score

Ability to absorb and manage heavy rainfall and urban flooding.

```
Flood Mitigation Score = permeable_surface × 0.40
                        + urban_greening × 0.30
                        + rainwater_storage × 0.20
                        + ai_sensor_control × 0.10
```

### Circularity Score

How completely resources are cycled within the urban system.

```
Circularity Score = (1 - potable_water_dependency) × 0.20
                   + rainwater_storage × 0.15
                   + reclaimed_water_capacity × 0.15
                   + greywater_reuse × 0.15
                   + organic_matter_recycling × 0.20
                   + local_food_capacity × 0.15
```

### Recovery Capacity Score

Speed and completeness of recovery after disaster events.

```
Recovery Capacity Score = battery_storage × 0.15
                         + distributed_energy × 0.15
                         + rainwater_storage × 0.15
                         + local_food_capacity × 0.10
                         + maintenance_capacity × 0.15
                         + governance_quality × 0.15
                         + ai_sensor_control × 0.15
```

---

## Disaster Event Equations

Each disaster event calculates the proportion of urban function maintained (0.0–1.0).

### Power Outage
```
= battery_storage × 0.40
+ distributed_energy × 0.40
+ ai_sensor_control × 0.20
```

### Water Outage
```
= rainwater_storage × 0.35
+ reclaimed_water_capacity × 0.30
+ greywater_reuse × 0.20
+ (1 - potable_water_dependency) × 0.15
```

### Extreme Heat
```
= mist_cooling × 0.35
+ urban_greening × 0.35
+ permeable_surface × 0.15
+ ai_sensor_control × 0.15
```

### Heavy Rainfall / Urban Flooding
```
= permeable_surface × 0.40
+ urban_greening × 0.25
+ rainwater_storage × 0.20
+ ai_sensor_control × 0.15
```

### Logistics Disruption
```
= local_food_capacity × 0.35
+ organic_matter_recycling × 0.20
+ rainwater_storage × 0.20
+ battery_storage × 0.15
+ distributed_energy × 0.10
```

---

## How to Run

**Requirements:** Python 3.8+, matplotlib, numpy

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the simulation:
```bash
python circular_city_resilience_simulation.py
```

The script will:
1. Print a summary table to the terminal
2. Save 7 PNG chart files in the same directory

---

## Output Charts

| File | Description |
|---|---|
| `circular_city_sustainability_index.png` | Sustainability Index across all retrofit levels |
| `circular_city_disaster_resilience_index.png` | Disaster Resilience Index across all retrofit levels |
| `water_autonomy_days.png` | Conceptual water autonomy (days) across levels |
| `energy_autonomy_score.png` | Energy autonomy score across levels |
| `heat_mitigation_score.png` | Heat mitigation score across levels |
| `retrofit_level_comparison.png` | All indexes side by side for all levels |
| `disaster_scenario_comparison.png` | Function maintained per disaster type per level |

### How to Interpret the Charts

- **Bar height** represents relative performance on that index. Higher is better for all indexes except `potable_water_dependency`, which is inverted in all formulas.
- **Color progression** from red (Level 0) to purple (Level 5) indicates increasing circularity.
- **The dashed line at 1.0** is a theoretical maximum. It is not a target or a standard.
- **Water Autonomy Days** uses a 30-day conceptual scale. Day values indicate relative improvement, not absolute survival capacity.
- **Disaster scenario charts** show how much urban function is maintained during each event, not recovery time.

> Note: Water Autonomy Days is a day-based indicator.  
> Therefore, it is shown as a separate chart and is not included in the normalized multi-index comparison chart.

---

## Limitations

This model has the following limitations. Users should be aware of these before drawing any conclusions.

1. **Not calibrated.** Variable values are not derived from real measurements. They are author-assigned conceptual estimates.
2. **Not location-specific.** The model does not account for climate zone, rainfall patterns, population density, or existing infrastructure.
3. **Linear aggregation.** Real infrastructure systems have non-linear interactions, feedback loops, and failure cascades that this model does not represent.
4. **No cost modeling.** The model does not include economic costs, investment requirements, or return on investment.
5. **No time dimension.** The model compares static states; it does not simulate transition timelines.
6. **No failure modeling.** The model assumes all installed systems are fully functional. Real systems fail, require maintenance, and degrade.
7. **Governance assumed consistent.** Governance quality and public acceptance are not modeled dynamically; they are set as static values.

---

## Why Conceptual, Not Predictive

The purpose of this simulation is to support **conceptual reasoning** about the direction of improvement, not to substitute for engineering or policy analysis.

Real urban infrastructure decisions require:
- Site-specific surveys and data collection
- Engineering feasibility studies
- Regulatory review
- Stakeholder engagement
- Pilot projects and monitoring

This model is a thinking tool. It helps visualize the structural logic of the Circular City Concept and compare the relative benefits of different retrofit levels in a transparent, reproducible way.

Numbers from this simulation should never be cited as predictions for specific cities or projects.

---

## Generated Charts

- `circular_city_sustainability_index.png`
- `circular_city_disaster_resilience_index.png`
- `water_autonomy_days.png`
- `energy_autonomy_score.png`
- `heat_mitigation_score.png`
- `retrofit_level_comparison.png`
- `disaster_scenario_comparison.png`

---

*Documentation version: June 2026*

---

## Author

Master / inchacomusho / InchaComisho

An independent Japanese concept designer, observer, proposer, AI tuner, and definer of Artificial Wisdom.  
Founder and advocate of the academic framework of Natural Complementary Science.  
Publicly active in natural-law philosophy, planetary circulation restoration, and co-creation with AI.

---

## License

CC BY 4.0

This article is released under the Creative Commons Attribution 4.0 International License (CC BY 4.0).  
Sharing, redistribution, translation, adaptation, and reuse are permitted as long as proper attribution is given.
