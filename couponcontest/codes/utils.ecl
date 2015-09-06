import recorddefinitions from $;
import python;
import std;

export utils() := module
    export integer getecldatebypy(inpdate,inpformat) := embed(python)
        import datetime
        if type(inpdate) is None:
            return 0
        pydate=datetime.datetime.strptime(inpdate,inpformat).strftime('%Y%m%d')
        return int(str(pydate))
    endembed;
    
    export std.date.date_t getecldate(string inpdate) := function
        basedatestr := '19000101';
        basedate := (std.date.date_t) basedatestr;
        toreturn := if(length(inpdate) < 10,basedate,(integer) (inpdate[1..4]+inpdate[6..7]+inpdate[9..10]));
        return toreturn;
    end;
end;