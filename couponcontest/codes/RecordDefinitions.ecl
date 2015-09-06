import std;

export recordDefinitions := module

    export capsuleNamesRec := record
        integer Frequency;
        unicode CAPSULE_TEXT;
        string English_Translation;
    end;
    
    export couponAreaRec := record
        unicode SMALL_AREA_NAME;
        unicode PREF_NAME;
        string COUPON_Id;
    end;
    
    export couponListRec := record
        unicode CAPSULE_TEXT;
        unicode GENRE_NAME;
        real PRICE_RATE;
        real CATALOG_PRICE;
        real DISCOUNT_PRICE;
        string DISPFROM;
        string DISPEND;
        integer DISPPERIOD;
        string VALIDFROM;
        string VALIDEND;
        integer VALIDPERIOD;
        string USABLE_DATE_MON;
        string USABLE_DATE_TUE;
        string USABLE_DATE_WED;
        string USABLE_DATE_THU;
        string USABLE_DATE_FRI;
        string USABLE_DATE_SAT;
        string USABLE_DATE_SUN;
        string USABLE_DATE_HOLIDAY;
        string USABLE_DATE_BEFORE_HOLIDAY;
        unicode large_area_name;
        unicode ken_name;
        unicode small_area_name;
        string COUPON_ID;
    end;
    
    export couponListModRec := record
        unicode CAPSULE_TEXT;
        unicode GENRE_NAME;
        real PRICE_RATE;
        real CATALOG_PRICE;
        real DISCOUNT_PRICE;
        string DISPFROM;
        string DISPEND;
        integer DISPPERIOD;
        string VALIDFROM;
        string VALIDEND;
        integer VALIDPERIOD;
        integer USABLE_DATE_MON;
        integer USABLE_DATE_TUE;
        integer USABLE_DATE_WED;
        integer USABLE_DATE_THU;
        integer USABLE_DATE_FRI;
        integer USABLE_DATE_SAT;
        integer USABLE_DATE_SUN;
        integer USABLE_DATE_HOLIDAY;
        integer USABLE_DATE_BEFORE_HOLIDAY;
        unicode large_area_name;
        unicode ken_name;
        unicode small_area_name;
        string COUPON_ID;
        std.date.date_t eclvalstdate; 
        std.date.date_t eclvalenddate;
        std.date.date_t ecldispstdate; 
        std.date.date_t ecldispenddate;
    end;
    
    export genreNamesRec := record
        integer genre_Freq;
        unicode CAPSULE_TEXT;
        string genre_eng;
    end;
    
    export prefectureRec := record
        unicode PREF_NAME;
        unicode PREFECTUAL_OFFICE;
        real LATITUDE;
        real LONGITUDE;
    end;
    
    export userListRec := record
        string REG_DATE;
        string2 SEX_ID;
        integer AGE;
        string WITHDRAW_DATE;
        unicode PREF_NAME;
        unicode USER_ID;
    end;

    export userlistmodrec := record
        userlistrec;
        std.date.date_t eclregdate;
        std.date.date_t eclwdrdate;
    end;
    
    export detailtrainrec := record
        integer ITEM_COUNT;
        string purchase_DATE;
        unicode SMALL_AREA_NAME;
        string PURCHASEID_hash;
        string USER_ID;
        string COUPON_ID;
    end;
    
    export detailtrainmodrec := record
        detailtrainrec;
        std.date.date_t eclpurchasedate;
    end;
    /*
    export couponlistengrec := record
        
    end;
    */
end;