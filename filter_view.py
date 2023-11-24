import streamlit as st
import pandas as pd
import numpy as np
import time
import os

from python_functions import tags_list_test, tags_list, tags_list_gpt4

print("")
# streamlit config
st.set_page_config(
    page_title="Filter View",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
)
# st.markdown(
#     """
#     <style>
#     .main {
#         width: 50% !important;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# if st.button("redo"):
#     # read excel file
#     df_new = pd.read_excel("data/tags_gpt4.xlsx")
#     # save as csv
#     df_new.to_csv("data/tags_gpt4.csv", index=False, encoding="utf-8")
st.title("Filter View")
# update tags list
new_columns, new_columns2 = st.columns([1, 3])

df2_gpt4 = pd.read_csv("data/df_tags_use_app_22_11_issoftware2.csv")
# file_select = st.selectbox(
#     "Select file", ["df_tags_use_app_22_11_issoftware", "tags_gpt4_issoftware"]
# )
# # df2_test = pd.read_csv("data/good_data/df_tags_use_app_15_11_test.csv")
# # df2_gpt4 = pd.read_csv("data/tags_gpt4_issoftware.csv")
# # df2_gpt4 = pd.read_csv("data/df_tags_use_app_22_11_issoftware.csv")
# # df2_gpt4 = pd.read_csv("data/good_data/tags_gpt4.csv")
# if file_select == "df_tags_use_app_22_11_issoftware":
#     df2_gpt4 = pd.read_csv("data/df_tags_use_app_22_11_issoftware.csv")
# if file_select == "tags_gpt4_issoftware":
#     df2_gpt4 = pd.read_csv("data/tags_gpt4_issoftware.csv")


# Display the DataFrame
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result


# get filter_data
@st.cache_data
def get_filter_data(df, tags_list=[]):
    # Get unique categories, split on comma, flatten list, remove whitespace, and remove duplicates
    categories = list(
        set(
            [
                category.strip()
                for sublist in df["Product category"].dropna().unique().tolist()
                for category in sublist.split(",")
            ]
        )
    )

    # change the and with &
    import ast

    tags_dict = {}
    for category in categories:
        tags = df[df["Product category"] == category]["filter_tags"].dropna().tolist()

        category_dict = {}
        for tag_str in tags:
            if pd.notna(tag_str):
                # Add { and } if they're not present
                if not tag_str.startswith("{"):
                    tag_str = "{" + tag_str
                if not tag_str.endswith("}"):
                    tag_str = tag_str + "}"

                try:
                    tag_dict = ast.literal_eval(tag_str)
                except SyntaxError:
                    print(f"SyntaxError for string: {tag_str}")
                    continue
            for high_level_tag, low_level_tags_str in tag_dict.items():
                if isinstance(low_level_tags_str, list):
                    low_level_tags = low_level_tags_str
                else:
                    if isinstance(low_level_tags_str, str):
                        low_level_tags = low_level_tags_str.split(",")
                    else:
                        low_level_tags = ast.literal_eval(low_level_tags_str)

                # Flatten the list regardless of how deeply nested it is
                flat_low_level_tags = flatten(low_level_tags)

                # Convert the flattened list to a set to remove duplicates
                unique_low_level_tags = list(set(flat_low_level_tags))

                # Remove tags that are in tags_list
                unique_low_level_tags = [
                    tag for tag in unique_low_level_tags if tag not in tags_list
                ]

                category_dict[high_level_tag] = unique_low_level_tags
            tags_dict[category] = category_dict

    # Return statement is outside the for loop
    return categories, tags_dict


categories, tags = get_filter_data(df2_gpt4, [])
# st.write(tags.keys())
if "filered_df" not in st.session_state:
    st.session_state.filered_df = df2_gpt4

