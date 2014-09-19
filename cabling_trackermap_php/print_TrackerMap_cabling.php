
<H1>Create your own TrackerMap</H1>

<?php
	$inpfile = "";
	$title = "";
	$outgrafic = "";
	$outfile = "";
	$plotwidth = "600";
// 	if(isset($_POST["withpixel"]) && ($_POST["withpixel"] =  = "Only")) $plotwidth = "300";
	$feature1 = "";
	$feature2 = "";
	$feature3 = "";
	$feature4 = "";
	$feature5 = "";
	$feature6 = "";
// 	$fedid1 = "";
	$fedid2 = "";
	$fedid3 = "";
	$fedid4 = "";
	$fedid5 = "";
	$fedid6 = "";
	$fedid7 = "";
	$fedid8 = "";
	$fedid9 = "";
	$exeok = false;
	$exeok2 = false;
	if(isset($_POST["go"])) {
		$inpfile = $_POST['userfile'];
		$userfile = $_POST['userfile'];
		$title = $_POST['title'];
		$outgrafic = $_POST["title"].".png";
		$outfile = $_POST["outfile"];
		$feature1 = $_POST["feature1"];
		$feature2 = $_POST["feature2"];
		$feature3 = $_POST["feature3"];
		$feature4 = $_POST["feature4"];
		$feature5 = $_POST["feature5"];
		$feature6 = $_POST["feature6"];
// 		$fedid1 = $_POST["fedid1"];
		$fedid2 = $_POST["fedid2"];
		$fedid3 = $_POST["fedid3"];
		$fedid4 = $_POST["fedid4"];
		$fedid5 = $_POST["fedid5"];
		$fedid6 = $_POST["fedid6"];
		$fedid7 = $_POST["fedid7"];
		$fedid8 = $_POST["fedid8"];
		$fedid9 = $_POST["fedid9"];
// 		if(isset($_POST["execopt"])) $execopt = $_POST["execopt"];
		if(isset($_POST["listopt"])) $listopt = $_POST["listopt"];
		if(isset($_POST["fedid1"])) $fedid1 = $_POST["fedid1"];
		if(isset($_POST["fedid2"])) $fedid2 = $_POST["fedid2"];
		if(isset($_POST["fedid3"])) $fedid3 = $_POST["fedid3"];
		if(isset($_POST["fedid4"])) $fedid4 = $_POST["fedid4"];
		if(isset($_POST["fedid5"])) $fedid5 = $_POST["fedid5"];
		if(isset($_POST["fedid6"])) $fedid6 = $_POST["fedid6"];
		if(isset($_POST["fedid7"])) $fedid7 = $_POST["fedid7"];
		if(isset($_POST["fedid8"])) $fedid8 = $_POST["fedid8"];
		if(isset($_POST["fedid9"])) $fedid9 = $_POST["fedid9"];
		if(isset($_POST["listoptb"])) $listoptb = $_POST["listoptb"];
	}
?>


<?php
function listfedid($postname, $fedidname, $fedidselected) {

	echo "${fedidname} <select name='${postname}' >";
// 	echo "Fedid1 <select name = 'fedid1' >";
	echo "<option value = '' > </option>";
	for ($i = 1; $i <= 489; $i++) {
		if ($fedidselected == $i) {
			echo "<option value = $i selected>$i";
		} else {
			echo "<option value = $i>$i";
		}
	}
	echo "</select>";
}
?>

