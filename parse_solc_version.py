import re
import sys

def get_solc_version_list():
    with open(sys.argv[1], 'r') as f:
        source_code = f.read()
    return source_code

def parse_solidity_version(source_code):
    version_pattern = r"pragma solidity\s*(>=|<=|>|<|=|~|\^)?\s*([0-9]+\.[0-9]+\.[0-9]+|\*)"
    matches = re.findall(version_pattern, source_code)
    print(matches)
    versions = []
    for match in matches:
        sign = match[0].strip()
        version = match[1].strip()
        versions.append((sign, version))

    return versions

# Solidity 버전 파싱
solidity_code = get_solc_version_list()
version_list = parse_solidity_version(solidity_code)

for sign, version in version_list:
    print("Sign:", sign)
    print("Version:", version)
    print("---")
