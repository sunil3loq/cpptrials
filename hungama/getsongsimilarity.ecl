
import RecordDefinitions from $;
import params from $;

export getsongsimilarity(dataset(RecordDefinitions.songuseracceptrec) inp) := module
	export generate() := function
		allsongsgroup:=join(inp,inp,left.category=right.category and left.songuniquecode<right.songuniquecode 
				and left.msisdn=right.msisdn, 
				transform(RecordDefinitions.allsongsrec,self.songcodeone:=left.songuniquecode;
					self.songcodetwo:=right.songuniquecode;self.category:=right.category;
					self.msisdn:=left.msisdn;self.acceptorrejectone:=left.acceptorreject;
					self.acceptorrejecttwo:=right.acceptorreject;),
				all);

		allsongsgroupswithcalcs := project(allsongsgroup,
							transform(recordof(left) or {integer commonornot},
							self.commonornot:=if(left.acceptorrejectone=1 and 
							left.acceptorrejecttwo=1,1,0);self:=left));
		songgroups := table(allsongsgroupswithcalcs,{category,songcodeone,songcodetwo,
					intersection:=sum(group,commonornot),union:=count(group)},
				category,songcodeone,songcodetwo);
		songgroupswithsimilarity := project(songgroups,transform(recordof(left) or {real similarity},
									self.similarity:=left.intersection/left.union;
									self:=left;));
		return songgroupswithsimilarity(union>params.mindenominator);
	end;
end;

