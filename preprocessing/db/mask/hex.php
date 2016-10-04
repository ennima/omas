<?php
	echo "HOLA \n";
	function hex2str($hex) {
	    $str = '';
	    echo "\n".$hex."\n";
	    for($i=0;$i<strlen($hex);$i+=2)
	    {
	    	echo "\n >HEx: ".substr($hex,$i,2)."\n";
	    	#echo "\n >Dec:".hexdec(substr($hex,$i,2))."\n";
	    	echo "\n >Acii: ".chr(hexdec(substr($hex,$i,2)))."\n";
	    	// echo chr(72);
	    	$str .= chr(hexdec(substr($hex,$i,2)));
	    }
	    return $str;
	}
	$hex_string = "4229d691b07b13341da53f17ab9f2416"; // 10 chars/bytes
	$packed_string = hex2str($hex_string); // 0xA1B2C3D4F5 // 5 chars/bytes.
	echo $hex_string."\n";
	echo $packed_string;
?>