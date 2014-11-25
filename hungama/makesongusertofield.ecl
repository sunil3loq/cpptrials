
import RecordDefinitions from $;
import params from $;
import ml;

export makesongusertofield(dataset(RecordDefinitions.songuseracceptrec) inp) := module
	export songmapgenerate() := function
		songsall := table(inp,{songuniquecode},songuniquecode);
		ml.appendid(songsall,id,songsallwithid);
		return songsallwithid;
	end;
	export usercatidgenerate() := function
		usercats := table(inp,{msisdn,category},msisdn,category);
		ml.appendid(usercats,id,usercatswithid);
		return usercatswithid;
	end;
	export generate() := function
		usercatsandid := usercatidgenerate();
		songandid := songmapgenerate();
		inpwithsongid := join(inp,songandid,left.songuniquecode=right.songuniquecode,
					transform(recordof(left) and not [songuniquecode] or {integer songid},
						self.songid:=right.id;self:=left;));
		inpwithallids := join(inpwithsongid,usercatsandid,left.msisdn=right.msisdn and left.category=right.category,
					transform(recordof(left) and not [msisdn,category] or {integer usercatid},
						self.usercatid=right.id;self:=left));
		songusertofield:=project(inpwithallids,transform(ml.types.field,self.id:=left.songuserid,));
		return inp;
	end;
end;
