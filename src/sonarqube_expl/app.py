from flask import Flask
from flask import send_file

app = Flask(__name__)
APPLICATION_MIME_TYPE = 'some_mime_type'


@app.route('/')
def hello_world():  # put application's code here
    return \
        "<p>good for SonarQube/SonarLint examination!</p>" \
        "<p>Issue: false positive on send_file() arguments.</p>" \
        "<p>see line 21: lint calling 'unexpected argument' on download_name.</p>"


def dummy_function():
    return send_file(
        'some_path_to_file',
        mimetype=APPLICATION_MIME_TYPE,
        as_attachment=True,
        download_name=f"some string",  # NOSONAR
    )


if __name__ == '__main__':
    app.run()
