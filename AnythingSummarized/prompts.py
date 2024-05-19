# prompts.py
PROMPTS = {
    "summary": """
    Objective: Summarize the provided text in about {max_words} words, focusing on the core information and actionable insights.
    Use bullets or headings wherever needed.
    
    Instructions:
    Key Points Identification:
    List the main themes and important messages.
    
    Summary Creation:
    Construct a summary under appropriate headings reflecting the text's structure.
    
    Action Items:
    Clearly list any recommendations or steps to be taken as highlighted in the text.
    
    Editing:
    Ensure the summary is clear and concise, within the specified word count.
    
    Format:
    Use headings to organize the summary into sections.
    Keep each section focused and succinct.
    """
    ,
    "news_article": """
    Objective: Summarize the news article, focusing on the key events, quotes, and conclusions. Use concise bullet points for readability.

    Instructions:
    1. Identify the main events and key messages.
    2. Highlight important quotes and statements.
    3. Summarize the conclusions and implications.

    Format:
    ### Main Events
    - Key event 1: Details
    - Key event 2: Details

    ### Quotes
    - "Important quote" - Speaker

    ### Conclusion
    - Summary of conclusions and implications
    """
    ,
    "scientific_journal": """
    Objective: Provide a detailed summary of the scientific journal article, including key findings, methodology, results, and discussions.

    Instructions:
    1. Summarize the abstract and introduction.
    2. Outline the methodology and experiments conducted.
    3. Highlight the key results and discussions.
    4. Summarize the conclusions and future directions.

    Format:
    ### Abstract
    - Brief summary of the abstract.

    ### Introduction
    - Main points from the introduction.

    ### Methodology
    - Description of the methods and experiments.

    ### Results
    - Key results and findings.

    ### Discussions
    - Important discussions and interpretations.

    ### Conclusions
    - Summary of the conclusions and future directions.
    """,
    
    "youtube_video": """
    Objective: Summarize the provided YouTube video, focusing on key points and actionable insights. Include important timestamps and use icons to highlight sections.
    
    Instructions:
    1. Identify the main themes and key messages.
    2. Note important timestamps with brief descriptions.
    3. Use bullet points and icons to enhance readability.

    Format:
    - 🕒 **[00:00] Introduction**: Brief description
    - 🕒 **[02:15] Main Topic 1**: Key points
    - 🕒 **[05:30] Example**: Explanation with key details
    - 🕒 **[10:45] Conclusion**: Summary and final thoughts
    """,
    "arxiv_paper": """
    Objective: Provide a detailed summary of the arXiv paper, including key findings, methodology, results, and conclusions. Use section headings for clarity.
    
    Instructions:
    1. Summarize the abstract and introduction.
    2. Outline the methodology and experiments conducted.
    3. Highlight the key results and findings.
    4. Summarize the conclusions and potential implications.

    Format:
    ### Abstract
    - Brief summary of the abstract.

    ### Introduction
    - Main points from the introduction.

    ### Methodology
    - Description of the methods and experiments.

    ### Results
    - Key results and findings.

    ### Conclusions
    - Summary of the conclusions and implications.
    """,
    "pdf_document": """
    Objective: Summarize the provided PDF document, focusing on the main points, findings, and conclusions. Use structured headings and bullet points.

    Instructions:
    1. Identify and summarize the main sections.
    2. Highlight key findings and conclusions.
    3. Use bullet points for important details.

    Format:
    ### Section 1: Title
    - Key points and details

    ### Section 2: Title
    - Key points and details

    ### Conclusion
    - Summary of main findings and conclusions
    """,
}
