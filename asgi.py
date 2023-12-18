
from application import create_app
import socket

app = create_app('config.Config')


@app.route("/")
def home():
    return "<h>hello world</h>"


if __name__ == "__main__":
    host_name = socket.gethostname()
    IP = socket.gethostbyname(host_name)
    port = 5050

    print('Starting backend webserver on http://{hostname}:{port}/v1/ui, {ip}:{port}'.format(
        ip=IP,
        hostname=host_name,
        port=port
    ))

    app.run(host='0.0.0.0', port=port)
    #use_reloader is the problem
    # app.run(host='0.0.0.0', port=port, use_reloader=False)
