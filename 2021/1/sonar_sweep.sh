readarray -t values < input

tail_array () { seq 0 $((${#values[@]}-1-$1)); }


# part 1
depth=0
for i in $(tail_array 0); do
  a=${values[$i]}
  b=${values[$(($i+1))]}
  [[ $b -gt $a ]] && let depth++
done; echo $depth


# part 2
depth=0
for i in $(tail_array 3); do
  i0=${values[$i]}
  i1=${values[$(($i+1))]}
  i2=${values[$(($i+2))]}
  i3=${values[$(($i+3))]}
  a=$(($i0+$i1+$i2))
  b=$(($i1+$i2+$i3))
  [[ $b -gt $a ]] && let depth++
done; echo $depth
