import streamlit as st

from constants import *

from calculations import (
    calculate_all,
)

from plotting import (
    draw_reference,
)

from ui_components import (
    tolerance_input_block,
    result_metric,
    parameter_block,
)

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="HV3PFE Volume Calculator",
    layout="wide",
)

# ======================================================
# TABS
# ======================================================

tab_input, tab_results = st.tabs(
    ["Input", "Results"]
)

# ======================================================
# INPUT TAB
# ======================================================

with tab_input:

    # ----------------------------------
    # HEADER
    # ----------------------------------

    left_top, right_top = st.columns(
        [2.3, 1]
    )

    with left_top:

        st.title(
            "🔵 HV3PFE Chip Volume Calculator"
        )

        st.write(
            """
Output shown in **µL**

- Water density = **0.998 g/mL**
- Valve thickness reduces AIR dome only
- Final Combined = Air + Liquid
- Output format = Nominal (Min ~ Max)
"""
        )

    with right_top:

        st.markdown(
            "##### 📐 Dimension Guide"
        )

        st.pyplot(
            draw_reference()
        )

    # ----------------------------------
    # VALVE
    # ----------------------------------

    st.subheader(
        "🔧 Valve Thickness"
    )

    v1, v2 = st.columns(2)

    with v1:

        valve_ld, valve_ld_plus, valve_ld_minus = (
            tolerance_input_block(
                "Valve Thickness LD",
                DEFAULT_VALVE_LD,
                DEFAULT_TOL_PLUS,
                DEFAULT_TOL_MINUS,
                "valve_ld",
            )
        )

    with v2:

        valve_sd, valve_sd_plus, valve_sd_minus = (
            tolerance_input_block(
                "Valve Thickness SD",
                DEFAULT_VALVE_SD,
                DEFAULT_TOL_PLUS,
                DEFAULT_TOL_MINUS,
                "valve_sd",
            )
        )

    # ----------------------------------
    # GRID
    # ----------------------------------

    c1, c2 = st.columns(2)
    c3, c4 = st.columns(2)

    # AIR LD

    with c1:

        st.subheader(
            "🟦 Air Layer LD"
        )

        d_air_ld, d_air_ld_plus, d_air_ld_minus = (
            tolerance_input_block(
                "Diameter Air LD",
                DEFAULT_D_AIR_LD,
                DEFAULT_TOL_PLUS,
                DEFAULT_TOL_MINUS,
                "d_air_ld",
            )
        )

        h_air_ld, h_air_ld_plus, h_air_ld_minus = (
            tolerance_input_block(
                "Dome Depth Air LD",
                DEFAULT_H_AIR_LD,
                DEFAULT_TOL_PLUS,
                DEFAULT_TOL_MINUS,
                "h_air_ld",
            )
        )

    # AIR SD

    with c2:

        st.subheader(
            "🟦 Air Layer SD"
        )

        d_air_sd, d_air_sd_plus, d_air_sd_minus = (
            tolerance_input_block(
                "Diameter Air SD",
                DEFAULT_D_AIR_SD,
                DEFAULT_TOL_PLUS,
                DEFAULT_TOL_MINUS,
                "d_air_sd",
            )
        )

        h_air_sd, h_air_sd_plus, h_air_sd_minus = (
            tolerance_input_block(
                "Dome Depth Air SD",
                DEFAULT_H_AIR_SD,
                DEFAULT_TOL_PLUS,
                DEFAULT_TOL_MINUS,
                "h_air_sd",
            )
        )

    # LIQ LD

    with c3:

        st.subheader(
            "🟩 Liquid Layer LD"
        )

        d_liq_ld, d_liq_ld_plus, d_liq_ld_minus = (
            tolerance_input_block(
                "Diameter Liquid LD",
                DEFAULT_D_LIQ_LD,
                DEFAULT_TOL_PLUS,
                DEFAULT_TOL_MINUS,
                "d_liq_ld",
            )
        )

        h_liq_ld, h_liq_ld_plus, h_liq_ld_minus = (
            tolerance_input_block(
                "Dome Depth Liquid LD",
                DEFAULT_H_LIQ_LD,
                DEFAULT_TOL_PLUS,
                DEFAULT_TOL_MINUS,
                "h_liq_ld",
            )
        )

    # LIQ SD

    with c4:

        st.subheader(
            "🟩 Liquid Layer SD"
        )

        d_liq_sd, d_liq_sd_plus, d_liq_sd_minus = (
            tolerance_input_block(
                "Diameter Liquid SD",
                DEFAULT_D_LIQ_SD,
                DEFAULT_TOL_PLUS,
                DEFAULT_TOL_MINUS,
                "d_liq_sd",
            )
        )

        h_liq_sd, h_liq_sd_plus, h_liq_sd_minus = (
            tolerance_input_block(
                "Dome Depth Liquid SD",
                DEFAULT_H_LIQ_SD,
                DEFAULT_TOL_PLUS,
                DEFAULT_TOL_MINUS,
                "h_liq_sd",
            )
        )

