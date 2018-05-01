import os
from flask import (Blueprint, current_app, render_template,
                   send_from_directory, url_for)


blueprint = Blueprint(
    'index',
    __name__,
    static_folder='static',
    template_folder='templates'
)

# @blueprint.route('/')
# def get_index():
#     pass

@blueprint.route('/media/<filename>')
def get_img(filename):
    media = os.path.join(current_app.root_path,
                         current_app.config['DIR']['media'])
    return send_from_directory(media, filename)
