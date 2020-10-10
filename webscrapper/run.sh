#!/bin/bash
sed -i -- 's/"id"/"_id"/g' *
for filename in *; do mongoimport --db scrapped_data --collection $1  --jsonArray --file $filename; done
