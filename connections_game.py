import streamlit as st
import random

# Define your categories and words
categories = {
    "Risk-Taking": ["Chutzpah", "Boldness", "Audacity", "Risk"],
    "Academics": ["Technion", "University", "STEM", "Research"],
    "Military": ["Military", "Unit", "Skills", "Problem-Solving"],
    "Innovation": ["Grants", "Funding", "Authority", "Cooperation"]
}

# Initialize session state variables
if 'selected_words' not in st.session_state:
    st.session_state.selected_words = []
if 'found_categories' not in st.session_state:
    st.session_state.found_categories = set()

# Create a list of all words and shuffle them
words = [word for category in categories.values() for word in category]
random.shuffle(words)

# Function to check if a selected group matches any category
def check_group(selected_words, categories):
    for category, group_words in categories.items():
        if sorted(selected_words) == sorted(group_words):
            return category
    return None

# Streamlit UI setup
st.title("Connections Game")
st.write("Select 4 words that belong to the same category.")

# Layout for displaying the word buttons
cols = st.columns(4)  # Create a grid of 4 columns
for i, word in enumerate(words):
    with cols[i % 4]:  # Ensure words are distributed evenly across columns
        if st.button(word):
            if word not in st.session_state.selected_words:
                st.session_state.selected_words.append(word)

# Display the selected words
st.write("Selected Words:", st.session_state.selected_words)

# Allow the user to submit their guess when 4 words are selected
if len(st.session_state.selected_words) == 4:
    category = check_group(st.session_state.selected_words, categories)

    if category and category not in st.session_state.found_categories:
        st.success(f"Correct! These words belong to the '{category}' category.")
        st.session_state.found_categories.add(category)
    else:
        st.error("Incorrect group. Try again!")

    # Reset selected words after checking
    st.session_state.selected_words = []

# Check if the game is finished
if len(st.session_state.found_categories) == len(categories):
    st.balloons()
    st.write("Congratulations! You've found all the groups!")
