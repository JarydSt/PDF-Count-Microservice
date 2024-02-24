import zmq
from PyPDF2 import PdfReader


def count_words_in_pdf(file_path):
    # Open the PDF file
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        # Iterate over each page and extract text
        for page in reader.pages:
            text += page.extract_text()
        # Count the words
        words = text.split()
        return len(words)


def main():
    # Prepare ZeroMQ context and socket
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("Word Count Microservice started on port 5555.")

    while True:
        # Wait for the next request from the client
        message = socket.recv()
        file_path = message.decode('utf-8')

        try:
            word_count = count_words_in_pdf(file_path)
            response = str(word_count)
        except Exception as e:
            response = f"Error: {e}"

        # Send the reply back to the client
        socket.send(response.encode('utf-8'))


if __name__ == "__main__":
    main()
