import utils

def get_all_clients():
  return ['all', 'clients']

def setup_parser(subparsers):
  parser = subparsers.add_parser('client')
  parser.add_argument('-l', '--list', action='store_true', help='List clients')
  return parser

def main(args):
  print(utils)
