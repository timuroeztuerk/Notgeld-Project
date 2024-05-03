*** Notgeld dataset with controls ***

clear all

global AVZ "D:\SarahSchaller\Universität Bayreuth\Öztürk, Volkan Timur - Württemberg_DFG\Sarah_Project_Notgeld"

global MY_IN_PATH "$AVZ"

global MY_DO_FILES "$AVZ\do\"

global MY_LOG_OUT "$AVZ\log\"

global MY_OUT_DATA "$AVZ\output\"

global MY_OUT_TEMP "$AVZ\temp\"


use "$AVZ/Controls_Cleaned.dta" 

keep if year==1907

drop married_f population_local_f population_local_m

merge 1:1 ID using "$AVZ/Notgeld"

drop _merge

*** first regressions ***


reg notgeld pop_1907

egen agri_share 