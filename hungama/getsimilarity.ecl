
import RecordDefinitions from $;
import params from $;
import gettransactions from $;
import getacceptrejectinfo from $;
import getsongsimilarity from $;

transmetarec := RecordDefinitions.transmetarec;
transmetadata := dataset('~hungama::nov172014::trasactionmetajoin',transmetarec,csv(heading(1),quote('"')));

sigtransactions := gettransactions(transmetadata).generate();
choosen(sigtransactions,10);

songuseraccept := getacceptrejectinfo(sigtransactions).generate();
output(songuseraccept,,'~hungama::nov172014::songuseraccept',csv(heading(single)),overwrite);

table(songuseraccept,{category},category);

songgroupssimilarity := getsongsimilarity(songuseraccept).generate();
output(songgroupssimilarity,,'~hungama::nov172014::songgroupssimilairty',csv(heading(single)),overwrite);

table(songgroupssimilarity,{union,cnt:=count(group)},union);

songuserfield := makesongusertofield(songuseraccept).generate();
