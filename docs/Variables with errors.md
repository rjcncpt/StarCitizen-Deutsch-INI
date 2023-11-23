# Incorrect variables in the English global.ini

| global.ini                                                     | Correct variable                                              |
| -------------------------------------------------------------- | :------------------------------------------------------------ |
| `seachbody_obj_short_02a=`                                     | `searchbody_obj_short_02a=`                                   |
| `ea_ui_matchmaking_error_CanceledByService =`                  | `ea_ui_matchmaking_error_CanceledByService=`                  |
| `Tut03_Part01_Obj01b_ToStation =`                              | `Tut03_Part01_Obj01b_ToStation=`                              |
| `~mission (description)`                                       | `~mission(description)`                                       |
| `~mission (title)`                                             | `~mission(title)`                                             |
| `~mission (item)`                                              | `~mission(item)`                                              |
| `~misssion(Item)`                                              | `~mission(Item)`                                              |
| `shop_ui_transactionResult_04 _InvalidPlayerInventoryId=`      | `shop_ui_transactionResult_04_InvalidPlayerInventoryId=`      |
| `shop_ui_transactionResult_05 _InventoryContainerRequestFail=` | `shop_ui_transactionResult_05_InventoryContainerRequestFail=` |
| `shop_ui_transactionResult_06 _InventoryItemFail=`             | `shop_ui_transactionResult_06_InventoryItemFail=`             |
| `Oxygen_Screen_ ErrorButtonMessage=`                           | `Oxygen_Screen_ErrorButtonMessage=`                           |

# Missing variables

| global.ini                                        | Description                                                                                                                                        |
| ------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------- |
| `???d_mining_gather???`                           | This variable is missing and is shown in the multitool display when collecting hand-mined minerals. Currently in ini: `ui_weapons_multi_gathering` |
| `itemPort_Canister_ATTACH`                        | This variable is missing and is shown in the multitool customization. Currently in ini `itemPort_CanisterSlot`                                     |
| `DXSM_SSCV_DRAK_OEM_UI_Shields_Left_75_Percent,P` | This variable is missing. 75% is available for all other sides.                                                                                    |
| `pause_Options_salvage_aim_nudge_sensivity`       | This variable is missing. Options menu -> Game Settings                                                                                            |
