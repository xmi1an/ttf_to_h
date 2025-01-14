import streamlit as st
import os


def generate_header_file(ttf_data):
    size = len(ttf_data)
    array_data = []

    for i in range(0, size, 4):
        chunk = ttf_data[i : i + 4]
        if len(chunk) < 4:
            chunk = chunk.ljust(4, b"\0")
        hex_value = int.from_bytes(chunk, byteorder="little", signed=False)
        array_data.append(hex_value)

    header_lines = []
    header_lines.append(f"// Generated header file\n")
    header_lines.append(f"// Join Telegram for More : https://t.me/zyrusmods\n\n")

    header_lines.append(f"static const unsigned int myfont_size = {size};\n")
    header_lines.append(f"static const unsigned int myfont_data[{size}/4] = {{\n")

    for i in range(0, len(array_data), 8):
        line_data = ", ".join(f"0x{val:08x}" for val in array_data[i : i + 8])
        header_lines.append(f"    {line_data},\n")

    header_lines.append("};\n")

    # display success message to user
    st.info(
        "Data Variable name is :orange[`myfont_data`] and \n Size Variable name is :orange[`myfont_size`]"
    )
    st.toast("Header file generated successfully!")

    return "".join(header_lines)


def main():
    st.title("TTF to Header File Converter")
    st.subheader("Convert TTF file to Header (.h)")

    st.markdown(
        "Join Telegram for More : <a href='https://t.me/zyrusmods' target='_blank'>https://t.me/zyrusmods</a>",
        unsafe_allow_html=True,
    )

    # Upload the TTF file
    ttf_file = st.file_uploader("Upload TTF file", type=["ttf"])

    if ttf_file:
        file_name = os.path.splitext(ttf_file.name)[0]  # remove .ttf extension
        ttf_data = ttf_file.read()
        header_content = generate_header_file(ttf_data)

        # Offer download of the header file
        st.download_button(
            "Download Header File", header_content, file_name=f"{file_name}.h"
        )


if __name__ == "__main__":
    main()
