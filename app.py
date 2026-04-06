import streamlit as st
col1 , col2, col3 = st.columns([1,8,1])   #Each st.columns() = new row,,Each st.columns() = new row,, Each st.columns() = new row
with col2:
    st.title("Contract change analyzer")
    st.write("*Upload two contract versions to analyze and highlight differences efficiently.*")
file1 = st.file_uploader("Upload OLD contract", type=["txt"])
file2 = st.file_uploader("Upload NEW contract", type=["txt"])
col1 , col2, col3 = st.columns([1,1,1])
with col2:
    clicked = st.button("Analyze Changes")
if clicked:     
    if file1 and file2:
        old_file = file1.read().decode("utf-8")
        new_file = file2.read().decode("utf-8")
        lines1 = old_file.split(".")
        lines2 = new_file.split(".")
        colA, colB, colC = st.columns([1,0.5,1])
        with colA:
            st.subheader("OLD Contract", divider=True)
        with colC:
            st.subheader("NEW Contract", divider=True)
        
        for line1, line2 in zip(lines1, lines2):
            if line1.strip() != line2.strip():
                with colA:
                    st.markdown(f"<span style='color: red;'>{line1}</span>", unsafe_allow_html=True)
                with colC:
                    st.markdown(f"<span style='color: green;'>{line2}</span>", unsafe_allow_html=True)
            else:
                with colA:
                    st.write(line1.strip())
                with colC:
                    st.write(line2.strip())
        if len(lines2) > len(lines1):
            for i in range(len(lines1), len(lines2)):
                with colA:
                    st.write("")   # empty placeholder
                with colC:
                    st.markdown(f"<span style='color:green'>{lines2[i]}</span>", unsafe_allow_html=True)
        if len(lines1) > len(lines2):
            for i in range(len(lines2), len(lines1)):
                with colA:
                    st.markdown(f"<span style='color:red'>{lines1[i]}</span>", unsafe_allow_html=True)
                with colC:
                    st.write("")
    else:
        st.error("Please upload both contract versions to analyze changes.")
