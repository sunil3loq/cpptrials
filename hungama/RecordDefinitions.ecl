import std;

export RecordDefinitions := module
	export transrecwithflags := RECORD
	  string songuniquecode;
	  integer8 duration;
	  string circle;
	  string date;
	  string msisdn;
	  string dnis;
	  string mode;
	  string businesscategory;
	  integer8 sigornot;
	  unsigned4 dateecl;
	  integer8 retornot;
	 END;
	export transrec := RECORD
    STRING SongUniqueCode;
    integer Duration;
    STRING Circle;
    STRING Date;
    STRING MSISDN;
    STRING DNIS;
    STRING Mode;
    STRING businesscategory;
END; 

	export metarec := RECORD
    STRING SNo;
    STRING SongUniqueCode;
    STRING ContentName;
    STRING AlbumName;
    STRING ReleaseYear;
    STRING ReleaseMonth;
    STRING MalePerformers;
    STRING FemalePerformers;
    STRING Lyricist;
    STRING MusicDirector;
    STRING MaleSingers;
    STRING FemaleSingers;
    STRING Language;
    STRING Genre;
END;
	
	export transmetarec := RECORD
  string songuniquecode;
  integer8 duration;
  string circle;
  string date;
  string msisdn;
  string dnis;
  string mode;
  string businesscategory;
  integer8 sigornot;
  unsigned4 dateecl;
  integer8 retornot;
  string sno;
  string contentname;
  string albumname;
  string releaseyear;
  string releasemonth;
  string maleperformers;
  string femaleperformers;
  string lyricist;
  string musicdirector;
  string malesingers;
  string femalesingers;
  string language;
  string genre;
  string category;
 END;

	export songuseracceptrec := RECORD
  string category;
  string songuniquecode;
  string msisdn;
  integer8 maxduration;
  integer8 acceptorreject;
 END;

	export allsongsrec := RECORD
		string songcodeone;
		string songcodetwo;
		string category;
		string msisdn;
		integer acceptorrejectone;
		integer acceptorrejecttwo;
	END;
end;
