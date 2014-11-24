import RecordDefinitions from $;

export cleangenre() := module
	export dataset generate(dataset(RecordDefinitions.transrec) inp) := function
		return inp;
	end;
end;