import utils
import dependencies
import json
import yaml
import os
import datetime

def setup_parser(subparsers):
  parser = subparsers.add_parser('client')
  subparsers = parser.add_subparsers(help='Client', dest='action')
  list = subparsers.add_parser('list')
  edit = subparsers.add_parser('edit')
  parser.add_argument('-o', '--output', default=['none'], type=str, nargs=1, help='None is normal, json will show json, yaml is yaml, and detailed will much more detailed output')
  
  list.add_argument('--indent', default=4, type=int, help='json indent only uses with -o json')
  
  edit.add_argument('macs', type=str, nargs='*', help='MAC of the machine you want to edit the config of')
  edit.add_argument('-o', '--output', default=['yaml'], type=str, nargs=1, help='yaml will be yaml and json will be json')
  return parser

def load_host(host):
  return {'mac': host.mac, 'config': json.loads(host.config)}

def edit_host(args):
  settings = dependencies.load_settings()
  editor = os.environ.get('EDITOR')
  db = settings['database']
  output = args.output[0]
  for mac in args.macs:
    host = db.find_host(mac)['host']
    host['config'] = json.loads(host['config'])
    if output == None:
      output = 'yaml'
    filename = f'/tmp/{mac}-{datetime.datetime.now()}.{args.output}'
    with open(filename, 'w') as stream:
      if output == 'yaml':
        stream.write(yaml.dump(host))
      else:
        stream.write(json.dumps(host, indent=4))
    os.system(f'{editor} "{filename}"')
    with open(filename, 'r') as stream:
      if output == 'yaml':
        updated_host = yaml.safe_load(stream)
      else:
        updated_host = json.load(stream)
    db.update_host(**updated_host)
    os.remove(filename)

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
  else:
    print(f'Error please report this {args}')

def main(args):
  if args.action == 'list':
    list_hosts(args)
  elif args.action == 'edit':
    edit_host(args)
