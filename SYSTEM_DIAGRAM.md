# Circular City Concept System Diagram
## Circulation Flows of Water, Heat, Energy, Organic Matter, Food, and AI Management

---

## Purpose of This Document

This document visualizes the Circular City Concept described in the README as relationships among water, heat, energy, organic matter, food, and AI management. The diagrams do not represent an already implemented system; they organize structure for validation and phased deployment.

---

## 1. Overall Circular City Flow

```mermaid
flowchart TD
    Rain[Rainwater] --> Storage[Rainwater Storage]
    Storage --> Toilet[Toilet Flushing]
    Storage --> Green[Greening and Irrigation]
    Storage --> Mist[Ultrasonic Mist Cooling]
    Wastewater[Wastewater and Drainage] --> Treatment[Wastewater and Advanced Treatment]
    Treatment --> Reclaimed[Reclaimed Water]
    Reclaimed --> Cooling[Cooling, Cleaning, and Landscape Water]
    Organic[Food Waste, Fallen Leaves, and Pruning Residues] --> Compost[Composting and Leaf Mold]
    Compost --> Soil[Urban Soil Regeneration]
    Soil --> Green
    Solar[Perovskite Solar Cells / BIPV] --> Battery[Distributed Batteries]
    Wind[Vertical-Axis Wind] --> Battery
    Hydro[Small Pressure Hydropower] --> Battery
    Battery --> Sensors[AI and Sensor Management]
    Sensors --> OS[Circular City OS]
    OS --> Storage
    OS --> Treatment
    OS --> Mist
    OS --> Green
```

---

## 2. Water Circulation Diagram

```mermaid
flowchart TD
    Potable[Potable Water] --> Drinking[Drinking, Cooking, and Bathing]
    Rain[Rainwater] --> FirstFlush[First-Flush Separation]
    FirstFlush --> RainTank[Rainwater Tank]
    RainTank --> NonPotable[Non-Potable Uses]
    Grey[Greywater] --> GreyTreatment[Building-Level Treatment]
    GreyTreatment --> NonPotable
    Wastewater[Wastewater] --> WWTP[Wastewater Treatment]
    WWTP --> Treated[Treated Wastewater]
    Treated --> Advanced[Advanced Treatment]
    Advanced --> Reclaimed[Reclaimed Water]
    Reclaimed --> NonPotable
    RainTank --> Emergency[Emergency Water]
    NonPotable --> Toilet[Toilet Flushing]
    NonPotable --> Irrigation[Irrigation and Greening]
    NonPotable --> Cleaning[Cleaning]
    NonPotable --> Cooling[Cooling]
```

---

## 3. Energy Circulation Diagram

```mermaid
flowchart TD
    BIPV[BIPV and Perovskite Solar] --> DC[DC Circuit]
    Wind[Vertical-Axis Wind] --> DC
    Hydro[Small Pressure Hydropower] --> DC
    DC --> Battery[Batteries]
    Battery --> Sensors[Sensors]
    Battery --> Pumps[Pumps]
    Battery --> Mist[Mist Cooling]
    Battery --> EmergencyPower[Emergency Power]
    WasteHeat[Drainage and Wastewater Heat] --> HeatPump[Heat Pump]
    HeatPump --> BuildingUse[Hot Water, HVAC, and Greenhouses]
    Sensors --> Control[Generation and Storage Control]
    Control --> Battery
```

---

## 4. Organic Matter and Soil Diagram

```mermaid
flowchart TD
    FoodWaste[Food Waste] --> Separation[Separation]
    Leaves[Fallen Leaves] --> Separation
    Pruning[Pruning Residues] --> Separation
    Separation --> ContamCheck[Foreign-Matter and Contamination Check]
    ContamCheck --> Compost[Composting]
    Compost --> Humus[Humus and Leaf Mold]
    Humus --> UrbanSoil[Urban Soil]
    UrbanSoil --> Greening[Greening]
    UrbanSoil --> UrbanAgri[Urban Agriculture]
    UrbanAgri --> Food[Food, Education, and Disaster Resilience]
    Greening --> Leaves
```

---

## 5. AI Control Layer Diagram

```mermaid
flowchart TD
    Sensors[Sensor Network] --> Data[Urban Circulation Data]
    Weather[Weather Forecast] --> Data
    Tank[Tank Water Level] --> Data
    WaterQuality[Water Quality] --> Data
    Generation[Power Generation] --> Data
    HeatRisk[Heat Risk] --> Data
    Data --> AI[AI-Assisted Judgment]
    AI --> Maintenance[Maintenance Prediction]
    AI --> Normal[Normal Operation]
    AI --> Emergency[Emergency Mode]
    Normal --> PumpControl[Pump Control]
    Normal --> MistControl[Mist Control]
    Normal --> Irrigation[Irrigation Control]
    Emergency --> Priority[Water and Power Prioritization]
```

---

## Node Explanations

| Node | Role |
| --- | --- |
| Rainwater storage | Entry point for using roof and wall runoff for non-potable purposes |
| Wastewater and advanced treatment | Hub for protecting public health while connecting to reclaimed water, heat, and resource recovery |
| Distributed batteries | Buffer variable solar, wind, and small hydropower generation |
| Urban soil regeneration | Connect organic-matter circulation with greening and urban agriculture |
| AI and sensor management | Support monitoring, anomaly detection, maintenance prediction, and emergency switching |

---

## Failure Points and Safety Control Points

| Area | Failure Point | Safety Control Point |
| --- | --- | --- |
| Water | Cross-connection, stagnation, bacterial growth, filter clogging | Labels, backflow prevention, water-quality monitoring, regular cleaning |
| Mist | Legionella, nozzle contamination, slippery surfaces | Disinfection, shutdown conditions, cleaning records |
| Energy | Battery degradation, overheating, unstable generation | Certified devices, temperature monitoring, disconnect devices |
| Organic matter | Odor, pests, heavy metals, microplastics | Separation, testing, maturity confirmation, input restrictions |
| AI | Sensor failure, misjudgment, black-box control | Human final authority, logs, manual fallback |

---

## Relationship to the README

The README explains the main thesis, technical elements, and roadmap of the Circular City Concept. This document reorganizes that concept as diagrams and shows which circulation each element belongs to and where validation, maintenance, and safety controls are required.

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
