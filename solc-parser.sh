#!/bin/bash

solidity_file="$1"  # Solidity 파일 경로
# python_script="version_parser.py"  # Python 스크립트 파일명

# # Solidity 버전 리스트 생성
# version_create=$(python3 "$python_script")

function print_version_info(){
    echo "Solidity version: $target_version"
    echo "Solidity sign: $target_sign"
}

function install_solc(){
    solc-select install $1
    solc-select use $1
}

# 솔리디티 버전 추출
target_version=$(cat "$solidity_file" | grep -oE "pragma solidity ((\^|=|~|>=|<=|>|<)?)([0-9]+\.[0-9]+(\.[0-9]+)?|\*)" | sed -E "s/pragma solidity ((\^|==|~|>=|<=|>|<)?)([0-9]+\.[0-9]+(\.[0-9]+)?|\*).*/\3/g")
target_sign=$(cat "$solidity_file" | grep -oE "pragma solidity ((\^|=|~|>=|<=|>|<)?)([0-9]+\.[0-9]+(\.[0-9]+)?|\*)" | sed -E "s/pragma solidity ((\^|==|~|>=|<=|>|<)?)([0-9]+\.[0-9]+(\.[0-9]+)?|\*).*/\2/g")

if [[ -n "$target_version" && ( -z "$target_sign" || "$target_sign" == "=" || "$target_sign" == "<=" ) ]]; then
    print_version_info
    install_solc "$target_version"

elif [[ -n "$target_version" && ( "$target_sign" == "^" || "$target_sign" == "~" || "$target_sign" == ">=" ) ]]; then
    print_version_info
    highest_version=$(python3 search_highest_version.py "$target_version")
    install_solc "$highest_version"
else
  echo "Solidity version not found."
fi

