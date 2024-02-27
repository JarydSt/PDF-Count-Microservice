# Word Count Microservice

This microservice is designed to count the number of words in a PDF file. It provides a simple interface for programmatically requesting the word count of a PDF.

## Usage

### Prerequisites

- Python 3.x installed on your system
- Required libraries installed (`PyPDF2`, `zmq`)
You can install the required libraries using pip. Run the following command in your terminal or command prompt:

```bash
pip install PyPDF2 zmq
```

### Running the Microservice

1. Clone repository to your local machine:

    ```bash
    git clone https://github.com/your-username/word-count-microservice.git
    ```

2. Navigate to the project directory:

    ```bash
    cd word-count-microservice
    ```

3. Start the microservice by running:

    ```bash
    python word_count_microservice.py
    ```

### Requesting Word Count Programmatically

To request the word count of a PDF file programmatically, you can use the provided client test program (`test_client.py`). Make sure to update the `pdf_file_path` variable in the script with the actual path to your PDF file.

4. Run the client test program:

    ```bash
    python test_client.py
    ```

## Communication Contract

The microservice provides a simple interface for requesting the word count of a PDF file:

- **Request**: The client sends a message containing the full path to the PDF file to the microservice.
- **Response**: The microservice processes the PDF file, counts the words, and sends back the word count as a response.

### Example Request

```python
import zmq

def request_word_count(pdf_file_path):
    # Prepare ZeroMQ context and socket
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")  # Connect to the microservice
    
    # Send the file path to the microservice
    socket.send(pdf_file_path.encode('utf-8'))
    
    # Wait for the reply (word count)
    word_count = socket.recv().decode('utf-8')
    return word_count

# Example call
pdf_file_path = r"path/to/your/pdf/file.pdf"
word_count = request_word_count(pdf_file_path)
print(f"The PDF file contains {word_count} words.")