<form enctype = "multipart/form-data" action = "print_TrackerMap_cabling.php" method = "POST">
	<input type = "hidden" name = "MAX_FILE_SIZE" value = "500000" />
	Write the web addres for Cabling file or write run number: <input name = "userfile" value = "<?php echo $userfile; ?>" type = "text" size = 70 />
	<br>
	<?php 
	if ($userfile !=  "") {
// // 		echo "$userfile";
		if (10 < strlen ($userfile)) {
			echo "Wrote a web address <br>";
		} else {
			echo "Wrote a run number <br> ";
		}
		echo "<select name = 'listopt' >";
		echo "<option value = ''> </option>";
		if ($listopt == "execopt1") {
			echo "<option value = 'execopt1' selected>Tracker map for the alias of some modules,write the Alias or something like: from TEC, TECmi, TECminus_2,TECminus_2_4 etc";
// 			$exeok = true;
		} else {
			echo "<option value = 'execopt1'>Tracker map for the alias of some modules,write the Alias or something like: from TEC, TECmi, TECminus_2,TECminus_2_4 etc";
		}
		if ($listopt == "execopt2") {
			echo "<option value = 'execopt2' selected>Tracker map of DetIds connected to some FEDs to locate them in the detector, write the FedIds";
// 			$exeok = true;
		} else {
			echo "<option value = 'execopt2'>Tracker map of DetIds connected to some FEDs to locate them in the detector, write the FedIds";
		}
		if ($listopt == "execopt3") {
			echo "<option value = 'execopt3' selected>Tracker map of modules with certain HV information. Write the Alias or something like: branchController05,easyCrate3, etc ";
		} else {
			echo "<option value = 'execopt3'>Tracker map of modules with certain HV information. Write the Alias or something like: branchController05,easyCrate3, etc ";
		}
		if ($listopt == "execopt4") {
			echo "<option value = 'execopt4' selected>List of DetIds of the cabling file in a txt";
		} else {
			echo "<option value = 'execopt4'>List of DetIds of the cabling file in a txt";
		}
		if ($listopt == "execopt5") {
			echo "<option value = 'execopt5' selected>List of DetIds of the cabling file in a txt file and a trackermap";
		} else {
			echo "<option value = 'execopt5'>List of DetIds of the cabling file in a txt file and a trackermap";
		}
		if ($listopt == "execopt6") {
			echo "<option value = 'execopt6' selected>Write the name of the file with the modules associated to a(some) Fed(s) ";
		} else {
			echo "<option value = 'execopt6'>Write the name of the file with the modules associated to a(some) Fed(s) ";
		}
		if ($listopt == "execopt7") {
			echo "<option value = 'execopt7' selected>Information about a(some) module(s),write the pairnumber of the module(s) selected,Info you want to know about the modules [FedCrate,FeUnit,FeChan...]";
		} else {
			echo "<option value = 'execopt7'>Information about a(some) module(s),write the pairnumber of the module(s) selected,Info you want to know about the modules [FedCrate,FeUnit,FeChan...]";
		}
		if ($listopt == "execopt8") {
			echo "<option value = 'execopt8' selected>Information about a(some) Fed(s),write the FedCh of the Fed(s) selected, Info you want to know about the Fed(s)[FedCrate,FeUnit,APV0...]";
		} else {
			echo "<option value = 'execopt8'>Information about a(some) Fed(s),write the FedCh of the Fed(s) selected, Info you want to know about the Fed(s)[FedCrate,FeUnit,APV0...] ";
		}
		if ($listopt == "execopt9") {
			echo "<option value = 'execopt9' selected>Info you want to know the modules associated to any value of the cabling [FedCh,FecCrate,LldChan,APV0,APV1...]";
		} else {
			echo "<option value = 'execopt9'>Info you want to know the modules associated to any value of the cabling [FedCh,FecCrate,LldChan,APV0,APV1...]";
		}
		if ($listopt == "execopt10") {
			echo "<option value = 'execopt10' selected>If you want to know the modules in common for several info of the cabling[FecCrate,APV0,APV1...]";
		} else {
			echo "<option value = 'execopt10'>If you want to know the modules in common for several info of the cabling[FecCrate,APV0,APV1...]";
		}		
		if ($listopt == "execopt11") {
			echo "<option value = 'execopt11' selected>Dump the Alias of the DetIds of the Cabling file in a txt file";
		} else {
			echo "<option value = 'execopt11'>Dump the Alias of the DetIds of the Cabling file in a txt file";
		}
		if ($listopt == "execopt12") {
			echo "<option value = 'execopt12' selected>Know the Alias of a (set of) module(s)";
		} else {
			echo "<option value = 'execopt12'>Know the Alias of a (set of) module(s)";
		}
		if ($listopt == "execopt13") {
			echo "<option value = 'execopt13' selected>Know the modules associated to some Alias,write the Alias or something like: from TEC, TECmi, TECminus_7,TECminus_7_5 etc";
		} else {
			echo "<option value = 'execopt13'>Know the modules associated to some Alias,write the Alias or something like: from TEC, TECmi, TECminus_7,TECminus_7_5 etc ";
		}
		if ($listopt == "execopt14") {
			echo "<option value = 'execopt14' selected>write the modules to know if they are located on certain subdetector. write the subdetector in order to know if the module is located there";
		} else {
			echo "<option value = 'execopt14'>write the modules to know if they are located on certain subdetector. write the subdetector in order to know if the module is located there";
		}
		if ($listopt == "execopt15") {
			echo "<option value = 'execopt15' selected>Write the modules in order to get some info. Write the options of the Info about a (set of) module(s)";
		} else {
			echo "<option value = 'execopt15'>Write the modules in order to get some info. Write the options of the Info about a (set of) module(s)";
		}
		if ($listopt == "execopt16") {
			echo "<option value = 'execopt16' selected>Modules associated to a(some) value(s),write the values whereof you want to know the modules associated,like cms_trk_dcs_05:CAEN,easyCrate3, easyBoard06, channel002 etc ";
		} else {
			echo "<option value = 'execopt16'>Modules associated to a(some) value(s),write the values whereof you want to know the modules associated,like cms_trk_dcs_05:CAEN,easyCrate3, easyBoard06, channel002 etc";
		}
		if ($listopt == "execopt17") {
			echo "<option value = 'execopt17' selected>HV Values with modules in common";
		} else {
			echo "<option value = 'execopt17'>HV Values with modules in common";
		}
if ($listopt == "execopt18") {
			echo "<option value = 'execopt18' selected>here goes the alias whereof you want to know the info cabling. info you want to know like:FedCrate,FedSlot,FedId ....";
		} else {
			echo "<option value = 'execopt18'>here goes the alias whereof you want to know the info cabling. info you want to know like:FedCrate,FedSlot,FedId .... ";
		}
		if ($listopt == "execopt19") {
			echo "<option value = 'execopt19' selected>write the property to know the location in the detector:value of the cabling,FedCrate,FedSlot,FedId,FeUnit,FeChan...";
		} else {
			echo "<option value = 'execopt19'>write the property to know the location in the detector:value of the cabling,FedCrate,FedSlot,FedId,FeUnit,FeChan...";
		}
		if ($listopt == "execopt20") {
			echo "<option value = 'execopt20' selected>Info you want to know the modules associated to any value of the cabling,FedCrate,FedSlot,FedId,FeUnit,FeChan...";
		} else {
			echo "<option value = 'execopt20'>Info you want to know the modules associated to any value of the cabling,FedCrate,FedSlot,FedId,FeUnit,FeChan...";
		}
		if ($listopt == "execopt21") {
			echo "<option value = 'execopt21' selected>property to know the location in the detector [FedCrate,FedSlot..]. subdetector whereof you want to know if the module chosen is there";
		} else {
			echo "<option value = 'execopt21'>property to know the location in the detector [FedCrate,FedSlot..]. subdetector whereof you want to know if the module chosen is there";
		}
		if ($listopt == "execopt22") {
			echo "<option value = 'execopt22' selected>To know the alias of modules with certain property of HV, write the alias. Write the hv property,PSUName,Cmstrk,Crate,Board,Branch,TrackerSY,Channel ";
		} else {
			echo "<option value = 'execopt22'>To know the alias of modules with certain property of HV, write the alias. Write the hv property,PSUName,Cmstrk,Crate,Board,Branch,TrackerSY,Channel";
		}
		if ($listopt == "execopt23") {
			echo "<option value = 'execopt23' selected>To know the alias of the modules with hv -p property, write the hv property,PSUName,Cmstrk,Crate,Board,Branch,TrackerSY,Channel";
		} else {
			echo "<option value = 'execopt23'>To know the alias of the modules with hv -p property, write the hv property,PSUName,Cmstrk,Crate,Board,Branch,TrackerSY,Channel";
		}
		if ($listopt == "execopt24") {
			echo "<option value = 'execopt24' selected>Write the cabling info you want to know, like: FedCrate,FedSlot, etc. write the hv property you know , like:cms_trk_dcs_05:CAEN, CMS_TRACKER_SY1527_8, etc";
		} else {
			echo "<option value = 'execopt24'>Write the cabling info you know, like: FedCrate,FedSlot, etc. write the hv property you want to know like,PSUName,Cmstrk,Crate,Board,Branch,TrackerSY,Channel";
		}
		if ($listopt == "execopt25") {
			echo "<option value = 'execopt25' selected>Write the hv property you know , like:branchController05,easyCrate3, etc. Write the cabling info you want to know";
		} else {
			echo "<option value = 'execopt25'>Write the hv property you know , like:branchController05,easyCrate3, etc. Write the cabling info you want to know";
		}

		if ($listopt == "execopth") {
			echo "<option value = 'execopth' selected>Show Help";
		} else {
			echo "<option value = 'execopth'>Show Help";
		}
		echo "</select><br>";

		if ($listopt == "execopt1" || $listopt == "execopt3" ) {
			echo "Write feature1 <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write feature2 <input name = 'feature2' value = '$feature2' type = 'text'>";
			echo "Write feature3 <input name = 'feature3' value = '$feature3' type = 'text'></a><br>";
			echo "Write feature4 <input name = 'feature4' value = '$feature4' type = 'text'>";
			echo "Write feature5 <input name = 'feature5' value = '$feature5' type = 'text'>";
			echo "Write feature6 <input name = 'feature6' value = '$feature6' type = 'text'></a><br>";
			echo "Write Map Title <input name = 'title' value = '$title' type = 'text'>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok = true;
			}
		}
		if ($listopt == "execopt2") {
			listfedid("fedid1", "FedID 1", "${fedid1}");
			listfedid("fedid2", "FedID 2", "${fedid2}");
			listfedid("fedid3", "FedID 3", "${fedid3}");
			listfedid("fedid4", "FedID 4", "${fedid4}");
			listfedid("fedid5", "FedID 5", "${fedid5}");
			listfedid("fedid6", "FedID 6", "${fedid6}");
			listfedid("fedid7", "FedID 7", "${fedid7}");
			listfedid("fedid8", "FedID 8", "${fedid8}");
			listfedid("fedid9", "FedID 9", "${fedid9}");
			echo "<br>";
			echo "Write Map Title <input name = 'title' value = '$title' type = 'text'>";
			echo "<br>";
			if ($fedid1 != "") {
				$exeok = true;
			}
		}
		if ($listopt == "execopt4" || $listopt == "execopt11") {
			echo "Write outfile .txt <input name = 'outfile' value = '$outfile' type = 'text'>";
			echo "<br>";
			if ($outfile != "") {
				$exeok2 = true;
			}
		}
		if ($listopt == "execopt5") {
			echo "Write Map Title <input name = 'title' value = '$title' type = 'text'>";
			echo "<br>";
			if ($title != "") {
				$exeok = true;
			}
		}
		if ($listopt == "execopt6") {
			listfedid("fedid1", "FedID 1", "${fedid1}");
			listfedid("fedid2", "FedID 2", "${fedid2}");
			listfedid("fedid3", "FedID 3", "${fedid3}");
			listfedid("fedid4", "FedID 4", "${fedid4}");
			listfedid("fedid5", "FedID 5", "${fedid5}");
			listfedid("fedid6", "FedID 6", "${fedid6}");
			listfedid("fedid7", "FedID 7", "${fedid7}");
			listfedid("fedid8", "FedID 8", "${fedid8}");
			listfedid("fedid9", "FedID 9", "${fedid9}");
			echo "<br>";
			echo "Write outfile .txt <input name = 'outfile' value = '$outfile' type = 'text'>";
			echo "<br>";
			if ($fedid1 != "") {
				$exeok2 = true;
			}
		}

		if ($listopt == "execopt7" ) {
			echo "Write Module <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write module <input name = 'feature2' value = '$feature2' type = 'text'>";
			echo "Write pairNumber <input name = 'feature3' value = '$feature3' type = 'text'></a><br>";
			echo "Write pairNumber <input name = 'feature4' value = '$feature4' type = 'text'>";
			echo "Write feature <input name = 'feature5' value = '$feature5' type = 'text'>";
			echo "Write feature <input name = 'feature6' value = '$feature6' type = 'text'>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok2 = true;
			}
		}

		if ($listopt == "execopt8" ) {
			echo "Write FedId <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write FedId <input name = 'feature2' value = '$feature2' type = 'text'>";
			echo "Write FeChanel <input name = 'feature3' value = '$feature3' type = 'text'></a><br>";
			echo "Write FeChanel <input name = 'feature4' value = '$feature4' type = 'text'>";
			echo "Write feature <input name = 'feature5' value = '$feature5' type = 'text'>";
			echo "Write feature <input name = 'feature6' value = '$feature6' type = 'text'>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok2 = true;
			}
		}
		if ($listopt == "execopt9" || $listopt == "execopt10" || $listopt == "execopt19" || $listopt == "execopt20") {
			echo "Write feature1 <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write feature2 <input name = 'feature2' value = '$feature2' type = 'text'></a><br>";
			echo "Write feature1 number <input name = 'feature3' value = '$feature3' type = 'text'>";
			echo "Write feature number <input name = 'feature4' value = '$feature4' type = 'text'>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok2 = true;
			}
		}
		if ($listopt == "execopt12" ) {
			echo "Write Module <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write Module <input name = 'feature2' value = '$feature2' type = 'text'>";
			echo "Write Module <input name = 'feature3' value = '$feature3' type = 'text'></a><br>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok2 = true;
			}
		}
		if ($listopt == "execopt13") {
			echo "Write alias <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write alias <input name = 'feature2' value = '$feature2' type = 'text'></a><br>";
			echo "Write outfile .txt <input name = 'outfile' value = '$outfile' type = 'text'>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok2 = true;
			}
		}
		if ($listopt == "execopt14") {
			echo "Write module <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write module <input name = 'feature2' value = '$feature2' type = 'text'>";
			echo "Write module <input name = 'feature3' value = '$feature3' type = 'text'></a><br>";
			echo "Write subdetector <input name = 'feature4' value = '$feature4' type = 'text'>";
			echo "Write subdetector <input name = 'feature5' value = '$feature5' type = 'text'>";
			echo "Write subdetector <input name = 'feature6' value = '$feature6' type = 'text'>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok2 = true;
			}
		}
		if ($listopt == "execopt15") {
			echo "Write module <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write module <input name = 'feature2' value = '$feature2' type = 'text'></a><br>";
			echo "Write Crate <input name = 'feature3' value = '$feature3' type = 'text'>";
			echo "Write Channel <input name = 'feature4' value = '$feature4' type = 'text'>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok2 = true;
			}
		}
		if ($listopt == "execopt16" || $listopt == "execopt17") {
			echo "Write HV piece of name <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write HV piece of name <input name = 'feature2' value = '$feature2' type = 'text'></a><br>";
			echo "Write outfile .txt <input name = 'outfile' value = '$outfile' type = 'text'>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok2 = true;
			}
		}
		if ($listopt == "execopt18" ) {
			echo "Write alias <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write alias <input name = 'feature2' value = '$feature2' type = 'text'></a><br>";
			echo "Write cabling feature1 <input name = 'feature3' value = '$feature3' type = 'text'>";
			echo "Write cabling feature2 <input name = 'feature4' value = '$feature4' type = 'text'>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok2 = true;
			}
		}
		if ($listopt == "execopt21") {
			echo "Write feature1 <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write feature1 number <input name = 'feature3' value = '$feature3' type = 'text'>";
			echo "Write subdetector(alias) <input name = 'feature5' value = '$feature5' type = 'text'>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok2 = true;
			}
		}
		if ($listopt == "execopt22") {
			echo "Write alias <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write alias <input name = 'feature2' value = '$feature2' type = 'text'></a><br>";
			echo "Write HV property <input name = 'feature3' value = '$feature3' type = 'text'>";
			echo "Write HV property <input name = 'feature4' value = '$feature4' type = 'text'>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok2 = true;
			}
		}
		if ($listopt == "execopt23") {
			echo "Write HV piece of name <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write HV piece of name <input name = 'feature2' value = '$feature2' type = 'text'>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok2 = true;
			}
		}
		if ($listopt == "execopt24") {
			echo "Write feature1 <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write feature2 <input name = 'feature2' value = '$feature2' type = 'text'></a><br>";
			echo "Write feature1 number <input name = 'feature3' value = '$feature3' type = 'text'>";
			echo "Write feature2 number <input name = 'feature4' value = '$feature4' type = 'text'></a><br>";
			echo "Write HV piece of name <input name = 'feature5' value = '$feature5' type = 'text'>";
			echo "Write HV piece of name <input name = 'feature6' value = '$feature6' type = 'text'>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok2 = true;
			}
		}
		if ($listopt == "execopt25") {
			echo "Write HV piece of name <input name = 'feature1' value = '$feature1' type = 'text'>";
			echo "Write HV piece of name <input name = 'feature2' value = '$feature2' type = 'text'></a><br>";
			echo "Write feature1 <input name = 'feature3' value = '$feature3' type = 'text'>";
			echo "Write feature2 <input name = 'feature4' value = '$feature4' type = 'text'>";
			echo "<br>";
			if ($feature1 != "") {
				$exeok2 = true;
			}
		}
		
	}
	?>
	<input type = "submit" name = "go" value = "Get!" />
