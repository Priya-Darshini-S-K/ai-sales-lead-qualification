import streamlit as st
import pandas as pd

from scoring import qualify_lead


# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="AI Sales Lead Qualification Agent",
    page_icon="🤖",
    layout="wide"
)


# -----------------------------
# TITLE
# -----------------------------

st.title("🤖 AI Sales Lead Qualification Agent")

st.write(
    "Upload your sales lead CSV and automatically identify "
    "which leads need attention first."
)


# -----------------------------
# SIDEBAR
# -----------------------------

st.sidebar.header("⚙️ Qualification Criteria")

st.sidebar.write("Maximum Score: 100")

st.sidebar.markdown("""
**Scoring**

- Budget Fit — 25
- Timeline — 20
- Need Fit — 20
- Decision Maker — 15
- Engagement — 10
- Company Fit — 10
""")

st.sidebar.divider()

st.sidebar.write("### Status")

st.sidebar.write("🟢 Ready — 75 to 100")
st.sidebar.write("🟡 Interested — 50 to 74")
st.sidebar.write("⚪ Later — 0 to 49")


# -----------------------------
# FILE UPLOAD
# -----------------------------

st.subheader("📂 Upload Lead Data")

uploaded_file = st.file_uploader(
    "Choose your CSV file",
    type=["csv"]
)


# -----------------------------
# MAIN APP
# -----------------------------

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    required_columns = [
        "Lead_ID",
        "Name",
        "Company",
        "Job_Role",
        "Industry",
        "Company_Size",
        "Budget",
        "Need",
        "Timeline",
        "Engagement",
        "Location"
    ]

    missing_columns = [
        column
        for column in required_columns
        if column not in df.columns
    ]

    if missing_columns:

        st.error(
            "Missing columns: "
            + ", ".join(missing_columns)
        )

        st.stop()


    # -----------------------------
    # QUALIFY LEADS
    # -----------------------------

    results = []

    for _, lead in df.iterrows():

        score, status, action = qualify_lead(lead)

        results.append({
            "Lead_ID": lead["Lead_ID"],
            "Name": lead["Name"],
            "Company": lead["Company"],
            "Job_Role": lead["Job_Role"],
            "Industry": lead["Industry"],
            "Budget": lead["Budget"],
            "Need": lead["Need"],
            "Timeline": lead["Timeline"],
            "Score": score,
            "Status": status,
            "Next Action": action
        })


    result_df = pd.DataFrame(results)


    # -----------------------------
    # METRICS
    # -----------------------------

    st.subheader("📊 Lead Overview")

    total_leads = len(result_df)

    ready_count = len(
        result_df[result_df["Status"] == "Ready"]
    )

    interested_count = len(
        result_df[result_df["Status"] == "Interested"]
    )

    later_count = len(
        result_df[result_df["Status"] == "Later"]
    )

    average_score = round(
        result_df["Score"].mean(),
        1
    )


    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric("Total Leads", total_leads)

    with col2:
        st.metric("🟢 Ready", ready_count)

    with col3:
        st.metric("🟡 Interested", interested_count)

    with col4:
        st.metric("⚪ Later", later_count)

    with col5:
        st.metric("Average Score", average_score)


    # -----------------------------
    # FILTER
    # -----------------------------

    st.divider()

    st.subheader("🔎 Filter Leads")

    selected_status = st.selectbox(
        "Select status",
        ["All", "Ready", "Interested", "Later"]
    )


    if selected_status == "All":

        filtered_df = result_df

    else:

        filtered_df = result_df[
            result_df["Status"] == selected_status
        ]


    # -----------------------------
    # TABLE
    # -----------------------------

    st.subheader("📋 Qualified Leads")

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )


    # -----------------------------
    # LEAD DETAILS
    # -----------------------------

    st.divider()

    st.subheader("🔍 Lead Details")

    selected_lead = st.selectbox(
        "Select Lead ID",
        result_df["Lead_ID"].tolist()
    )


    lead_data = result_df[
        result_df["Lead_ID"] == selected_lead
    ].iloc[0]


    col1, col2 = st.columns(2)


    with col1:

        st.markdown("### 👤 Lead Information")

        st.write(f"**Name:** {lead_data['Name']}")

        st.write(f"**Company:** {lead_data['Company']}")

        st.write(f"**Role:** {lead_data['Job_Role']}")

        st.write(f"**Industry:** {lead_data['Industry']}")

        st.write(f"**Need:** {lead_data['Need']}")

        st.write(
            f"**Budget:** ₹{lead_data['Budget']:,.0f}"
        )

        st.write(
            f"**Timeline:** {lead_data['Timeline']}"
        )


    with col2:

        st.markdown("### 🎯 Qualification")

        score = lead_data["Score"]

        if score >= 75:

            st.success(
                f"🟢 READY — {score}/100"
            )

        elif score >= 50:

            st.warning(
                f"🟡 INTERESTED — {score}/100"
            )

        else:

            st.info(
                f"⚪ LATER — {score}/100"
            )


        st.write(
            f"**Next Action:** {lead_data['Next Action']}"
        )


    # -----------------------------
    # DOWNLOAD
    # -----------------------------

    st.divider()

    st.subheader("📥 Export Results")

    csv_data = result_df.to_csv(
        index=False
    ).encode("utf-8")


    st.download_button(
        label="Download Qualified Leads CSV",
        data=csv_data,
        file_name="qualified_leads.csv",
        mime="text/csv"
    )


else:

    st.info(
        "👆 Upload your realistic_100_sales_leads.csv file to begin."
    )