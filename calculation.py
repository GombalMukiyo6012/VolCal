import math

from constants import (
    WATER_DENSITY,
    LD_REFERENCE,
    SD_REFERENCE,
)

# ======================================================
# BASIC HELPERS
# ======================================================

def clamp(v):
    return max(0, v)


def mm3_to_uL(v):
    return v / WATER_DENSITY


def fmt(v):
    return f"{v:.3f}"


def rss_tolerance(*values):
    return math.sqrt(
        sum(v**2 for v in values)
    )


# ======================================================
# GEOMETRY
# ======================================================

def spherical_cap_volume_mm3(
    diameter,
    height,
):

    if diameter <= 0 or height <= 0:
        return 0.0

    R = diameter / 2

    if height > diameter:
        return 0.0

    return (
        math.pi
        * height**2
        * (3 * R - height)
    ) / 3


# ======================================================
# AIR CALC
# ======================================================

def calc_air(
    diameter,
    dome_depth,
    valve_thickness,
):

    h_final = clamp(
        dome_depth - valve_thickness
    )

    original = spherical_cap_volume_mm3(
        diameter,
        dome_depth,
    )

    final = spherical_cap_volume_mm3(
        diameter,
        h_final,
    )

    return original, final


# ======================================================
# ERROR FORMAT
# ======================================================

def volume_error_percent(
    reference,
    vmin,
    vnom,
    vmax,
):

    err_nom = (
        (vnom - reference)
        / reference
    ) * 100

    err_min = (
        (vmin - reference)
        / reference
    ) * 100

    err_max = (
        (vmax - reference)
        / reference
    ) * 100

    return (
        f"{err_nom:+.2f}% "
        + f"({err_min:+.2f}% ~ {err_max:+.2f}%)"
    )


# ======================================================
# MAIN CALC
# ======================================================

