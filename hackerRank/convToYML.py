# << Swami Shreeji >>
# Python utils 
# K8s dashboard gives JSON when copied. Prefer YAML

import sys, json, yaml

with open(sys.argv[1]) as test:
	print yaml.safe_dump(json.load(test), default_flow_style=False)