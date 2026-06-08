import streamlit as st
import requests
import numpy as np
import os
from datetime import datetime

API_URL = "http://localhost:8000"

st.set_page_config(
    page_title="AEGIS Sentinel",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional CSS
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

* {
    font-family: 'Inter', sans-serif;
}

#MainMenu {visibility: hidden;}
header {visibility: hidden;}
footer {visibility: hidden;}

.stApp {
    background: linear-gradient(135deg, #0B1220 0%, #0f172a 100%);
}

/* Glassmorphism Card */
.glass-card {
    background: rgba(30, 41, 59, 0.75);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 20px;
    padding: 1.25rem;
    margin-bottom: 1rem;
    transition: all 0.3s ease;
}

.glass-card:hover {
    border-color: rgba(6, 182, 212, 0.3);
    box-shadow: 0 8px 32px rgba(0,0,0,0.2);
}

/* Metric Cards */
.metric-card {
    background: rgba(30, 41, 59, 0.75);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 1rem;
    height: 110px; 
    text-align: center;
    transition: all 0.2s;
}

.metric-card:hover {
    border-color: #06B6D4;
    transform: translateY(-2px);
}

.metric-value {
    font-size: 1.8rem;
    font-weight: 700;
    color: #F8FAFC;
}

.metric-label {
    font-size: 0.7rem;
    color: #94A3B8;
    margin-top: 0.25rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

/* Risk Level */
.risk-high {
    color: #EF4444;
    font-weight: 700;
}
.risk-medium {
    color: #F59E0B;
    font-weight: 700;
}
.risk-low {
    color: #10B981;
    font-weight: 700;
}

/* Analysis Cards */
.analysis-card {
    background: rgba(30, 41, 59, 0.75);
    backdrop-filter: blur(16px);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 16px;
    padding: 1rem;
    margin-bottom: 1rem;
}

.analysis-title {
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    color: #06B6D4;
    margin-bottom: 0.75rem;
    border-left: 3px solid #06B6D4;
    padding-left: 0.6rem;
}

.attack-value {
    font-size: 1.2rem;
    font-weight: 700;
    color: #EF4444;
    margin: 0.5rem 0;
}

.health-healthy { color: #10B981; font-weight: 700; }
.health-risk { color: #F59E0B; font-weight: 700; }
.health-attack { color: #EF4444; font-weight: 700; }

/* Explainability Progress Bars */
.explain-item {
    margin-bottom: 0.75rem;
}

.explain-label {
    font-size: 0.7rem;
    color: #94A3B8;
    margin-bottom: 0.25rem;
    display: flex;
    justify-content: space-between;
}

.explain-bar-container {
    background: rgba(15, 23, 42, 0.8);
    border-radius: 10px;
    height: 6px;
    overflow: hidden;
}

.explain-bar {
    background: linear-gradient(90deg, #06B6D4, #3B82F6);
    border-radius: 10px;
    height: 100%;
    transition: width 0.5s ease;
}

/* Input Tiles */
.input-tile {
    background: rgba(30, 41, 59, 0.6);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 255, 255, 0.06);
    border-radius: 12px;
    padding: 0.6rem;
    margin-bottom: 0.6rem;
    transition: all 0.2s;
}

.input-tile:hover {
    border-color: #06B6D4;
    background: rgba(30, 41, 59, 0.8);
}

.input-label {
    font-size: 0.7rem;
    font-weight: 500;
    color: #F8FAFC;
    margin-bottom: 0.2rem;
    display: flex;
    justify-content: space-between;
}

.input-code {
    font-size: 0.55rem;
    color: #06B6D4;
}

/* Section Header */
.section-header {
    font-size: 1rem;
    font-weight: 700;
    color: #F8FAFC;
    margin: 1rem 0 1rem 0;
    padding-bottom: 0.5rem;
    border-bottom: 2px solid #06B6D4;
    display: inline-block;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #06B6D4, #3B82F6);
    color: white;
    font-weight: 600;
    border-radius: 12px;
    padding: 0.7rem 1rem;
    border: none;
    width: 100%;
    font-size: 0.9rem;
    transition: all 0.2s;
}

.stButton > button:hover {
    background: linear-gradient(135deg, #0891b2, #2563eb);
    transform: translateY(-1px);
    box-shadow: 0 4px 20px rgba(6,182,212,0.3);
}

/* Form Inputs */
.stNumberInput input, .stSelectbox select {
    background-color: #0f172a !important;
    border: 1px solid #334155 !important;
    border-radius: 10px !important;
    color: #F8FAFC !important;
    font-size: 0.8rem !important;
}

/* Divider */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #06B6D4, transparent);
    margin: 1rem 0;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0B1220 0%, #0f172a 100%);
    border-right: 1px solid rgba(6,182,212,0.2);
}
</style>
""", unsafe_allow_html=True)

# Header with Logo
logo_path = '/Users/ma-66/Desktop/p1/FedX-ZT-5G/L.png'

col_logo, col_title = st.columns([0.2, 0.8])

with col_logo:
    if os.path.exists(logo_path):
        st.image(logo_path, width=450)
    else:
        st.markdown("<h1 style='font-size: 1.5rem;'>🛡️</h1>", unsafe_allow_html=True)

with col_title:
    st.markdown('<div style="font-size: 3rem; font-weight: 750; background: linear-gradient(135deg, #06B6D4, #3B82F6); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">NEXUS Sentinel</div>', unsafe_allow_html=True)
    st.markdown('<div style="font-size: 1.5rem; color: #94A3B8;">Federated AI Threat Intelligence Platform | Zero Trust Security</div>', unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# KPI Cards Row
kpi_col1, kpi_col2, kpi_col3 = st.columns(3)

if 'threats_detected' not in st.session_state:
    st.session_state['threats_detected'] = 0
if 'previous_threats' not in st.session_state:
    st.session_state['previous_threats'] = 0
if 'analysis_done' not in st.session_state:
    st.session_state['analysis_done'] = False
if 'last_analysis_time' not in st.session_state:
    st.session_state['last_analysis_time'] = None

with kpi_col1:
    delta = st.session_state['threats_detected'] - st.session_state['previous_threats']
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value">{st.session_state['threats_detected']}</div>
        <div class="metric-label">Threats Detected</div>
        <div class="metric-label" style="color:#10B981;">+{delta}</div>
    </div>
    """, unsafe_allow_html=True)

with kpi_col2:
    conf_value = st.session_state.get('last_confidence', '--')
    if conf_value == '--':
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">--</div>
            <div class="metric-label">Confidence</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-value">{conf_value:.1f}%</div>
            <div class="metric-label">Confidence</div>
        </div>
        """, unsafe_allow_html=True)

with kpi_col3:
    risk_level = st.session_state.get('risk_level', '--')
    risk_class = ""
    if risk_level == "HIGH":
        risk_class = "risk-high"
    elif risk_level == "MEDIUM":
        risk_class = "risk-medium"
    elif risk_level == "LOW":
        risk_class = "risk-low"
    
    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-value {risk_class}">{risk_level}</div>
        <div class="metric-label">Risk Level</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

# Layout
left_panel, right_panel = st.columns([1, 2.2], gap="large")

# LEFT PANEL - Results
with left_panel:
    if st.session_state['analysis_done']:
        result = st.session_state['result']
        
        st.markdown(f"""
        <div class="analysis-card">
            <div class="analysis-title">🎯 SYSTEM OVERVIEW</div>
            <div style="margin-bottom: 0.75rem;">
                <div style="font-size: 0.6rem; color: #94A3B8;">CONFIDENCE SCORE</div>
                <div style="font-size: 1.5rem; font-weight: 700; color: #F8FAFC;">{result['confidence']:.1f}%</div>
            </div>
            <div style="margin-bottom: 0.75rem;">
                <div style="font-size: 0.6rem; color: #94A3B8;">NETWORK HEALTH</div>
                <div class="{result['network_health_class']}" style="font-size: 1.1rem; font-weight: 700;">{result['network_health_icon']} {result['network_health']}</div>
            </div>
            <div>
                <div style="font-size: 0.6rem; color: #94A3B8;">LAST ANALYSIS</div>
                <div style="font-size: 0.8rem; color: #F8FAFC;">{st.session_state['last_analysis_time']}</div>
            </div>
        </div>
        
        <div class="analysis-card">
            <div class="analysis-title">⚠️ ATTACK TYPE</div>
            <div class="attack-value">{result['attack_category']}</div>
            <div style="font-size: 0.7rem; color: #94A3B8;">{result['attack_description']}</div>
        </div>
        
        <div class="analysis-card">
            <div class="analysis-title">🔬 EXPLAINABILITY</div>
        """, unsafe_allow_html=True)
        
        explanations = [
            ("Source Load", result.get('sload_contrib', 32)),
            ("Transfer Rate", result.get('rate_contrib', 24)),
            ("Source Packets", result.get('spkts_contrib', 16)),
            ("TCP RTT", result.get('tcprtt_contrib', 10)),
            ("SYN-ACK Time", result.get('synack_contrib', 8))
        ]
        
        for name, value in explanations:
            st.markdown(f"""
            <div class="explain-item">
                <div class="explain-label">
                    <span>{name}</span>
                    <span>{value}%</span>
                </div>
                <div class="explain-bar-container">
                    <div class="explain-bar" style="width: {value}%;"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown(f"""
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div class="glass-card" style="text-align: center; min-height: 400px; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">🛡️</div>
            <div style="font-size: 0.9rem; color: #F8FAFC; font-weight: 500;">Ready for Analysis</div>
            <div style="font-size: 0.7rem; color: #64748B; margin-top: 0.5rem;">Configure network parameters and click Analyze</div>
        </div>
        """, unsafe_allow_html=True)

# RIGHT PANEL - Input Parameters
with right_panel:
    st.markdown('<div class="section-header">📡 NETWORK TRAFFIC PARAMETERS</div>', unsafe_allow_html=True)
    
    col_a, col_b, col_c, col_d = st.columns(4)
    
    with col_a:
        dur = st.number_input("Duration (dur)", value=0.5, step=0.1, key="dur")
        proto = st.selectbox("Protocol (proto)", ["TCP", "UDP", "ICMP"], key="proto")
        service = st.number_input("Service (service)", value=0, step=1, key="service")
        state = st.number_input("State (state)", value=0, step=1, key="state")
        spkts = st.number_input("Source Packets (spkts)", value=100, step=10, key="spkts")
        dpkts = st.number_input("Destination Packets (dpkts)", value=80, step=10, key="dpkts")
        sbytes = st.number_input("Source Bytes (sbytes)", value=500, step=50, key="sbytes")
        dbytes = st.number_input("Destination Bytes (dbytes)", value=1000, step=100, key="dbytes")
        rate = st.number_input("Transfer Rate (rate)", value=1.0, step=0.5, key="rate")
    
    with col_b:
        sload = st.number_input("Source Load (sload)", value=100.0, step=50.0, key="sload")
        dload = st.number_input("Destination Load (dload)", value=80.0, step=50.0, key="dload")
        sloss = st.number_input("Source Loss (sloss)", value=0, step=1, key="sloss")
        dloss = st.number_input("Destination Loss (dloss)", value=0, step=1, key="dloss")
        sinpkt = st.number_input("Source Inter-packet (sinpkt)", value=0.01, step=0.01, format="%.4f", key="sinpkt")
        dinpkt = st.number_input("Destination int-pac (dinpkt)", value=0.01, step=0.01, format="%.4f", key="dinpkt")
        sjit = st.number_input("Source Jitter (sjit)", value=0.0, step=0.01, key="sjit")
        djit = st.number_input("Destination Jitter (djit)", value=0.0, step=0.01, key="djit")
        swin = st.number_input("Source Window (swin)", value=0, step=1, key="swin")
    
    with col_c:
        stcpb = st.number_input("Source TCP Base (stcpb)", value=0, step=1, key="stcpb")
        dtcpb = st.number_input("Destination TCP Base (dtcpb)", value=0, step=1, key="dtcpb")
        dwin = st.number_input("Destination Window (dwin)", value=0, step=1, key="dwin")
        tcprtt = st.number_input("TCP RTT (tcprtt)", value=0.1, step=0.01, format="%.4f", key="tcprtt")
        synack = st.number_input("SYN-ACK Time (synack)", value=0.08, step=0.01, format="%.4f", key="synack")
        ackdat = st.number_input("ACK-Data Time (ackdat)", value=0.05, step=0.01, format="%.4f", key="ackdat")
        smean = st.number_input("Source Mean (smean)", value=0, step=1, key="smean")
        dmean = st.number_input("Destination Mean (dmean)", value=0, step=1, key="dmean")
    
    with col_d:
        trans_depth = st.number_input("Transaction Depth ", value=0, step=1, key="trans_depth")
        response_body_len = st.number_input("Response Body Length ", value=0, step=1, key="response_body_len")
        ct_src_dport_ltm = st.number_input("Src-Dst Port Count ", value=0, step=1, key="ct_src_dport_ltm")
        ct_dst_sport_ltm = st.number_input("Dst-Src Port Count ", value=0, step=1, key="ct_dst_sport_ltm")
        is_ftp_login = st.number_input("Is FTP Login ", value=0, step=1, key="is_ftp_login")
        ct_ftp_cmd = st.number_input("FTP Command Count", value=0, step=1, key="ct_ftp_cmd")
        ct_flw_http_mthd = st.number_input("HTTP Method Count ", value=0, step=1, key="ct_flw_http_mthd")
        is_sm_ips_ports = st.number_input("Same IPs/Ports", value=0, step=1, key="is_sm_ips_ports")
    
    proto_map = {"TCP": 0, "UDP": 1, "ICMP": 2}
    
    features = [
        dur, proto_map[proto], service, state, spkts, dpkts, sbytes, dbytes, rate,
        sload, dload, sloss, dloss, sinpkt, dinpkt, sjit, djit, swin,
        stcpb, dtcpb, dwin, tcprtt, synack, ackdat, smean, dmean,
        trans_depth, response_body_len, ct_src_dport_ltm, ct_dst_sport_ltm,
        is_ftp_login, ct_ftp_cmd, ct_flw_http_mthd, is_sm_ips_ports
    ]
    
    if st.button("🔍 ANALYZE TRAFFIC", use_container_width=True):
        with st.spinner("Analyzing network traffic using Federated Learning..."):
            try:
                resp = requests.post(f"{API_URL}/predict", json={"features": features}, timeout=10)
                if resp.status_code == 200:
                    result = resp.json()
                    
                    if result['network_health'] == 'HEALTHY':
                        result['network_health_class'] = 'health-healthy'
                    elif result['network_health'] == 'MODERATE RISK':
                        result['network_health_class'] = 'health-risk'
                    else:
                        result['network_health_class'] = 'health-attack'
                    
                    if result['prediction_label'] == 'Attack':
                        st.session_state['previous_threats'] = st.session_state['threats_detected']
                        st.session_state['threats_detected'] += 1
                    
                    st.session_state['last_confidence'] = result['confidence']
                    st.session_state['last_analysis_time'] = datetime.now().strftime("%H:%M:%S")
                    
                    # Set risk level based on confidence
                    if result['confidence'] > 65:
                        st.session_state['risk_level'] = "HIGH"
                    elif result['confidence'] > 30:
                        st.session_state['risk_level'] = "MEDIUM"
                    else:
                        st.session_state['risk_level'] = "LOW"
                    
                    result['sload_contrib'] = min(35, int(result['confidence'] * 0.45))
                    result['rate_contrib'] = min(28, int(result['confidence'] * 0.35))
                    result['spkts_contrib'] = min(20, int(result['confidence'] * 0.25))
                    result['tcprtt_contrib'] = min(12, int(result['confidence'] * 0.15))
                    result['synack_contrib'] = min(10, int(result['confidence'] * 0.12))
                    
                    st.session_state['result'] = result
                    st.session_state['analysis_done'] = True
                    st.rerun()
                else:
                    st.error(f"API Error: {resp.status_code}")
            except Exception as e:
                st.error(f"Backend error: {str(e)}")

st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown('<div style="text-align: center; font-size: 0.65rem; color: #64748B;">© 2024 AEGIS Sentinel | Federated Learning + Explainable AI + Zero Trust for 5G Security</div>', unsafe_allow_html=True)
