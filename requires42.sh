#!/bin/sh

export REQUIRES42_TOKEN=06454b2f03c92c87119448838ec31b2716c21a70
set -- .

cd "$1" || exit

temp1="$(mktemp)" || exit
temp2="$(mktemp)" || exit
temp3="$(mktemp)" || exit

(
    find . -type f -name "*.py" -type f -maxdepth 1 | cut -c3- | rev | cut -c4- | rev
    find . -type f -name "__init__.py" -type f -maxdepth 2 | sed 's#/[^/]*$##' | cut -c3-
) > "$temp1" || exit
(
    find . -type f -name "*.py" -exec cat {} \; | grep ^'import ' | grep -v ^'#' | awk '{print $2}'
    find . -type f -name "*.py" -exec cat {} \; | grep ^'from ' | grep ' import' | grep -v ^'#' | grep -v ^'from \.' | awk '{print $2}'
) | grep -v ^$  | sort | awk -F '.' '{print $1}' | uniq > "$temp2"

awk 'FNR==NR{array[$0];next}{if ($0 in array) next;print $0}' "$temp1" "$temp2" > "$temp3"
curl -s -X POST -H "Authorization: Token $REQUIRES42_TOKEN" -H "Content-Type: text/plain" --data-binary "@$temp3" https://api.requires42.com/requires; exit=$?
rm -f "$temp1" "$temp2" "$temp3" 2> /dev/null
exit $exit
