# Blog Generation Using LLM

## Steps to Execute

1. Download the Llama-2-7B-Chat-GGML model from [Hugging Face](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main) and copy it into the `models` folder.
2. Install Anaconda3.
3. Create a new environment named `vijayenv` with Python version 3.9 using the following command:
    ```sh
    conda create -p vijayenv python=3.9 --yes
    ```
4. Activate the newly created environment:
    ```sh
    conda activate vijayenv
    ```
5. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
6. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```
