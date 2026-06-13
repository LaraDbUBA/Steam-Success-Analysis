
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

st.set_page_config(
    page_title="Steam Games Analysis",
    page_icon="🎮",
    layout="wide"
)

st.markdown("""
<style>

.stApp {
    background-color: #171A21;
}

h1, h2, h3, p, div {
    color: white;
}

[data-testid="stSidebar"] {
    background-color: #1B2838;
}

</style>
""", unsafe_allow_html=True)


steam_palette = [
    "#66C0F4",
    "#4B6B88",
    "#2A475E",
    "#1F518E",
    "#5C7E10"
]

data = pd.read_csv(
    "data/processed/steam_dashboard.csv"
)

st.title("Steam Games Analysis")
st.write("What characteristics are associated with success on Steam?")
st.sidebar.image(
    "images/steam_banner.jpg",
    width=90
)
st.sidebar.title("Filters")
selected_year = st.sidebar.slider(
    "Release Year",
    2000,
    2025,
    (2010, 2025)
)


filtered_data = data[
    (data['release_year'] >= selected_year[0]) &
    (data['release_year'] <= selected_year[1])
]

plt.style.use('dark_background')

STEAM_DARK = "#171A21"
STEAM_BLUE = "#1B2838"
STEAM_LIGHT = "#66C0F4"


tab1, tab2, tab3 = st.tabs([
    "📈 Commercial Success",
    "🎮 Engagement",
    "⭐ Player Satisfaction"
])

# --- COMMERCIAL SUCCESS ---
with tab1:
    st.header("Commercial Success")
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "🎮 Games",
        f"{len(filtered_data):,}"
    )

    col2.metric(
        "🏆 Successful Games",
        f"{filtered_data['is_successful'].sum():,}"
    )

    col3.metric(
        "⭐ Success Rate",
        f"{100*filtered_data['is_successful'].mean():.1f}%"
    )
    non_games = [
        'Movie',
        'Web Publishing',
        'Video Production',
        'Audio Production',
        'Game Development',
        'Photo Editing',
        'Animation & Modeling',
        'Design & Illustration',
        'Utilities',
        'Software Training',
        'Education',
        'Accounting'
    ]

    filtered_data['genres_list'] = filtered_data['genres_list'].apply(ast.literal_eval)
    filtered_data['tags_list'] = filtered_data['tags_list'].apply(ast.literal_eval)

    genres_exploded = filtered_data.explode('genres_list')

    genres_exploded = genres_exploded[
        ~genres_exploded['genres_list'].isin(non_games)
    ]
    genre_success = (
        genres_exploded
        .groupby('genres_list')['is_successful']
        .mean()
        .sort_values(ascending=False)
    )

    top_genres = genre_success.head(10)

    fig, ax = plt.subplots(figsize=(10,6))
    fig.patch.set_facecolor(STEAM_DARK)
    ax.set_facecolor(STEAM_BLUE)
    sns.barplot(
        x=top_genres.values,
        y=top_genres.index,
        hue=top_genres.index,
        palette=steam_palette,
        legend=False,
        ax=ax
    )

    ax.set_xlabel("Success Rate")
    ax.set_ylabel("Genre")

    st.pyplot(fig)
    price_success = (
        filtered_data
        .groupby('price_range')['is_successful']
        .mean()
        .reindex(['Free', '0-5', '5-10', '10-20', '20-40', '40-60', '60+'])
    )
    fig, ax = plt.subplots(figsize=(8,5))
    fig.patch.set_facecolor(STEAM_DARK)
    ax.set_facecolor(STEAM_BLUE)
    sns.barplot(
        x=price_success.index,
        y=price_success.values,
        hue=price_success.index,
        palette=steam_palette,
        legend=False,
        ax=ax
    )

    ax.set_title('Success Rate by Price Range')
    ax.set_xlabel('Price Range (USD)')
    ax.set_ylabel('Success Rate')

    st.pyplot(fig)

    language_success = (
        filtered_data
        .groupby('language_group')['is_successful']
        .mean()
        .reindex(['1', '2-5', '6-10', '11-20', '20+'])
    )
    fig, ax = plt.subplots(figsize=(8,5))
    fig.patch.set_facecolor(STEAM_DARK)
    ax.set_facecolor(STEAM_BLUE)
    sns.barplot(
        x=language_success.index,
        y=language_success.values,
        hue=language_success.index,
        palette=steam_palette,
        legend=False,
    )

    ax.set_title('Success Rate by Supported Languages')
    ax.set_xlabel('Number of Supported Languages')
    ax.set_ylabel('Success Rate')

    st.pyplot(fig)

    st.divider()

