import streamlit as st
import time

st.set_page_config(layout="wide")

st.title("Agentic AI Demo")




import streamlit as st
import pandas as pd
import time

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Agentic Workflow Dashboard",
    page_icon="✈️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
}

.main {
    background-color: #f4f7fb;
}

.big-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #1f4e79;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #555;
    font-size: 16px;
    margin-bottom: 30px;
}

.card {
    background: white;
    padding: 18px;
    border-radius: 14px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    border-left: 6px solid #1f77b4;
    margin-bottom: 15px;
}

.agent-card {
    background: white;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    font-weight: bold;
    box-shadow: 0 3px 8px rgba(0,0,0,0.08);
    margin-bottom: 12px;
    transition: 0.3s;
}

.agent-card:hover {
    transform: scale(1.03);
}

.step-box {
    background: #eef5ff;
    padding: 14px;
    border-radius: 10px;
    margin: 8px 0;
    border-left: 5px solid #2e86de;
    font-weight: 500;
}

.output-box {
    background: #ffffff;
    padding: 20px;
    border-radius: 14px;
    border-left: 6px solid #28a745;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}

.center-text {
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown("<div class='big-title'>✈️ AI Agentic Workflow Dashboard</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>Travel Booking Automation using Multiple AI Agents</div>",
    unsafe_allow_html=True
)

# ---------------- SCENARIO ----------------
st.markdown("## 📌 Scenario")

st.markdown("""
<div class='card'>
<b>Goal:</b> Book a trip from <b>Kolkata → Mumbai</b><br><br>
✔ Cheapest Flight / Train <br>
✔ 3-Star Hotel <br>
✔ Cab Booking <br>
✔ User Approval <br>
✔ Payment Confirmation <br>
✔ Notification
</div>
""", unsafe_allow_html=True)

# ---------------- AGENTS ----------------
st.markdown("## 🤖 Available Agents")

agents = [
    "🔍 Search Agent",
    "✈️ Flight Search Agent",
    "🚆 Train Search Agent",
    "🏨 Hotel Search Agent",
    "🚖 Cab Booking Agent",
    "✅ Approval Agent",
    "💳 Payment Agent",
    "📩 Notification Agent"
]

cols = st.columns(4)

for i, agent in enumerate(agents):
    with cols[i % 4]:
        st.markdown(
            f"<div class='agent-card'>{agent}</div>",
            unsafe_allow_html=True
        )

# ---------------- WORKFLOW ----------------
st.markdown("## 🔄 Design Workflow")

selected_agents = st.multiselect(
    "Select AI Agents",
    agents,
    default=agents
)

workflow = []

if "🔍 Search Agent" in selected_agents:
    workflow.append("Search travel route & policies")

if "✈️ Flight Search Agent" in selected_agents:
    workflow.append("Find lowest-cost flights")

if "🚆 Train Search Agent" in selected_agents:
    workflow.append("Find lowest-cost trains")

if "🏨 Hotel Search Agent" in selected_agents:
    workflow.append("Book 3-star hotel")

if "🚖 Cab Booking Agent" in selected_agents:
    workflow.append("Arrange cab booking")

if "✅ Approval Agent" in selected_agents:
    workflow.append("Ask for user approval")

if "💳 Payment Agent" in selected_agents:
    workflow.append("Process payment")

if "📩 Notification Agent" in selected_agents:
    workflow.append("Send ticket + confirmation")

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### Workflow Flow")

    for i, step in enumerate(workflow, 1):
        st.markdown(
            f"<div class='step-box'>Step {i}: {step}</div>",
            unsafe_allow_html=True
        )
        if i != len(workflow):
            st.markdown(
                "<div class='center-text'>⬇️</div>",
                unsafe_allow_html=True
            )

with col2:
    st.markdown("### Selected Agents Summary")

    df = pd.DataFrame({
        "Step": list(range(1, len(selected_agents)+1)),
        "Agent": selected_agents
    })

    st.dataframe(df, use_container_width=True)

# ---------------- ORCHESTRATION ----------------
st.markdown("## ⚙️ Orchestration Pattern")

pattern = st.radio(
    "Choose Pattern",
    ["Sequential", "Parallel", "Hierarchical", "Hybrid"],
    horizontal=True
)

st.success(f"Selected Pattern: {pattern}")

# ---------------- USER INPUT ----------------
st.markdown("## 🧾 Travel Input")

col1, col2, col3 = st.columns(3)

with col1:
    from_city = st.text_input("From City", "Kolkata")

with col2:
    to_city = st.text_input("To City", "Mumbai")

with col3:
    budget = st.number_input("Budget ₹", min_value=1000, value=12000)

# ---------------- RUN BUTTON ----------------
st.markdown("## 🚀 Run AI Workflow")

if st.button("Run Workflow Simulation"):
    st.subheader("Running Agents...")

    progress = st.progress(0)

    for i, step in enumerate(workflow):
        st.write(f"✅ {step}")
        time.sleep(0.7)
        progress.progress((i + 1) / len(workflow))

    st.success("Workflow Completed Successfully!")

    # Final itinerary
    st.markdown("## 📦 Final Output")

    st.markdown(f"""
    <div class='output-box'>
        <h3>🎯 Best Travel Itinerary</h3>
        <hr>
        <b>Route:</b> {from_city} → {to_city}<br><br>
        <b>Travel Mode:</b> Flight ✈️<br>
        <b>Flight Cost:</b> ₹4500<br>
        <b>Hotel:</b> 3-Star Hotel (₹3500)<br>
        <b>Cab:</b> Airport Pickup (₹800)<br>
        <b>Total Cost:</b> ₹8800<br>
        <b>Budget:</b> ₹{budget}<br>
        <b>Status:</b> Approved & Booked ✅<br>
        <b>Payment:</b> Successful 💳<br>
        <b>Notification:</b> Ticket Sent 📩
    </div>
    """, unsafe_allow_html=True)

# ---------------- REFLECTION ----------------
st.markdown("## 🧠 Reflection")

reflection = st.text_area(
    "Why is this orchestration suitable?",
    "This workflow uses Hybrid orchestration. "
    "Search-related tasks can run in parallel, while approval, payment, "
    "and notification follow sequential order. "
    "The Search Agent behaves as a parent planner."
)

if reflection:
    st.info(reflection)

# ---------------- FOOTER ----------------
st.markdown("---")
st.caption("AI Agentic Workflow Dashboard | Streamlit Assignment Project")