</form>

<?php
// 	include 'plot_from_tmp_cabling.php';
// 	ini_set('display_errors', 'On');
// 	error_reporting(E_ALL);
	if(isset($_POST["go"])) {
		$title = $_POST["title"];
		$outgrafic = $title.".png";
		$inpfile = $_POST["userfile"];
		
		if ($listopt !=  "execopth") {
			if ($inpfile !=  "") {
				if ($listopt == "execopt1") {
// 					$execution = "1";
					$option1 = "-y";
					$option2 = "--yf";
				} else if ($listopt == "execopt2") {
					$option1 = "-b";
					$option2 = "--bf";
				} else if ($listopt == "execopt3") {
					$option1 = "-v";
					$option2 = "--vf";
				} else if ($listopt == "execopt4") {
					$option1 = "-a";
				} else if ($listopt == "execopt5") {
					$option2 = "--at";
				} else if ($listopt == "execopt6") {
					$option1 = "-z";
					$option2 = "--zi";
				} else if ($listopt == "execopt7") {
					$option1 = "-c";
					$option2 = "--cp";
					$option3 = "--ci";
				} else if ($listopt == "execopt8") {
					$option1 = "-g";
					$option2 = "--gf";
					$option3 = "--gi";
				} else if ($listopt == "execopt9") {
					$option1 = "-d";
					$option2 = "--di";
				} else if ($listopt == "execopt10") {
					$option1 = "-n";
					$option2 = "--ni";
				} else if ($listopt == "execopt11") {
					$option1 = "-k";
				} else if ($listopt == "execopt12") {
					$option1 = "-l";
				}else if ($listopt == "execopt13") {
					$option1 = "-m";
					$option2 = "--mf";
				}else if ($listopt == "execopt14") {
					$option1 = "-o";
					$option2 = "--os";
				} else if ($listopt == "execopt15") {
					$option1 = "-r";
					$option2 = "--ri";
				} else if ($listopt == "execopt16") {
					$option1 = "-t";
					$option2 = "--tf";
				} else if ($listopt == "execopt17") {
					$option1 = "-w";
					$option2 = "--wf";
				}else if ($listopt == "execopt18") {
					$option1 = "-j";
					$option2 = "--ja";
				} else if ($listopt == "execopt19") {
					$option1 = "-e";
					$option2 = "--en";
				} else if ($listopt == "execopt20") {
					$option1 = "-d";
					$option2 = "--di";
				} else if ($listopt == "execopt21") {
					$option1 = "-i";
					$option2 = "--in";
					$option3 = "--ia";
				} else if ($listopt == "execopt22") {
					$option1 = "-q";
					$option2 = "--qi";
				} else if ($listopt == "execopt23") {
					$option1 = "-p";
				} else if ($listopt == "execopt24") {
					$option1 = "-s";
					$option2 = "--sc";
					$option3 = "--sh";
				} else if ($listopt == "execopt25") {
					$option1 = "-u";
					$option2 = "--uc";
				}

				
				if ($exeok == true) {
					if (10 < strlen ($userfile)) {
						$command = "./print_TrackerMap_cabling.sh --fu $inpfile $option1  $feature1 $feature2 $feature3 $feature4 $feature5 $feature6 $fedid1 $fedid2 $fedid3 $fedid4 $fedid5 $fedid6 $fedid7 $fedid8 $fedid9 $option2 $outfile $outgrafic";
// 						echo "Wrote a web address <br>";
					} else {
						$command = "./print_TrackerMap_cabling.sh -f $inpfile $option1  $feature1 $feature2 $feature3 $feature4 $feature5 $feature6 $fedid1 $fedid2 $fedid3 $fedid4 $fedid5 $fedid6 $fedid7 $fedid8 $fedid9 $option2 $outfile $outgrafic";
// 						echo "Wrote a run number  <br> ";
					}
					echo $command . "<br>";
					system($command);
//	                 		exec($command);

					exec ("rm -f temp/*");
// 					exec ("mkdir temp");
					exec ("mv DetIdCab.txt temp/");
					exec ("mv faliastkm.txt temp/");
					exec ("mv ModulestoFeds.txt temp/");
					exec ("mv filevamod.txt temp/");
					exec ("mv $outfile temp/");
					exec ("mv file.txt temp/");
					exec ("mv $outgrafic temp/");
					exec ("mv infofeds.txt temp/");
					exec ("mv $inpfile temp/");
					exec ("mv CablingInfo* temp/");


					echo "</a><br><br>";
					
					if ($listopt == "execopt1") {
// 						echo "<a href = 'plot_from_tmp_cabling.php?file = ${outgrafic}'><img src = 'plot_from_tmp_cabling.php?file = ${outgrafic}' width = ${plotwidth}></a><br><br>";
 						echo "<a href = 'temp/DetIdCab.txt'>Download DetIdCab file </a><br><br>";
// 						echo "<a href = 'temp/file.txt'>Download file.txt file </a><br><br>";
						echo "<a href = 'temp/faliastkm.txt'>Download faliastkm.txt file </a><br><br>";
					} else if ($listopt == "execopt2") {
 						echo "<a href = 'temp/DetIdCab.txt'>Download DetIdCab file </a><br><br>";
// 						echo "<a href = 'temp/file.txt'>Download file.txt file </a><br><br>";
						echo "<a href = 'temp/ModulestoFeds.txt'>Download ModulestoFeds file </a><br><br>";
					} else if ($listopt == "execopt3") {
						echo "<a href = 'temp/DetIdCab.txt'>Download DetIdCab file </a><br><br>";
						echo "<a href = 'temp/file.txt'>Download file.txt file </a><br><br>";
						echo "<a href = 'temp/filevamod.txt'>Download filevamod.txt file </a><br><br>";
					} else if ($listopt == "execopt5") {
						echo "<a href = 'temp/DetIdCab.txt'>Download DetIdCab file </a><br><br>";
						echo "<a href = 'temp/trackermapdetids.txt'>Download trackermapdetids.txt file </a><br><br>";
					}

						
					// write log
					$logFile = "print_TrackerMap.log";
					$fh = fopen($logFile,'a');
					$date = date('d/m/Y H:i:s', time());
					$logstring = $date." ".$_SERVER["REMOTE_ADDR"]." ".$inpfile." ".$command."\n";
					fwrite($fh,$logstring);
					fclose($fh);
 				echo "<a href='plot_from_tmp_cabling.php?file=temp/${outgrafic}'><img src='plot_from_tmp_cabling.php?file=temp/${outgrafic}' width=${plotwidth}></a>";
				}
			

				if ($exeok2 == true) {
					if (10 < strlen ($userfile)) {
						$command = "./print_TrackerMap_cabling.sh --fu $inpfile $option1 $feature1 $feature2 $option2 $feature3 $feature4 $fedid1 $fedid2 $fedid3 $fedid4 $fedid5 $fedid6 $fedid7 $fedid8 $fedid9  $outfile $option3 $feature5 $feature6";
// 						echo "Wrote a web address <br>";
					} else {
						$command = "./print_TrackerMap_cabling.sh -f $inpfile $option1 $feature1 $feature2 $option2 $feature3 $feature4 $fedid1 $fedid2 $fedid3 $fedid4 $fedid5 $fedid6 $fedid7 $fedid8 $fedid9  $outfile $option3 $feature5 $feature6";
// 						echo "Wrote a run number <br> ";
					}
// 					$command = "./print_TrackerMap_cabling.sh $inpfile $option1 $feature1 $feature2 $option2 $feature3 $feature4 $fedid1 $fedid2 $fedid3 $fedid4 $fedid5 $fedid6 $fedid7 $fedid8 $fedid9  $outfile $option3 $feature5 $feature6";
					echo $command . "<br>";
					system($command);
//	                 		exec($command);

					exec ("rm -f temp/*");
// 					exec ("mkdir temp");
					exec ("mv DetIdCab.txt temp/");
					exec ("mv faliastkm.txt temp/");
					exec ("mv ModulestoFeds.txt temp/");
					exec ("mv filevamod.txt temp/");
					exec ("mv $outfile temp/");
					exec ("mv file.txt temp/");
					exec ("mv $outgrafic temp/");
					exec ("mv infofeds.txt temp/");
					exec ("mv ModofCab.txt temp/");
					exec ("mv Modulescommon.txt temp/");
					exec ("mv AliasModules.txt temp/");
					exec ("mv TrueFalseAlias.txt temp/");
					exec ("mv InfoModuleHV.txt temp/");
					exec ("mv $inpfile temp/");
					exec ("mv CablingInfo* temp/");
					exec ("mv CabofAlias.txt temp/");
					exec ("mv AliasforCabling.txt temp/");
					exec ("mv ModofCab.txt temp/");
					exec ("mv CabinSubdector.txt temp/");
					exec ("mv aliastohv.txt temp/");
					exec ("mv hvofcab.txt temp/");
					exec ("mv Cabofhv.txt temp/");
					exec ("mv hvofalias.txt temp/");


					echo "</a><br><br>";
					
					if ($listopt == "execopt4") {
 						echo "<a href = 'temp/$outfile'>Download '$outfile' file </a><br><br>";
// 						echo "<a href = 'temp/DetIdCab.txt'>Download DetIdCab file </a><br><br>";
					}
					if ($listopt == "execopt6") {
 						echo "<a href = 'temp/$outfile'>Download '$outfile' file </a><br><br>";
					}
					if ($listopt == "execopt7") {
 						echo "<a href = 'temp/infomodules.txt'>Download infomodules.txt file </a><br><br>";
					}
					if ($listopt == "execopt8") {
 						echo "<a href = 'temp/infofeds.txt'>Download infofeds.txt file </a><br><br>";
					}
					if ($listopt == "execopt9") {
 						echo "<a href = 'temp/ModofCab.txt'>Download ModofCab.txt file </a><br><br>";
					}
					if ($listopt == "execopt10") {
 						echo "<a href = 'temp/Modulescommon.txt'>Download Modulescommon.txt file </a><br><br>";
					}
					if ($listopt == "execopt11") {
 						echo "<a href = 'temp/$outfile'>Download '$outfile' file </a><br><br>";
					}
					if ($listopt == "execopt12") {
 						echo "<a href = 'temp/AliasModules.txt'>Download AliasModules.txt file </a><br><br>";
					}
					if ($listopt == "execopt13") {
 						echo "<a href = 'temp/$outfile'>Download '$outfile' file </a><br><br>";
					}
					if ($listopt == "execopt14") {
 						echo "<a href = 'temp/TrueFalseAlias.txt'>Download TrueFalseAlias.txt file </a><br><br>";
					}
					if ($listopt == "execopt15") {
 						echo "<a href = 'temp/InfoModuleHV.txt'>Download InfoModuleHV.txt file </a><br><br>";
					}
					if ($listopt == "execopt16" || $listopt == "execopt17") {
 						echo "<a href = 'temp/$outfile'>Download '$outfile' file </a><br><br>";
					}
if ($listopt == "execopt18") {
 						echo "<a href = 'temp/CabofAlias.txt'>Download CabofAlias.txt file </a><br><br>";
					}
					if ($listopt == "execopt19") {
 						echo "<a href = 'temp/AliasforCabling.txt'>Download AliasforCabling.txt file </a><br><br>";
					}
					if ($listopt == "execopt20") {
 						echo "<a href = 'temp/ModofCab.txt'>Download ModofCab.txt file </a><br><br>";
					}
					if ($listopt == "execopt21") {
 						echo "<a href = 'temp/CabinSubdector.txt'>Download CabinSubdector.txt file </a><br><br>";
					}
					if ($listopt == "execopt22") {
 						echo "<a href = 'temp/hvofalias.txt'>Download hvofalias.txt file </a><br><br>";
					}
					if ($listopt == "execopt23") {
 						echo "<a href = 'temp/aliastohv.txt'>Download aliastohv.txt file </a><br><br>";
					}
					if ($listopt == "execopt24") {
 						echo "<a href = 'temp/hvofcab.txt'>Download hvofcab.txt file </a><br><br>";
					}
					if ($listopt == "execopt25") {
 						echo "<a href = 'temp/Cabofhv.txt'>Download Cabofhv.txt file </a><br><br>";
					}

					// write log
					$logFile = "print_TrackerMap.log";
					$fh = fopen($logFile,'a');
					$date = date('d/m/Y H:i:s', time());
					$logstring = $date." ".$_SERVER["REMOTE_ADDR"]." ".$inpfile." ".$command."\n";
					fwrite($fh,$logstring);
					fclose($fh);
			
			}

//	echo "<a href='plot_from_tmp_cabling.php?file=temp/${outgrafic}'><img src='plot_from_tmp_cabling.php?file=temp/${outgrafic}' width=${plotwidth}></a>";
//				echo "<a href = 'plot_from_tmp_cabling.php?file = temp/${outgrafic}'><img src = 'plot_from_tmp_cabling.php?file = temp/${outgrafic}' width = ${plotwidth}></a><br><br>";
			}
		} else {
			$fp = fopen("ayuda.txt", "r");
			$texto = fread($fp, filesize("ayuda.txt"));
			//Para mostrarlo
			$texto = nl2br($texto); 
			echo "<font face = 'monospace' $texto</font>";
			fclose ($fp);
		}
//echo "<a href = 'plot_from_tmp_cabling.php?file = ${outgrafic}'><img src = 'plot_from_tmp_cabling.php?file = ${outgrafic}' width = ${plotwidth}></a><br><br>";
	}
?>