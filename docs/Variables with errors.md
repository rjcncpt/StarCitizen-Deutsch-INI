# Incorrect variables in the English global.ini
Last updated: June 25, 2025

This information should help CIG correct the error:

```
Line:	GoblinG_MicroTech_RecoverCargo_S_Desc=
Bug:	<EM4>mission(Destination|Address)</EM4>
Fix:	<EM4>~mission(Destination|Address)</EM4>

Line:	item_shortMining_Head_S00_Arbor_SCItem,P=
Bug:	Arbor S00
Fix:	Arbor S0

Line:	item_shortMining_Head_S00_Hofstede_SCItem,P=
Bug:	Hofstede S00
Fix:	Hofstede S0

Line:	item_NameMining_Head_S00_Hofstede_SCItem,P=
Bug:	S00 Hofstede
Fix:	S0 Hofstede

Bug:	seachbody_obj_short_02a=
Fix:	searchbody_obj_short_02a=

Line:	item_Mining_Consumable_Lifeline_Desc=
Bug:	Laser Instability: -20
Fix:	Laser Instability: -20%

Bug:	vehicl_DescMISC_Hull_B=
Fix:	vehicle_DescMISC_Hull_B=

Bug:	Event_ShipTItle_TheGladius=
Fix:	Event_ShipTitle_TheGladius=

Line:	crusader_bounty_fps_tokenLink_Description=
Bug:	~(Contractor|BountyFPSDescription)
Fix:	~mission(Contractor|BountyFPSDescription)

Bug:	dfm_ui_param_FracKilometres=%.*f� km
Fix:	dfm_ui_param_FracKilometres=%.*f km

Line:	mg_clovus_bladesteal_obj_long_06=
Bug:	~misssion(Item)
Fix:	~mission(Item)

Line:	mg_miles_collectcargo_legal_desc=
Bug:	~mission (description)
Fix:	~mission(description)

Line:	mg_miles_collectcargo_legal_title=
Bug:	~mission (title)
Fix:	~mission(title)

Line:	mg_miles_delivercargo_lawful_var_0001=
Bug:	~mission (item)
Fix:	~mission(item)

Line:	Bacchus_Star2_Desc=
Bug:	Bacchus B
Fix:	Bacchus A

Line:	ui_CIMFDSoftSelectMFD10Long=
Bug:	MDF 10
Fix:	MFD 10

Line:	CFP_CH2_JournalTitleShort_Phase2=
Bug:	CFP Op. Reclaim Pyro -  Phase 2
Fix:	CFP Op. Reclaim Pyro - Phase 2

Line:	CFP_CH2_JournalTitle_Phase1=
Bug:	CFP Op. Reclaim Pyro -  Launch Summary
Fix:	CFP Op. Reclaim Pyro - Launch Summary

Line:	CFP_CH2_JournalTitle_Phase2=
Bug:	CFP Op. Reclaim Pyro -  Phase 2 Summary
Fix:	CFP Op. Reclaim Pyro - Phase 2 Summary
```
