
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
    end;
    
    export genreNamesRec := record
        integer Frequency;
        unicode CAPSULE_TEXT;
        string English_Translation;
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

end;