# --- ENGAGEMENT ---
with tab2:
    st.header("Engagement")
    playtime_data = genres_exploded[
        genres_exploded['average_playtime_forever'] > 0
    ]

    genre_playtime = (
        playtime_data
        .groupby('genres_list')['average_playtime_forever']
        .median()
        .sort_values(ascending=False)
    )

    top_playtime = genre_playtime.head(10)

    fig, ax = plt.subplots(figsize=(10,6))
    fig.patch.set_facecolor(STEAM_DARK)
    ax.set_facecolor(STEAM_BLUE)
    sns.barplot(
        x=top_playtime.values,
        y=top_playtime.index,
        hue=top_playtime.index,
        palette=steam_palette,
        legend=False,
    )

    ax.set_title("Median Playtime by Genre")
    ax.set_xlabel("Median Playtime (minutes)")
    ax.set_ylabel("Genre")

    st.pyplot(fig)

    achievement_playtime = (
        filtered_data[
            filtered_data['average_playtime_forever'] > 0
        ]
        .groupby('achievement_group')
        ['average_playtime_forever']
        .median()
        .reindex(['0','1-10','11-25','26-50','51-100','100+'])
    )

    fig, ax = plt.subplots(figsize=(8,5))
    fig.patch.set_facecolor(STEAM_DARK)
    ax.set_facecolor(STEAM_BLUE)
    sns.barplot(
        x=achievement_playtime.index,
        y=achievement_playtime.values,
    # color="#1b2838",
        palette= steam_palette,
        ax=ax
    )

    ax.set_title("Playtime by Achievement Count")
    ax.set_xlabel("Achievement Group")
    ax.set_ylabel("Median Playtime (minutes)")

    st.pyplot(fig)

    st.divider()
# --- PLAYER SATISFACTION ---
with tab3:
    st.header("Player Satisfaction")
    col1, col2 = st.columns(2)

    col1.metric(
        "Average Weighted Score",
        round(filtered_data['weighted_score'].mean(), 1)
    )

    col2.metric(
        "Games with Reviews",
        (filtered_data['review_count'] >= 100).sum()
    )

    tags_exploded = filtered_data.explode('tags_list')
    tags_exploded = tags_exploded[
        tags_exploded['review_count'] >= 100
    ]
    tag_counts = tags_exploded['tags_list'].value_counts()
    valid_tags = tag_counts[
        tag_counts >= 1000
    ].index
    tag_summary = (
        tags_exploded[
            tags_exploded['tags_list'].isin(valid_tags)
        ]
        .groupby('tags_list')
        .agg(
            avg_score=('weighted_score','mean'),
            count=('tags_list','size')
        )
    )
    best_tags = (
        tag_summary
        .sort_values('avg_score', ascending=False)
        .head(10)
    )
    worst_tags = (
        tag_summary
        .sort_values('avg_score')
        .head(10)
    )
    col1, col2 = st.columns(2)
    with col1:

        fig, ax = plt.subplots(figsize=(8,5))
        fig.patch.set_facecolor(STEAM_DARK)
        ax.set_facecolor(STEAM_BLUE)
        sns.barplot(
            x='avg_score',
            y=best_tags.index,
            data=best_tags,
            palette= steam_palette,
            ax=ax
        )

        ax.set_title("Top Rated Tags")

        st.pyplot(fig)

    with col2:

        fig, ax = plt.subplots(figsize=(8,5))
        fig.patch.set_facecolor(STEAM_DARK)
        ax.set_facecolor(STEAM_BLUE)
        sns.barplot(
            x='avg_score',
            y=worst_tags.index,
            data=worst_tags,
            palette= steam_palette,
            ax=ax
        )

        ax.set_title("Lowest Rated Tags")

        st.pyplot(fig)
    st.divider()
top_games = (
    filtered_data
    .sort_values("owners_midpoint", ascending=False)
    .head(5)
)

st.subheader("Top Steam Games")

cols = st.columns(5)

for col, (_, row) in zip(cols, top_games.iterrows()):
    with col:
        appid = row["appID"]

        image_url = (
            f"https://cdn.cloudflare.steamstatic.com/"
            f"steam/apps/{appid}/header.jpg"
        )

        st.image(image_url)
        st.caption(row["name"])
