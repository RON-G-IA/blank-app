import streamlit as st

# --- CONFIGURACIÓN DE NIVEL DIRECTOR ---
st.set_page_config(page_title="ECD-OS v2.0 | WAR ROOM", layout="wide")

# --- DISEÑO ELITE (FONDO OSCURO Y BORDES NEÓN) ---
st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #050a18 !important; border-right: 2px solid #1e293b; }
    .stMetric { 
        background-color: #0f172a; 
        padding: 20px; 
        border-radius: 15px; 
        border: 1px solid #3b82f6;
        box-shadow: 0 4px 15px rgba(59, 130, 246, 0.2);
    }
    h1, h2, h3 { color: #3b82f6 !important; font-family: 'Courier New', monospace; }
    .stRadio > label { color: #94a3b8 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# --- MENÚ DE MANDO ---
with st.sidebar:
    st.title("🛡️ ECD-OS v2.0")
    st.markdown("**DIRECTOR: R. CARBAJAL**")
    st.divider()
    tab = st.radio("NAVEGACIÓN MAESTRA", [
        "📊 DASHBOARD / BRINCOS", "📞 MARCACIÓN", "⚡ OPERACIÓN CRM", 
        "🧪 LAB ESTRATEGIAS", "🏆 RANKING SITES", "🔮 PROYECCIONES IA"
    ])

# --- PANTALLA PRINCIPAL: SALA DE GUERRA ---
if tab == "📊 DASHBOARD / BRINCOS":
    st.title("🛰️ WAR ROOM: MONITOR GLOBAL")
    st.subheader("Control Operativo: Vallejo | Toledo | Tlalpan")
    
    # KPIs con estilo de consola
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("OBJETIVO DE RECUPERACIÓN", "$8,000,000", "Meta Abril")
    with m2:
        st.metric("RECUPERADO (REAL-TIME)", "$529,450", "+6.6%")
    with m3:
        st.metric("HONORARIOS GENERADOS", "$79,766", "Tasa 17%")

    st.divider()
    
    # Estatus de Motores
    st.subheader("⚡ Estatus de Motores de Cobranza")
    col_a, col_b, col_c = st.columns(3)
    col_a.success("✅ TDC INBURSA: ACTIVO")
    col_b.success("✅ TELCEL: ACTIVO")
    col_c.warning("⚠️ ICP: AJUSTE DE ESTRATEGIA")
