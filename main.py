import prometheus_client as pc
import time
import sample_counter
import sample_gauge

port = 8080

if __name__ == "__main__":
    i = pc.Info('info', 'Info on sample app')
    i.info({'version': '1.0', 'maintainer': 'me@email.com'})
    sample_counter.init()
    sample_gauge.init()
    pc.start_http_server(port)
    print(f'server started at localhost:{port}/metrics')
    while True:
        time.sleep(1)
