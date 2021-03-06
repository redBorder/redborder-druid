#!/bin/bash

function usage() {
  echo
  echo "rb_druid_start.sh [-h] [-c <component>]"
  echo "  -h -> print this help"
  echo "  -c component -> start druid component (it can be coordinator, broker, historical, middlemanager, overlord or realtime)"
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

components_arr=("coordinator" "overlord" "broker" "historical" "middleManager" "realtime")

if [ "x$component" != "x" ] && in_array;then
  source /etc/sysconfig/druid_$component
  exec /usr/bin/java ${JAVA_ARGS} -cp ${CONF_DIR}/_common:${CONF_DIR}/$component:/usr/lib/druid/lib/* io.druid.cli.Main server $component
else
  usage;
fi
