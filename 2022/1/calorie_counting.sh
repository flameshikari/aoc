readarray -t file < input

summary=0
inventories=()

for row in "${file[@]}"; do
  if [[ -z $row ]]; then
    inventories+=($summary)
    summary=0
  else
    summary=$(($summary+$row))
  fi
done

readarray -t inventories < <(echo ${inventories[@]} | awk 'BEGIN{RS=" ";} {print $1}' | sort)


# part 1
echo "part 1: ${inventories[@]: -1} calories"

# part 2
numbers="${inventories[@]: -3:3}"
echo "part 2: $((${numbers// /+})) calories"