# ======================================================
# CALCULATIONS
# ======================================================

results = calculate_all(

    valve_ld=valve_ld,
    valve_sd=valve_sd,

    valve_ld_plus=valve_ld_plus,
    valve_ld_minus=valve_ld_minus,

    valve_sd_plus=valve_sd_plus,
    valve_sd_minus=valve_sd_minus,

    d_air_ld=d_air_ld,
    d_air_ld_plus=d_air_ld_plus,
    d_air_ld_minus=d_air_ld_minus,

    h_air_ld=h_air_ld,
    h_air_ld_plus=h_air_ld_plus,
    h_air_ld_minus=h_air_ld_minus,

    d_air_sd=d_air_sd,
    d_air_sd_plus=d_air_sd_plus,
    d_air_sd_minus=d_air_sd_minus,

    h_air_sd=h_air_sd,
    h_air_sd_plus=h_air_sd_plus,
    h_air_sd_minus=h_air_sd_minus,

    d_liq_ld=d_liq_ld,
    d_liq_ld_plus=d_liq_ld_plus,
    d_liq_ld_minus=d_liq_ld_minus,

    h_liq_ld=h_liq_ld,
    h_liq_ld_plus=h_liq_ld_plus,
    h_liq_ld_minus=h_liq_ld_minus,

    d_liq_sd=d_liq_sd,
    d_liq_sd_plus=d_liq_sd_plus,
    d_liq_sd_minus=d_liq_sd_minus,

    h_liq_sd=h_liq_sd,
    h_liq_sd_plus=h_liq_sd_plus,
    h_liq_sd_minus=h_liq_sd_minus,
)

# ======================================================
# RESULTS TAB
# ======================================================

with tab_results:

    st.title("📊 Results")

    # Mean

    st.markdown(
        "## Nominal Volume"
    )

    m1, m2 = st.columns(2)

    with m1:

        result_metric(
            "LD",
            results["ld_mean"],
            "success",
        )

    with m2:

        result_metric(
            "SD",
            results["sd_mean"],
            "success",
        )

    # RSS

    st.markdown(
        "## Volume Error – RSS"
    )

    r1, r2 = st.columns(2)

    with r1:

        result_metric(
            "LD",
            results["ld_rss"],
            "info",
        )

    with r2:

        result_metric(
            "SD",
            results["sd_rss"],
            "info",
        )

    # Worst case

    st.markdown(
        "## Volume Error – Worst Case"
    )

    w1, w2 = st.columns(2)

    with w1:

        result_metric(
            "LD",
            results["ld_wc"],
            "warning",
        )

    with w2:

        result_metric(
            "SD",
            results["sd_wc"],
            "warning",
        )

    # Parameters

    st.markdown(
        "## Parameters"
    )

    p1, p2 = st.columns(2)

    with p1:

        parameter_block(
            "LD",
            {
                "Valve": valve_ld,
                "Air D": d_air_ld,
                "Air H": h_air_ld,
                "Liquid D": d_liq_ld,
                "Liquid H": h_liq_ld,
            },
        )

    with p2:

        parameter_block(
            "SD",
            {
                "Valve": valve_sd,
                "Air D": d_air_sd,
                "Air H": h_air_sd,
                "Liquid D": d_liq_sd,
                "Liquid H": h_liq_sd,
            },
        )

# ======================================================
# FOOTER
# ======================================================

st.caption(
    "Tolerance calculated using RSS and worst-case analysis"
)

st.caption(
    "Format = Nominal (Min ~ Max)"
)
