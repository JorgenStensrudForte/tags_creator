import streamlit as st
import pandas as pd
import numpy as np
import time
import os
import json


# import ipynb.fs
from python_functions import tags_list_test, tags_list, tags_list_gpt4

# from .defs.usage_app_tags import tags_dict

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
#     </style>r
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


df2_gpt4 = pd.read_csv("data/df_tags_splitted_30_11.csv")
runar_tags = pd.read_csv("data/tags_runar_01_12_splitted.csv")

filter_30_11 = pd.read_excel("filter_tags.xlsx")
filter_runar = pd.read_csv("data/filter_tags - RAO.csv")

grouped_df = pd.read_csv("data/tags_30_11.csv")
grouped_df_runar = pd.read_csv("data/tags_runar_01_12_grouped.csv")
# splitted_tags_runar = pd.read_csv("data/df_tags_splitted_runar.csv")

multiselect_tags = st.selectbox(
    "Select csv file",
    ["Tags list 30.11", "runar tags"],
)
# st.write(tags)
if "splitted" not in st.session_state:
    st.session_state.splitted_tags = df2_gpt4

if "filter_tags" not in st.session_state:
    st.session_state.filter_tags = filter_30_11

if "grouped_tags" not in st.session_state:
    st.session_state.grouped_tags = grouped_df


if multiselect_tags == "Tags list 30.11":
    st.session_state.splitted_tags = df2_gpt4
    st.session_state.filter_tags = filter_30_11
    st.session_state.grouped_tags = grouped_df

elif multiselect_tags == "runar tags":
    st.session_state.splitted_tags = runar_tags
    st.session_state.filter_tags = filter_runar
    st.session_state.grouped_tags = grouped_df_runar


def get_filter_to_list(df):
    product_type_list = [
        item.strip()
        for sublist in st.session_state.filter_tags["product type"].tolist()
        for item in sublist.split(",")
    ]
    technology_list = [
        item.strip()
        for sublist in st.session_state.filter_tags["technology"].tolist()
        for item in sublist.split(",")
    ]
    applications_list = [
        item.strip()
        for sublist in st.session_state.filter_tags["application"].tolist()
        for item in sublist.split(",")
    ]

    # Concatenate the lists
    filter_tags_list = product_type_list + technology_list + applications_list
    return filter_tags_list


# Display the DataFrame
def flatten(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten(i))
        else:
            result.append(i)
    return result


def get_filter_data(df, tags_df, tags_list=[]):
    # Convert tags_df to a DataFrame if it's not already one
    if not isinstance(tags_df, pd.DataFrame):
        tags_df = pd.DataFrame(tags_df)

    # Get unique categories, split on comma, flatten list, remove whitespace, and remove duplicates
    categories = list(
        [
            category.strip()
            for sublist in df["Product category"].dropna().unique().tolist()
            for category in sublist.split(",")
        ]
    )

    # Initialize new_tags_dict
    new_tags_dict = {}

    for category in categories:
        if category in tags_df["category"].values:
            category_row = tags_df[tags_df["category"] == category]
            category_dict = {}
            for high_level_tag in ["product type", "technology", "application"]:
                low_level_tags = category_row[high_level_tag].values[0]
                if isinstance(low_level_tags, str):
                    low_level_tags = low_level_tags.split(",")

                # Flatten the list regardless of how deeply nested it is
                flat_low_level_tags = flatten(low_level_tags)

                # Remove duplicates while preserving order
                unique_low_level_tags = list(dict.fromkeys(flat_low_level_tags))

                # Remove tags that are in tags_list
                unique_low_level_tags = [
                    tag for tag in unique_low_level_tags if tag not in tags_list
                ]

                category_dict[high_level_tag] = unique_low_level_tags
            new_tags_dict[category] = category_dict
    # Return statement is outside the for loop
    return categories, new_tags_dict


categories, tags = get_filter_data(
    st.session_state.splitted_tags, st.session_state.filter_tags, []
)
filter_tags_list = get_filter_to_list(st.session_state.filter_tags)

categories = sorted(set(categories))

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

# st.write(st.session_state.filered_df.columns)
with columns2:
    # Filter the DataFrame based on the selected tags
    st.session_state.splitted_tags = st.session_state.splitted_tags[
        st.session_state.splitted_tags["product_tags"].apply(
            lambda x: all(tag.lower() in x.lower() for tag in selected_tags)
            if isinstance(x, str)
            else False
        )
        & st.session_state.splitted_tags["Product category"].apply(
            lambda x: selected_category.lower() in x.lower()
            if isinstance(x, str)
            else False
        )
    ]
    # If the 'select software' checkbox is checked, filter the DataFrame based on the 'is_software' column
    if select_software == "Software":
        st.session_state.splitted_tags = st.session_state.splitted_tags[
            st.session_state.splitted_tags["is_software"] == True
        ]
    elif select_software == "Hardware":
        st.session_state.filered_df = st.session_state.splitted_tags[
            st.session_state.splitted_tags["is_software"] == False
        ]
    else:
        st.session_state.splitted_tags = st.session_state.splitted_tags

    if show_all:
        st.session_state.splitted_tags = df2_gpt4

    # Display the filtered DataFrame
    cols = st.columns(3)

    # Iterate over the filtered DataFrame
    for i, row in enumerate(st.session_state.splitted_tags.itertuples()):
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
        # Display the product tags as a multiselect component

        if isinstance(row.product_tags, str):
            product_tags = row.product_tags.split(",")
            product_tags = [
                tag.strip() for tag in product_tags if tag.strip() in filter_tags_list
            ]

            # multi_select_tags = col.multiselect(
            #     "Product Tags",
            #     options=filter_tags_list,
            #     default=product_tags,
            #     key=row.Product_Name,
            # )

            # # If a tag is removed from the multiselect, update the DataFrame
            # if set(multi_select_tags) != set(product_tags):
            #     # Update the 'product_tags' column in the DataFrame
            #     st.session_state.splitted_tags.loc[
            #         st.session_state.splitted_tags["Product_Name"] == row.Product_Name,
            #         "product_tags",
            #     ] = ",".join(multi_select_tags)

# Convert the 'filter_tags' DataFrame columns to lists and split each string on comma


# Get the unique product names from the filtered DataFrame
filtered_product_names = st.session_state.splitted_tags["Product_Name"].unique()

# Filter the other DataFrame to only include rows where 'Product_Name' is in filtered_product_names
df_other_filtered = st.session_state.grouped_tags[
    st.session_state.grouped_tags["Product_Name"].isin(filtered_product_names)
]

# Display the filtered DataFrame
st.dataframe(df_other_filtered)

# Filter df2_gpt4 to only include rows where 'Product' is in unique_products
# st.data_editor(
#     st.session_state.filered_df[
#         ["Product_Name", "Product category", "product_tags", "url", "is_software"]
#     ],
#     column_config={
#         "url": st.column_config.LinkColumn("website url"),
#     },
#     height=1000,
# )

print(len(st.session_state.splitted_tags))
print(len(df_other_filtered))

# Initialize the session state variable if it doesn't exist
if "button_pressed" not in st.session_state:
    st.session_state.button_pressed = False

if st.button("show_category_tags:"):
    # Toggle the session state variable
    st.session_state.button_pressed = not st.session_state.button_pressed

# Display st.session_state.filter_tags if the button has been pressed an odd number of times
if st.session_state.button_pressed:
    st.write(st.session_state.filter_tags)
