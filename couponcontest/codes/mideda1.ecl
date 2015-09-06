
import recorddefinitions from $;
import python;
import utils from $;
import std;

locprefix := '~couponcontest::';

rd := recorddefinitions;

capnames := dataset(locprefix+'capsule_names',rd.capsulenamesrec,csv(heading(1),quote('"')));
areatrainfull := dataset(locprefix+'coupon_area_train',rd.couponarearec,csv(heading(1),quote('"')));
areatestfull := dataset(locprefix+'coupon_area_test',rd.couponarearec,csv(heading(1),quote('"')));
listtrainfull := dataset(locprefix+'coupon_list_train',rd.couponlistrec,csv(heading(1),quote('"')));
listtestfull := dataset(locprefix+'coupon_list_test',rd.couponlistrec,csv(heading(1),quote('"')));
gennames := dataset(locprefix+'genre_names',rd.genrenamesrec,csv(heading(1),quote('"')));
prelocs := dataset(locprefix+'prefecture_locations',rd.prefecturerec,csv(heading(1),quote('"')));
userlist := dataset(locprefix+'user_list',rd.userlistrec,csv(heading(1),quote('"')));
detailtrainfull := dataset(locprefix+'coupon_detail_train',rd.detailtrainrec,csv(heading(1),quote('"')));

//reading of the modified date data
listtrainfull1 := dataset(locprefix+'coupon_list_train_mod1',rd.couponlistmodrec,csv(heading(1),quote('"')));

listtraineng1 := join(listtrainfull1,gennames,left.genre_name=right.genre_name,
                    transform(recordof(left) or recordof(right),self:=left;
                        self:=right),skew(1),smart);
                        

listtraineng2 := join(listtraineng1,capnames,left.capsule_text=right.capsule_text,
                    transform(recordof(left) or recordof(right),self:=left;
                        self:=right),smart,skew(1));
                        
choosen(listtraineng2,10);



