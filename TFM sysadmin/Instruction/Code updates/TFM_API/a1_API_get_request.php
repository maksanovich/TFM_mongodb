

<?php


require_once ("a0_API_allowed_IP.php");


function check_client_IP_run_task () {
	
	
  $client_IP = $_SERVER['REMOTE_ADDR'];
  
  echo 'User IP Address - '.$_SERVER['REMOTE_ADDR']; 

  #must use abosolute or real path, or the code won't work 
   $file_path = realpath ("a3_API_task_router.py");

  #echo "\n \n" . $file_path;
  
  
  #$client_IP = "173.208.190.18";
  
  $allowed_client_ips = array(get_allowed_IP()); #must convert the function into array

  foreach ($allowed_client_ips as $subarray) {
	  
  
    if (!in_array($client_IP, $subarray)){

       echo "client IP NOT ALLOWED" . "  client IP = $client_IP";
	   

  }   else {
	  
	  
        echo "client IP ALLOWED" . "  client IP = $client_IP" ; 
		echo "  task_file = $file_path" ;
		
        echo "\n \n" . $file_path;

        $TFM_task = $_GET['TFM_task'];#name of TFM_task = LOG database name 
        $TFM_task_action = $_GET['TFM_task_action']; #name of TFM_task_action => trans_start_date, trans_end_date

        $command = escapeshellcmd("python $file_path $TFM_Task $TFM_task_action");
        $output = shell_exec($command);
        echo ($output);

	
  }

  }

}

check_client_IP_run_task ()

  
?>