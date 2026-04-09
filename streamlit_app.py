import streamlit as st
import pandas as pd
import numpy as np

# 1. CONFIGURACIÓN DE ALTA DIRECCIÓN
st.set_page_config(page_title="ECD-OS v2.0 | INTELIGENCIA OPERATIVA", layout="wide")

# 2. ESTILO "FINANCIAL TERMINAL" (ALTO IMPACTO)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
    .stApp { background-color: #0f172a; font-family: 'Inter', sans-serif; color: #f8fafc; }
    [data-testid="stSidebar"] { background-color: #020617 !important; border-right: 1px solid #1e293b; }
    
    /* Tarjetas de Métricas de Precisión */
    div[data-testid="stMetric"] {
        background: #1e293b;
        border: 1px solid #334155;
        padding: 20px;
        border-radius: 4px;
        border-top: 4px solid #3b82f6;
    }
    
    h1, h2, h3 { font-weight: 700; color: #ffffff !important; letter-spacing: -1px; }
    .stTable { background-color: #1e293b; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# 3. PANEL DE CONTROL LATERAL (IDENTIDAD)
with st.sidebar:
    st.markdown("<h2 style='text-align: center;'>🛡️ ECD-OS</h2>", unsafe_allow_html=True)
    st.markdown(f"""
        <div style='background: #1e40af; padding: 15px; border-radius: 5px; margin-bottom: 20px;'>
            <p style='margin:0; font-size: 0.8rem; opacity: 0.8;'>GERENTE DE COBRANZA</p>
            <p style='margin:0; font-weight: bold;'>RONALD CARBAJAL ROMERO</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    menu = st.radio("SISTEMAS DE ANÁLISIS", [
        "📊 CONSOLIDADO NACIONAL", 
        "📈 TENDENCIAS Y PROYECCIÓN",
        "⚙️ ARQUITECTURA DE MOTORES"
    ])

# 4. MONITOR DE ALTO NIVEL
if menu == "📊 CONSOLIDADO NACIONAL":
    st.header("SISTEMA DE MANDO: RECUPERACIÓN ESTRATÉGICA")
    st.caption("Consolidado Operativo: Vallejo | Toledo | Tlalpan")
    
    # KPIs de Impacto Financiero
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("ASIGNACIÓN TOTAL", "$120,000,000", "Q2 2026")
    c2.metric("OBJETIVO MENSUAL", "$8,000,000", "ABRIL")
    c3.metric("RECUPERACIÓN REAL", "$529,450", "6.6% EFF")
    c4.metric("HONORARIOS NETOS", "$79,766", "17% FEE")

    st.divider()

    # Análisis de Salud por Sede
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader("📡 DESEMPEÑO POR NODO OPERATIVO")
        df_sedes = pd.DataFrame({
            "Sede": ["VALLEJO HQ", "TOLEDO", "TLALPAN"],
            "Cartera Principal": ["TDC Inbursa", "Telcel", "ICP"],
            "Meta": ["$4M", "$2.5M", "$1.5M"],
            "Avance": [0.65, 0.45, 0.30],
            "Estatus": ["🟢 ÓPTIMO", "🟡 PREVENTIVO", "🔴 CRÍTICO"]
        })
        st.data_editor(
            df_sedes,
            column_config={
                "Avance": st.column_config.ProgressColumn("Cumplimiento", min_value=0, max_value=1),
            },
            hide_index=True,
            use_container_width=True
        )

    with col_right:
        st.subheader("🎯 MIX DE CARTERA")
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['Inbursa', 'Telcel', 'Walmart']
        )
        st.area_chart(chart_data)

    st.divider()
    
    # Mensaje de Acción
    st.warning("⚠️ **ALERTA DIRECTIVA:** Sede Tlalpan requiere ajuste de estrategia en tramos 90+ para alcanzar el 17% de honorarios proyectado.")

# 5. MÓDULO DE MOTORES
elif menu == "⚙️ ARQUITECTURA DE MOTORES":
    st.header("⚙️ CONTROL DE MOTORES Y FLUJO DE DATOS")
    st.code("CONEXIÓN ACTIVA: SUPABASE_CLUSTER_VALLEJO", language="bash")
    
    m1, m2, m3 = st.columns(3)
    m1.success("✅ MOTOR INBURSA\nIntegración API: Activa")
    m2.success("✅ MOTOR TELCEL\nCarga masiva: Completada")
    m3.error("❌ MOTOR ICP\nError de segmentación de tramos")
