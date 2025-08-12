from tools import client
import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  subparsers = parser.add_subparsers(help='Tools', dest='tool')
  client_parser = client.setup_parser(subparsers)
  args = parser.parse_args()
  # if args.tools
  print(args)
