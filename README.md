# Implementing Graph RAG with LlamaIndex 

Retrieval-Augmented Generation (RAG) has revolutionized the way we extract information from large datasets. However, traditional RAG approaches have limitations, especially when it comes to understanding summarized semantic concepts or traversing disparate pieces of information. To address these limitations, we can integrate Knowledge Graphs with RAG, creating a more robust solution known as Graph RAG. This article will guide you through the process of creating a Knowledge Graph and implementing Graph RAG using LlamaIndex. 

## Understanding the Limitations of Baseline RAG 

Baseline RAG primarily uses vector similarity as the search technique. While effective in many scenarios, it falls short in certain areas: 

1. Connecting Disparate Information: Baseline RAG struggles to synthesize new insights from disparate pieces of information.
2. Holistic Understanding: It performs poorly when tasked with understanding summarized semantic concepts over large data collections or singular large documents.

**Example** 

For queries like “What are the top 5 themes in the data?”, traditional RAG relies on vector search of semantically similar text content. This approach lacks the capability to direct the query to the correct information, resulting in poor performance. 

## Introducing Graph RAG 

Graph RAG leverages Knowledge Graphs to enhance the RAG process. A Knowledge Graph is a structured representation of information that highlights relationships between different entities within a dataset. It uses nodes to represent entities and edges to represent relationships. 

  

### Benefits of Graph RAG 

Structured Insights: The structure of the knowledge graph provides insights into the overall dataset. 

Enhanced Query Understanding: It allows for better understanding and answering of complex queries. 

## How to run the pipeline

**Step 1:**
Clone this repository:
```shell
git clone https://github.com/username/repository-name
```
**Step 2:**
Navigate to the project directory.

**Step 3:**
Install the required dependencies:
```shell
pip install requirements.txt
```
**Step 4:**
Store your api keys in the `.env` file.
**Step 5:**
Store your data folder in the `src/data` directory.
**Step 6:**
Run the `main.py`:
```python
python main.py
```
It will save the index in the persist directory and it will also save the graph created in the `html` form in the `src/Graphs` directory which you can visualize by opening it in any browser.

**Step 7:** Then you can ask question about your data from the graph that has been created.
