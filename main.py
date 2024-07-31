from llama_index.core import PropertyGraphIndex
from dotenv import load_dotenv
from llama_index.core import SimpleDirectoryReader
from llama_index.llms.groq import Groq
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from datetime import datetime
from llama_index.core import StorageContext, load_index_from_storage

model_name = "mixtral-8x7b-32768"
load_dotenv()
documents = SimpleDirectoryReader("src/data/paul_graham/").load_data()
llm = Groq(model=model_name)
embedding_model = HuggingFaceEmbedding(model_name="sentence-transformers/all-MiniLM-L6-v2")

index = PropertyGraphIndex.from_documents(
    documents,
    llm=llm,
    embed_model=embedding_model,
    show_progress=True,
)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

index.property_graph_store.save_networkx_graph(name=f"./src/Graphs/{model_name}{timestamp}.html")

index.storage_context.persist(persist_dir="./storage")


# First run the above code to create the graph and store it.
# When running the above graph creation section comment out the code below
# And when the indexing is complete, comment out the above code and run the below code, and make sure to change the
# query about your data.
# It will load the index and then you can ask questions about it.

index = load_index_from_storage(
    StorageContext.from_defaults(persist_dir="./storage"),
    embed_model=embedding_model,
    llm=llm
)
query_engine = index.as_query_engine(
    llm=llm,
    include_text=True,
)

response = query_engine.query("Who is Paul Graham?")

print(str(response))

