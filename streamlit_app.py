import streamlit as st

# --- CONFIGURACIÓN DE INTERFAZ ELITE ---
st.set_page_config(page_title="ECD-OS v2.0 | War Room", layout="wide")

# Estilo Dark Mode / Velvet
st.markdown("""
    <style>
    .main { background-color: #020617; color: white; }
    [data-testid="stSidebar"] { background-color: #0f172a !important; border-right: 1px solid #1e293b; }
    .stMetric { background-color: #1e293b; padding: 15px; border-radius: 10px; border-left: 5px solid #3b82f6; }
    </style>
    """, unsafe_allow_html=True)

# --- MENÚ LATERAL (11 PESTAÑAS ACORDADAS) ---
with st.sidebar:
    st.title("🛡️ ECD-OS v2.0")
    st.caption("DIRECTOR: R. CARBAJAL")
    st.divider()
    tab = st.radio("NAVEGACIÓN MAESTRA", [
        "📊 HOME / Brincos", "📞 MARCACIÓN", "⚡ OPERACIÓN CRM", 
        "🧪 LAB. ESTRATEGIAS A/B", "🏆 RANKING SITES", "👥 EQUIPOS", 
        "💰 CONCILIACIÓN", "🔮 PROYECCIONES IA", "📊 PÓRTICO TRAMOS", 
        "📑 HISTÓRICO", "⚙️ ESTATUS"
    ])

# --- CONTENIDO DINÁMICO (LÓGICA CLAUDE + GPT) ---
if tab == "📊 HOME / Brincos":
    st.title("War Room: Dashboard de Mando")
    c1, c2, c3 = st.columns(3)
    c1.metric("META GLOBAL", "$8,000,000", "Abril 2026")
    c2.metric("RECUPERADO HOY", "$529,450", "+6.6%")
    c3.metric("HONORARIOS EST.", "$79,766", "Tasa 17%")
    st.divider()
    st.subheader("Motores Activos en Supabase")
    st.write("✅ TDC INBURSA | ✅ TELCEL | ✅ ICP")
