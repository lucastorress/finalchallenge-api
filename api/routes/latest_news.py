from flask import jsonify
from api import app

import logging as logger
from api.controllers import requestLatestNews as request_latest_news


@app.route('/api/v1/latestnews', methods=['GET'])
def latest_news():
    logger.debug("Inside the get method of latest_news")
    return jsonify({
        'latestnews': request_latest_news.latest_news()
    }), 200
