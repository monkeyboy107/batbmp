from tools import clients, test
import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  subparsers = parser.add_subparsers(help='Tools', dest='tool')
  client_parser = clients.setup_parser(subparsers)
  test_parser = test.setup_parser(subparsers)
  args = parser.parse_args()
  # if args.tools
