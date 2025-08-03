import argparse
import db

def create_default():
  connect.db.create_all()

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument('--hostname', '-H', required=True, help='Default hostname')
  parser.add_argument('--distro', '-d', required=True, help='Distro name')
  parser.add_argument('--distro_version', required=True, help='Distro version')
  parser.add_argument('--arch', required=True, help='The CPU architeture')
  parser.add_argument('--mirror_host', required=True, help='Hostname of the mirror')
  parser.add_argument('--mirror_protocol', required=True, help='Procotocl for the mirror')
  parser.add_argument('--fullname', required=True, help='Fullname for the user')
  parser.add_argument('--ssh_key', required=True, help='The SSH pub key')
  
  args = parser.parse_args()
  print(args)
