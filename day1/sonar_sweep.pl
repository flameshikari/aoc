use strict;
use warnings;

open(my $file, "<", "input");
chomp(my @values = <$file>);
close($file);


# part 1
my $depth = 0;
for my $i (0..@values-2) {
  $a = $values[$i];
  $b = $values[$i+1];
  if ($b > $a) { $depth += 1 };
}; print("part 1: $depth measurments\n");


# part 2
$depth = 0;
for my $i (0..@values-4) {
  $a = $values[$i] + $values[$i+1] + $values[$i+2];
  $b = $values[$i+1] + $values[$i+2] + $values[$i+3];
  if ($b > $a) { $depth += 1 };
}; print("part 2: $depth measurments\n");
