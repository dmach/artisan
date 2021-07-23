import prettytable
import re
from PyQt5.QtWidgets import QApplication

def content():
    strlist = []
    helpstr = ''  #@UnusedVariable
    newline = '\n'  #@UnusedVariable
    strlist.append('<head><style> td, th {border: 1px solid #ddd;  padding: 6px;} th {padding-top: 6px;padding-bottom: 6px;text-align: left;background-color: #0C6AA6; color: white;} </style></head> <body>')
    strlist.append("<b>")
    strlist.append(QApplication.translate('HelpDlg','Energy and CO2 Calculator',None))
    strlist.append("</b>")
    tbl_Introtop = prettytable.PrettyTable()
    tbl_Introtop.header = False
    tbl_Introtop.add_row([QApplication.translate('HelpDlg','The Energy tab displays a roast&#39;s energy consumption.   CO2 emissions are also calculated to monitor the impact of the roasting operation.  Settings must be made for each energy load.  Loads are the main burners, motors and blowers, and an afterburner if one is used.  The energy used for preheating, between batch, and roaster cooling protocols are included in the calculations, and settings are available for them as well.\n\nNote that pre-heating and roaster cooling energy values are applied to the first roast of a roasting session.  Between batch energies are applied to every roast except the first.  Tick the "Between batches after Pre-Heating box to apply the between batch value to the first roast.\n\nFollow the steps below to set the energy inputs for the roast machine and afterburner.',None)+newline+QApplication.translate('HelpDlg','',None)+newline+QApplication.translate('HelpDlg','Blank entries  are the same as a zero entry.  Negative values are not allowed.',None)])
    strlist.append(tbl_Introtop.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    tbl_Introbottom = prettytable.PrettyTable()
    tbl_Introbottom.header = False
    tbl_Introbottom.add_row([QApplication.translate('HelpDlg','Once you set up the Loads sub-tab and the Protocols sub-tab, it is a good idea to click "Save Defaults" on both  sub-tabs (they are saved separately).  When loading a profile with existing energy values, the profile settings will be read and will overwrite the values on the Loads and Profiles sub-tabs.  Having them saved as defaults allow for them to be quickly restored by clicking "Restore Defaults" on each sub-tab.',None)])
    strlist.append(tbl_Introbottom.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("<br/><br/><b>")
    strlist.append(QApplication.translate('HelpDlg','1. Details Sub-Tab',None))
    strlist.append("</b>")
    tbl_Detailstop = prettytable.PrettyTable()
    tbl_Detailstop.header = False
    tbl_Detailstop.add_row([QApplication.translate('HelpDlg','This sub-tab shows a detailed table of the energy consumption and CO2 production data for the roast.  The values in this table are based on current Profile and the settings made on the Loads and Protocols sub-tabs.  Columns may be sorted by clicking on the column title.  To return to original sort click on the &#39;Kind&#39; column title.',None)])
    strlist.append(tbl_Detailstop.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    tbl_Details = prettytable.PrettyTable()
    tbl_Details.field_names = [QApplication.translate('HelpDlg','Field',None),QApplication.translate('HelpDlg','Description',None)]
    tbl_Details.add_row([QApplication.translate('HelpDlg','Results in',None),QApplication.translate('HelpDlg','Choose the energy units for the summary displays and the Details sub-tab.',None)])
    strlist.append(tbl_Details.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("<br/><br/><b>")
    strlist.append(QApplication.translate('HelpDlg','2. Loads Sub-Tab',None))
    strlist.append("</b>")
    tbl_Loadstop = prettytable.PrettyTable()
    tbl_Loadstop.header = False
    tbl_Loadstop.add_row([QApplication.translate('HelpDlg','Begin by making entries on the Loads sub-tab  to define the sources of energy used by this roast. It might be a good idea to save those settings as defaults to be used to calculate the energy consumption of future roasts',None)+newline+QApplication.translate('HelpDlg','',None)+newline+QApplication.translate('HelpDlg','Power ratings for up to four energy loads may be entered.  Loads will be the main burners or heaters, motors and blowers, and the afterburner if one is used.  Enter one load per line.  Motors and blowers that run continuously may be aggregated and entered as one load.',None)+newline+QApplication.translate('HelpDlg','',None)+newline+QApplication.translate('HelpDlg','Loads are assumed to run continuously. Variable loads, such as the main burner setting, can be recorded in Artisan using one of the four special events.  The settings can be captured from a button, slider or in some cases read directly from the roaster.  The load setup allows linking a load to one of these events.  The energy calculator will then determine the setting percentage and the duration of the setting to calculate the energy consumed.',None)+newline+QApplication.translate('HelpDlg','',None)+newline+QApplication.translate('HelpDlg','Burner entries require knowing the power rating of the burner.  Roasting machine manufacturer&#39;s typically provide this information.  If this information can not be found for your machine this table provides approximate values based on roaster capacities.  https://artisan-scope.org/ratings/',None)])
    strlist.append(tbl_Loadstop.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    tbl_Loads = prettytable.PrettyTable()
    tbl_Loads.field_names = [QApplication.translate('HelpDlg','Field',None),QApplication.translate('HelpDlg','Description',None)]
    tbl_Loads.add_row([QApplication.translate('HelpDlg','Label',None),QApplication.translate('HelpDlg','Enter your personal description for this burner.  Examples are &#39;Main&#39; and &#39;Afterburner&#39;.',None)])
    tbl_Loads.add_row([QApplication.translate('HelpDlg','Rating',None),QApplication.translate('HelpDlg','This is the power rating of the load  Choose the units in the next column.  ',None)])
    tbl_Loads.add_row([QApplication.translate('HelpDlg','Unit',None),QApplication.translate('HelpDlg','Select the appropriate power unit. Some manufacturers incorrectly use BTU.  In that case use BTU/h for the unit.',None)])
    tbl_Loads.add_row([QApplication.translate('HelpDlg','Fuel',None),QApplication.translate('HelpDlg','Select the type of fuel used by this load  &#39;Elec&#39; is assumed to be electricity generated from dirty coal.  There is a setting below to adjust for renewable clean energy sources.',None)])
    tbl_Loads.add_row([QApplication.translate('HelpDlg','Event',None),QApplication.translate('HelpDlg','Special Events are often used to record load settings, such as a burner setting, in the roast profile.  Select the Event that corresponds to the load setting here.  \n\nWhen blank the load is assumed to be at a constant setting, which is the percent &#39;Value 100%&#39; multiplied by the rating.  A 10 kW load at &#39;100% Value&#39;= 60 would thus be 10 kW * 60% = 6 kW. Continuous loads are typically motors and blowers and the afterburner.',None)])
    tbl_Loads.add_row([QApplication.translate('HelpDlg','Pressure %',None),QApplication.translate('HelpDlg','For gas loads tick this box when  the readings are made in units of pressure.  Some roasters and some controllers provide readings in heat energy.  When the readings are made in heat energy leave this box unticked.',None)])
    tbl_Loads.add_row([QApplication.translate('HelpDlg','Value 0%',None),QApplication.translate('HelpDlg','When an Event is selected in the previous column this value can be set to match the 0% burner setting to the event setting.  In most cases a 0 Event value will correspond to the 0% load setting.',None)])
    tbl_Loads.add_row([QApplication.translate('HelpDlg','Value 100%',None),QApplication.translate('HelpDlg','When an Event is selected this value can be set to match the 100% load setting to the event setting.  This is useful when the 100% load setting is recorded as a different number in the Event.  For instance, maybe the burner event is recorded as 10x the kPa reading on the gas manometer.  An event value of 35 is recoded to signify 3.5 kPa, which is 50% pressure.  If the 100% burner setting corresponds to 7 kPa then the &#39;Value 100%&#39; should be set to 70, which is 7 * 10  = 70.  Thus 3.5 kPa will be seen by he energy calculator as 50%.  For pressure readings be sure to tick the Pressure box.  Heat energy readings are normally 0%-100% and do not require any adjustment to this  setting.',None)])
    tbl_Loads.add_row([QApplication.translate('HelpDlg','Electric Energy Mix',None),QApplication.translate('HelpDlg','This setting allows to set a mix of renewable energy that sources the electric loads.  0% assumes all the energy comes from burning dirty coal and maximizes the CO2 in the calculations.  100% assumes the energy comes only from renewable sources with no CO2 produced.',None)])
    tbl_Loads.add_row([QApplication.translate('HelpDlg','Save Defaults',None),QApplication.translate('HelpDlg','Stores the current settings on this sub-tab as defaults to be recalled later.  The default values will be stored when saving settings (Help>Save Settings) to a file.  ',None)])
    tbl_Loads.add_row([QApplication.translate('HelpDlg','Restore Defaults',None),QApplication.translate('HelpDlg','Overwrites the values on this sub-tab with those stored as the defaults.  When a profile with energy settings is opened, the values on this tab will be read from the profile.   They will be overwritten when clicking Restore Defaults.',None)])
    strlist.append(tbl_Loads.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("<br/><br/><b>")
    strlist.append(QApplication.translate('HelpDlg','3. Protocol Sub-Tab',None))
    strlist.append("</b>")
    tbl_Protocoltop = prettytable.PrettyTable()
    tbl_Protocoltop.header = False
    tbl_Protocoltop.add_row([QApplication.translate('HelpDlg','The Protocol settings allow including Pre-Heating, Between Batch (BBP) and Cooling protocol energy consumption.  There are two ways to specify these values.  The first assumes a constant load setting for a defined period of time.  An example for Preheating is to set a Duration of 45:00 (45 minutes) at 30% Burner setting.  Percentages may be entered either as a decimal (.30) or a percentage (30%).  When a percentage is entered  a corresponding Duration must be entered.',None)+newline+QApplication.translate('HelpDlg','',None)+newline+QApplication.translate('HelpDlg','The second type of entry is a "measured" energy value.  This can be any value greater than 1.0.  Artisan can inspect the open profile to determine energy values for each Load that is associated with an Event on the Loads sub-tab.  Click the [...] button for each Protocol to auto fill the Measured Energy fields.   The Artisan measurements for Pre-Heating and Between Batches are made from the start of the profile until CHARGE.  If there is no CHARGE event the measurement is from the start to the end of profile.  The values measured for Pre-Heating and Between Batches are the same.  Be sure you do not use the same profile to enter both values.  The Cooling energy is measured from DROP to the end of the profile.  If there is no DROP event the measurement begins at CHARGE.  If there is no CHARGE event the measurement is from the start to the end of the profile.',None)+newline+QApplication.translate('HelpDlg','',None)+newline+QApplication.translate('HelpDlg','To use the Artisan energy measurement feature you will need to record one or more profiles that include the protocol of interest.  For example, to measure the Pre-Heating energy, START recording when the roaster is turned on.  Let Artisan record the entire pre-heating procedure.  At the end of the pre-heating you can either STOP recording the profile or go forward with the roast.  The CHARGE event will mark the end of pre-heating when Artisan measures the pre-heat energy.  Similarly a Between Batches protocol can be recorded with START followed by a normal roast.  A Cooling protocol would be captured by not turning the Artisan recording OFF until the roaster is fully cooled.',None)+newline+QApplication.translate('HelpDlg','',None)+newline+QApplication.translate('HelpDlg','The Artisan measurements for Pre-Heating and Between Batches are made from the start of the profile until CHARGE.  If there is no CHARGE event the measurement is from the start to the end of profile.  The values measured for Pre-Heating and Between Batches are the same.  Be sure you do not use the same profile to enter both values.  The Cooling energy is measured from DROP to the end of the profile.  If there is no DROP event the measurement begins at CHARGE.  If there is no CHARGE event the measurement is from the start to the end of the profile.',None)])
    strlist.append(tbl_Protocoltop.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    tbl_Protocol = prettytable.PrettyTable()
    tbl_Protocol.field_names = [QApplication.translate('HelpDlg','Field',None),QApplication.translate('HelpDlg','Description',None)]
    tbl_Protocol.add_row([QApplication.translate('HelpDlg','Pre-Heating',None),QApplication.translate('HelpDlg','This row sets the values for pre-heating energy.  Percentage or measured values may be entered for each burner.  When a percentage is used the Duration field must be set.\n\nPre-Heating energy is applied only to the first batch of a roasting session.',None)])
    tbl_Protocol.add_row([QApplication.translate('HelpDlg','Between Batches',None),QApplication.translate('HelpDlg','This row sets the values for between batches protocol for the roasting session.  Percentage or measured values may be entered for each burner.  When a percentage is used the Duration field must be set.\n\nBetween Batches energy is applied to each batch of the roasting session, except the first batch.  Tick the &#39;Between Batches after Pre-Heating&#39; box to apply Between Batches energies to the first batch of the session too.',None)])
    tbl_Protocol.add_row([QApplication.translate('HelpDlg','Cooling',None),QApplication.translate('HelpDlg','This row sets the values for the energy used for cooling.  Most common loads are motors and blowers that consume energy during the roaster cool down period.  Percentage or measured values may be entered for each burner.  When a percentage is used the Duration field must be set.\n\nPre-Heating energy is applied only to the first batch of a roasting session.',None)])
    tbl_Protocol.add_row([QApplication.translate('HelpDlg','Duration',None),QApplication.translate('HelpDlg','The length (mm:ss) of protocol.  It is used with a burner&#39;s percentage setting to calculate the energy consumed  by that burner.  When a percentage entry is made for the burner, the Duration field must be set.',None)])
    tbl_Protocol.add_row([QApplication.translate('HelpDlg','Measured Energy or Output %',None),QApplication.translate('HelpDlg','The value is either the measured energy for the protocol or the burner constant percentage setting for the length of the Duration field.',None)])
    tbl_Protocol.add_row([QApplication.translate('HelpDlg','Measure Profile [...]',None),QApplication.translate('HelpDlg','Energy is measured from the open profile for each load where an event is specified on the Loads tab.  Click OK to auto fill in the associated Measured Energy field.',None)])
    tbl_Protocol.add_row([QApplication.translate('HelpDlg','Between Batches after Pre-Heating',None),QApplication.translate('HelpDlg','This box should be ticked when a Between Batches protocol run is done after the Preheating and before the roast.',None)])
    tbl_Protocol.add_row([QApplication.translate('HelpDlg','Save Defaults',None),QApplication.translate('HelpDlg','Stores the current settings on this sub-tab as defaults to be recalled later.  The default values will be stored when saving settings (Help>Save Settings) to a file.  ',None)])
    tbl_Protocol.add_row([QApplication.translate('HelpDlg','Restore Defaults',None),QApplication.translate('HelpDlg','Overwrites the values on this sub-tab with those stored as the defaults.  When a profile with energy settings is opened, the values on this tab will be read from the profile.   They will be overwritten when clicking Restore Defaults.',None)])
    strlist.append(tbl_Protocol.get_html_string(attributes={"width":"100%","border":"1","padding":"1","border-collapse":"collapse"}))
    strlist.append("</body>")
    helpstr = "".join(strlist)
    helpstr = re.sub(r"&amp;", r"&",helpstr)
    return helpstr