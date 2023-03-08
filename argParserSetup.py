import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--start', dest='start', type=int, help='The index of the start page to scrape', required=True)
parser.add_argument('--end', dest='end', type=int, help='The index of the last page to scrape', required=True)
parser.add_argument('--target_url', dest='target_url', type=str, help='The url of the profile you want '
                                                                      'to scrape the connection from',
                    required=True)

args = parser.parse_args()