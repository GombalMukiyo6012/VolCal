import streamlit as st

# ======================================================
# TOLERANCE INPUT
# ======================================================

def tolerance_input_block(
    label,
    default_value,
    tol_plus,
    tol_minus,
    key,
):

    st.markdown(
        f"##### {label}"
    )

    main_val = st.number_input(
        f"{label} (mm)",
        value=default_value,
        step=0.001,
        format="%.3f",
        key=f"{key}_main",
    )

    c1, c2, c3, c4 = st.columns(
        [0.22, 2, 0.22, 2]
    )

    # -------------------------
    # +
    # -------------------------

    with c1:

        st.markdown(
            """
<div style="
height:38px;
display:flex;
align-items:center;
justify-content:center;
font-size:22px;
font-weight:700;
line-height:1;
margin-top:2px;
">+</div>
""",
            unsafe_allow_html=True,
        )

    with c2:

        plus_val = st.number_input(
            " ",
            value=tol_plus,
            step=0.001,
            format="%.3f",
            key=f"{key}_plus",
            label_visibility="collapsed",
        )

    # -------------------------
    # -
    # -------------------------

    with c3:

        st.markdown(
            """
<div style="
height:38px;
display:flex;
align-items:center;
justify-content:center;
font-size:22px;
font-weight:700;
line-height:1;
margin-top:2px;
">−</div>
""",
            unsafe_allow_html=True,
        )

    with c4:

        minus_val = st.number_input(
            "  ",
            value=tol_minus,
            step=0.001,
            format="%.3f",
            key=f"{key}_minus",
            label_visibility="collapsed",
        )

    st.markdown("---")

    return (
        main_val,
        plus_val,
        minus_val,
    )


# ======================================================
# RESULT CARD
# ======================================================

def result_metric(
    label,
    value,
    style="info",
):

    text = f"{label} : {value}"

    if style == "success":
        st.success(text)

    elif style == "warning":
        st.warning(text)

    else:
        st.info(text)


# ======================================================
# PARAMETER BLOCK
# ======================================================

def parameter_block(
    title,
    params: dict,
):

    st.markdown(
        f"### {title}"
    )

    for label, values in params.items():

        nominal = values["nominal"]
        tol_plus = values["plus"]
        tol_minus = values["minus"]

        st.write(
            f"{label} : "
            f"{nominal:.3f} mm "
            f"(+{tol_plus:.3f} / -{tol_minus:.3f})"
        )
