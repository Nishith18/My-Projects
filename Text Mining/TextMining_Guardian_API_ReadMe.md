Project Name: Right-Wing News Analysis
Description: This project analyses the representation of right-wing politics in news 
articles from the United States and India, focusing on the period after January 1, 
2020. Data is fetched from the Guardian API and categorized into five main topics: 
policy, violence, COVID-19, religion, and politics. The project compares the 
distribution of these topics across the two countries.

Business Question:
To understand how different categories regarding right-wing politics in the United 
States and India are being represented in the UK Guardian articles after January 1, 
2020.

Methodology:
1. Fetch news articles from the Guardian API using Python.
2. Extract relevant text from the articles.
3. Tokenize the text into individual words and phrases.
4. Classify each token into one of the five main topics.
5. Calculate the percentage of tokens in each topic for each country.
6. Compare the distribution of topics across the two countries.

Key Findings:
• The United States focuses more on policy and politics, while India focuses more 
on religion and COVID-19.
• The biggest difference is in COVID-related tokens, with India having more than 
double the percentage of such tokens compared to the US.
• Another large difference is religion, with India having significantly more religion-related tokens than the US.
• For the category of violence, the two countries are more closely aligned.

Recommendations:
• Perform further analysis to control for the larger article count in the US.
• Investigate the reasons for the observed differences in topic distribution.
• Analyze the relationship between certain topics and the prevalence of 
right-wing sentiment in the articles.

Technical Notes:
• The project uses the following Python libraries:
o requests: For fetching data from the Guardian API
o pandas: For data manipulation and analysis
• The project also utilizes the NLTK (Natural Language Toolkit) for additional text-processing tasks.

Data Sources:
• Guardian API: https://open-platform.theguardian.com/
• NLTK: https://www.nltk.org/
