bkp_t="~ Command `ProCmdModelOpen` \n~ Trail `UI Desktop` `UI Desktop` `DLG_PREVIEW_POST` \ \n `file_open`\n~ Update `file_open` `Inputname` `b.prt`\n~ FocusIn `file_open` `EMBED_BROWSER_SEARCH_IP`\n~ FocusOut `file_open` `EMBED_BROWSER_SEARCH_IP`\n~ Command `ProFileSelPushOpen@context_dlg_open_cmd`\n~ Command `ProCmdModelBackup` \n~ Update `file_saveas` `Inputname` `D:\\\\TO UTCIL SVN\\\\FROST SENSING\\\\CAD FILES`\n~ Activate `file_saveas` `OK`\n~ Command `ProCmdWinCloseGroup`"
b="C:\\Users\\Public\\Documents"
path=b.replace("\\","\\\\")
bkp=bkp_t.replace("D:\\\\TO UTCIL SVN\\\\FROST SENSING\\\\CAD FILES",path)
print(bkp_t)
print("\n\n\n\n")
print(bkp)