def calculate_all(**p):

    # ----------------------------------
    # nominal
    # ----------------------------------

    air_ld_org, air_ld_fin = calc_air(
        p["d_air_ld"],
        p["h_air_ld"],
        p["valve_ld"],
    )

    air_sd_org, air_sd_fin = calc_air(
        p["d_air_sd"],
        p["h_air_sd"],
        p["valve_sd"],
    )

    liq_ld = spherical_cap_volume_mm3(
        p["d_liq_ld"],
        p["h_liq_ld"],
    )

    liq_sd = spherical_cap_volume_mm3(
        p["d_liq_sd"],
        p["h_liq_sd"],
    )

    final_ld = air_ld_fin + liq_ld
    final_sd = air_sd_fin + liq_sd

    # ----------------------------------
    # worst case min
    # ----------------------------------

    air_ld_min = calc_air(
        clamp(
            p["d_air_ld"]
            - p["d_air_ld_minus"]
        ),
        clamp(
            p["h_air_ld"]
            - p["h_air_ld_minus"]
        ),
        p["valve_ld"]
        + p["valve_ld_plus"],
    )[1]

    air_ld_max = calc_air(
        p["d_air_ld"]
        + p["d_air_ld_plus"],
        p["h_air_ld"]
        + p["h_air_ld_plus"],
        clamp(
            p["valve_ld"]
            - p["valve_ld_minus"]
        ),
    )[1]

    liq_ld_min = spherical_cap_volume_mm3(
        clamp(
            p["d_liq_ld"]
            - p["d_liq_ld_minus"]
        ),
        clamp(
            p["h_liq_ld"]
            - p["h_liq_ld_minus"]
        ),
    )

    liq_ld_max = spherical_cap_volume_mm3(
        p["d_liq_ld"]
        + p["d_liq_ld_plus"],
        p["h_liq_ld"]
        + p["h_liq_ld_plus"],
    )

    final_ld_min = (
        air_ld_min + liq_ld_min
    )

    final_ld_max = (
        air_ld_max + liq_ld_max
    )

    # ----------------------------------
    # SD worst case
    # ----------------------------------

    air_sd_min = calc_air(
        clamp(
            p["d_air_sd"]
            - p["d_air_sd_minus"]
        ),
        clamp(
            p["h_air_sd"]
            - p["h_air_sd_minus"]
        ),
        p["valve_sd"]
        + p["valve_sd_plus"],
    )[1]

    air_sd_max = calc_air(
        p["d_air_sd"]
        + p["d_air_sd_plus"],
        p["h_air_sd"]
        + p["h_air_sd_plus"],
        clamp(
            p["valve_sd"]
            - p["valve_sd_minus"]
        ),
    )[1]

    liq_sd_min = spherical_cap_volume_mm3(
        clamp(
            p["d_liq_sd"]
            - p["d_liq_sd_minus"]
        ),
        clamp(
            p["h_liq_sd"]
            - p["h_liq_sd_minus"]
        ),
    )

    liq_sd_max = spherical_cap_volume_mm3(
        p["d_liq_sd"]
        + p["d_liq_sd_plus"],
        p["h_liq_sd"]
        + p["h_liq_sd_plus"],
    )

    final_sd_min = (
        air_sd_min + liq_sd_min
    )

    final_sd_max = (
        air_sd_max + liq_sd_max
    )

    # ----------------------------------
    # RSS
    # ----------------------------------

    d_air_ld_tol = rss_tolerance(
        p["d_air_ld_plus"],
        p["d_air_ld_minus"],
    ) / 2

    h_air_ld_tol = rss_tolerance(
        p["h_air_ld_plus"],
        p["h_air_ld_minus"],
    ) / 2

    valve_ld_tol = rss_tolerance(
        p["valve_ld_plus"],
        p["valve_ld_minus"],
    ) / 2

    d_liq_ld_tol = rss_tolerance(
        p["d_liq_ld_plus"],
        p["d_liq_ld_minus"],
    ) / 2

    h_liq_ld_tol = rss_tolerance(
        p["h_liq_ld_plus"],
        p["h_liq_ld_minus"],
    ) / 2

    final_ld_rss_min = (
        calc_air(
            p["d_air_ld"]
            - d_air_ld_tol,
            p["h_air_ld"]
            - h_air_ld_tol,
            p["valve_ld"]
            + valve_ld_tol,
        )[1]
        + spherical_cap_volume_mm3(
            p["d_liq_ld"]
            - d_liq_ld_tol,
            p["h_liq_ld"]
            - h_liq_ld_tol,
        )
    )

    final_ld_rss_max = (
        calc_air(
            p["d_air_ld"]
            + d_air_ld_tol,
            p["h_air_ld"]
            + h_air_ld_tol,
            p["valve_ld"]
            - valve_ld_tol,
        )[1]
        + spherical_cap_volume_mm3(
            p["d_liq_ld"]
            + d_liq_ld_tol,
            p["h_liq_ld"]
            + h_liq_ld_tol,
        )
    )

    # SD RSS

    d_air_sd_tol = rss_tolerance(
        p["d_air_sd_plus"],
        p["d_air_sd_minus"],
    ) / 2

    h_air_sd_tol = rss_tolerance(
        p["h_air_sd_plus"],
        p["h_air_sd_minus"],
    ) / 2

    valve_sd_tol = rss_tolerance(
        p["valve_sd_plus"],
        p["valve_sd_minus"],
    ) / 2

    d_liq_sd_tol = rss_tolerance(
        p["d_liq_sd_plus"],
        p["d_liq_sd_minus"],
    ) / 2

    h_liq_sd_tol = rss_tolerance(
        p["h_liq_sd_plus"],
        p["h_liq_sd_minus"],
    ) / 2

    final_sd_rss_min = (
        calc_air(
            p["d_air_sd"]
            - d_air_sd_tol,
            p["h_air_sd"]
            - h_air_sd_tol,
            p["valve_sd"]
            + valve_sd_tol,
        )[1]
        + spherical_cap_volume_mm3(
            p["d_liq_sd"]
            - d_liq_sd_tol,
            p["h_liq_sd"]
            - h_liq_sd_tol,
        )
    )

    final_sd_rss_max = (
        calc_air(
            p["d_air_sd"]
            + d_air_sd_tol,
            p["h_air_sd"]
            + h_air_sd_tol,
            p["valve_sd"]
            - valve_sd_tol,
        )[1]
        + spherical_cap_volume_mm3(
            p["d_liq_sd"]
            + d_liq_sd_tol,
            p["h_liq_sd"]
            + h_liq_sd_tol,
        )
    )

    # ----------------------------------
    # output
    # ----------------------------------

    return {

        "ld_mean":
            f"{mm3_to_uL(final_ld):.3f} µL",

        "sd_mean":
            f"{mm3_to_uL(final_sd):.3f} µL",

        "ld_wc":
            volume_error_percent(
                LD_REFERENCE,
                mm3_to_uL(final_ld_min),
                mm3_to_uL(final_ld),
                mm3_to_uL(final_ld_max),
            ),

        "sd_wc":
            volume_error_percent(
                SD_REFERENCE,
                mm3_to_uL(final_sd_min),
                mm3_to_uL(final_sd),
                mm3_to_uL(final_sd_max),
            ),

        "ld_rss":
            volume_error_percent(
                LD_REFERENCE,
                mm3_to_uL(final_ld_rss_min),
                mm3_to_uL(final_ld),
                mm3_to_uL(final_ld_rss_max),
            ),

        "sd_rss":
            volume_error_percent(
                SD_REFERENCE,
                mm3_to_uL(final_sd_rss_min),
                mm3_to_uL(final_sd),
                mm3_to_uL(final_sd_rss_max),
            ),
    }
