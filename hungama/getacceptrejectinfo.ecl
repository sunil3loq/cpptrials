
import RecordDefinitions from $;
import params from $;

export getacceptrejectinfo(dataset(RecordDefinitions.transmetarec) inp) := module
	export generate() := function
		//for each catagory, get if the user has accpted or rejected the song
		usersongmaxtime := table(inp,{category,songuniquecode,msisdn,maxduration:=max(group,duration)},
					category,songuniquecode,msisdn);
		//add if the song is accept or reject
		usersongaccept := project(usersongmaxtime,
					transform(recordof(left) or {integer acceptorreject},
						self.acceptorreject:=if(left.maxduration<=params.rejectcutoff,0,1);
						self:=left));
		return usersongaccept;
	end;
end; 
