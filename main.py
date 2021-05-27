import prometheus_client as pc
import time
import sample_counter
import sample_gauge

if __name__ == "__main__":
    i = pc.Info('info', 'Info on sample app')
    i.info({'version': '1.0', 'maintainer': 'me@email.com'})
    sample_counter.init()
    sample_gauge.init()
    pc.start_http_server(8080)
    while True:
        time.sleep(1)
