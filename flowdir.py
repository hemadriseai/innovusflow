import os,shutil
mode=0o777

##########customscripts directory###########
#####dont change anything inside##########
try:
	name="centralscripts"
	project=['project']
	block=["blockname"]
	tools=["innovus","genus","lec","calibre","voltus","starRc"]
	sub_plug=["scripts","inputs","customscripts","input_lib"]
	for projects in project:
		for blocks in block:
			for tool in tools:
				for plug in sub_plug:
					os.makedirs(os.path.join(name,projects,blocks,tool,plug),mode=mode)
except FileExistsError:pass
except Exception as e:print(e)

#########directory structure#######

pname=str.strip(input("enter the name of your project : "))
run=input("enter the run {ex: run1 run2 ...}  : " )
projectname=pname
rtlrelease=["1.0"]
prog=["blockname"]
f=['PD','RTL','DV','SYNTH','STA','EMIR','PV','LEC','INPUT_LIB']
workarea='username'
runname=run
level1=['logs','reports','outputs','inputs','data','scripts','customscripts','snapshots']
stages=['Floorplan','Place','CTS','Route']
csv_folder="csv"
for rtlreleases in rtlrelease: 
	for progs in prog:
		for i in f:
			for k in level1:		
				os.makedirs(os.path.join(projectname,rtlreleases,progs,i,workarea,runname),mode=mode,exist_ok=True)
				if ((i =='PD') or (i=='SYNTH')):
					os.makedirs(os.path.join(projectname,rtlreleases,progs,i,workarea,runname,k),mode=mode,exist_ok=True)
					pdpath=os.path.join(projectname,rtlreleases,progs,i,workarea,runname,k)
					if ((k=='reports') or (k=='outputs') or (k=='logs') or (k=='data')):
						if (k=='reports'):
							if (i=='PD'):
								for j in stages:
									os.makedirs(os.path.join(pdpath,j,csv_folder),mode=mode,exist_ok=True)
						if ((k=='outputs') or (k=='logs') or (k=='data')):
							if (i=='PD'):
								for j in stages:
									os.makedirs(os.path.join(pdpath,j),mode=mode,exist_ok=True)
						if (k=='reports') :
							if (i=='SYNTH'):
								os.makedirs(os.path.join(pdpath,csv_folder),mode=mode,exist_ok=True)
					
			if (i=='PD'):
				try:
					shutil.copytree(f"{name}/{project[0]}/{block[0]}/innovus/inputs",f"{pname}/{rtlreleases}/{progs}/{i}/{workarea}/{run}/inputs",dirs_exist_ok=True)
					shutil.copytree(f"{name}/{project[0]}/{block[0]}/innovus/scripts",f"{pname}/{rtlreleases}/{progs}/{i}/{workarea}/{run}/scripts",dirs_exist_ok=True)
					shutil.copytree(f"{name}/{project[0]}/{block[0]}/innovus/customscripts",f"{pname}/{rtlreleases}/{progs}/{i}/{workarea}/{run}/customscripts",dirs_exist_ok=True)
				except Exception as e:print(e)
			if (i=='SYNTH'):
				try:
					shutil.copytree(f"{name}/{project[0]}/{block[0]}/genus/inputs",f"{pname}/{rtlreleases}/{progs}/{i}/{workarea}/{run}/inputs",dirs_exist_ok=True)
					shutil.copytree(f"{name}/{project[0]}/{block[0]}/genus/scripts",f"{pname}/{rtlreleases}/{progs}/{i}/{workarea}/{run}/scripts",dirs_exist_ok=True)
					shutil.copytree(f"{name}/{project[0]}/{block[0]}/genus/customscripts",f"{pname}/{rtlreleases}/{progs}/{i}/{workarea}/{run}/customscripts",dirs_exist_ok=True)
				except Exception as e:print(e)


