import streamlit as st

# --- CONFIGURACIÓN DE NIVEL DIRECTOR ---
st.set_page_config(page_title="ECD-OS v2.0 | WAR ROOM", layout="wide")

# --- CSS: ESTÉTICA DE BÚNKER E INGENIERÍA DE DETALLE ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    .stApp { background-color: #000000; font-family: 'JetBrains Mono', monospace; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #020617 !important; border-right: 2px solid #3b82f6; }
    
    /* Indicadores estilo Pantalla de Radar */
    .stMetric { 
        background: #0f172a; 
        padding: 20px; border-radius: 0px; 
        border: 1px solid #1e293b;
        border-left: 5px solid #3b82f6;
    }
    h1, h2, h3 { color: #3b82f6 !important; text-transform: uppercase; font-weight: 700; }
    .stAlert { background-color: #020617; border: 1px solid #1e293b; color: white; }
    </style>
    """, unsafe_allow_html=True)

# --- PANEL DE IDENTIDAD Y MANDO ---
with st.sidebar:
    st.markdown("<h2 style='color:white !important;'>🛡️ ECD-OS v2.0</h2>", unsafe_allow_html=True)
    st.code("DIR: R. CARBAJAL\nLOC: VALLEJO HQ\nEST: EN LÍNEA", language="bash")
    st.divider()
    tab = st.radio("SELECCIONAR MÓDULO TÁCTICO", [
        "🛰️ MONITOR GLOBAL", "📞 MARCACIÓN", "⚡ OPERACIÓN CRM", 
        "🧪 LAB ESTRATEGIAS", "🏆 RANKING SITES", "🔮 PROYECCIONES IA"
    ])

# --- MÓDULO: MONITOR GLOBAL (SALA DE GUERRA) ---
if tab == "🛰️ MONITOR GLOBAL":
    st.title("SISTEMA DE MANDO OPERATIVO")
    st.caption("INTEGRACIÓN ESTRATÉGICA: VALLEJO | TOLEDO | TLALPAN")
    
    # KPIs de Alto Nivel
    c1, c2, c3 = st.columns(3)
    c1.metric("META GLOBAL", "$8,000,000", "ABRIL 2026")
    c2.metric("AVANCE OPERATIVO", "6.62%", "+1.2% TREND")
    c3.metric("
