import re
from os import environ

id_pattern = re.compile(r'^.\d+$')


support_group = environ.get('SUPPORT_GROUP', '-1002029882658')
SUPPORT_GROUP = int(support_group) if support_group and id_pattern.search(support_group) else None
