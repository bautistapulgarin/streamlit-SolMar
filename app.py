import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="SolMar",
    page_icon="🌞",
    layout="wide"
)

# CSS actualizado para ocultar elementos de Streamlit Cloud
HIDE_UI = """
<style>

    /* Ocultar barra superior completa */
    header[data-testid="stHeader"] {
        display: none !important;
    }

    /* Ocultar toolbar superior derecha */
    div[data-testid="stToolbar"] {
        display: none !important;
    }

    /* Ocultar menú hamburguesa */
    button[kind="header"] {
        display: none !important;
    }

    /* Ocultar cualquier footer */
    footer, footer * {
        visibility: hidden !important;
        display: none !important;
    }

    /* OCULTAR EL NUEVO BOTÓN "Manage app" — MÉTODO QUE SÍ FUNCIONA EN 2025 */

    /* El botón se monta en un DIV dentro del body fuera del contenedor principal */
    body > div:last-child {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        height: 0 !important;
        width: 0 !important;
        pointer-events: none !important;
    }

    /* Versión alternativa: algunos despliegues lo presentan como “portal” */
    div[data-testid="stApp"] + div {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }

    /* Para asegurar que cualquier botón con ese título desaparezca */
    [title="Manage app"] {
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
    }

</style>
"""

st.markdown(HIDE_UI, unsafe_allow_html=True)
