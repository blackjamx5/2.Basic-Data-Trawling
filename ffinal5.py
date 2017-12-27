text = ""
with open("CN.txt") as file:
 text = file.read()


class Deaths:
 def __init__(self):
     self.death_year = ""
     self.cause_of_death = ""
     self.sex = ""
     self.race_ethnicity = ""
     self.all_ages = ""
     self.age_less_than_5 = ""
     self.age_5_to_9 = ""
     self.age_10_to_14 = ""
     self.age_15_to_19 = ""
     self.age_20_to_24 = ""
     self.age_25_to_29 = ""
     self.age_30_to_34 = ""
     self.age_35_to_39 = ""
     self.age_40_to_44 = ""
     self.age_45_to_49 = ""
     self.age_50_to_54 = ""
     self.age_55_to_59 = ""
     self.age_60_to_64 = ""
     self.age_65_to_69 = ""
     self.age_70_to_74 = ""
     self.age_75_to_79 = ""
     self.age_80_to_84 = ""
     self.age_greater_than_85 = ""
     self.age_unknown = ""

def read_database():
 n = -1
 list_of_causes = []
 for line in text.splitlines():
     n += 1
     line = line.split("\t")
     a = str(n)
     a = Deaths()
     a.death_year = line[1]
     a.cause_of_death = line[2]
     a.sex = line[3]
     a.race_ethnicity = line[4]
     a.all_ages = line[5]
     a.age_less_than_5 = line[6]
     a.age_5_to_9 = line[7]
     a.age_10_to_14 = line[8]
     a.age_15_to_19 = line[9]
     a.age_20_to_24 = line[10]
     a.age_25_to_29 = line[11]
     a.age_30_to_34 = line[12]
     a.age_35_to_39 = line[13]
     a.age_40_to_44 = line[14]
     a.age_45_to_49 = line[15]
     a.age_50_to_54 = line[16]
     a.age_55_to_59 = line[17]
     a.age_60_to_64 = line[18]
     a.age_65_to_69 = line[19]
     a.age_70_to_74 = line[20]
     a.age_75_to_79 = line[21]
     a.age_80_to_84 = line[22]
     a.age_greater_than_85 = line[23]
     a.age_unknown = line [24]

     list_of_causes.append(a)

 return list_of_causes

def white_non_hispanic_at_risk_age_group():
    dic = {}
    list_allages = 0
    list_agelessthan_5 = 0
    list_age5to9 = 0
    list_age10to14 = 0
    list_age15to19 = 0
    list_age20to24 = 0
    list_age25to29 = 0
    list_age30to34 = 0
    list_age35to39 = 0
    list_age40to44 = 0
    list_age45to49 = 0
    list_age50to54 = 0
    list_age55to59 = 0
    list_age60to64 = 0
    list_age65to69 = 0
    list_age70to74 = 0
    list_age75to79 = 0
    list_age80to84 = 0
    list_agegreaterthan85 = 0
    list_ageunknown = 0
    for a in read_database():
        if a.cause_of_death == str('"X60-X84,Y87.0 Suicide"'):
            if a.race_ethnicity == str('"WHITE, NON-HISPANIC"'):
                if a.sex == str("BOTH SEXES"):
                    list_allages += (int(a.all_ages))
                    list_agelessthan_5 += (int(a.age_less_than_5))
                    list_age5to9 += (int(a.age_5_to_9))
                    list_age10to14 += (int(a.age_10_to_14))
                    list_age15to19 += (int(a.age_15_to_19))
                    list_age20to24 += (int(a.age_20_to_24))
                    list_age25to29 += (int(a.age_25_to_29))
                    list_age30to34 += (int(a.age_30_to_34))
                    list_age35to39 += (int(a.age_35_to_39))
                    list_age40to44 += (int(a.age_40_to_44))
                    list_age45to49 += (int(a.age_45_to_49))
                    list_age50to54 += (int(a.age_50_to_54))
                    list_age55to59 += (int(a.age_55_to_59))
                    list_age60to64 += (int(a.age_60_to_64))
                    list_age65to69 += (int(a.age_65_to_69))
                    list_age70to74 += (int(a.age_70_to_74))
                    list_age75to79 += (int(a.age_75_to_79))
                    list_age80to84 += (int(a.age_80_to_84))
                    list_agegreaterthan85 += (int(a.age_greater_than_85))
                    list_ageunknown += (int(a.age_unknown))
    dic["ageslessthan5"] = list_agelessthan_5/list_allages
    dic["age5to9"] = list_age5to9/list_allages
    dic["age10to14"] = list_age10to14/list_allages
    dic["age15to19"] = list_age15to19/list_allages
    dic["age20to24"] = list_age20to24/list_allages
    dic["age25to29"] = list_age25to29/list_allages
    dic["age30to34"] = list_age30to34/list_allages
    dic["age35to39"] = list_age35to39/list_allages
    dic["age40to44"] = list_age40to44/list_allages
    dic["age45to49"] = list_age45to49/list_allages
    dic["age50to54"] = list_age50to54/list_allages
    dic["age55to59"] = list_age55to59/list_allages
    dic["age60to64"] = list_age60to64/list_allages
    dic["age65to69"] = list_age65to69/list_allages
    dic["age70to74"] = list_age70to74/list_allages
    dic["age75to79"] = list_age75to79/list_allages
    dic["age80to84"] = list_age80to84/list_allages
    dic["agegreaterthan85"] = list_agegreaterthan85/list_allages
    dic["ageunknown"] = list_ageunknown/list_allages

    highest = max(dic.values())
    m = [k for k, v in dic.items() if v == highest]
    maximum = max(dic, key=dic.get)
    format = (dic[maximum])

    return ("Whites At Risk", m, format)
