from urllib.request import urlopen
import io

def scrape(url):
    page = urlopen(url)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    

scrape('https://kevinhoffman.medium.com/coping-with-mutable-state-in-multiple-threads-with-rust-9059c83b6c01')
