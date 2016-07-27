#!/bin/bash

#source /etc/sysconfig/druid-coordinator


function usage() {
  echo 
  echo "rb_druid_start.sh [-h] [-c <component>]"
  echo "  -h -> print this help"
  echo "  -c component -> start druid component (it can be coordinator, broker, historical, middlemanager or overlord)"
  echo
  exit 0
}

function in_array() {
  for i in ${components_arr[@]} ; do
      if [ "x$i" == "x$component" ] ; then
          return 0
      fi
  done
  return 1
}

while getopts "hc:" name
do
  case $name in
    c) component="$OPTARG";;
    h) usage;;
  esac
done

components_arr=("coordinator" "overlord" "broker" "historical" "middlemanager" "overlord")

if [ "x$component" != "x" ] && in_array;then
  source /etc/sysconfig/druid_$component
  exec /usr/bin/java ${JAVA_ARGS} -cp /etc/druid/_common:/etc/druid/coordinator:/usr/lib/druid/lib/* io.druid.cli.Main server coordinator
else
  usage;
fi
