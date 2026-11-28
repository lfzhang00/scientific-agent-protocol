#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

if [[ $# -ne 1 ]]; then
  echo "usage: bash scripts/package.sh <version-or-tag>" >&2
  exit 1
fi

version="$1"
version="${version#v}"
if [[ ! "${version}" =~ ^[0-9]+(\.[0-9]+)*([.-][A-Za-z0-9.-]+)?$ ]]; then
  echo "invalid version: ${version}" >&2
  exit 1
fi
tag="v${version}"

if ! git rev-parse -q --verify "refs/tags/${tag}" >/dev/null; then
  echo "local tag ${tag} not found" >&2
  exit 1
fi

mkdir -p dist
out="dist/scientific-agent-protocol-${tag}.zip"
git archive --format=zip --prefix="scientific-agent-protocol-${tag}/" "${tag}" -o "${out}"
echo "${out}"
