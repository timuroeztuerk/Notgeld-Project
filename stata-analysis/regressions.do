cd "C:\Users\bt307300\Desktop\notgeld\stata-analysis"

import delimited "C:\Users\bt307300\Desktop\notgeld\stata-analysis\wurttemberg-reichsbank-database.csv", clear

drop v1 geometry
rename ıd ID

merge 1:1 ID using "C:\Users\bt307300\Desktop\notgeld\stata-analysis\outcomes-and-controls.dta"

drop _

merge 1:1 ID using "C:\Users\bt307300\Desktop\notgeld\stata-analysis\agr-share.dta"

drop _

reg count distance, robust

reg count distance pop, robust

reg count distance reichsbank population_ipolate d_steam_engine_1869 road_dummy inheritance_type_v1, robust

reg count distance reichsbank agr population_ipolate d_steam_engine_1869 road_dummy inheritance_type_v1, robust

reg count distance agr, robust

keep if pop < 5000

reg count distance population_ipolate d_steam_engine_1869 road_dummy inheritance_type_v1, robust

reg count distance agr population_ipolate d_steam_engine_1869 road_dummy inheritance_type_v1, robust

reg count distance agr, robust
