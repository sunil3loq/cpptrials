
filename := '~hungama::nov172014::tatadocomo';
//string _jklfd  := 'kas';

transrec := RECORD
    STRING SongUniqueCode;
    integer Duration;
    STRING Circlefield3;
    STRING Datefield4;
    STRING MSISDNfield5;
    STRING DNISfield6;
    STRING Modefield7;
    STRING businesscategoryfield8;
END;

transdata := dataset(filename,transrec,csv(heading(1)));

import ml;
export dataset getntileranges(integer numbertiles) := function
	
	ml.appendid(transdata,id,transdatawithid);
	
	ml.tofield(transdatawithid,durationinfield,id,'_duration_');
	
	agg := ml.fieldaggregates(durationinfield);
	
	deciledata := agg.ntileranges(numbertiles);
	
	return deciledata;
end;

tileddata := getntileranges(10);
tileddata;