
import RecordDefinitions from $;
import params from $;

export gettransactions(dataset(RecordDefinitions.transmetarec) inp) := module
	export generate() := function
		return inp(duration>params.notatranscutoff);
	end;
end;