def black_non_hispanic_at_risk_age_group():
    dic = {}
    list_allages = 0
    list_agelessthan_5 = 0
    list_age5to9 = 0
    list_age10to14 = 0
    list_age15to19 = 0
    list_age20to24 = 0
    list_age25to29 = 0
    list_age30to34 = 0
    list_age35to39 = 0
    list_age40to44 = 0
    list_age45to49 = 0
    list_age50to54 = 0
    list_age55to59 = 0
    list_age60to64 = 0
    list_age65to69 = 0
    list_age70to74 = 0
    list_age75to79 = 0
    list_age80to84 = 0
    list_agegreaterthan85 = 0
    list_ageunknown = 0
    for a in read_database():
        if a.cause_of_death == str('"X60-X84,Y87.0 Suicide"'):
            if a.race_ethnicity == str('"BLACK, NON-HISPANIC"'):
                if a.sex == str("BOTH SEXES"):
                    list_allages += (int(a.all_ages))
                    list_agelessthan_5 += (int(a.age_less_than_5))
                    list_age5to9 += (int(a.age_5_to_9))
                    list_age10to14 += (int(a.age_10_to_14))
                    list_age15to19 += (int(a.age_15_to_19))
                    list_age20to24 += (int(a.age_20_to_24))
                    list_age25to29 += (int(a.age_25_to_29))
                    list_age30to34 += (int(a.age_30_to_34))
                    list_age35to39 += (int(a.age_35_to_39))
                    list_age40to44 += (int(a.age_40_to_44))
                    list_age45to49 += (int(a.age_45_to_49))
                    list_age50to54 += (int(a.age_50_to_54))
                    list_age55to59 += (int(a.age_55_to_59))
                    list_age60to64 += (int(a.age_60_to_64))
                    list_age65to69 += (int(a.age_65_to_69))
                    list_age70to74 += (int(a.age_70_to_74))
                    list_age75to79 += (int(a.age_75_to_79))
                    list_age80to84 += (int(a.age_80_to_84))
                    list_agegreaterthan85 += (int(a.age_greater_than_85))
                    list_ageunknown += (int(a.age_unknown))
    dic["ageslessthan5"] = list_agelessthan_5 / list_allages
    dic["age5to9"] = list_age5to9 / list_allages
    dic["age10to14"] = list_age10to14 / list_allages
    dic["age15to19"] = list_age15to19 / list_allages
    dic["age20to24"] = list_age20to24 / list_allages
    dic["age25to29"] = list_age25to29 / list_allages
    dic["age30to34"] = list_age30to34 / list_allages
    dic["age35to39"] = list_age35to39 / list_allages
    dic["age40to44"] = list_age40to44 / list_allages
    dic["age45to49"] = list_age45to49 / list_allages
    dic["age50to54"] = list_age50to54 / list_allages
    dic["age55to59"] = list_age55to59 / list_allages
    dic["age60to64"] = list_age60to64 / list_allages
    dic["age65to69"] = list_age65to69 / list_allages
    dic["age70to74"] = list_age70to74 / list_allages
    dic["age75to79"] = list_age75to79 / list_allages
    dic["age80to84"] = list_age80to84 / list_allages
    dic["agegreaterthan85"] = list_agegreaterthan85 / list_allages
    dic["ageunknown"] = list_ageunknown / list_allages

    highest = max(dic.values())
    m = [k for k, v in dic.items() if v == highest]
    maximum = max(dic, key=dic.get)
    format = (dic[maximum])

    return ("Blacks At Risk", m, format)
