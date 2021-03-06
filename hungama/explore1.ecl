import std;
import RecordDefinitions from $;
import cleanlanguageandgenre from $;
import python;

string transstr := '~hungama::nov172014::tatadocomo';

transrec := RecordDefinitions.transrec;

transdata := dataset(transstr,transrec,csv(heading(1)));

//choosen(transdata,100);

metastr := '~hungama::nov172014::tataendlesscatalogue';

metarec := RecordDefinitions.metarec;

metadata := dataset(metastr,metarec,csv(heading(1)));

//choosen(metadata,100);

song_bus_map := table(transdata,{songuniquecode,businesscategory,count(group)},songuniquecode,businesscategory);

//all possible combinations of the bus categories
cat_combos := join(song_bus_map,song_bus_map,left.songuniquecode=right.songuniquecode and left.businesscategory<right.businesscategory,
					transform({string catone;string cattwo},self.catone:=left.businesscategory;self.cattwo:=right.businesscategory),all);

//get commo songs by categories tuple
//output(sort(table(cat_combos,{catone,cattwo,occurnum:=count(group)},catone,cattwo),-occurnum),named('commonssongsbycatgroups'));

//get top 5 categories by circle
transdata_20 := transdata(duration>20);

circletopcat:=sort(topn(group(table(transdata_20,{circle,businesscategory,transcnt:=count(group)},circle,businesscategory),circle,all),5,-transcnt)
					,circle,-transcnt);
circlewisetrans := table(transdata_20,{circle,tottrans:=count(group)},circle);

circletopcat_norm := join(circletopcat,circlewisetrans,left.circle=right.circle,
							transform(recordof(left) or {real prcttrans},self:=left;self.prcttrans:=left.transcnt/right.tottrans));
//output(circletopcat_norm,named('top5catsbycircle'));

//check the reappearances
transwithsig := project(transdata,transform(recordof(left) or {integer sigornot},self.sigornot:=if(left.duration>20,1,0);self:=left));
recwithdate:=recordof(transwithsig) or {std.date.date_t dateecl};
recwithdate getrightdate(recordof(transwithsig) inp) := transform
	slist := std.str.splitwords(inp.date,'-');
	UNSIGNED2 yearend := (UNSIGNED2)slist[1];
	UNSIGNED2 monthend := (UNSIGNED2)slist[2];
	UNSIGNED2 dayend := (UNSIGNED2)slist[3];
	self.dateecl := std.date.datefromparts(yearend,monthend,dayend);
	self:=inp;
end;
transrightdate := project(transwithsig,getrightdate(left));
choosen(transrightdate,10);
cust_first:= table(transrightdate,{msisdn,mindate:=min(group,dateecl)},msisdn);
transwithretflag := join(transrightdate,cust_first,left.msisdn=right.msisdn,
						transform(recordof(left) or {integer retornot},self.retornot:=if(left.dateecl=right.mindate,0,1);self:=left));
						
distmsisdn:=count(table(transwithretflag,{msisdn},msisdn));
//output(distmsisdn,named('distinctusers'));

disretsigforcust := table(transwithretflag,{msisdn,retornot,sigornot},msisdn,retornot,sigornot);

//output(count(table(disretsigforcust(retornot=1),{msisdn},msisdn)),named('numberofreturningcust'));

//output(count(table(disretsigforcust(retornot=1 and sigornot=1),{msisdn},msisdn)),named('numberofreturningwithsig'));

//count o returning or not transactions

//output(table(transwithretflag,{retornot,sigornot,cnttrans:=count(group)},retornot,sigornot),named('retsiftrans'));

//output(sort(table(transdata,{businesscategory},businesscategory),businesscategory),named('distinctbusinesscategories'));

output(sort(table(metadata,{genre},genre),genre),named('distinctgenre'));

output(sort(table(metadata,{language},language),language),named('distinctlanguage'));

//output(transwithretflag,,'~micromax::hungama::testdata',csv(heading(single)),overwrite);

metacleandata := cleanlanguageandgenre().generate(metadata);

output(sort(table(metacleandata,{language},language),language),named('dislanguage'));

output(sort(table(metacleandata,{genre},genre),genre),named('disgenre'));

metadatawithcat := project(metacleandata,transform(recordof(left) or {string category},self.category:=left.language+left.genre;
							self:=left));

output(metadatawithcat,,'~hungama::nov172014::metacleandata',csv(heading(single),quote('"')),overwrite);

output(sort(table(metadatawithcat,{category},category),category),named('discategory'));
//distinct songs in category
transupbcat := project(transwithretflag,transform(recordof(left),
							self.businesscategory:=std.str.touppercase(left.businesscategory);
							self:=left));

//join the song info to understand which songs are in a b category
transleftmeta := join(transupbcat,metadatawithcat,left.songuniquecode=right.songuniquecode,
			transform(recordof(left) or recordof(right),self:=left;self:=right));

catmap:=sort(table(table(transleftmeta,{businesscategory,songuniquecode,category},businesscategory,songuniquecode,category),
	{businesscategory,category,cnttrans:=count(group)},businesscategory,category),businesscategory,-cnttrans);

//catmap;

output(transleftmeta,,'~hungama::nov172014::trasactionmetajoin',csv(heading(single),quote('"')),overwrite);

output(sort(table(transleftmeta,{category},category),category),named('discategorylast'));

output(count(transleftmeta),named('join'));
output(count(transwithretflag),named('trans'));
