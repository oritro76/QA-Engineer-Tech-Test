import http.server
import socketserver
import json
from urllib.parse import urlparse
import threading
from random_data.random_posts_data import PostsData


class MockServerHandler(http.server.BaseHTTPRequestHandler):
    posts_data = PostsData()

    def _set_headers(self, status_code=200, content_type="application/json"):
        self.send_response(status_code)
        self.send_header("Content-type", content_type)
        self.end_headers()

    def do_GET(self):
        self._handle_get()

    def do_POST(self):
        self._handle_post()

    def do_PUT(self):
        self._handle_put()

    def do_DELETE(self):
        self._handle_delete()

    def _handle_get(self):
        parsed_url = urlparse(self.path)
        print(parsed_url)
        if parsed_url.path == "/posts":
            self._set_headers()
            self.wfile.write(json.dumps(self.posts_data.get_all_posts()).encode())
        elif parsed_url.path.startswith("/posts/"):
            try:
                post_id = int(parsed_url.path.split("/")[2])
                post = self.posts_data.get_post_by_id(post_id)
                if post:
                    self._set_headers()
                    self.wfile.write(json.dumps(post).encode())
                else:
                    self._set_headers(404)
                    self.wfile.write()
            except ValueError:
                self._set_headers(400)
                self.wfile.write()
        else:
            self._set_headers(404)
            self.wfile.write()
                
            

    def _handle_post(self):
        try:
            content_length = int(self.headers["Content-Length"])
            post_data = json.loads(self.rfile.read(content_length))
            new_post = {
                "userId": post_data["userId"],
                "title": post_data["title"],
                "body": post_data["body"]
            }
            new_post = self.posts_data.add_post(new_post)
            self._set_headers(200)
            self.wfile.write(json.dumps(new_post).encode())
        except (KeyError, ValueError):
            self._set_headers(400)
            self.wfile.write()

    def _handle_put(self):
        parsed_url = urlparse(self.path)
        if parsed_url.path.startswith("/posts/"):
            post_id = int(parsed_url.path.split("/")[2])
            content_length = int(self.headers["Content-Length"])
            post_data = json.loads(self.rfile.read(content_length))
            updated_post_data = self.posts_data.update_post(post_id, post_data)
            if updated_post_data:
                self._set_headers()
                self.wfile.write(json.dumps(updated_post_data).encode())
            else:
                self._set_headers(404)
                self.wfile.write()
        else:
            self._set_headers(404)
            self.wfile.write()

    def _handle_delete(self):
        parsed_url = urlparse(self.path)
        if parsed_url.path.startswith("/posts/"):
            post_id = int(parsed_url.path.split("/")[2])
            self.posts_data.delete_post(post_id)
            self._set_headers(200)
            self.wfile.write()
        else:
            self._set_headers(404)
            self.wfile.write()


class MockServer:
    def __init__(self, port=8000):
        self.port = port
        self.posts_data = []
        self.server = None
        self.server_thread = None

    def start(self):
        self.server = socketserver.TCPServer(("localhost", self.port), MockServerHandler)
        self.server.posts_data = self.posts_data
        self.server_thread = threading.Thread(target=self.server.serve_forever)
        self.server_thread.daemon = True
        self.server_thread.start()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()
        self.server_thread.join()
        self.server = None
        self.server_thread = None

    def reset_data(self):
        self.posts_data = []