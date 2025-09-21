import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from datetime import datetime

# Basic page setup
st.set_page_config(layout="wide", page_title="Financial Dashboards Suite")
# Simple CSS styling
st.markdown(
    """
<style>
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        border-left: 4px solid #667eea;
        margin-bottom: 1rem;
    }
    .phase-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 8px;
        border: 1px solid #dee2e6;
        text-align: center;
        margin-bottom: 1rem;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: bold;
        color: #2d3748;
        margin: 0.5rem 0;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #718096;
        font-weight: 500;
    }
    .tab-header {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 1rem;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Main title
st.markdown(
    '<div class="tab-header">💼 Financial Performance Dashboard Suite</div>',
    unsafe_allow_html=True,
)

# Create tabs
tab1, tab2, tab3 = st.tabs(
    ["🏦 Revolut Youth", "🏛️ Telda Case Study", "💳 American Express"]
)

# ====================== REVOLUT YOUTH TAB ======================
with tab1:
    st.title("🏦 Revolut Youth - Financial Performance Dashboard")
    st.markdown(f"**Dashboard updated:** {datetime.now().strftime('%B %d, %Y')}")
    st.markdown("---")

    # Data definitions for Revolut
    revenue_data = pd.DataFrame(
        {"Year": ["FY20", "FY21", "FY22", "FY23"], "Revenue": [0, 25, 80, 188]}
    )

    user_data = pd.DataFrame(
        {"Year": [2019, 2020, 2021, 2022, 2023], "Users": [0, 0.2, 0.8, 1.5, 2.0]}
    )

    financial_projections = pd.DataFrame(
        {
            "Year": ["FY21", "FY23", "Proj. H1 2025"],
            "Revenue": [25, 188, 145],
            "Operating_Profit": [15, 122, 101.5],
        }
    )

    roi_data = {
        'Phase': ['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4'],
        'ROI': [-100, 52.8, 265.4, 630.9]
    }

    cac_ltv_data = {
        'Phase': ['Phase 1', 'Phase 2', 'Phase 3', 'Phase 4'],
        'CAC': [40, 20, 15, 10],
        'LTV': [500, 550, 600, 650]
    }

    arpu_data = pd.DataFrame(
        {"Year": ["FY20", "FY21", "FY23", "Proj. FY25"], "ARPU": [0, 10, 30, 55]}
    )

    # Key Performance Indicators
    st.subheader("📊 Key Performance Indicators")

    kpi_cols = st.columns(4)
    kpis = [
        ("Total Revenue (FY23)", "£188M", "+135% YoY"),
        ("Active Users (2023)", "2.0M", "+33% YoY"),
        ("ARPU (FY23)", "£94", "+213% YoY"),
        ("Operating Margin", "65%", "Best in class"),
    ]

    for col, (label, value, change) in zip(kpi_cols, kpis):
        with col:
            st.markdown(
                f"""
            <div class="metric-card">
                <div class="metric-label">{label}</div>
                <div class="metric-value">{value}</div>
                <div style="color: #38a169; font-weight: 500; font-size: 0.9rem;">{change}</div>
            </div>
            """,
                unsafe_allow_html=True,
            )

    st.markdown("---")

    # Financial Performance Charts
    st.subheader("💰 Financial Performance")

    chart_cols = st.columns(2)

    # Revenue Growth Chart
    with chart_cols[0]:
        fig_revenue = go.Figure()
        fig_revenue.add_trace(
            go.Scatter(
                x=revenue_data["Year"],
                y=revenue_data["Revenue"],
                mode="lines+markers",
                line=dict(color="#667eea", width=4),
                marker=dict(size=8, color="#667eea"),
                name="Revenue",
                hovertemplate="<b>%{x}</b><br>Revenue: £%{y}M<extra></extra>",
            )
        )

        fig_revenue.update_layout(
            title="Revenue Growth Trajectory",
            xaxis_title="Fiscal Year",
            yaxis_title="Revenue (£M)",
            height=400,
        )

        st.plotly_chart(fig_revenue, use_container_width=True)


    # User Growth Chart
    with chart_cols[1]:
        fig_users = go.Figure()
        fig_users.add_trace(
            go.Scatter(
                x=user_data["Year"],
                y=user_data["Users"],
                mode="lines+markers",
                line=dict(color="#764ba2", width=4),
                marker=dict(size=8, color="#764ba2"),
                name="Users",
                hovertemplate="<b>%{x}</b><br>Users: %{y}M<extra></extra>",
            )
        )

        fig_users.update_layout(
            title="User Growth Curve",
            xaxis_title="Year",
            yaxis_title="Users (Millions)",
            height=400,
        )

        st.plotly_chart(fig_users, use_container_width=True)

    # Revenue vs Profit Comparison
    st.subheader("📈 Revenue vs Operating Profit")

    fig_comparison = go.Figure()

    fig_comparison.add_trace(
        go.Bar(
            x=financial_projections["Year"],
            y=financial_projections["Revenue"],
            name="Revenue",
            marker_color="#667eea",
        )
    )

    fig_comparison.add_trace(
        go.Bar(
            x=financial_projections["Year"],
            y=financial_projections["Operating_Profit"],
            name="Operating Profit",
            marker_color="#764ba2",
        )
    )

    fig_comparison.update_layout(
        title="Revenue vs Operating Profit Comparison",
        xaxis_title="Fiscal Year",
        yaxis_title="Amount (£M)",
        barmode="group",
        height=400,
    )

    st.plotly_chart(fig_comparison, use_container_width=True)

    # CAC vs LTV
    fig_cac_ltv = go.Figure()
    fig_cac_ltv.add_trace(go.Bar(
        x=cac_ltv_data['Phase'],
        y=cac_ltv_data['CAC'],
        name='CAC',
        marker_color='#764ba2'
    ))
    fig_cac_ltv.add_trace(go.Bar(
        x=cac_ltv_data['Phase'],
        y=cac_ltv_data['LTV'],
        name='LTV',
        marker_color='#667eea'
    ))
    fig_cac_ltv.update_layout(
        title='CAC vs. LTV Progression (£)',
        barmode='group',

    )
    st.plotly_chart(fig_cac_ltv, use_container_width=True)

    import plotly.graph_objects as go

    # Data
    years = ['FY20', 'FY21', 'FY23', 'Proj. FY25']
    arpu_values = [0, 20, 35, 60]

    # Line Chart
    fig_arpu = go.Figure()
    fig_arpu.add_trace(go.Scatter(
        x=years, y=arpu_values,
        mode='lines+markers',
        line=dict(color='#764ba2', width=3),
        marker=dict(size=8),
        name='ARPU (£/user/year)'
    ))

    fig_arpu.update_layout(
        title='Annual Revenue Per User (ARPU)',
        xaxis_title='Fiscal Year',
        yaxis_title='ARPU (£)',
        template='plotly_white',
        margin=dict(l=40, r=40, t=60, b=40)
    )
    st.plotly_chart(fig_arpu, use_container_width=True)
    # fig_arpu.show()

    # Cumulative ROI
    fig_roi = go.Figure()
    fig_roi.add_trace(go.Scatter(
        x=roi_data['Phase'],
        y=roi_data['ROI'],
        mode='lines+markers',
        line=dict(color='#764ba2', width=2),
        name='ROI'
    ))
    fig_roi.update_layout(
        title='Cumulative ROI & Payback',
        xaxis_title='Phase',
        yaxis_title='ROI (%)'
    )
    st.plotly_chart(fig_roi, use_container_width=True)






    # Strategic Phases Analysis
    st.subheader("🚀 Strategic Phase Analysis")

    phase_cols = st.columns(4)
    phases_data = [
        {
            "title": "Foundation",
            "phase": "Phase 1",
            "investment": "£6M",
            "revenue": "£0M",
            "roi": "-100%",
            "description": "Initial setup & infrastructure",
        },
        {
            "title": "Growth",
            "phase": "Phase 2",
            "investment": "£14M",
            "revenue": "£25M",
            "roi": "+78.6%",
            "description": "User acquisition & scaling",
        },
        {
            "title": "Expansion",
            "phase": "Phase 3",
            "investment": "£10.5M",
            "revenue": "£80M",
            "roi": "+661.9%",
            "description": "Market expansion & features",
        },
        {
            "title": "Scale",
            "phase": "Phase 4",
            "investment": "£5M",
            "revenue": "£188M",
            "roi": "+3,660%",
            "description": "Optimization & profitability",
        },
    ]

    for col, phase in zip(phase_cols, phases_data):
        with col:
            roi_color = "#dc3545" if phase["roi"].startswith("-") else "#28a745"
            st.markdown(
                f"""
            <div class="phase-card">
                <h4 style="color: #667eea; margin: 0 0 0.5rem 0;">{phase['title']}</h4>
                <p style="color: #6c757d; font-size: 0.85rem; margin: 0 0 1rem 0;">{phase['description']}</p>
                <div style="margin: 1rem 0;">
                    <div style="font-size: 0.9rem; margin: 0.3rem 0;">
                        <strong>Investment:</strong> {phase['investment']}
                    </div>
                    <div style="font-size: 0.9rem; margin: 0.3rem 0;">
                        <strong>Revenue:</strong> {phase['revenue']}
                    </div>
                    <div style="font-size: 1.2rem; font-weight: bold; color: {roi_color}; margin: 0.5rem 0;">
                        ROI: {phase['roi']}
                    </div>
                </div>
            </div>
            """,
                unsafe_allow_html=True,
            )

# ====================== TELDA CASE STUDY TAB ======================
with tab2:
    st.title("🏛️ Telda Case Study Dashboard")
    st.markdown("---")

    # User Growth Data
    user_growth_data = pd.DataFrame(
        {
            "Date": pd.to_datetime(["Apr 2021", "Oct 2022", "2023"]),
            "Users": [30000, 135000, 500000],
        }
    )

    # Create two columns for the first row
    col1, col2 = st.columns(2)

    # User Growth Chart in first column
    with col1:
        st.subheader("Explosive User Growth (2021-2023)")
        fig_growth = px.line(
            user_growth_data, x="Date", y="Users", markers=True, line_shape="linear"
        )

        # Update the line color to a dark brown and add markers
        fig_growth.update_traces(
            line=dict(color="#663300"), marker=dict(color="#663300")
        )

        # Update layout to match the image's style
        fig_growth.update_layout(
            xaxis_title="",
            yaxis_title="",
            showlegend=False,
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            yaxis=dict(showgrid=True, gridcolor="#D3D3D3"),
            xaxis=dict(showgrid=False),
            font=dict(color="#000000", size=12),
            height=400,
        )
        st.plotly_chart(fig_growth, use_container_width=True)

    # Financial Metrics in second column
    with col2:
        st.subheader("Robust Financial Performance")
        col2_1, col2_2 = st.columns(2)

        with col2_1:
            st.metric("Transaction Volume (2023)", "$300M")
        with col2_2:
            st.metric("Revenue per Employee", "$143K")

    # Create two columns for the second row
    col3, col4 = st.columns(2)

    # Users Under 30 Donut Chart
    with col3:
        st.subheader("Youth-Centric Product Design")
        fig_donut = go.Figure(
            data=[
                go.Pie(
                    labels=["Users Under 30", "Other Users"],
                    values=[70, 30],
                    hole=0.7,
                    marker_colors=["#800020", "#4A0404"],
                )
            ]
        )
        fig_donut.update_layout(
            annotations=[dict(text="70%", x=0.5, y=0.5, font_size=20, showarrow=False)],
            height=400,
        )
        st.plotly_chart(fig_donut, use_container_width=True)

        st.markdown(
            """
        - Mobile-first user experience
        - Integrated social payment features (GIFs, emojis)
        - Intuitive interface tailored for digital natives
        """
        )

    # Market Opportunity Pie Chart
    with col4:
        st.subheader("Market Opportunity: Egyptian Youth Segment")
        fig_pie = go.Figure(
            data=[
                go.Pie(
                    labels=["Youth (18-29)", "Other population"],
                    values=[19.9, 80.1],
                    hole=0,
                    marker_colors=["#800020", "#4A0404"],
                )
            ]
        )
        fig_pie.update_layout(height=400)
        st.plotly_chart(fig_pie, use_container_width=True)

        st.markdown(
            """
        The youth segment (18-29) comprises 21.3M of the total population, 
        representing a significant market opportunity.
        """
        )

    # Footer
    st.markdown("---")
    st.markdown("*Data source: Telda Case Study 2023*")

# ====================== AMERICAN EXPRESS TAB ======================
with tab3:
    st.title("💳 American Express Case Study")
    st.markdown("### 2024 Financial Highlights")
    st.markdown("---")

    # Custom color scheme
    COLOR_BURGUNDY = "#722F37"
    COLOR_LIGHT_RED = "#A85751"
    COLOR_MEDIUM_RED = "#8B3E3E"
    COLOR_GOLD = "#FFD700"

    import streamlit as st
    import pandas as pd
    import plotly.express as px

    # Create two columns with equal width
    col1, col2 = st.columns(2)

    import streamlit as st
    import pandas as pd
    import plotly.express as px

    # Create two columns with equal width
    col1, col2 = st.columns(2)

    # Chart 1: Revenue and Profit
    with col1:
        st.subheader("Record Growth in (B$)")
        data1 = pd.DataFrame({
            "Category": ["Revenue", "Net Income"],
            "Value": [ 65.9 , 10.1]
        })

        colors = ["#722F37", "#A85751"]

        fig1 = px.bar(
            data1,
            x="Category",
            y="Value",
            color= "Category",
            color_discrete_sequence=colors,
        )
        fig1.update_layout(height=300)
        st.plotly_chart(fig1, use_container_width=True)

    # Chart 2: ROI vs. Competitors
    with col2:
        st.subheader("ROI vs. Competitors")
        # All code within this block must be indented
        roi_data = pd.DataFrame(
            {"Company": ["American Express", "Visa", "Mastercard"], "ROI": [22.5, 18.3, 17.9]}
        )

        colors = ["#722F37", "#A85751", "#8B3E3E"]

        fig2 = px.bar(
            roi_data,
            x="Company",
            y="ROI",
            color="Company",
            color_discrete_sequence=colors,
            labels={"ROI": "ROI (%)"},
        )
        fig2.update_layout(
            title="",
            showlegend=False,
            height=300
        )
        st.plotly_chart(fig2, use_container_width=True)




    # Create two columns for the second row
    col3, col4 = st.columns(2)

    # Customer Value Growth
    with col3:
        years = [2019, 2020, 2021, 2022, 2023]
        values = [350000, 385000, 420000, 455000, 490000]

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=years, y=values, mode="lines+markers", line=dict(color=COLOR_BURGUNDY)
            )
        )
        fig.update_layout(
            title="Customer Value Growth",
            xaxis_title="Year",
            yaxis_title="Revenue per Customer ($)",
            height=300,
        )
        st.plotly_chart(fig, use_container_width=True)

    # Customer Acquisition Cost
    with col4:
        quarters = ["Q1 2023", "Q2 2023", "Q3 2023", "Q4 2023", "Q1 2024"]
        cac = [75, 72, 68, 65, 63]

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=quarters, y=cac, mode="lines+markers", line=dict(color=COLOR_BURGUNDY)
            )
        )
        fig.update_layout(
            title="Customer Acquisition Cost (CAC)",
            xaxis_title="Quarter",
            yaxis_title="Cost ($)",
            height=300,
        )
        st.plotly_chart(fig, use_container_width=True)

    # Market Share and Investor Confidence
    st.subheader("📈 Market Performance")

    col5, col6 = st.columns(2)

    # Market Share
    with col5:
        years = ["2021", "2022", "2023"]
        market_share = [18, 19, 21]
        colors = ["#800020", "#B76E79", "#D8A7B1"]

        fig = go.Figure()
        fig.add_trace(
            go.Bar(
                x=years,
                y=market_share,
                marker_color=colors,
                text=[f"{v}%" for v in market_share],
                textposition="outside",
            )
        )
        fig.update_layout(
            title="Market Share Growth",
            xaxis_title="Year",
            yaxis_title="Market Share (%)",
            height=300,
        )
        st.plotly_chart(fig, use_container_width=True)

    # Investor Confidence
    with col6:
        dates = ["Jan 2020", "Mar 2025"]
        confidence = [0, 120]

        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=dates,
                y=confidence,
                mode="lines+markers",
                line=dict(color="#800020", width=4),
                marker=dict(size=8, color="#D8A7B1"),
                name="Investor Confidence",
            )
        )
        fig.update_layout(
            title="Investor Confidence Index",
            xaxis_title="Date",
            yaxis_title="Confidence Index",
            yaxis=dict(range=[0, 130]),
            showlegend=False,
            height=300,
        )
        st.plotly_chart(fig, use_container_width=True)



    # Create two columns for profit analysis
    col9, col10 = st.columns(2)

    # Profit Margin by Card Type
    with col9:
        card_types = ["Platinum", "Gold", "Green", "Cobrand"]
        margins = [40, 30, 15, 15]

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=card_types,
                    values=margins,
                    marker_colors=[
                        COLOR_BURGUNDY,
                        COLOR_MEDIUM_RED,
                        COLOR_LIGHT_RED,
                        "#B87070",
                    ],
                )
            ]
        )
        fig.update_layout(title="Profit Margin by Card Type", height=400)
        st.plotly_chart(fig, use_container_width=True)

    # Growth Drivers
    with col10:
        categories = ["Gen Z/Millennials", "Other"]
        distribution = [75, 25]

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=categories,
                    values=distribution,
                    marker_colors=[COLOR_BURGUNDY, COLOR_LIGHT_RED],
                )
            ]
        )
        fig.update_layout(title="Growth Drivers - Customer Acquisition", height=400)
        st.plotly_chart(fig, use_container_width=True)



        # Financial Ratios
        st.subheader("💰 Key Financial Ratios")

        col7, col8 = st.columns(2)


        # Dividend Yield Chart
        with col7:
            st.header("Dividend Yield")

            # Use Plotly for the chart only
            fig1 = go.Figure(
                data=[
                    go.Pie(
                        values=[0.93, 100 - 0.93],
                        hole=0.6,
                        marker_colors=["#800020", "#F0F0F0"],
                        textinfo="none",
                        showlegend=False,
                    )
                ]
            )

            # Adjust layout to place text inside the chart
            fig1.update_layout(
                height=300,
                margin=dict(t=0, b=0, l=0, r=0),
                annotations=[
                    dict(
                        text="<b>0.93%</b>",
                        x=0.5, y=0.5,
                        font=dict(size=40, color="#800020"),
                        showarrow=False
                    ),
                    dict(
                        text="<br>Consistent returns",
                        x=0.5, y=0.35,
                        font=dict(size=12, color="gray"),
                        showarrow=False,
                    ),
                ],
            )

            st.plotly_chart(fig1, use_container_width=True)

        # P/E Ratio Chart
        with col8:
            st.header("P/E Ratio")

            # Use Plotly for the chart only
            fig2 = go.Figure(
                data=[
                    go.Pie(
                        values=[22.98, 100 - 22.98],
                        hole=0.6,
                        marker_colors=["#800020", "#F0F0F0"],
                        textinfo="none",
                        showlegend=False,
                    )
                ]
            )

            # Adjust layout to place text inside the chart
            fig2.update_layout(
                height=300,
                margin=dict(t=0, b=0, l=0, r=0),
                annotations=[
                    dict(
                        text="<b>22.98</b>",
                        x=0.5, y=0.5,
                        font=dict(size=40, color="#800020"),
                        showarrow=False
                    ),
                    dict(
                        text="<br>Healthy valuation",
                        x=0.5, y=0.35,
                        font=dict(size=12, color="gray"),
                        showarrow=False,
                    ),
                ],
            )

            st.plotly_chart(fig2, use_container_width=True)




    # Key Performance Indicators
    st.markdown("### Key Performance Indicators")
    kpi1, kpi2, kpi3 = st.columns(3)

    with kpi1:
        st.metric("Customer Retention", "92%")

    with kpi2:
        st.metric("Avg. Transaction Value", "$1,250")

    with kpi3:
        st.metric("Cross-Sell Rate", "1.5x")

    # Spending Trends
    st.markdown("### Spending Trends")
    generations = ["Gen Z", "Millennials", "Gen X", "Baby Boomers"]
    spending = [16, 12, 7, 4]

    fig = px.bar(x=generations, y=spending, color_discrete_sequence=[COLOR_BURGUNDY])
    fig.update_layout(
        title="Spending Growth by Generation (%)",
        xaxis_title="Generation",
        yaxis_title="Growth (%)",
        height=300,
    )
    st.plotly_chart(fig, use_container_width=True)

    # Footer
    st.markdown("---")
    st.markdown("*Data reflects strong performance across key metrics and segments*")

# Overall footer
st.markdown("---")
st.markdown("### 📊 Dashboard Suite Summary")
col_summary1, col_summary2, col_summary3 = st.columns(3)

with col_summary1:
    st.markdown(
        """
    **🏦 Revolut Youth**
    - £188M Revenue (FY23)
    - 2M Active Users
    - 3,660% ROI Achievement
    """
    )

with col_summary2:
    st.markdown(
        """
    **🏛️ Telda**
    - 500K Users by 2023
    - $300M Transaction Volume
    - 70% Youth Market Focus
    """
    )

with col_summary3:
    st.markdown(
        """
    **💳 American Express**
    - $75B Revenue (2024)
    - 21% ROI vs Competitors
    - 75% Millennial/Gen Z Growth
    """
    )