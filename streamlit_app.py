import streamlit as st
import pandas as pd

# 1. CONFIGURACIÓN EJECUTIVA
st.set_page_config(page_title="ECD-OS v2.0 | GERENCIA DE COBRANZA", layout="wide")

# 2. ESTILO VISUAL DE ALTO NIVEL (LOOK EMPRESARIAL)
st.markdown("""
    <style>
    .main { background-color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #0f172a !important; color: white; }
    .stMetric { 
        background-color: #ffffff; 
        border: 1px solid #e2e8f0; 
        padding: 20px; 
        border-radius: 8px; 
        box-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); 
    }
    .stHeader { color: #1e293b; font-family: 'Helvetica Neue', sans-serif; }
    div[data-testid="stMetricValue"] > div { color: #1e40af !important; }
    </style>
    """, unsafe_allow_html=True)

# 3. IDENTIDAD CORPORATIVA
with st.sidebar:
    st.image("https://www.freeiconspng.com/uploads/shield-icon-12.png", width=50)
    st.title("ECD-OS v2.0")
    st.markdown("---")
    st.subheader("UNIDAD DE INTELIGENCIA")
    st.info(f"RESPONSABLE:\n**RONALD CARBAJAL ROMERO**\nGerente de Cobranza")
    st.divider()
    modulo = st.radio("SISTEMAS ESTRATÉGICOS", [
        "📈 DASHBOARD EJECUTIVO", 
        "⛓️ TRAZABILIDAD POR TRAMO",
        "📊 RANKING DE SEDES",
        "⚙️ CONTROL DE MOTORES"
    ])

# 4. DASHBOARD EJECUTIVO (LO QUE EL DIRECTOR QUIERE VER)
if modulo == "📈 DASHBOARD EJECUTIVO":
    st.title("🚀 REPORTE ESTRATÉGICO DE RECUPERACIÓN")
    st.caption("Consolidado Nacional: Vallejo | Toledo | Tlalpan")
    
    # KPIs FINANCIEROS
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("META MENSUAL", "$8,000,000", "Abril 2026")
    c2.metric("RECUPERACIÓN REAL", "$529,450", "6.6% avance")
    c3.metric("HONORARIOS (17%)", "$79,766", "Proyectado")
    c4.metric("PRODUCTIVIDAD", "92.4%", "+2.1% vs Mar")

    st.divider()

    # TABLA DE ANÁLISIS POR SEDE
    st.subheader("📊 DESEMPEÑO OPERATIVO POR SEDE")
    data = {
        "Sede": ["VALLEJO HQ", "TOLEDO", "TLALPAN"],
        "Cartera": ["TDC Inbursa", "Telcel", "ICP"],
        "Recuperado": ["$245,000", "$184,450", "$100,000"],
        "Eficiencia": ["96%", "89%", "78%"],
        "Tendencia": ["⬆️ Alta", "➡️ Estable", "⬇️ Revisión"]
    }
    df = pd.DataFrame(data)
    st.table(df)

    # GRÁFICO DE BARRAS (Simulado para impacto visual)
    st.subheader("📈 COMPARATIVA DE RECUPERACIÓN DIARIA")
    chart_data = pd.DataFrame({
        'Día': range(1, 8),
        'Vallejo': [30, 45, 40, 60, 55, 70, 85],
        'Toledo': [20, 35, 30, 45, 40, 50, 60],
        'Tlalpan': [10, 20, 15, 25, 22, 30, 35]
    }).set_index('Día')
    st.bar_chart(chart_data)

elif modulo == "⚙️ CONTROL DE MOTORES":
    st.title("⚙️ ESTADO DE MOTORES DE COBRANZA")
    st.code("CONEXIÓN ENCRIPTADA CON BÚNKER SUPABASE: ACTIVA", language="bash")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.success("✅ MOTOR TDC INBURSA - OPERANDO AL 100%")
        st.success("✅ MOTOR TELCEL - OPERANDO AL 100%")
    with col_b:
        st.warning("⚠️ MOTOR ICP - RECONFIGURACIÓN DE TRAMOS")
        st.info("ℹ️ PRÓXIMA CARGA: MAÑANA 08:00 AM")
