*** Notgeld with controls ***

*use "D:\SarahSchaller\Universität Bayreuth\Öztürk, Volkan Timur - Württemberg_DFG\Sarah_Project_Notgeld\Braun_Franke_2022_data_full_sample.dta", clear

* keep ID year ind_popshare_occ agr_popshare_occ trade_popshare_occ tax_income_base_priv_pc d_steamengine pop_log

* steam engine data latest for 1867

* created by Timur using Python:

*use "D:\SarahSchaller\Universität Bayreuth\Öztürk, Volkan Timur - Württemberg_DFG\Sarah_Project_Notgeld\Dataset_Edited_With_Loop.dta", clear

use "E:\Sarah Schaller\Universität Bayreuth\Öztürk, Volkan Timur - Dokumente\Württemberg_DFG\Sarah_Project_Notgeld\Dataset_Edited_With_Loop.dta", clear


* data for 1905, except steam engine dummy which is for 1867:
keep if year==1905

*merge 1:1 ID using "D:\SarahSchaller\Universität Bayreuth\Öztürk, Volkan Timur - Württemberg_DFG\Sarah_Project_Notgeld\Notgeld"

merge 1:1 ID using "E:\Sarah Schaller\Universität Bayreuth\Öztürk, Volkan Timur - Dokumente\Württemberg_DFG\Sarah_Project_Notgeld\Notgeld"


* drop 7 observations from using dataset because for them notgeld=0
drop if _ == 2

* replace with zero for the 101 observations from master dataset that could not be matched
replace notgeld = 0 if _ == 1


* regressions

reg notgeld agr_popshare_occ trade_popshare_occ tax_income_base_priv_pc d_steamengine pop_log

reg notgeld ind_popshare_occ

reg notgeld agr_popshare_occ

reg notgeld trade_popshare_occ

reg notgeld tax_income_base_priv_pc

reg notgeld pop_log

* logistic regression (https://blogs.ubc.ca/datawithstata/home-page/regression/ordinary-least-square/)

logistic notgeld ind_popshare_occ agr_popshare_occ trade_popshare_occ tax_income_base_priv_pc d_steamengine pop_log
margins, dydx(*)

* kernel density

twoway (kdensity ind_popshare_occ if notgeld == 0) (kdensity ind_popshare_occ if notgeld == 1), legend(pos(6) row(1) lab(1 "Gemeinden ohne Notgeld") lab(2 "Gemeinden mit Notgeld"))

twoway (kdensity agr_popshare_occ if notgeld == 0) (kdensity agr_popshare_occ if notgeld == 1), legend(pos(6) row(1) lab(1 "Gemeinden ohne Notgeld") lab(2 "Gemeinden mit Notgeld"))

twoway (kdensity trade_popshare_occ if notgeld == 0) (kdensity trade_popshare_occ if notgeld == 1), legend(pos(6) row(1) lab(1 "Gemeinden ohne Notgeld") lab(2 "Gemeinden mit Notgeld"))

twoway (kdensity tax_income_base_priv_pc if notgeld == 0) (kdensity agr_popshare_occ if notgeld == 1), legend(pos(6) row(1) lab(1 "Gemeinden ohne Notgeld") lab(2 "Gemeinden mit Notgeld"))

twoway (kdensity d_steamengine if notgeld == 0) (kdensity d_steamengine if notgeld == 1), legend(pos(6) row(1) lab(1 "Gemeinden ohne Notgeld") lab(2 "Gemeinden mit Notgeld"))

twoway (kdensity pop_log if notgeld == 0) (kdensity pop_log if notgeld == 1), legend(pos(6) row(1) lab(1 "Gemeinden ohne Notgeld") lab(2 "Gemeinden mit Notgeld"))

