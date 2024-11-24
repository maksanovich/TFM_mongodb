

<?php



function get_allowed_IP () { 

  $CSV_allowed_ip = realpath ('allowed_IP.csv');
  
  echo $CSV_allowed_ip ."<br/>";

  $allowed_ip_list = array ();

  $f = fopen($CSV_allowed_ip, 'r');

  while(!feof($f)) {

    $row = fgetcsv($f);

    if (!empty($row)) {
          #echo "$row[0]"  . "<br />";
		  
		  array_push($allowed_ip_list, $row[0]);
    }

	
}

  #print_r ($allowed_ip_list);
  return $allowed_ip_list;


}

#get_allowed_IP ()	
	
	
	

?>