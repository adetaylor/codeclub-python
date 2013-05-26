#!/bin/bash
# Assumes changes have been checked into airport-problem
git checkout stage-3-solution
git merge airport-problem

function do_merge {
  local A="$1"
  local B="$2"
  git checkout stage-$B-solution
  git merge stage-$A-solution
}

do_merge 3 4
do_merge 4 5
do_merge 5 6
do_merge 6 7
do_merge 7 8
