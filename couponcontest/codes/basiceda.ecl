
import recorddefinitions from $;
import python;

locprefix := 'couponcontest::';

rd := recorddefinitions;

capnames := dataset(locprefix+'capsule_names',rd.capsulenamesrec,csv(heading(1),quote('"')));

capnames;

a := 10;
a;