def hispanic_at_risk_age_group():
    dic = {}
    list_allages = 0
    list_agelessthan_5 = 0
    list_age5to9 = 0
    list_age10to14 = 0
    list_age15to19 = 0
    list_age20to24 = 0
    list_age25to29 = 0
    list_age30to34 = 0
    list_age35to39 = 0
    list_age40to44 = 0
    list_age45to49 = 0
    list_age50to54 = 0
    list_age55to59 = 0
    list_age60to64 = 0
    list_age65to69 = 0
    list_age70to74 = 0
    list_age75to79 = 0
    list_age80to84 = 0
    list_agegreaterthan85 = 0
    list_ageunknown = 0
    for a in read_database():
        if a.cause_of_death == str('"X60-X84,Y87.0 Suicide"'):
            if a.race_ethnicity == str('"HISPANIC, ANY RACE"'):
                if a.sex == str("BOTH SEXES"):
                    list_allages += (int(a.all_ages))
                    list_agelessthan_5 += (int(a.age_less_than_5))
                    list_age5to9 += (int(a.age_5_to_9))
                    list_age10to14 += (int(a.age_10_to_14))
                    list_age15to19 += (int(a.age_15_to_19))
                    list_age20to24 += (int(a.age_20_to_24))
                    list_age25to29 += (int(a.age_25_to_29))
                    list_age30to34 += (int(a.age_30_to_34))
                    list_age35to39 += (int(a.age_35_to_39))
                    list_age40to44 += (int(a.age_40_to_44))
                    list_age45to49 += (int(a.age_45_to_49))
                    list_age50to54 += (int(a.age_50_to_54))
                    list_age55to59 += (int(a.age_55_to_59))
                    list_age60to64 += (int(a.age_60_to_64))
                    list_age65to69 += (int(a.age_65_to_69))
                    list_age70to74 += (int(a.age_70_to_74))
                    list_age75to79 += (int(a.age_75_to_79))
                    list_age80to84 += (int(a.age_80_to_84))
                    list_agegreaterthan85 += (int(a.age_greater_than_85))
                    list_ageunknown += (int(a.age_unknown))
    dic["ageslessthan5"] = list_agelessthan_5 / list_allages
    dic["age5to9"] = list_age5to9 / list_allages
    dic["age10to14"] = list_age10to14 / list_allages
    dic["age15to19"] = list_age15to19 / list_allages
    dic["age20to24"] = list_age20to24 / list_allages
    dic["age25to29"] = list_age25to29 / list_allages
    dic["age30to34"] = list_age30to34 / list_allages
    dic["age35to39"] = list_age35to39 / list_allages
    dic["age40to44"] = list_age40to44 / list_allages
    dic["age45to49"] = list_age45to49 / list_allages
    dic["age50to54"] = list_age50to54 / list_allages
    dic["age55to59"] = list_age55to59 / list_allages
    dic["age60to64"] = list_age60to64 / list_allages
    dic["age65to69"] = list_age65to69 / list_allages
    dic["age70to74"] = list_age70to74 / list_allages
    dic["age75to79"] = list_age75to79 / list_allages
    dic["age80to84"] = list_age80to84 / list_allages
    dic["agegreaterthan85"] = list_agegreaterthan85 / list_allages
    dic["ageunknown"] = list_ageunknown / list_allages

    highest = max(dic.values())
    m = [k for k, v in dic.items() if v == highest]
    maximum = max(dic, key=dic.get)
    format = (dic[maximum])

    return ("Hispanic At Risk",m ,format)
