#!/bin/sh

offset_headers() {
    awk '{
        if ($1 ~ /^#+$/) {
            print "##" $0; # Prepend an extra # to headers
        } else {
            print $0;
        }
    }'
}

mkdir -p pdfdocs
cp static/docs/01-index.md pdfdocs/docs.md
echo "" >> pdfdocs/docs.md

echo "## Contributor Documentation" >> pdfdocs/docs.md
echo "" >> pdfdocs/docs.md
for f in static/docs/contributor/*.md; do
	offset_headers < $f >> pdfdocs/docs.md
	echo "" >> pdfdocs/docs.md
done

echo "## Maintainer Documentation" >> pdfdocs/docs.md
echo "" >> pdfdocs/docs.md
for f in static/docs/maintainer/*.md; do
	offset_headers < $f >> pdfdocs/docs.md
	echo "" >> pdfdocs/docs.md
done

cp static/docs/maintainer/02--secret-setup.png pdfdocs/

echo "## UmBox Spec" >> pdfdocs/docs.md
echo "" >> pdfdocs/docs.md
for f in static/docs/spec/*.md; do
	offset_headers < $f >> pdfdocs/docs.md
	echo "" >> pdfdocs/docs.md
done

echo "## User Documentation" >> pdfdocs/docs.md
echo "" >> pdfdocs/docs.md
for f in static/docs/user/*.md; do
	offset_headers < $f >> pdfdocs/docs.md
	echo "" >> pdfdocs/docs.md
done

cd pdfdocs
pandoc docs.md -o docs.pdf