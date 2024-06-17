# Geeta GPT
GEETA GPT is an advanced AI application built using Retrieval-Augmented Generation (RAG). It leverages the powerful capabilities of the Large Language Models to provide insightful and accurate responses based on the rich content of the Bhagavad Gita.

Large language models (LLMs) are like students who excel at imitating what they're taught. Their training data is their textbook, and they become very good at following the patterns they see there. However, this can limit their understanding. They can't truly reason or apply knowledge outside of what they've been exposed to.

That's why we're using techniques like Retrieval-Augmented Generation (RAG) to expand their knowledge. It's like giving them access to a giant library! RAG lets LLMs consult external documents when responding,  helping them ground their answers in real-world information and reducing made-up facts.

## Pipeline
![Pipeline image](/images/pipeline.png "This is a pipeline image.")

## Demo 
![Demo of GEETA GPT](/images/Geeta_gpt_demo.gif "This is a Demo of app.")

## Getting Started
1. Clone the Repository
```
git clone https://github.com/rushidarge/Geeta-GPT.git
cd Geeta-GPT
```
2. Install Dependencies
```
pip install -r requirements.txt
```
3. Add API key in app.py file at
You need a Gemini API key, that is freely available. Get yours by clicking [here](https://aistudio.google.com/app/apikey).
```
os.environ["GOOGLE_API_KEY"] = "Your API key"
```
4. Run the Application
```
streamlit run app.py
```

## Usage
- Ask Questions: Type your questions about the Bhagavad Gita and receive insightful responses.
- Explore Teachings: Delve deeper into specific teachings and verses of the Gita.
- Personal Guidance: Use the app for personal reflection and guidance based on the Gita's wisdom.

## Limitations
Retrieval-Augmented Generation (RAG) applications, while powerful,  have some limitations
- Limited Reasoning: RAG struggles with iterative reasoning. It retrieves information based on similarity but can't assess if it's truly relevant to the task.
- Scalability Issues:  Large datasets can overwhelm RAG's retrieval methods, especially with techniques like K-Nearest Neighbors (KNN).
- Data Dependence:  The quality of retrieved information directly impacts RAG's output. Biases or inaccuracies in the data can lead to unreliable responses.
- Challenges with Large Datasets:  Storing and processing massive datasets can be difficult for RAG, impacting retrieval speed and accuracy.

## Future Scope
GEETA GPT's <b>capabilities are not limited to the Bhagavad Gita</b>. The architecture can be extended to work with any text-based document or PDF, opening up a range of possibilities:

1. Expand to Other Religious Texts: Adapt the system to provide insights from other religious or philosophical texts.
2. Academic Papers: Assist in understanding and summarizing academic papers or research documents.
3. Technical Manuals: Provide support for technical documentation and manuals, making it easier to find specific information.
4. Legal Documents: Enhance the understanding and accessibility of legal texts and contracts.

License
This project is licensed under the MIT License - see the LICENSE file for details.

## Bibliography
- LLM Model : https://gemini.google.com/
- Tutorials: https://medium.com/

