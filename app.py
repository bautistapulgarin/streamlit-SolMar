import streamlit as st

# Configuración inicial de la página
st.set_page_config(
    page_title="SolMar",
    page_icon="🌞",  # puedes eliminar el icono si prefieres algo más formal
    layout="wide"
)



# Ocultar elementos de Streamlit (barra superior, menú, manage app)
hide_streamlit_style = """
    <style>
        /* Ocultar menú superior derecho: Share, GitHub, Options */
        header[data-testid="stHeader"] {
            display: none !important;
        }

        /* Ocultar hamburger menu (≡) en modo viewer */
        button[kind="header"] {
            display: none !important;
        }

        /* Ocultar footer "Manage App" */
        footer {
            visibility: hidden !important;
        }
        footer:after {
            content:'' !important;
            visibility:hidden !important;
        }

        /* Ocultar barra inferior por si aparece en modo editor */
        div[data-testid="stStatusWidget"] {
            display: none !important;
        }

        /* Ocultar toolbar de la esquina superior derecha */
        div[data-testid="stToolbar"] {
            display: none !important;
        }
    </style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

hide_streamlit_elements = """
    <style>

        /* Ocultar la barra superior (Share, GitHub, Options) */
        header[data-testid="stHeader"] {
            display: none !important;
        }
        div[data-testid="stToolbar"] {
            display: none !important;
        }

        /* OCULTAR EL BOTÓN "Manage app" */
        /* Este botón vive en un shadow-root, pero Streamlit lo expone por este selector */
        iframe[src*="streamlit.io/cloud"] {
            display: none !important;
            visibility: hidden !important;
        }

        /* Este selector adicional cubre variaciones y futuros cambios */
        div[data-testid="stAppViewContainer"] + div {
            display: none !important;
            visibility: hidden !important;
            height: 0 !important;
        }

        /* Algunas versiones lo exponen como un widget */
        div[data-testid="ManageAppButton"] {
            display: none !important;
        }
        button[data-testid="manage-app-button"] {
            display: none !important;
        }

        /* Asegurar eliminación total */
        [title="Manage app"] {
            display: none !important;
            visibility: hidden !important;
        }

        /* Opcional: ocultar footer residual */
        footer {
            visibility: hidden !important;
            height: 0 !important;
        }

    </style>
"""
import streamlit as st
st.markdown(hide_streamlit_elements, unsafe_allow_html=True)




