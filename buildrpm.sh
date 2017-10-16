#!/bin/env bash

Usage() {
  echo "This scripts creates the build tree and builds the RPM."
  echo "It needs a directory name that contains a 'src' dir and a 'spec' dir."
  echo "  $0 <path>"
  exit 1
}

[ -z $1 ] && Usage

SRCDIR=${1}/src
SPECDIR=${1}/spec

[ whoami == "root" ] && { echo "NEVER RUN THIS SCRIPT AS ROOT USER OR VIA SUDO!"; exit 1; }

BASEDIR=${PWD}

# Check if SRCDIR is a valid path and SPECDIR contains a spec-file
[ ! -d ${SRCDIR} ] && { echo "$SRCDIR is not a valid path!"; exit 1; }
ls ${SPECDIR}/*spec > /dev/null || { echo "No spec-file found in ${SPECDIR}!"; exit 1; }

# Build the RPMBUILD tree
rm -rf ~/rpmbuid/*
rpmdev-setuptree || { echo "Something went wrong during setup of the buildtree... Aborting"; exit 1; }

for SPECFILE in ${SPECDIR}/*spec
do
  # Get the version from the spec-file
  NAME=$(awk '/^Name: / { print $NF }' ${SPECFILE})
  VRS=$(awk '/^Version: / { print $NF }' ${SPECFILE})
  REL=$(awk '/^Release: / { print $NF }' ${SPECFILE})

  # Copy the specfile to the BUILD-dir
  cp ${SPECFILE} ~/rpmbuild/SPECS

  # Create the source tarball in ~/rpmbuild/SOURCES
  cd ${SRCDIR}
  tar cfz ~/rpmbuild/SOURCES/${NAME}-${VRS}-${REL}.tgz .
  cd ${BASEDIR}

  # Build the binary RPM
  rpmbuild -bb --clean ~/rpmbuild/SPECS/${SPECFILE##*/}
done
