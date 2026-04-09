import streamlit as st

# --- CONFIGURACIÓN DE ALTA PRIORIDAD ---
st.set_page_config(page_title="ECD-OS v2.0 | CONTROL TÁCTICO", layout="wide")

# --- CSS DE INGENIERÍA DE DETALLE (LOOK DE RADAR) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&display=swap');
    
    .stApp { background-color: #000000; font-family: 'JetBrains Mono', monospace; }
    [data-testid="stSidebar"] { background-color: #020617 !important; border-right: 2px solid #3b82f6; }
    
    /* Contenedores de KPIs estilo Búnker */
    .stMetric { 
        background: linear-gradient(135deg, #0f172a 0%, #020617 100%);
        padding: 25px; border-radius: 5px; 
        border: 1px solid #1e293b;
        border-left: 10px solid #3b82f6;
        box-shadow: 0 0 20px rgba(59, 130, 246, 0.1);
    }
    
    /* Títulos con efecto de terminal */
    h1, h2, h3 { color: #3b82f6 !important; text-transform: uppercase; letter-spacing: 2px; }
    .status-box { 
        padding: 10px; border: 1px solid #3b82f6; 
        background: rgba(59, 130, 246, 0.05); color: #60a5fa;
        font-size: 0.8rem; margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- PANEL DE IDENTIDAD ---
with st.sidebar:
    st.markdown("<h2 style='color:white !important;'>🛡️ ECD-OS v2.0</h2>", unsafe_allow_html=True)
    st.markdown(f"<div class='status-box'>DIRECTOR: R. CARBAJAL<br>SITE: VALLEJO HQ<br>ESTATUS: ONLINE</div>", unsafe_allow_html=True)
    st.divider()
    tab = st.radio("SELECCIONAR MÓDULO", [
        "🛰️ MONITOR GLOBAL", "📞 MARCACIÓN TÁCTICA", "⚡ OPERACIÓN CRM", 
        "🧪 LAB ESTRATEGIAS", "🏆 RANKING SITES", "🔮 PROYECCIONES IA"
    ])

# --- MÓDULO 1: MONITOR GLOBAL (WAR ROOM) ---
if tab == "🛰️ MONITOR GLOBAL":
    st.title("SISTEMA DE MANDO OPERATIVO")
    
    # Grid de Metas Principales
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("RECUPERACIÓN TOTAL", "$529,450", "OBJ: $8M")
    with m1 := st.container():
        st.metric("AVANCE DE META", "6.62%", "TREND: +1.2%")
    with c3:
        st.metric("HONORARIOS (17%)", "$79,766", "ESTIMADO")

    st.markdown("### 📡 ESTATUS POR SEDE")
    s1, s2, s3 = st.columns(3)
    
    # Vallejo (Tu Base)
    with s1:
        st.info("**SEDE VALLEJO**\n\nEficiencia: 94%\n\nEstatus: Liderando")
    with s2:
        st.info("**SEDE TOLEDO**\n\nEficiencia: 88%\n\nEstatus: Estable")
    with s3:
        st.info("**SEDE TLALPAN**\n\nEficiencia: 82%\n\nEstatus: Alerta")

    st.divider()
    
    # Motores de Cobranza (Supabase Bridge)
    st.markdown("### ⚙️ MOTORES DE COBRANZA ACTIVOS")
    st.code("CONECTADO A BÚNKER ID: jboowhjsaevszlktgkzs", language="bash")
    
    col_a, col_b, col_c = st.columns(3)
    col_a.success("🟢 TDC INBURSA")
    col_b.success("🟢 TELCEL")
    col_c.warning("🟡 ICP (RECONFIGURANDO)")
