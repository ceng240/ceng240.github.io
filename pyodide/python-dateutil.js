var Module=typeof pyodide._module!=="undefined"?pyodide._module:{};Module.checkABI(1);if(!Module.expectedDataFileDownloads){Module.expectedDataFileDownloads=0;Module.finishedDataFileDownloads=0}Module.expectedDataFileDownloads++;(function(){var loadPackage=function(metadata){var PACKAGE_PATH;if(typeof window==="object"){PACKAGE_PATH=window["encodeURIComponent"](window.location.pathname.toString().substring(0,window.location.pathname.toString().lastIndexOf("/"))+"/")}else if(typeof location!=="undefined"){PACKAGE_PATH=encodeURIComponent(location.pathname.toString().substring(0,location.pathname.toString().lastIndexOf("/"))+"/")}else{throw"using preloaded data can only be done on a web page or in a web worker"}var PACKAGE_NAME="python-dateutil.data";var REMOTE_PACKAGE_BASE="python-dateutil.data";if(typeof Module["locateFilePackage"]==="function"&&!Module["locateFile"]){Module["locateFile"]=Module["locateFilePackage"];err("warning: you defined Module.locateFilePackage, that has been renamed to Module.locateFile (using your locateFilePackage for now)")}var REMOTE_PACKAGE_NAME=Module["locateFile"]?Module["locateFile"](REMOTE_PACKAGE_BASE,""):REMOTE_PACKAGE_BASE;var REMOTE_PACKAGE_SIZE=metadata.remote_package_size;var PACKAGE_UUID=metadata.package_uuid;function fetchRemotePackage(packageName,packageSize,callback,errback){var xhr=new XMLHttpRequest;xhr.open("GET",packageName,true);xhr.responseType="arraybuffer";xhr.onprogress=function(event){var url=packageName;var size=packageSize;if(event.total)size=event.total;if(event.loaded){if(!xhr.addedTotal){xhr.addedTotal=true;if(!Module.dataFileDownloads)Module.dataFileDownloads={};Module.dataFileDownloads[url]={loaded:event.loaded,total:size}}else{Module.dataFileDownloads[url].loaded=event.loaded}var total=0;var loaded=0;var num=0;for(var download in Module.dataFileDownloads){var data=Module.dataFileDownloads[download];total+=data.total;loaded+=data.loaded;num++}total=Math.ceil(total*Module.expectedDataFileDownloads/num);if(Module["setStatus"])Module["setStatus"]("Downloading data... ("+loaded+"/"+total+")")}else if(!Module.dataFileDownloads){if(Module["setStatus"])Module["setStatus"]("Downloading data...")}};xhr.onerror=function(event){throw new Error("NetworkError for: "+packageName)};xhr.onload=function(event){if(xhr.status==200||xhr.status==304||xhr.status==206||xhr.status==0&&xhr.response){var packageData=xhr.response;callback(packageData)}else{throw new Error(xhr.statusText+" : "+xhr.responseURL)}};xhr.send(null)}function handleError(error){console.error("package error:",error)}var fetchedCallback=null;var fetched=Module["getPreloadedPackage"]?Module["getPreloadedPackage"](REMOTE_PACKAGE_NAME,REMOTE_PACKAGE_SIZE):null;if(!fetched)fetchRemotePackage(REMOTE_PACKAGE_NAME,REMOTE_PACKAGE_SIZE,function(data){if(fetchedCallback){fetchedCallback(data);fetchedCallback=null}else{fetched=data}},handleError);function runWithFS(){function assert(check,msg){if(!check)throw msg+(new Error).stack}Module["FS_createPath"]("/","lib",true,true);Module["FS_createPath"]("/lib","python3.7",true,true);Module["FS_createPath"]("/lib/python3.7","site-packages",true,true);Module["FS_createPath"]("/lib/python3.7/site-packages","dateutil",true,true);Module["FS_createPath"]("/lib/python3.7/site-packages/dateutil","tz",true,true);Module["FS_createPath"]("/lib/python3.7/site-packages/dateutil","zoneinfo",true,true);Module["FS_createPath"]("/lib/python3.7/site-packages/dateutil","parser",true,true);Module["FS_createPath"]("/lib/python3.7/site-packages","python_dateutil-2.8.1-py3.7.egg-info",true,true);function DataRequest(start,end,audio){this.start=start;this.end=end;this.audio=audio}DataRequest.prototype={requests:{},open:function(mode,name){this.name=name;this.requests[name]=this;Module["addRunDependency"]("fp "+this.name)},send:function(){},onload:function(){var byteArray=this.byteArray.subarray(this.start,this.end);this.finish(byteArray)},finish:function(byteArray){var that=this;Module["FS_createPreloadedFile"](this.name,null,byteArray,true,true,function(){Module["removeRunDependency"]("fp "+that.name)},function(){if(that.audio){Module["removeRunDependency"]("fp "+that.name)}else{err("Preloading file "+that.name+" failed")}},false,true);this.requests[this.name]=null}};function processPackageData(arrayBuffer){Module.finishedDataFileDownloads++;assert(arrayBuffer,"Loading data file failed.");assert(arrayBuffer instanceof ArrayBuffer,"bad input to processPackageData");var byteArray=new Uint8Array(arrayBuffer);var curr;var compressedData={data:null,cachedOffset:303573,cachedIndexes:[-1,-1],cachedChunks:[null,null],offsets:[0,1382,2538,3564,4505,5651,7010,8085,9286,10433,11219,12123,12876,13692,14709,15758,16708,17419,18270,19095,20302,21659,22689,23531,24486,25435,26443,27599,28626,29667,30758,31755,32541,33507,34948,36343,37624,38898,39912,40956,41845,42682,43338,44347,44957,45646,46408,47563,48926,50154,51375,52450,53441,54516,55864,57133,58144,59336,60343,61453,62654,63779,64979,66124,67097,68414,69628,70736,71950,73102,74107,74861,75730,76936,77961,78707,79727,80931,82290,83441,84533,85858,87065,88305,89270,90460,91497,92926,94041,95209,96521,97835,98985,100385,101798,103128,104398,106305,108353,110401,112449,114497,116545,118593,120641,122689,124737,126785,128833,130879,132935,134975,137023,139080,141137,143185,145229,147277,149325,151345,153402,155450,157498,159546,161602,163650,165698,167746,169794,171851,173899,175947,177995,180043,182091,184147,186195,188244,190257,192305,194353,196401,198458,200513,202561,204609,206657,208705,210753,212801,214857,216905,218953,220998,223046,225094,227142,229190,231238,233295,235348,237396,239444,241492,243540,245588,247636,249684,251732,253780,255828,257876,259337,260604,261633,262608,263695,264917,266095,267597,269015,270105,270842,271977,273111,274078,274997,276147,276970,278148,279346,280476,281356,282326,283352,284346,285172,286288,287525,288689,289795,290976,292224,293482,294389,295164,296058,296965,297987,299164,300448,301827,302980],sizes:[1382,1156,1026,941,1146,1359,1075,1201,1147,786,904,753,816,1017,1049,950,711,851,825,1207,1357,1030,842,955,949,1008,1156,1027,1041,1091,997,786,966,1441,1395,1281,1274,1014,1044,889,837,656,1009,610,689,762,1155,1363,1228,1221,1075,991,1075,1348,1269,1011,1192,1007,1110,1201,1125,1200,1145,973,1317,1214,1108,1214,1152,1005,754,869,1206,1025,746,1020,1204,1359,1151,1092,1325,1207,1240,965,1190,1037,1429,1115,1168,1312,1314,1150,1400,1413,1330,1270,1907,2048,2048,2048,2048,2048,2048,2048,2048,2048,2048,2048,2046,2056,2040,2048,2057,2057,2048,2044,2048,2048,2020,2057,2048,2048,2048,2056,2048,2048,2048,2048,2057,2048,2048,2048,2048,2048,2056,2048,2049,2013,2048,2048,2048,2057,2055,2048,2048,2048,2048,2048,2048,2056,2048,2048,2045,2048,2048,2048,2048,2048,2057,2053,2048,2048,2048,2048,2048,2048,2048,2048,2048,2048,2048,1461,1267,1029,975,1087,1222,1178,1502,1418,1090,737,1135,1134,967,919,1150,823,1178,1198,1130,880,970,1026,994,826,1116,1237,1164,1106,1181,1248,1258,907,775,894,907,1022,1177,1284,1379,1153,593],successes:[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,0,0,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]};compressedData.data=byteArray;assert(typeof Module.LZ4==="object","LZ4 not present - was your app build with  -s LZ4=1  ?");Module.LZ4.loadPackage({metadata:metadata,compressedData:compressedData});Module["removeRunDependency"]("datafile_python-dateutil.data")}Module["addRunDependency"]("datafile_python-dateutil.data");if(!Module.preloadResults)Module.preloadResults={};Module.preloadResults[PACKAGE_NAME]={fromCache:false};if(fetched){processPackageData(fetched);fetched=null}else{fetchedCallback=processPackageData}}if(Module["calledRun"]){runWithFS()}else{if(!Module["preRun"])Module["preRun"]=[];Module["preRun"].push(runWithFS)}};loadPackage({files:[{filename:"/lib/python3.7/site-packages/dateutil/_version.py",start:0,end:116,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/rrule.py",start:116,end:66855,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/__init__.py",start:66855,end:67077,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/tzwin.py",start:67077,end:67136,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/easter.py",start:67136,end:69820,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/_common.py",start:69820,end:70752,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/relativedelta.py",start:70752,end:95656,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/utils.py",start:95656,end:97615,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/tz/tz.py",start:97615,end:160547,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/tz/_factories.py",start:160547,end:163116,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/tz/__init__.py",start:163116,end:163560,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/tz/_common.py",start:163560,end:176537,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/tz/win.py",start:176537,end:189472,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/zoneinfo/rebuild.py",start:189472,end:191191,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/zoneinfo/__init__.py",start:191191,end:197080,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/zoneinfo/dateutil-zoneinfo.tar.gz",start:197080,end:350395,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/parser/isoparser.py",start:350395,end:363493,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/parser/__init__.py",start:363493,end:365259,audio:0},{filename:"/lib/python3.7/site-packages/dateutil/parser/_parser.py",start:365259,end:424063,audio:0},{filename:"/lib/python3.7/site-packages/python_dateutil-2.8.1-py3.7.egg-info/PKG-INFO",start:424063,end:433382,audio:0},{filename:"/lib/python3.7/site-packages/python_dateutil-2.8.1-py3.7.egg-info/top_level.txt",start:433382,end:433391,audio:0},{filename:"/lib/python3.7/site-packages/python_dateutil-2.8.1-py3.7.egg-info/requires.txt",start:433391,end:433400,audio:0},{filename:"/lib/python3.7/site-packages/python_dateutil-2.8.1-py3.7.egg-info/zip-safe",start:433400,end:433401,audio:0},{filename:"/lib/python3.7/site-packages/python_dateutil-2.8.1-py3.7.egg-info/dependency_links.txt",start:433401,end:433402,audio:0},{filename:"/lib/python3.7/site-packages/python_dateutil-2.8.1-py3.7.egg-info/SOURCES.txt",start:433402,end:435470,audio:0}],remote_package_size:307669,package_uuid:"82a364f3-d1a9-415f-b51a-42bbf8b9b3e4"})})();