def other_non_hispanic_at_risk_age_group():
    dic = {}
    list_allages = 0
    list_agelessthan_5 = 0
    list_age5to9 = 0
    list_age10to14 = 0
    list_age15to19 = 0
    list_age20to24 = 0
    list_age25to29 = 0
    list_age30to34 = 0
    list_age35to39 = 0
    list_age40to44 = 0
    list_age45to49 = 0
    list_age50to54 = 0
    list_age55to59 = 0
    list_age60to64 = 0
    list_age65to69 = 0
    list_age70to74 = 0
    list_age75to79 = 0
    list_age80to84 = 0
    list_agegreaterthan85 = 0
    list_ageunknown = 0
    for a in read_database():
        if a.cause_of_death == str('"X60-X84,Y87.0 Suicide"'):
            if a.race_ethnicity == str('"OTHER, NON-HISPANIC"'):
                if a.sex == str("BOTH SEXES"):
                    list_allages += (int(a.all_ages))
                    list_agelessthan_5 += (int(a.age_less_than_5))
                    list_age5to9 += (int(a.age_5_to_9))
                    list_age10to14 += (int(a.age_10_to_14))
                    list_age15to19 += (int(a.age_15_to_19))
                    list_age20to24 += (int(a.age_20_to_24))
                    list_age25to29 += (int(a.age_25_to_29))
                    list_age30to34 += (int(a.age_30_to_34))
                    list_age35to39 += (int(a.age_35_to_39))
                    list_age40to44 += (int(a.age_40_to_44))
                    list_age45to49 += (int(a.age_45_to_49))
                    list_age50to54 += (int(a.age_50_to_54))
                    list_age55to59 += (int(a.age_55_to_59))
                    list_age60to64 += (int(a.age_60_to_64))
                    list_age65to69 += (int(a.age_65_to_69))
                    list_age70to74 += (int(a.age_70_to_74))
                    list_age75to79 += (int(a.age_75_to_79))
                    list_age80to84 += (int(a.age_80_to_84))
                    list_agegreaterthan85 += (int(a.age_greater_than_85))
                    list_ageunknown += (int(a.age_unknown))
    dic["ageslessthan5"] = list_agelessthan_5 / list_allages
    dic["age5to9"] = list_age5to9 / list_allages
    dic["age10to14"] = list_age10to14 / list_allages
    dic["age15to19"] = list_age15to19 / list_allages
    dic["age20to24"] = list_age20to24 / list_allages
    dic["age25to29"] = list_age25to29 / list_allages
    dic["age30to34"] = list_age30to34 / list_allages
    dic["age35to39"] = list_age35to39 / list_allages
    dic["age40to44"] = list_age40to44 / list_allages
    dic["age45to49"] = list_age45to49 / list_allages
    dic["age50to54"] = list_age50to54 / list_allages
    dic["age55to59"] = list_age55to59 / list_allages
    dic["age60to64"] = list_age60to64 / list_allages
    dic["age65to69"] = list_age65to69 / list_allages
    dic["age70to74"] = list_age70to74 / list_allages
    dic["age75to79"] = list_age75to79 / list_allages
    dic["age80to84"] = list_age80to84 / list_allages
    dic["agegreaterthan85"] = list_agegreaterthan85 / list_allages
    dic["ageunknown"] = list_ageunknown / list_allages

    highest = max(dic.values())
    m = [k for k, v in dic.items() if v == highest]
    maximum = max(dic, key=dic.get)
    format = (dic[maximum])

    return ("Other At Risk", m, format)


