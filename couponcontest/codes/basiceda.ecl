
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

//


//coupon detail train dataset
//output(choosen(detailtrainfull,100),named('detailtrainsample'));

//user coupon maps
usercouponsum := table(detailtrainfull,{user_id,coupon_id,cntcoupons:=sum(group,item_count)},user_id,coupon_id);

couponusercnt := table(usercouponsum,{coupon_id,cntusers := count(group)},coupon_id);

detailtrainfull1:= project(detailtrainfull,transform(rd.detailtrainmodrec,
                                                self.eclpurchasedate := utils().getecldate(left.purchase_date);
                                                self:=left;));

output(detailtrainfull1,,locprefix+'coupon_detail_train_mod1',csv(heading(single),quote('"')),overwrite);

// user list dataset
//choosen(userlist,5);

//table(userlist,{withdraw_date,cnt:=count(group)},withdraw_date);

userlist1 := project(userlist,transform(rd.userlistmodrec,
                                self.eclregdate:=utils().getecldate(left.reg_date);
                                self.eclwdrdate:=if(left.withdraw_date='NA',
                                                    utils().getecldate('1900-01-01 00:00:00'),
                                                    utils().getecldate(left.withdraw_date));
                                self:=left));

//choosen(userlist1,100);
//output(userlist1,,locprefix+'user_list_mod1',csv(heading(single),quote('"')),overwrite);

//now the coupon list data sets
//choosen(listtrainfull,10);
//choosen(listtestfull,10);

/*
table(listtrainfull,{USABLE_DATE_MON,cnt:=count(group)},USABLE_DATE_MON);
table(listtrainfull,{USABLE_DATE_tue,cnt:=count(group)},USABLE_DATE_tue);
table(listtrainfull,{USABLE_DATE_wed,cnt:=count(group)},USABLE_DATE_wed);
table(listtrainfull,{USABLE_DATE_sun,cnt:=count(group)},USABLE_DATE_sun);
table(listtrainfull,{USABLE_DATE_before_holiday,cnt:=count(group)},USABLE_DATE_before_holiday);
*/

listtrainfull1 := project(listtrainfull,transform(rd.couponlistmodrec,
                                        self.eclvalstdate := if(left.validfrom='NA',
                                                    utils().getecldate('1900-01-01 00:00:00'),
                                                    utils().getecldate(left.validfrom));
                                        self.eclvalenddate := if(left.validend='NA',
                                                    utils().getecldate('1900-01-01 00:00:00'),
                                                    utils().getecldate(left.validend));
                                        self.ecldispstdate := if(left.dispfrom='NA',
                                                    utils().getecldate('1900-01-01 00:00:00'),
                                                    utils().getecldate(left.dispfrom));
                                        self.ecldispenddate := if(left.dispend='NA',
                                                    utils().getecldate('1900-01-01 00:00:00'),
                                                    utils().getecldate(left.dispend));
                                        self.USABLE_DATE_MON := if(left.USABLE_DATE_MON='NA',
                                                    10,(integer) left.USABLE_DATE_MON);
                                        self.USABLE_DATE_tue := if(left.USABLE_DATE_tue='NA',
                                                    10,(integer) left.USABLE_DATE_tue);
                                        self.USABLE_DATE_wed := if(left.USABLE_DATE_wed='NA',
                                                    10,(integer) left.USABLE_DATE_wed);
                                        self.USABLE_DATE_thu := if(left.USABLE_DATE_thu='NA',
                                                    10,(integer) left.USABLE_DATE_thu);
                                        self.USABLE_DATE_fri := if(left.USABLE_DATE_fri='NA',
                                                    10,(integer) left.USABLE_DATE_fri);
                                        self.USABLE_DATE_sat := if(left.USABLE_DATE_sat='NA',
                                                    10,(integer) left.USABLE_DATE_sat);
                                        self.USABLE_DATE_sun := if(left.USABLE_DATE_sun='NA',
                                                    10,(integer) left.USABLE_DATE_sun);
                                        self.USABLE_DATE_holiday := if(left.USABLE_DATE_holiday='NA',
                                                    10,(integer) left.USABLE_DATE_holiday);
                                        self.USABLE_DATE_before_holiday := if(left.USABLE_DATE_before_holiday='NA',
                                                    10,(integer) left.USABLE_DATE_before_holiday);
                                        self:=left));

//output(listtrainfull1,,locprefix+'coupon_list_train_mod1',csv(heading(single),quote('"')),overwrite);

listtestfull1 := project(listtestfull,transform(rd.couponlistmodrec,
                                        self.eclvalstdate := if(left.validfrom='NA',
                                                    utils().getecldate('1900-01-01 00:00:00'),
                                                    utils().getecldate(left.validfrom));
                                        self.eclvalenddate := if(left.validend='NA',
                                                    utils().getecldate('1900-01-01 00:00:00'),
                                                    utils().getecldate(left.validend));
                                        self.ecldispstdate := if(left.dispfrom='NA',
                                                    utils().getecldate('1900-01-01 00:00:00'),
                                                    utils().getecldate(left.dispfrom));
                                        self.ecldispenddate := if(left.dispend='NA',
                                                    utils().getecldate('1900-01-01 00:00:00'),
                                                    utils().getecldate(left.dispend));
                                        self.USABLE_DATE_MON := if(left.USABLE_DATE_MON='NA',
                                                    10,(integer) left.USABLE_DATE_MON);
                                        self.USABLE_DATE_tue := if(left.USABLE_DATE_tue='NA',
                                                    10,(integer) left.USABLE_DATE_tue);
                                        self.USABLE_DATE_wed := if(left.USABLE_DATE_wed='NA',
                                                    10,(integer) left.USABLE_DATE_wed);
                                        self.USABLE_DATE_thu := if(left.USABLE_DATE_thu='NA',
                                                    10,(integer) left.USABLE_DATE_thu);
                                        self.USABLE_DATE_fri := if(left.USABLE_DATE_fri='NA',
                                                    10,(integer) left.USABLE_DATE_fri);
                                        self.USABLE_DATE_sat := if(left.USABLE_DATE_sat='NA',
                                                    10,(integer) left.USABLE_DATE_sat);
                                        self.USABLE_DATE_sun := if(left.USABLE_DATE_sun='NA',
                                                    10,(integer) left.USABLE_DATE_sun);
                                        self.USABLE_DATE_holiday := if(left.USABLE_DATE_holiday='NA',
                                                    10,(integer) left.USABLE_DATE_holiday);
                                        self.USABLE_DATE_before_holiday := if(left.USABLE_DATE_before_holiday='NA',
                                                    10,(integer) left.USABLE_DATE_before_holiday);
                                        self:=left));

//output(listtestfull1,,locprefix+'coupon_list_test_mod1',csv(heading(single),quote('"')),overwrite);

//