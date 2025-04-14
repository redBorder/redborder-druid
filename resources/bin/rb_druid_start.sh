#!/bin/bash

function usage() {
  echo
  echo "rb_druid_start.sh [-h] [-c <component>]"
  echo "  -h -> print this help"
  echo "  -c component -> start druid component (it can be coordinator, broker, historical, middlemanager, overlord, indexer, router)"
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

components_arr=("coordinator" "overlord" "broker" "historical" "middleManager" "indexer" "router")

if [ "x$component" != "x" ] && in_array;then
  source /etc/sysconfig/druid_$component
  exec /usr/lib/druid/bin/run-java ${JAVA_ARGS} -Ddruid.node.type=$component -Ddruid.log.path=/usr/lib/druid/bin/log -cp /etc/druid/_common:/etc/druid/$component:/usr/lib/druid/lib/*: org.apache.druid.cli.Main server $component
else
  usage;
fi
