#!/bin/bash
page="<style>html{background: linear-gradient(90deg,"
while read -r line
do
    page="${page}${line},"
done < "$1"
page="${page::-1});}</style>"
echo $page
# echo $page > .html
# firefox .html
