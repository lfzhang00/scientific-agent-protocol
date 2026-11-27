#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

version="${1:-2.1.1}"
version="${version#v}"
tag="v${version}"

if ! git rev-parse -q --verify "refs/tags/${tag}" >/dev/null; then
  echo "tag ${tag} not found; create and push it first" >&2
  exit 1
fi

mkdir -p dist
out="dist/scientific-agent-protocol-${tag}.zip"
git archive --format=zip --prefix="scientific-agent-protocol-${tag}/" "${tag}" -o "${out}"
echo "${out}"