def suicides_total_white():
    allages = 0
    count = 1999
    for a in read_database():
        if count < 2012:
            if a.death_year == str(count):
                if a.cause_of_death == str('"X60-X84,Y87.0 Suicide"'):
                    if a.race_ethnicity == str('"WHITE, NON-HISPANIC"'):
                        if a.sex == str("BOTH SEXES"):
                            allages =+ (int(a.all_ages))
                            count += 1

    suiciderate = allages/total_deaths_for_all_year_whites()
    return "White Suicide Rate", suiciderate
def total_deaths_for_all_year_whites():
    total_deaths = 0
    for a in read_database():
        if a.cause_of_death == str('"TOTAL, ALL CAUSES"'):
            if a.sex == str("BOTH SEXES"):
                if a.race_ethnicity == ('"WHITE, NON-HISPANIC"'):
                    total_deaths =+ (int(a.all_ages))
    return total_deaths

def suicides_total_black():
    allages = 0
    count = 1999
    for a in read_database():
        if count < 2012:
            if a.death_year == str(count):
                if a.cause_of_death == str('"X60-X84,Y87.0 Suicide"'):
                    if a.race_ethnicity == str('"BLACK, NON-HISPANIC"'):
                        if a.sex == str("BOTH SEXES"):
                            allages =+ (int(a.all_ages))
                            count += 1

    suiciderate = allages/total_deaths_for_all_year_black()
    return "Black Suicide Rate", suiciderate
def total_deaths_for_all_year_black():
    total_deaths = 0
    for a in read_database():
        if a.cause_of_death == str('"TOTAL, ALL CAUSES"'):
            if a.sex == str("BOTH SEXES"):
                if a.race_ethnicity == ('"BLACK, NON-HISPANIC"'):
                    total_deaths =+ (int(a.all_ages))
    return total_deaths

def suicides_total_hispanics():
    allages = 0
    count = 1999
    for a in read_database():
        if count < 2012:
            if a.death_year == str(count):
                if a.cause_of_death == str('"X60-X84,Y87.0 Suicide"'):
                    if a.race_ethnicity == str('"HISPANIC, ANY RACE"'):
                        if a.sex == str("BOTH SEXES"):
                            allages =+ (int(a.all_ages))
                            count += 1

    suiciderate = allages/total_deaths_for_all_year_hispanics()
    return "Hispanic Suicide Rate", suiciderate
def total_deaths_for_all_year_hispanics():
    total_deaths = 0
    for a in read_database():
        if a.cause_of_death == str('"TOTAL, ALL CAUSES"'):
            if a.sex == str("BOTH SEXES"):
                if a.race_ethnicity == ('"HISPANIC, ANY RACE"'):
                    total_deaths =+ (int(a.all_ages))
    return total_deaths

def suicides_total_other():
    allages = 0
    count = 1999
    for a in read_database():
        if count < 2012:
            if a.death_year == str(count):
                if a.cause_of_death == str('"X60-X84,Y87.0 Suicide"'):
                    if a.race_ethnicity == str('"OTHER, NON-HISPANIC"'):
                        if a.sex == str("BOTH SEXES"):
                            allages =+ (int(a.all_ages))
                            count += 1

    suiciderate = allages/total_deaths_for_all_year_other()
    return "Other Suicide Rate", suiciderate
def total_deaths_for_all_year_other():
    total_deaths = 0
    for a in read_database():
        if a.cause_of_death == str('"TOTAL, ALL CAUSES"'):
            if a.sex == str("BOTH SEXES"):
                if a.race_ethnicity == ('"OTHER, NON-HISPANIC"'):
                    total_deaths =+ (int(a.all_ages))
    return total_deaths

if __name__ == "__main__":
    read_database()
    print(white_non_hispanic_at_risk_age_group())
    print(black_non_hispanic_at_risk_age_group())
    print(hispanic_at_risk_age_group())
    print(other_non_hispanic_at_risk_age_group())

    print(suicides_total_white())
    print(suicides_total_black())
    print(suicides_total_hispanics())
    print(suicides_total_other())
