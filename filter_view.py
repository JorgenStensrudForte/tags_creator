import streamlit as st
import pandas as pd
import numpy as np
import time
import os

from python_functions import tags_list_test, tags_list, tags_list_gpt4


# streamlit config
st.set_page_config(
    page_title="Filter View",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# if st.button("redo"):
#     # read excel file
#     df_new = pd.read_excel("data/tags_gpt4.xlsx")
#     # save as csv
#     df_new.to_csv("data/tags_gpt4.csv", index=False, encoding="utf-8")
st.title("Filter View")
# update tags list
new_columns, new_columns2 = st.columns([1, 3])


# df = pd.read_csv("data/good_data/df_tech_new_tags_test.csv")
# df = pd.read_csv("data/df_tags_technology_15_11.csv")

# df2_test = pd.read_csv("data/good_data/df_tags_use_app_15_11_test.csv")
df2_gpt4 = pd.read_csv("data/tags_gpt4.csv")
# df2_gpt4 = pd.read_csv("data/good_data/tags_gpt4.csv")
# df2 = pd.read_csv("data/df_tags_use_app_15_11.csv")
# remove any rows with NaN values

# st.dataframe(df2.head(10))
# df2_tags = df2[["Product_Name", "product_tags"]]


# # Merge the two DataFrames on "Product_Name"
# merged_df = pd.merge(df, df2_tags, on="Product_Name", suffixes=("_df", "_df2"))

# # Combine 'tags_df' and 'tags_df2' into one column
# merged_df["tags_combined"] = (
#     merged_df["tags_df"].astype(str) + ", " + merged_df["tags_df2"].astype(str)
# )
# st.write(df2.head(10))


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

# df = pd.read_csv("data/df_tech_new_tags_test.csv")


# st.write(tags)
# make a filter view in col1 and product view in col2
# Create a selectbox for the categories
import streamlit as st
import imgkit

columns1, columns2 = st.columns([1, 3])
# with columns1:
#     selected_category = st.selectbox("Select a category", categories)

#     selected_tags = []
#     # Check if the selected_category exists in the tags dictionary
#     if selected_category in tags:
#         for high_level_tag in tags[selected_category]:
#             if st.checkbox(high_level_tag, key=selected_category + high_level_tag):
#                 for low_level_tag in tags[selected_category][high_level_tag]:
#                     col1, col2 = st.columns([1, 11])
#                     with col2:
#                         if st.checkbox(
#                             low_level_tag,
#                             key=selected_category + high_level_tag + low_level_tag,
#                         ):
#                             selected_tags.append(low_level_tag)
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

with columns2:
    # Filter the DataFrame based on the selected tags
    filtered_df = df2_gpt4[
        df2_gpt4["product_tags"].apply(
            lambda x: all(tag in x for tag in selected_tags)
            if isinstance(x, (list, str))
            else False
        )
        & (df2_gpt4["Product category"] == selected_category)
    ]
    # Display the filtered DataFrame
    cols = st.columns(3)
    # Iterate over the filtered DataFrame
    for i, row in enumerate(filtered_df.itertuples()):
        # Get the column to display the image in
        col = cols[i % 3]

        # Display the image
        # col.image(row.image_url, use_column_width=True)
        col.markdown(
            f'<div style="display: flex; flex-direction: column; justify-content: center; align-items: center; border: 1px solid #ddd; padding: 10px; margin: 10px; width: 250px; height: 250px; overflow: hidden;">'
            f'<img src="{row.image_url}" style="max-width: 100%; max-height: 50%; object-fit: cover;"/>'
            f'<h4 style="margin-top: 10px; text-align: center; word-wrap: break-word;">{row.Product_Name}</h4>'
            f'<a href="{row.url}" target="_blank" style="text-align: center;">Go to site</a>'
            f"</div>",
            unsafe_allow_html=True,
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
