from threading import Thread
import time
from wsgiref.simple_server import make_server
from flask import Flask, request, jsonify, logging
from flask_paginate import Pagination, get_page_args
from loguru import logger
import requests
from random_data.random_posts_data import PostsData

posts_data = PostsData()

class MockServer:
    def __init__(self, port=5050):
        self.port = int(port)
        self.app = Flask(__name__)
        self.server = make_server('localhost', self.port, self.app)
        self.url = "http://localhost:%s" % self.port
        self.thread = None

        @self.app.route('/alive', methods=['GET'])
        def alive():
            return "True"
        
        @self.app.route("/posts", methods=["GET"])
        def get_all_posts():
            
            """
            Returns a paginated JSON list of all posts with custom page and limit parameters.
            """
            # Get page and limit arguments from request (with defaults)
            self.app.logger.debug(request.query_string.decode())
            self.app.logger.debug(request.args)

            page = request.args.get('_page')
            limit = request.args.get('_limit')
            all_posts = posts_data.get_all_posts()

            
            self.app.logger.debug("inside get posts")

            if page is None and limit is None:
                self.app.logger.debug("no params")
                return jsonify(all_posts)
            
            page, per_page, offset = get_page_args(
                page_parameter='_page',
                per_page_parameter='_limit',
                default=1,
                default_per_page=10
            )

            self.app.logger.debug(f"{page}, {per_page}, {offset}")
            posts = all_posts[offset:offset + per_page]

            pagination = Pagination(page=page, per_page=per_page, total=len(all_posts))

            return jsonify(posts)

        @self.app.route("/posts/<int:post_id>", methods=["GET"])
        def get_post_by_id(post_id):
            """
            Returns a JSON object of a post with the specified ID.
            404 error if post not found.
            """
            post = posts_data.get_post_by_id(post_id)
            if post:
                return jsonify(post)
            else:
                return jsonify({"error": "Post not found"}), 404

        @self.app.route("/posts", methods=["POST"])
        def create_post():
            """
            Creates a new post from the request body (JSON data).
            Returns the created post object (JSON) on success.
            400 error on invalid data.
            """
            try:
                data = request.get_json()
                new_post = posts_data.add_post(data)
                return jsonify(new_post), 200
            except (KeyError, ValueError):
                return jsonify({"error": "Invalid data"}), 400

        @self.app.route("/posts/<int:post_id>", methods=["PUT"])
        def update_post(post_id):
            """
            Updates a post with the specified ID using the request body (JSON data).
            Returns the updated post object (JSON) on success.
            400 error on invalid data or non-existent post.
            """
            try:
                data = request.get_json()
                updated_post = posts_data.update_post(post_id, data)
                if updated_post:
                    return jsonify(updated_post)
                else:
                    return jsonify({"error": "Post not found"}), 404
            except (KeyError, ValueError):
                return jsonify({"error": "Invalid data"}), 400

        @self.app.route("/posts/<int:post_id>", methods=["DELETE"])
        def delete_post(post_id):
            """
            Deletes a post with the specified ID.
            Returns a 200 status code on success.
            404 error if post not found.
            """
            posts_data.delete_post(post_id)
            return "", 200

        @self.app.route("/reset", methods=["POST"])
        def reset_data():
            """
            Resets the internal post data to an empty list.
            """
            posts_data.reset_data()
            return "", 200

    def start(self):
        self.thread = Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

        # Ensure server is alive before we continue running tests
        server_is_alive = False
        liveliness_attempts = 0
        while not server_is_alive:
            if liveliness_attempts >= 50:
                raise Exception('Failed to start and connect to mock server. '
                                f'Is port {self.port} in use by another application?')
            liveliness_attempts += 1
            try:
                requests.get(self.url + '/alive', timeout=0.2)
                server_is_alive = True
            except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
                time.sleep(0.1)

    def stop(self):
        self.server.shutdown()
        self.thread.join()