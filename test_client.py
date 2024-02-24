import zmq


def request_word_count(pdf_file_path):
    # Prepare ZeroMQ context and socket
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    # Send the file path to the microservice
    socket.send(pdf_file_path.encode('utf-8'))

    # Wait for the reply (word count)
    word_count = socket.recv().decode('utf-8')
    return word_count


if __name__ == "__main__":
    # Replace 'path_to_pdf.pdf' with the path to the PDF for testing
    pdf_file_path = r""

    word_count = request_word_count(pdf_file_path)
    print(f"The PDF file contains {word_count} words.")
