import streamlit as st
from st_default_width import set_use_container_width_default


def main():
    st.header("`st_default_width`", divider="rainbow")
    st.markdown("**Examples:**")

    with st.sidebar:
        st.markdown("Set `use_container_width` to a default value for all elements")

    with st.echo():
        set_use_container_width_default()

        cols = st.columns([1, 2])
        with cols[0]:
            st.image("https://placehold.co/50x50")
            st.button("A button :)")

        with cols[1]:
            st.image("https://placehold.co/100x50")
            st.button("A button :D")

    st.divider()

    with st.echo():
        set_use_container_width_default(False)

        cols = st.columns([1, 2])
        with cols[0]:
            st.image("https://placehold.co/50x50")
            st.button("A button :()")

        with cols[1]:
            st.image("https://placehold.co/100x50")
            st.button("A button :S")


if __name__ == "__main__":
    st.set_page_config(page_title="`st_default_width", page_icon="↔️")

    intro_page = st.Page(main, title="Basic Example", icon="↔️", default=True)

    interactive_page = st.Page(
        "app_pages/interactive.py", title="Interactive", icon="🕹️"
    )

    pg = st.navigation([intro_page, interactive_page])
    pg.run()
