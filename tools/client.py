import utils
import dependencies
import json
import yaml

def get_all_clients():
  return ['all', 'clients']

def setup_parser(subparsers):
  parser = subparsers.add_parser('client')
  parser.add_argument('action', help='List clients')
  parser.add_argument('-o', '--output', default='None', type=str, nargs=1, help='None is normal, json will show json, yaml is yaml, and detailed will much more detailed output')
  parser.add_argument('--indent', default=4, type=int, help='json indent only uses with -o json')
  return parser

def load_host(host):
  return {'mac': host.mac, 'config': json.loads(host.config)}

def list_hosts(args):
  settings = dependencies.load_settings()
  padding = 50
  hostname_padding = len("ab:cd:ef:12:34:56") + 1
  db = settings['database']
  hosts = db.find_all_hosts()['hosts']
  if args.output[0].lower() == 'none':
    print(f'{"-"* padding}')
    for host in hosts:
      print(f'|host: {json.loads(host.config)["host"]["name"]: <{hostname_padding}} | mac {host.mac}|')
    print(f'{"-"* padding}')
  elif args.output[0].lower() == 'json' or args.output[0].lower() == 'yaml':
    json_hosts = []
    for host in hosts:
      json_hosts.append(load_host(host))
    if args.output[0].lower() == 'json':
      print(json.dumps(json_hosts, indent=args.indent))
    else:
      print(yaml.dump(json_hosts))

def main(args):
  if args.action == 'list':
    list_hosts(args)
