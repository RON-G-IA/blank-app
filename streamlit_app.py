import streamlit as st

# 1. CONFIGURACIÓN DE ALTA PRIORIDAD
st.set_page_config(page_title="ECD-OS v2.0 | CONTROL TÁCTICO", layout="wide")

# 2. INTERFAZ "GUERREO ÉLITE" (CSS BLINDADO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    .stApp { background-color: #000000; font-family: 'JetBrains Mono', monospace; color: #ffffff; }
    [data-testid="stSidebar"] { background-color: #050a18 !important; border-right: 2px solid #3b82f6; }
    
    /* Indicadores estilo Radar de Búnker */
    .stMetric { 
        background: linear-gradient(180deg, #0f172a 0%, #020617 100%);
        padding: 20px; 
        border: 1px solid #1e293b;
        border-left: 5px solid #3b82f6;
    }
    
    h1, h2, h3 { color: #3b82f6 !important; text-transform: uppercase; letter-spacing: 2px; }
    .stAlert { background-color: #020617; border: 1px solid #3b82f6; color: #60a5fa; }
    
    /* Personalización de texto de métricas */
    [data-testid="stMetricValue"] { color: #ffffff !important; font-size: 1.8rem !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. BARRA DE MANDO (IDENTIDAD DEL DIRECTOR)
with st.sidebar:
    st.markdown("<h2 style='color:white !important;'>🛡️ ECD-OS</h2>", unsafe_allow_html=True)
    st.code("DIRECTOR: R. CARBAJAL\nSTATUS: OPERATIVO\nNODE: VALLEJO_HQ", language="bash")
    st.divider()
    
    menu = [
        "🛰️ MONITOR GLOBAL", 
        "📞 MARCACIÓN TÁCTICA", 
        "⚡ OPERACIÓN CRM", 
        "🏆 RANKING SITES", 
        "🔮 PROYECCIONES IA"
    ]
    tab = st.radio("SISTEMAS ACTIVOS", menu)

# 4. MONITOR GLOBAL (WAR ROOM)
if tab == "🛰️ MONITOR GLOBAL":
    st.title("SISTEMA DE MANDO OPERATIVO")
    st.caption("INTEGRACIÓN ESTRATÉGICA DE SEDES")
    
    # KPIs de la Operación (Metas de $8M)
    m1, m2, m3 = st.columns(3)
    with m1:
        st.metric("META DE RECUPERACIÓN", "$8,000,000", "ABRIL 2026")
    with m2:
        st.metric("AVANCE REAL", "$529,450", "6.62% DEL TOTAL")
    with m3:
        st.metric("HONORARIOS EST.", "$79,766", "TASA 17%")

    st.divider()
    
    # Estatus de Fuerza por Sede
    st.markdown("### 📡 ESTADO DE FUERZA")
    s1, s2, s3 = st.columns(3)
    
    with s1:
        st.info("**SEDE VALLEJO**\n\nEstatus: Liderando\n\nEficiencia: 94%")
    with s2:
        st.info("**SEDE TOLEDO**\n\nEstatus: Estable\n\nEficiencia: 88%")
    with s3:
        st.warning("**SEDE TLALPAN**\n\nEstatus: Crítico\n\nEficiencia: 72%")

    st.divider()
    
    # Motores de Cobranza (Conexión al Búnker)
    st.markdown("### ⚙️ MOTORES DE COBRANZA (SUPABASE)")
    st.caption("CONECTADO A: jboowhjsaevszlktgkzs")
    
    c1, c2, c3 = st.columns(3)
    c1.success("🟢 TDC INBURSA")
    c2.success("🟢 TELCEL")
    c3.success("🟢 ICP")
