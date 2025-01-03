import streamlit as st
from PIL import Image

# Set page configuration
st.set_page_config(page_title="News Blog", page_icon="📰", layout="centered")

# News Blog Content
st.title("📰 Daily News Blog")
st.write("""
Welcome to the **Daily News Blog**, your go-to source for the latest updates around the world. 
Stay informed with our curated news articles covering technology, business, sports, and entertainment.
""")

# Example News Articles
st.subheader("🔍 Tech News")
st.write("""
- **AI Revolution in 2025:** A deep dive into how AI is reshaping industries globally. [Read more](https://example.com).
- **Quantum Computing Breakthrough:** Researchers achieve a major milestone in quantum error correction. [Read more](https://example.com).
- **Next-Gen Smartphones:** What to expect from the upcoming releases of flagship devices. [Read more](https://example.com).
- **Space Tech Advancements:** Private companies push the boundaries of space exploration in 2025. [Read more](https://example.com).
- **5G Expansion:** How global infrastructure upgrades are accelerating connectivity. [Read more](https://example.com).
- **Green Tech Innovations:** Exploring sustainable technologies and their impact on reducing carbon footprints. [Read more](https://example.com).
- **Cybersecurity Trends:** Top strategies to safeguard against evolving cyber threats. [Read more](https://bloggers.streamlit.app/).
- **Augmented Reality Boom:** How AR is transforming industries like retail, gaming, and healthcare. [Read more](https://example.com).
- **Edge Computing Revolution:** Bringing computing closer to the data source for faster and efficient processing. [Read more](https://example.com).
- **The Future of Biotech:** Integrating AI and biotechnology for revolutionary healthcare solutions. [Read more](https://example.com).
""")

st.subheader("💼 Business News")
st.write("""
- **Stock Markets Surge:** Key indices hit record highs as investor confidence grows. [Read more](https://example.com).
- **Startup Spotlight:** A rising fintech disruptor secures $50M in Series B funding. [Read more](https://example.com).
- **Global Trade Dynamics:** The latest on trade negotiations between major economies and their impact on industries worldwide. [Read more](https://example.com).
- **Corporate Layoffs:** Tech giants announce strategic layoffs amidst economic uncertainty. [Read more](https://example.com).
- **ESG Investments Rise:** Environmentally sustainable businesses are attracting record levels of capital from global investors. [Read more](https://example.com).
- **Cryptocurrency Regulation:** Governments debate new policies to regulate the growing crypto market and its volatility. [Read more](https://example.com).
- **Real Estate Trends:** Urban areas see an uptick in commercial real estate investments as remote work evolves. [Read more](https://example.com).
- **Consumer Spending Report:** Retailers report a surge in holiday season spending, indicating strong consumer confidence. [Read more](https://example.com).
""")

st.subheader("🎭 Entertainment News")
st.write("""
- **Award Season Buzz:** Predictions for the top contenders in the upcoming film awards. [Read more](https://example.com).
- **Streaming Wars:** New platform announces aggressive content acquisition strategy. [Read more](https://example.com).
- **Blockbuster Returns:** A popular movie franchise is making a comeback with its next installment set to release in 2025. [Read more](https://example.com).
- **Music Industry Trends:** The rise of AI-generated music and its impact on traditional artists. [Read more](https://example.com).
- **Broadway Revival:** A classic musical gets a modern twist in its much-anticipated stage comeback. [Read more](https://example.com).
- **Celebrity Spotlight:** An exclusive interview with a renowned actor on their new humanitarian project. [Read more](https://example.com).
- **Oscars Controversy:** Behind the scenes of the latest debates surrounding award show nominations. [Read more](https://example.com).
- **Global Cinema:** A deep dive into how international films are dominating the box office in 2025. [Read more](https://example.com).
""")

# Add a divider before footer
st.divider()

# Footer with social media icons
st.write("## 📱 Connect with Us")

# Load icons (ensure you have these images in the same directory as the script or provide URLs)
youtube_icon = Image.open("download (5).png")  # Replace with the path to your YouTube icon
twitter_icon = Image.open("download (6).png")  # Replace with the path to your Twitter icon
insta_icon = Image.open("download.jpg")  # Replace with the path to your Instagram icon
linkedin_icon = Image.open("download (7).png")  # Replace with the path to your LinkedIn icon

# Display clickable icons in columns
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image(youtube_icon, width=50)
    st.markdown("[YouTube](https://youtube.com)", unsafe_allow_html=True)

with col2:
    st.image(twitter_icon, width=50)
    st.markdown("[Twitter](https://twitter.com)", unsafe_allow_html=True)

with col3:
    st.image(insta_icon, width=50)
    st.markdown("[Instagram](https://instagram.com)", unsafe_allow_html=True)

with col4:
    st.image(linkedin_icon, width=50)
    st.markdown("[LinkedIn](https://linkedin.com)", unsafe_allow_html=True)

st.divider()
st.write("© 2025 Daily News Blog. All rights reserved.")

