import RecordDefinitions from $;
import std;
import python;

export cleanlanguageandgenre() := module

	export string cleangenre(string inpgenre) := EMBED(Python)
		inpstrnew = inpgenre.strip()
		inpnospace = inpstrnew.replace(' ','')
		if inpnospace[:3] == 'NEW':
			inpcleanone = 'NEWARRIVALS'
		else:
			inpcleanone = inpnospace
		returnvalue = inpcleanone
		return returnvalue
        ENDEMBED;

	export string cleanlanguage(string inplanguage) := EMBED(Python)
		inpstrnew = inplanguage.strip()
		inpnospace = inpstrnew.replace(' ','')
		if inpnospace == 'HARYANVI':
			inpcleanone =  'HARYANAVI'
		else:
			inpcleanone = inpnospace
		returnvalue = inpcleanone
		return returnvalue
        ENDEMBED;

	export dataset generate(dataset(RecordDefinitions.metarec) inp) := function
		inpupcase := project(inp,transform(recordof(left),self.genre:=std.str.touppercase(left.genre);
							self.language:=std.str.touppercase(left.language);
							self:=left));
		inpclean := project(inpupcase,transform(recordof(left),self.genre:=cleangenre(left.genre),
							self.language:=cleanlanguage(left.language);
							self:=left));
		return inpclean;
	end;
end;
