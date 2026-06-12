"""
Circular City Concept — Conceptual Resilience Simulation
=========================================================

PURPOSE
-------
This simulation is a conceptual model only.
It does NOT predict real-world outcomes for any specific city.
It compares how circular infrastructure interventions may improve
sustainability and disaster resilience across six retrofit levels.

All values are normalized between 0.0 (none) and 1.0 (maximum conceptual).
All equations are intentionally simple and transparent.

RETROFIT LEVELS
---------------
Level 0 : Current Linear City
Level 1 : Household-Level Circularity
Level 2 : Building-Level Circulation
Level 3 : District-Level Circular Infrastructure
Level 4 : Municipal Circular Infrastructure
Level 5 : Circular City OS

ASSUMPTION
----------
Variable values per level are conceptual estimates, not measured data.
They represent relative improvement across levels for comparison purposes.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# ---------------------------------------------------------------------------
# SECTION 1: RETROFIT LEVEL DEFINITIONS
# ---------------------------------------------------------------------------
# Each level is defined by a dictionary of normalized variables (0.0–1.0).
# Higher values are generally better, except potable_water_dependency
# (which represents dependence on external supply — lower is more autonomous).

LEVELS = {
    "L0\nLinear City": {
        # Water variables
        "rainwater_storage":         0.00,  # No rainwater collection
        "reclaimed_water_capacity":  0.00,  # No reclaimed water system
        "greywater_reuse":           0.00,  # No greywater reuse
        "potable_water_dependency":  1.00,  # Fully dependent on mains water

        # Energy variables
        "distributed_energy":        0.05,  # Near-zero local generation
        "battery_storage":           0.00,  # No local battery storage
        "solar_bipv":                0.05,  # Minimal conventional solar
        "vertical_axis_wind":        0.00,  # No urban wind turbines
        "small_hydropower":          0.00,  # No pressure-recovery hydro

        # Green infrastructure
        "urban_greening":            0.05,  # Minimal green surface
        "mist_cooling":              0.00,  # No mist cooling
        "permeable_surface":         0.05,  # Almost entirely impermeable

        # Organic matter and food
        "organic_matter_recycling":  0.05,  # Almost all organic waste incinerated
        "local_food_capacity":       0.02,  # No meaningful local food production

        # Governance and operation
        "ai_sensor_control":         0.00,  # No sensor-based management
        "maintenance_capacity":      0.30,  # Minimal system maintenance
        "governance_quality":        0.30,  # Conventional city governance
        "public_acceptance":         0.30,  # Low awareness of circular concepts
    },

    "L1\nHousehold": {
        # Individual households adopt rainwater tanks, small solar, composting
        "rainwater_storage":         0.20,
        "reclaimed_water_capacity":  0.10,
        "greywater_reuse":           0.10,
        "potable_water_dependency":  0.80,

        "distributed_energy":        0.15,
        "battery_storage":           0.10,
        "solar_bipv":                0.15,
        "vertical_axis_wind":        0.00,
        "small_hydropower":          0.00,

        "urban_greening":            0.15,
        "mist_cooling":              0.05,
        "permeable_surface":         0.10,

        "organic_matter_recycling":  0.20,
        "local_food_capacity":       0.10,

        "ai_sensor_control":         0.05,
        "maintenance_capacity":      0.35,
        "governance_quality":        0.35,
        "public_acceptance":         0.40,
    },

    "L2\nBuilding": {
        # Buildings install rooftop storage, greywater systems, BIPV, green walls
        "rainwater_storage":         0.35,
        "reclaimed_water_capacity":  0.25,
        "greywater_reuse":           0.30,
        "potable_water_dependency":  0.65,

        "distributed_energy":        0.30,
        "battery_storage":           0.25,
        "solar_bipv":                0.30,
        "vertical_axis_wind":        0.05,
        "small_hydropower":          0.05,

        "urban_greening":            0.30,
        "mist_cooling":              0.15,
        "permeable_surface":         0.20,

        "organic_matter_recycling":  0.35,
        "local_food_capacity":       0.20,

        "ai_sensor_control":         0.20,
        "maintenance_capacity":      0.45,
        "governance_quality":        0.45,
        "public_acceptance":         0.50,
    },

    "L3\nDistrict": {
        # District-scale reclaimed water pipes, rain gardens, mist networks, urban farms
        "rainwater_storage":         0.55,
        "reclaimed_water_capacity":  0.50,
        "greywater_reuse":           0.50,
        "potable_water_dependency":  0.45,

        "distributed_energy":        0.50,
        "battery_storage":           0.45,
        "solar_bipv":                0.50,
        "vertical_axis_wind":        0.20,
        "small_hydropower":          0.15,

        "urban_greening":            0.50,
        "mist_cooling":              0.35,
        "permeable_surface":         0.40,

        "organic_matter_recycling":  0.55,
        "local_food_capacity":       0.35,

        "ai_sensor_control":         0.45,
        "maintenance_capacity":      0.60,
        "governance_quality":        0.60,
        "public_acceptance":         0.65,
    },

    "L4\nMunicipal": {
        # Municipal-scale advanced wastewater reuse, heat recovery, public facility generation
        "rainwater_storage":         0.75,
        "reclaimed_water_capacity":  0.70,
        "greywater_reuse":           0.70,
        "potable_water_dependency":  0.25,

        "distributed_energy":        0.70,
        "battery_storage":           0.65,
        "solar_bipv":                0.70,
        "vertical_axis_wind":        0.40,
        "small_hydropower":          0.30,

        "urban_greening":            0.70,
        "mist_cooling":              0.60,
        "permeable_surface":         0.65,

        "organic_matter_recycling":  0.75,
        "local_food_capacity":       0.55,

        "ai_sensor_control":         0.70,
        "maintenance_capacity":      0.75,
        "governance_quality":        0.75,
        "public_acceptance":         0.75,
    },

    "L5\nCircular OS": {
        # Full Circular City OS: all flows managed as integrated urban metabolism
        "rainwater_storage":         0.90,
        "reclaimed_water_capacity":  0.90,
        "greywater_reuse":           0.90,
        "potable_water_dependency":  0.10,

        "distributed_energy":        0.90,
        "battery_storage":           0.85,
        "solar_bipv":                0.90,
        "vertical_axis_wind":        0.60,
        "small_hydropower":          0.50,

        "urban_greening":            0.90,
        "mist_cooling":              0.85,
        "permeable_surface":         0.85,

        "organic_matter_recycling":  0.90,
        "local_food_capacity":       0.75,

        "ai_sensor_control":         0.90,
        "maintenance_capacity":      0.90,
        "governance_quality":        0.90,
        "public_acceptance":         0.90,
    },
}

LEVEL_LABELS = list(LEVELS.keys())
LEVEL_DATA   = list(LEVELS.values())

# ---------------------------------------------------------------------------
# SECTION 2: INDEX CALCULATION FUNCTIONS
# ---------------------------------------------------------------------------
# Each function takes a variable dictionary and returns a normalized score.
# Equations are weighted averages designed for conceptual comparison.

def sustainability_index(v):
    """
    Reflects how well the city circulates resources rather than consuming linearly.
    Combines water reuse, energy independence, greening, and organic matter recovery.
    """
    water_score  = (v["rainwater_storage"] + v["reclaimed_water_capacity"]
                    + v["greywater_reuse"] + (1.0 - v["potable_water_dependency"])) / 4.0
    energy_score = (v["distributed_energy"] + v["solar_bipv"]
                    + v["battery_storage"]) / 3.0
    green_score  = (v["urban_greening"] + v["permeable_surface"]) / 2.0
    organic_score= (v["organic_matter_recycling"] + v["local_food_capacity"]) / 2.0
    return 0.35 * water_score + 0.25 * energy_score + 0.20 * green_score + 0.20 * organic_score


def disaster_resilience_index(v):
    """
    Measures how functional the city remains during and after disaster events.
    Weighted toward autonomous water, energy, and governance capacity.
    """
    water_res  = (v["rainwater_storage"] + v["reclaimed_water_capacity"]
                  + (1.0 - v["potable_water_dependency"])) / 3.0
    energy_res = (v["battery_storage"] + v["distributed_energy"]) / 2.0
    food_res   = v["local_food_capacity"]
    gov_res    = (v["maintenance_capacity"] + v["governance_quality"]
                  + v["ai_sensor_control"]) / 3.0
    flood_res  = (v["permeable_surface"] + v["urban_greening"]) / 2.0
    return (0.25 * water_res + 0.25 * energy_res + 0.15 * food_res
            + 0.20 * gov_res + 0.15 * flood_res)


def water_autonomy_days(v):
    """
    Conceptual estimate: how many days the city could function on stored/
    recirculated water without external mains supply.
    Scale: 0–30 days (conceptual maximum).
    """
    autonomy_score = (v["rainwater_storage"] * 0.35
                      + v["reclaimed_water_capacity"] * 0.30
                      + v["greywater_reuse"] * 0.20
                      + (1.0 - v["potable_water_dependency"]) * 0.15)
    return round(30.0 * autonomy_score, 1)


def energy_autonomy_score(v):
    """
    Combined score for distributed energy generation and local storage.
    Reflects ability to maintain power independently of the grid.
    """
    return (v["distributed_energy"] * 0.25 + v["battery_storage"] * 0.30
            + v["solar_bipv"] * 0.25 + v["vertical_axis_wind"] * 0.10
            + v["small_hydropower"] * 0.10)


def heat_mitigation_score(v):
    """
    Reflects the city's capacity to reduce urban heat island and
    protect residents during extreme heat events.
    """
    return (v["urban_greening"] * 0.35 + v["mist_cooling"] * 0.35
            + v["permeable_surface"] * 0.20
            + (1.0 - v["potable_water_dependency"]) * 0.10)


def flood_mitigation_score(v):
    """
    Reflects the city's ability to absorb, slow, and manage heavy rainfall
    and urban flooding events.
    """
    return (v["permeable_surface"] * 0.40 + v["urban_greening"] * 0.30
            + v["rainwater_storage"] * 0.20 + v["ai_sensor_control"] * 0.10)


def circularity_score(v):
    """
    How completely resources (water, organic matter, food) are cycled
    within the urban system rather than imported and discarded.
    """
    return ((1.0 - v["potable_water_dependency"]) * 0.20
            + v["rainwater_storage"] * 0.15
            + v["reclaimed_water_capacity"] * 0.15
            + v["greywater_reuse"] * 0.15
            + v["organic_matter_recycling"] * 0.20
            + v["local_food_capacity"] * 0.15)


def recovery_capacity_score(v):
    """
    Speed and completeness of urban function recovery after a disaster.
    Depends on redundant energy, water buffers, governance, and AI management.
    """
    return (v["battery_storage"] * 0.15 + v["distributed_energy"] * 0.15
            + v["rainwater_storage"] * 0.15 + v["local_food_capacity"] * 0.10
            + v["maintenance_capacity"] * 0.15 + v["governance_quality"] * 0.15
            + v["ai_sensor_control"] * 0.15)


# ---------------------------------------------------------------------------
# SECTION 3: DISASTER EVENT MODELING
# ---------------------------------------------------------------------------
# Each event returns a "function maintained" score (0.0–1.0) showing how
# much of normal city function is retained during that disaster scenario.

DISASTER_EVENTS = {
    "Power\nOutage": lambda v: (
        v["battery_storage"] * 0.40
        + v["distributed_energy"] * 0.40
        + v["ai_sensor_control"] * 0.20
    ),
    "Water\nOutage": lambda v: (
        v["rainwater_storage"] * 0.35
        + v["reclaimed_water_capacity"] * 0.30
        + v["greywater_reuse"] * 0.20
        + (1.0 - v["potable_water_dependency"]) * 0.15
    ),
    "Extreme\nHeat": lambda v: (
        v["mist_cooling"] * 0.35
        + v["urban_greening"] * 0.35
        + v["permeable_surface"] * 0.15
        + v["ai_sensor_control"] * 0.15
    ),
    "Heavy Rain\n/ Flooding": lambda v: (
        v["permeable_surface"] * 0.40
        + v["urban_greening"] * 0.25
        + v["rainwater_storage"] * 0.20
        + v["ai_sensor_control"] * 0.15
    ),
    "Logistics\nDisruption": lambda v: (
        v["local_food_capacity"] * 0.35
        + v["organic_matter_recycling"] * 0.20
        + v["rainwater_storage"] * 0.20
        + v["battery_storage"] * 0.15
        + v["distributed_energy"] * 0.10
    ),
}

# ---------------------------------------------------------------------------
# SECTION 4: COMPUTE ALL INDEXES
# ---------------------------------------------------------------------------

def compute_indexes(levels_data):
    results = {
        "sustainability_index": [],
        "disaster_resilience_index": [],
        "water_autonomy_days": [],
        "energy_autonomy_score": [],
        "heat_mitigation_score": [],
        "flood_mitigation_score": [],
        "circularity_score": [],
        "recovery_capacity_score": [],
    }
    for v in levels_data:
        results["sustainability_index"].append(sustainability_index(v))
        results["disaster_resilience_index"].append(disaster_resilience_index(v))
        results["water_autonomy_days"].append(water_autonomy_days(v))
        results["energy_autonomy_score"].append(energy_autonomy_score(v))
        results["heat_mitigation_score"].append(heat_mitigation_score(v))
        results["flood_mitigation_score"].append(flood_mitigation_score(v))
        results["circularity_score"].append(circularity_score(v))
        results["recovery_capacity_score"].append(recovery_capacity_score(v))
    return results


def compute_disaster_scores(levels_data):
    scores = {event: [] for event in DISASTER_EVENTS}
    for v in levels_data:
        for event, fn in DISASTER_EVENTS.items():
            scores[event].append(fn(v))
    return scores


INDEXES = compute_indexes(LEVEL_DATA)
DISASTER_SCORES = compute_disaster_scores(LEVEL_DATA)

# ---------------------------------------------------------------------------
# SECTION 5: COLOR PALETTE
# ---------------------------------------------------------------------------
# Colors progress from warm red/orange (low resilience) to cool blue/green
LEVEL_COLORS = [
    "#c0392b",  # L0  deep red
    "#e67e22",  # L1  orange
    "#f1c40f",  # L2  yellow
    "#2ecc71",  # L3  green
    "#3498db",  # L4  blue
    "#8e44ad",  # L5  purple
]

# ---------------------------------------------------------------------------
# SECTION 6: CHART GENERATION
# ---------------------------------------------------------------------------

LABEL_SHORT = ["L0", "L1", "L2", "L3", "L4", "L5"]
X = np.arange(len(LEVEL_LABELS))
BAR_WIDTH = 0.55
DISCLAIMER = (
    "Conceptual model only — values are normalized estimates, not real-world measurements."
)


def save_fig(fig, filename):
    fig.savefig(filename, dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved: {filename}")


# --- Chart 1: Sustainability Index ---
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(X, INDEXES["sustainability_index"], width=BAR_WIDTH,
              color=LEVEL_COLORS, edgecolor="white", linewidth=0.8)
for bar, val in zip(bars, INDEXES["sustainability_index"]):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.015,
            f"{val:.2f}", ha="center", va="bottom", fontsize=10, fontweight="bold")
ax.set_xticks(X)
ax.set_xticklabels(LEVEL_LABELS, fontsize=9)
ax.set_ylim(0, 1.1)
ax.set_ylabel("Sustainability Index (0.0–1.0)", fontsize=11)
ax.set_title("Circular City — Sustainability Index by Retrofit Level", fontsize=13, fontweight="bold")
ax.axhline(1.0, color="gray", linestyle="--", linewidth=0.6, alpha=0.6)
ax.text(5.55, 1.02, "Max", fontsize=8, color="gray")
fig.text(0.5, -0.01, DISCLAIMER, ha="center", fontsize=8, color="gray", style="italic")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save_fig(fig, "circular_city_sustainability_index.png")


# --- Chart 2: Disaster Resilience Index ---
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(X, INDEXES["disaster_resilience_index"], width=BAR_WIDTH,
              color=LEVEL_COLORS, edgecolor="white", linewidth=0.8)
for bar, val in zip(bars, INDEXES["disaster_resilience_index"]):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.015,
            f"{val:.2f}", ha="center", va="bottom", fontsize=10, fontweight="bold")
ax.set_xticks(X)
ax.set_xticklabels(LEVEL_LABELS, fontsize=9)
ax.set_ylim(0, 1.1)
ax.set_ylabel("Disaster Resilience Index (0.0–1.0)", fontsize=11)
ax.set_title("Circular City — Disaster Resilience Index by Retrofit Level", fontsize=13, fontweight="bold")
ax.axhline(1.0, color="gray", linestyle="--", linewidth=0.6, alpha=0.6)
fig.text(0.5, -0.01, DISCLAIMER, ha="center", fontsize=8, color="gray", style="italic")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save_fig(fig, "circular_city_disaster_resilience_index.png")


# --- Chart 3: Water Autonomy Days ---
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(X, INDEXES["water_autonomy_days"], width=BAR_WIDTH,
              color=LEVEL_COLORS, edgecolor="white", linewidth=0.8)
for bar, val in zip(bars, INDEXES["water_autonomy_days"]):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
            f"{val:.1f}d", ha="center", va="bottom", fontsize=10, fontweight="bold")
ax.set_xticks(X)
ax.set_xticklabels(LEVEL_LABELS, fontsize=9)
ax.set_ylim(0, 35)
ax.set_ylabel("Conceptual Water Autonomy (Days)", fontsize=11)
ax.set_title("Circular City — Water Autonomy Days by Retrofit Level", fontsize=13, fontweight="bold")
ax.axhline(30, color="gray", linestyle="--", linewidth=0.6, alpha=0.6)
ax.text(5.55, 30.5, "30d\nmax", fontsize=8, color="gray")
fig.text(0.5, -0.01, DISCLAIMER, ha="center", fontsize=8, color="gray", style="italic")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save_fig(fig, "water_autonomy_days.png")


# --- Chart 4: Energy Autonomy Score ---
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(X, INDEXES["energy_autonomy_score"], width=BAR_WIDTH,
              color=LEVEL_COLORS, edgecolor="white", linewidth=0.8)
for bar, val in zip(bars, INDEXES["energy_autonomy_score"]):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.015,
            f"{val:.2f}", ha="center", va="bottom", fontsize=10, fontweight="bold")
ax.set_xticks(X)
ax.set_xticklabels(LEVEL_LABELS, fontsize=9)
ax.set_ylim(0, 1.1)
ax.set_ylabel("Energy Autonomy Score (0.0–1.0)", fontsize=11)
ax.set_title("Circular City — Energy Autonomy Score by Retrofit Level", fontsize=13, fontweight="bold")
ax.axhline(1.0, color="gray", linestyle="--", linewidth=0.6, alpha=0.6)
fig.text(0.5, -0.01, DISCLAIMER, ha="center", fontsize=8, color="gray", style="italic")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save_fig(fig, "energy_autonomy_score.png")


# --- Chart 5: Heat Mitigation Score ---
fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(X, INDEXES["heat_mitigation_score"], width=BAR_WIDTH,
              color=LEVEL_COLORS, edgecolor="white", linewidth=0.8)
for bar, val in zip(bars, INDEXES["heat_mitigation_score"]):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.015,
            f"{val:.2f}", ha="center", va="bottom", fontsize=10, fontweight="bold")
ax.set_xticks(X)
ax.set_xticklabels(LEVEL_LABELS, fontsize=9)
ax.set_ylim(0, 1.1)
ax.set_ylabel("Heat Mitigation Score (0.0–1.0)", fontsize=11)
ax.set_title("Circular City — Heat Mitigation Score by Retrofit Level", fontsize=13, fontweight="bold")
ax.axhline(1.0, color="gray", linestyle="--", linewidth=0.6, alpha=0.6)
fig.text(0.5, -0.01, DISCLAIMER, ha="center", fontsize=8, color="gray", style="italic")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save_fig(fig, "heat_mitigation_score.png")


# --- Chart 6: Retrofit Level Comparison — multi-index radar or grouped bar ---
fig, ax = plt.subplots(figsize=(12, 6))

index_keys = [
    ("sustainability_index",    "Sustainability"),
    ("disaster_resilience_index","Disaster\nResilience"),
    ("energy_autonomy_score",   "Energy\nAutonomy"),
    ("heat_mitigation_score",   "Heat\nMitigation"),
    ("flood_mitigation_score",  "Flood\nMitigation"),
    ("circularity_score",       "Circularity"),
    ("recovery_capacity_score", "Recovery\nCapacity"),
]

n_indexes = len(index_keys)
n_levels  = len(LEVEL_LABELS)
group_w   = 0.75
bar_w     = group_w / n_levels
x_pos     = np.arange(n_indexes)

for i, (lbl, color) in enumerate(zip(LEVEL_LABELS, LEVEL_COLORS)):
    offsets = x_pos - group_w / 2 + bar_w * i + bar_w / 2
    vals = [INDEXES[k][i] for k, _ in index_keys]
    ax.bar(offsets, vals, width=bar_w * 0.92, color=color,
           edgecolor="white", linewidth=0.5, label=lbl.replace("\n", " "))

ax.set_xticks(x_pos)
ax.set_xticklabels([lbl for _, lbl in index_keys], fontsize=9)
ax.set_ylim(0, 1.15)
ax.set_ylabel("Score (0.0–1.0)", fontsize=11)
ax.set_title("Circular City — All Indexes by Retrofit Level (Comparison)", fontsize=13, fontweight="bold")
ax.legend(loc="upper left", fontsize=9, framealpha=0.8, ncol=3)
ax.axhline(1.0, color="gray", linestyle="--", linewidth=0.6, alpha=0.5)
fig.text(0.5, -0.01, DISCLAIMER, ha="center", fontsize=8, color="gray", style="italic")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
save_fig(fig, "retrofit_level_comparison.png")


# ---------------------------------------------------------------------------
# SECTION 7: DISASTER SCENARIO CHART (BONUS — embedded in comparison suite)
# ---------------------------------------------------------------------------

fig, axes = plt.subplots(1, len(DISASTER_EVENTS), figsize=(16, 5), sharey=True)
fig.suptitle("Circular City — Urban Function Maintained During Disaster Events",
             fontsize=13, fontweight="bold", y=1.02)

for ax_i, (event, scores) in zip(axes, DISASTER_SCORES.items()):
    bars = ax_i.bar(LABEL_SHORT, scores, color=LEVEL_COLORS,
                    edgecolor="white", linewidth=0.8)
    for bar, val in zip(bars, scores):
        ax_i.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.02,
                  f"{val:.2f}", ha="center", va="bottom", fontsize=8, fontweight="bold")
    ax_i.set_title(event, fontsize=10, fontweight="bold")
    ax_i.set_ylim(0, 1.15)
    ax_i.axhline(1.0, color="gray", linestyle="--", linewidth=0.5, alpha=0.5)
    ax_i.spines["top"].set_visible(False)
    ax_i.spines["right"].set_visible(False)
    ax_i.tick_params(axis="x", labelsize=8)

axes[0].set_ylabel("Function Maintained (0.0–1.0)", fontsize=10)
fig.text(0.5, -0.03, DISCLAIMER, ha="center", fontsize=8, color="gray", style="italic")
plt.tight_layout()
save_fig(fig, "disaster_scenario_comparison.png")


# ---------------------------------------------------------------------------
# SECTION 8: PRINT SUMMARY TABLE
# ---------------------------------------------------------------------------

SEPARATOR = "-" * 88

def print_table():
    print()
    print("=" * 88)
    print("  CIRCULAR CITY CONCEPT - CONCEPTUAL SIMULATION RESULTS")
    print("=" * 88)
    print(f"  {'Index':<32} {'L0':>7} {'L1':>7} {'L2':>7} {'L3':>7} {'L4':>7} {'L5':>7}")
    print(SEPARATOR)

    rows = [
        ("Sustainability Index",       "sustainability_index",      "{:.2f}"),
        ("Disaster Resilience Index",  "disaster_resilience_index", "{:.2f}"),
        ("Water Autonomy (Days)",      "water_autonomy_days",       "{:.1f}"),
        ("Energy Autonomy Score",      "energy_autonomy_score",     "{:.2f}"),
        ("Heat Mitigation Score",      "heat_mitigation_score",     "{:.2f}"),
        ("Flood Mitigation Score",     "flood_mitigation_score",    "{:.2f}"),
        ("Circularity Score",          "circularity_score",         "{:.2f}"),
        ("Recovery Capacity Score",    "recovery_capacity_score",   "{:.2f}"),
    ]

    for label, key, fmt in rows:
        vals = "".join(f"{fmt.format(v):>7}" for v in INDEXES[key])
        print(f"  {label:<32}{vals}")

    print(SEPARATOR)
    print()
    print(f"  {'Disaster Event':<32} {'L0':>7} {'L1':>7} {'L2':>7} {'L3':>7} {'L4':>7} {'L5':>7}")
    print(SEPARATOR)
    for event, scores in DISASTER_SCORES.items():
        label = event.replace("\n", " ")
        vals = "".join(f"{s:>7.2f}" for s in scores)
        print(f"  {label:<32}{vals}")

    print(SEPARATOR)
    print()
    print("  NOTE: All values are conceptual estimates (0.0-1.0).")
    print("        Water autonomy uses a conceptual 30-day maximum scale.")
    print("        This model does not predict outcomes for any real city.")
    print("=" * 88)
    print()


print_table()
print("Charts saved:")
print("  circular_city_sustainability_index.png")
print("  circular_city_disaster_resilience_index.png")
print("  water_autonomy_days.png")
print("  energy_autonomy_score.png")
print("  heat_mitigation_score.png")
print("  retrofit_level_comparison.png")
print("  disaster_scenario_comparison.png")
print()
print("Done.")
