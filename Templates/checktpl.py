from jinja2 import Environment, FileSystemLoader
import sys
import yaml

env=Environment(loader = FileSystemLoader("./"))

template = env.get_template(sys.argv[1])
data = yaml.load(open(sys.argv[2],"r"))

print template.render(**data)

