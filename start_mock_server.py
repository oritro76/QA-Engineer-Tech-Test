import os
import threading
import signal

from mock_server.mock_server import MockServer


def start_mock_server(port=int(os.getenv("MOCK_SERVER_PORT", 8000))):
    """
    Starts the mock server and handles user interruption (Ctrl+C).

    Args:
        port (int, optional): Port to run the server on. Defaults to the value
                              of the MOCK_SERVER_PORT environment variable or 8000.
    """

    server = MockServer(port)
    server_thread = threading.Thread(target=server.start)
    server_thread.daemon = True

    def handle_interrupt(signum, frame):
        print("Stopping mock server...")
        server.stop()
        server_thread.join()
        exit(0)

    signal.signal(signal.SIGINT, handle_interrupt)  # Register Ctrl+C handler

    server_thread.start()
    print(f"Mock server running on port {server.port}")

    # Keep the main script running while the server thread continues
    while True:
        pass  # Empty loop to keep the script running


if __name__ == "__main__":
    start_mock_server()