columns1, columns2 = st.columns([1, 4])
with columns1:
    selected_category = st.selectbox("Select a category", categories)
    selected_tags = []
    # Check if the selected_category exists in the tags dictionary
    if selected_category in tags:
        for high_level_tag in tags[selected_category]:
            with st.expander(high_level_tag):
                for low_level_tag in tags[selected_category][high_level_tag]:
                    if st.checkbox(
                        low_level_tag,
                        key=selected_category + high_level_tag + low_level_tag,
                    ):
                        selected_tags.append(low_level_tag)
    select_software = st.selectbox(
        "Software/Hardware Selector", ["All", "Software", "Hardware"]
    )
    show_all = st.checkbox("Show all")


with columns2:
    # Filter the DataFrame based on the selected tags
    st.session_state.filered_df = df2_gpt4[
        df2_gpt4["product_tags"].apply(
            lambda x: all(tag in x for tag in selected_tags)
            if isinstance(x, (list, str))
            else False
        )
        & df2_gpt4["Product category"].apply(
            lambda x: selected_category in x if isinstance(x, str) else False
        )
    ]
    # If the 'select software' checkbox is checked, filter the DataFrame based on the 'is_software' column
    if select_software == "Software":
        st.session_state.filered_df = st.session_state.filered_df[
            st.session_state.filered_df["is_software"] == "True"
        ]
    elif select_software == "Hardware":
        st.session_state.filered_df = st.session_state.filered_df[
            st.session_state.filered_df["is_software"] == "False"
        ]
    else:
        st.session_state.filered_df = st.session_state.filered_df

    if show_all:
        st.session_state.filered_df = df2_gpt4

    # Display the filtered DataFrame
    cols = st.columns(3)
    # Iterate over the filtered DataFrame
    for i, row in enumerate(st.session_state.filered_df.itertuples()):
        # Get the column to display the image in
        col = cols[i % 3]

        # Display the image
        # col.image(row.image_url, use_column_width=True)
        col.markdown(
            f'<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; border: 1px solid #ddd; padding: 10px; margin: 10px; width: 250px; height: 175px; overflow: hidden;">'
            f'<img src="{row.image_url}" style="max-width: 100%; max-height: 50%; object-fit: cover;"/>'
            f'<h5 style="margin-top: 10px; text-align: center; word-wrap: break-word;">{row.Product_Name}</h5>'
            f'<a href="{row.url}" target="_blank" style="text-align: center;">Go to site</a>'
            f"</div>",
            unsafe_allow_html=True,
        )

# Get the unique products in filtered_df

# Filter df2_gpt4 to only include rows where 'Product' is in unique_products
st.data_editor(
    st.session_state.filered_df,
    column_config={
        "url": st.column_config.LinkColumn("website url"),
    },
    height=1000,
)

# if "delete_list" not in st.session_state:
#     st.session_state.delete_list = []

# delete_button = new_columns2.button("Delete selcted tags")
# new_columns2.write(selected_tags)
# if delete_button:
#     for tag in selected_tags:
#         st.session_state.delete_list.append(tag)


# new_columns2.write(st.session_state.delete_list)
# filtered_df = filtered_df[["Product_Name", "Product category", "product_tags"]]
# st.dataframe(
#     filtered_df,
#     column_config={"image_url": st.column_config.ImageColumn("Preview", width="large")},
# )
# if st.button("delete from csv"):
#     # Check if delete_list exists in the session state
#     if "delete_list" in st.session_state:
#         # Iterate over the tags in delete_list
#         for tag in st.session_state.delete_list:
#             # Update the DataFrame to exclude rows where the "filter_tags" column contains the tag
#             df2_gpt4 = df2_gpt4[
#                 ~df2_gpt4["filter_tags"].apply(
#                     lambda x: tag in x.values() if isinstance(x, dict) else False
#                 )
#             ]

#     # Write the updated DataFrame back to the CSV file
#     df2_gpt4.to_csv("data/good_data/tags_gpt4.csv", index=False, encoding="utf-8")

# # Redo:
